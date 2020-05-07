import 'package:flutter/material.dart';
import 'package:fluro/fluro.dart';

class FluroRouter {
  static Router router = Router();

  // The following example was made for the landing screen

  /*static Handler _landingHandler = Handler(
      handlerFunc: (BuildContext context, Map<String, dynamic> params) =>
          LandingScreen());*/

  static void setupRouter() {
    /*router.define(
      'landing',
      handler: _landingHandler,
    );*/
  }
}
