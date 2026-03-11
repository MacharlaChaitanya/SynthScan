# SYNTH Scan

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Security](https://img.shields.io/badge/Cybersecurity-WAPT-red)
![License](https://img.shields.io/badge/License-MIT-green)

SYNTH Scan is an AI-assisted **Web Application Penetration Testing (WAPT)** tool that performs automated vulnerability scanning and security analysis on web applications.

The platform detects common vulnerabilities, analyzes security posture, and presents the results in an interactive cybersecurity dashboard with real-time scan logs and risk scoring.

---

# Features

### Core Scanning Modules

- Port Scanning
- Directory Discovery
- Subdomain Discovery
- Cross-Site Scripting (XSS) Detection
- SQL Injection Detection

### Security Analysis

- Security Header Analysis
- Technology Fingerprinting
- Robots.txt Analysis
- Vulnerability Severity Scoring

### AI-Assisted Security

- AI Security Analysis
- AI Fix Recommendations

### Reporting

- Automated Security Reports
- Risk Score Calculation
- Severity Classification

---

# Live Scan Console

Synth Scan includes a **real-time scanning console** that simulates penetration testing activity similar to professional security tools.

Example scan logs:
# SYNTH Scan

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Security](https://img.shields.io/badge/Cybersecurity-WAPT-red)
![License](https://img.shields.io/badge/License-MIT-green)

SYNTH Scan is an AI-assisted **Web Application Penetration Testing (WAPT)** tool that performs automated vulnerability scanning and security analysis on web applications.

The platform detects common vulnerabilities, analyzes security posture, and presents the results in an interactive cybersecurity dashboard with real-time scan logs and risk scoring.

---

# Features

### Core Scanning Modules

- Port Scanning
- Directory Discovery
- Subdomain Discovery
- Cross-Site Scripting (XSS) Detection
- SQL Injection Detection

### Security Analysis

- Security Header Analysis
- Technology Fingerprinting
- Robots.txt Analysis
- Vulnerability Severity Scoring

### AI-Assisted Security

- AI Security Analysis
- AI Fix Recommendations

### Reporting

- Automated Security Reports
- Risk Score Calculation
- Severity Classification

---

# Live Scan Console

Synth Scan includes a **real-time scanning console** that simulates penetration testing activity similar to professional security tools.

Example scan logs:
[+] Starting scan
[+] Scanning ports
[+] Discovering directories
[+] Checking SQL Injection
[+] Running security analysis
[+] Scan completed


---

# Dashboard

After scanning, the platform displays a structured results dashboard including:

- Open Ports
- Discovered Directories
- Technologies Detected
- Vulnerabilities Found
- Risk Score
- Severity Level

---

# Project Architecture
Frontend (HTML / CSS / JavaScript)
↓
Flask API Server
↓
Scanning Engine
↓
Security Modules
↓
Results Dashboard


---

# Project Structure
SYNTH-SCAN
│
├ engine
│ ├ port_scanner.py
│ ├ dir_scanner.py
│ ├ xss_scanner.py
│ ├ sql_scanner.py
│ └ header_scanner.py
│
├ utils
│ ├ scan_controller.py
│ ├ report_generator.py
│ └ severity_score.py
│
├ ai
│ ├ ai_analysis.py
│ └ ai_fix_generator.py
│
├ wordlists
│ ├ directories.txt
│ └ subdomains.txt
│
├ reports
│ └ security_report.txt
│
├ frontend
│ ├ scan.html
│ └ assets
│
├ api_server.py
└ main.py



---

# Installation

Clone the repository:
git clone https://github.com/yourusername/synth-scan.git
cd synth-scan

Install dependencies:

pip install flask flask-cors requests
Running the Application

Start the backend server:

python api_server.py

You should see:

Running on http://127.0.0.1:5000

Then open the frontend:

frontend/scan.html
Example Test Target

Use this intentionally vulnerable testing site:

testphp.vulnweb.com



# Tech Stack

Backend

Python

Flask

Frontend

HTML

CSS

JavaScript

Security Modules

Custom vulnerability scanners

Directory brute forcing

Header analysis

Technology detection

# Disclaimer

This project is developed for educational and ethical security research purposes only.

Do not scan systems without permission.

Unauthorized security testing may be illegal.

# Author

Developed by Chaitanya M

Cybersecurity & FinTech Enthusiast
