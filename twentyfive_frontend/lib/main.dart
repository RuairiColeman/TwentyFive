import 'package:flutter/material.dart';
import 'api_service.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Twenty Five Game',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ApiService apiService = ApiService();
  final TextEditingController playerController = TextEditingController();
  List<String> players = [];
  String message = '';
  Map<String, dynamic> gameData = {};

  void _createPlayers() async {
    final response = await apiService.createPlayers(players);
    setState(() {
      message = response['message'];
    });
  }

  void _dealCards() async {
    final response = await apiService.dealCards();
    setState(() {
      message = response['message'];
      gameData = response;
    });
  }

  void _playGame() async {
    final response = await apiService.playGame();
    setState(() {
      message = response['message'];
      gameData = response;
    });
  }

  void _showHands() async {
    final response = await apiService.showHands();
    setState(() {
      gameData = response;
    });
  }

  void _rotateDealer() async {
    final response = await apiService.rotateDealer();
    setState(() {
      message = response['new_dealer'];
    });
  }

  void _players() async {
    final response = await apiService.players();
    setState(() {
      message = response['players'];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Twenty Five Game'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: playerController,
              decoration: InputDecoration(labelText: 'Player Name'),
            ),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  players.add(playerController.text);
                  playerController.clear();
                });
              },
              child: Text('Add Player'),
            ),
            ElevatedButton(
              onPressed: _createPlayers,
              child: Text('Create Players'),
            ),
            ElevatedButton(
              onPressed: _dealCards,
              child: Text('Deal Cards'),
            ),
            ElevatedButton(
              onPressed: _playGame,
              child: Text('Play Game'),
            ),
            ElevatedButton(
              onPressed: _showHands,
              child: Text('Show Hands'),
            ),
            ElevatedButton(
              onPressed: _rotateDealer,
              child: Text('Rotate Dealer'),
            ),
            ElevatedButton(
              onPressed: _players,
              child: Text('Show Players'),
            ),
            Text(message),
            Expanded(
              child: ListView.builder(
                itemCount: gameData.length,
                itemBuilder: (context, index) {
                  String key = gameData.keys.elementAt(index);
                  return ListTile(
                    title: Text('$key: ${gameData[key]}'),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}