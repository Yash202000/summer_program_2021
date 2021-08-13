import 'package:flutter/material.dart';
import 'package:visitcity/pages/DrawerC.dart';
import 'package:visitcity/pages/slider.dart';

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0.1,
        iconTheme: IconThemeData(color: Colors.black),
        backgroundColor: Colors.white,
        actions: [
          IconButton(
            onPressed: () {},
            icon: Icon(Icons.search),
          ),
        ],
      ),
      drawer: SideDrawer(), //from DrawerC.dart.
      body: ListView(
        children: [
          Divider(thickness: 2),
          SliderListView(),
          Divider(thickness: 2),
        ],
      ),
    );
  }
}
