import 'package:flutter/material.dart';

void main() {
  FluroRouter.setupRouter();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: themeLight(),
      // ! YO, you will only change the code here okay?!
      // initialRoute: 'landing',
      onGenerateRoute: FluroRouter.router.generator,
    );
  }
}
