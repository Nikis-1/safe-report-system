import 'package:flutter/material.dart';
import '../services/api_service.dart';
import 'login_screen.dart';
import 'report_screen.dart';
import 'report_history_screen.dart';
// Import other screens you’ll add later
// import 'admin_dashboard.dart';
// import 'reviewer_dashboard.dart';

import 'package:shared_preferences/shared_preferences.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String role = '';

  @override
  void initState() {
    super.initState();
    _getRole();
  }

  Future<void> _getRole() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      role = prefs.getString('role') ?? '';
    });
  }

  void _logout() async {
    await ApiService().logout();
    Navigator.pushReplacement(
        context, MaterialPageRoute(builder: (_) => const LoginScreen()));
  }

  void _goToReport(BuildContext context) {
    Navigator.push(
        context, MaterialPageRoute(builder: (_) => const ReportScreen()));
  }

  void _goToReportHistory(BuildContext context) {
    Navigator.push(context,
        MaterialPageRoute(builder: (_) => const ReportHistoryScreen()));
  }

  // Add more navigation handlers for admin/reviewer screens

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home'),
        actions: [
          IconButton(icon: const Icon(Icons.logout), onPressed: _logout),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: _logout,
          )
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (role == 'reporter') ...[
              ElevatedButton(
                onPressed: () => _goToReport(context),
                child: const Text('Submit a Report'),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () => _goToReportHistory(context),
                child: const Text('View My Reports'),
              ),
            ],
            if (role == 'reviewer') ...[
              const Text('Reviewer Dashboard Coming Soon!'),
              // Add reviewer buttons here
            ],
            if (role == 'admin') ...[
              const Text('Admin Dashboard Coming Soon!'),
              // Add admin buttons here
            ],
          ],
        ),
      ),
    );
  }
}
