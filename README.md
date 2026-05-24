# SentinelShield

## Project Overview

SentinelShield is a lightweight Intrusion Detection and Web Protection System developed using Python and Flask.

The project simulates the behavior of a Web Application Firewall (WAF) by inspecting incoming requests, detecting attack patterns, applying rate limiting, generating logs, and displaying security events through a dashboard.

## Features

- SQL Injection Detection
- Cross-Site Scripting (XSS) Detection
- Directory Traversal Detection
- Command Injection Detection
- Request Rate Limiting
- Security Event Logging
- Dashboard Monitoring

## Technologies Used

- Python
- Flask
- Pandas
- HTML

## Project Structure

- detector.py
- logger.py
- rate_limiter.py
- app.py
- templates/
- logs/

## How To Run

```bash
pip install flask pandas
python app.py
```

Open:

http://127.0.0.1:5000
