# A CLI to make your life easier when creating a flutter project
# By: Miguel Ferreira (@esfoliante)
import os
import time
import platform

projectName = ""
path = ""

# PLEASE CHANGE THIS PATH IF NEEDED
ezcliPath = "/home/miguel/dev/ezCLI/"


def createProject():
    # See this pretty boy right here (global)? It will tell our beatiful code
    # that the variable projectName is refering to the global variable
    global projectName, path
    option = "no"

    path = input(
        'Please insert the path where you want to create your project: ')

    if path.strip() == "":
        print("\nThis path doesn't exist!!")
        return 0

    while option.lower != "yes":
        projectName = input('Insert the project name: ')
        correctProjectName()
        selectedOption = input(
            'Are you sure you want to name your project ' + projectName + ' ? (yes) ')
        if selectedOption.lower() == "yes":
            option = "yes"
            os.system('flutter create ' + path + projectName)
            print(
                '----------------------\n\n  Project created 🎉\n\n----------------------')
            createFiles()
            break
        else:
            os.system("cls" if platform.system() ==
                      "Windows" else "clear")


projectName


def correctProjectName():
    global projectName

    if projectName.strip() != "":
        projectName = projectName.lower()
        projectName = projectName.replace(" ", "_")
    else:
        projectName = "my_project"


# Let's create the files needed and that are super boring to create
def createFiles():
    global projectName, path, ezcliPath

    project = path + projectName

    os.chdir(project + "/lib/")
    os.system('touch routes.dart')
    os.system('touch theme.dart')
    os.system("md screens" if platform.system()
              == "Windows" else "mkdir screens")
    os.system("md widgets" if platform.system()
              == "Windows" else "mkdir widgets")
    copyFile("routes")
    copyFile("theme")
    copyFile("main")
    os.chdir("screens")
    os.system("fsutil example.dart" if platform.system()
              == "Windows" else "touch example.dart")
    copyFile("example")
    print(
        '---------------------------\n\n  Copy was successful! 🎉\n\n---------------------------')


# We have created this function because the code is really extense
# and as you can see we repeat it at least 3 times, soooo
def copyFile(fileName):
    global projectName, path, ezcliPath

    project = path + projectName + "/"

    if fileName != "example":
        with open(ezcliPath + fileName + ".dart", "r") as f:
            lines = f.readlines()
            lines = [l for l in lines]
            with open(project + "lib/" + fileName + ".dart", "w") as f1:
                f1.writelines(lines)
    else:
        with open(ezcliPath + fileName + ".dart", "r") as f:
            lines = f.readlines()
            lines = [l for l in lines]
            with open(project + "lib/screens/" + fileName + ".dart", "w") as f1:
                f1.writelines(lines)


def main():
    createProject()


main()
