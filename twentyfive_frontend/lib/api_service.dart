import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:5000';

  Future<Map<String, dynamic>> createPlayers(List<String> playerNames) async {
    final response = await http.post(
      Uri.parse('$baseUrl/create_players'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'player_names': playerNames}),
    );
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> dealCards() async {
    final response = await http.post(Uri.parse('$baseUrl/deal_cards'));
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> playGame() async {
    final response = await http.post(Uri.parse('$baseUrl/play_game'));
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> showHands() async {
    final response = await http.get(Uri.parse('$baseUrl/show_hands'));
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> rotateDealer() async {
    final response = await http.post(Uri.parse('$baseUrl/rotate_dealer'));
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> players() async {
    final response = await http.get(Uri.parse('$baseUrl/players'));
    return jsonDecode(response.body);
  }
}