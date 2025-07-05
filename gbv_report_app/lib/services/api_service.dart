import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../utils/constants.dart';

class ApiService {
  Future<bool> register(String username, String email, String password) async {
    final response = await http.post(
      Uri.parse('${baseUrl}register/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'username': username,
        'email': email,
        'password': password,
        'password2': password,
        'role': 'reporter',
      }),
    );

    return response.statusCode == 201;
  }

  Future<bool> login(String username, String password) async {
    final response = await http.post(
      Uri.parse('${baseUrl}login/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'username': username,
        'password': password,
      }),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      SharedPreferences prefs = await SharedPreferences.getInstance();
      await prefs.setString('token', data['access']);
      await prefs.setString('role', data['role']);
      return true;
    } else {
      return false;
    }
  }

  Future<void> logout() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.remove('token');
    await prefs.remove('role');
  }
}
