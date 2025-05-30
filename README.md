# Sensitive Data Loss Prevention System

A comprehensive Python-based system designed to detect, prevent, and alert on the leakage of sensitive data such as credit card numbers, personally identifiable information (PII), and confidential documents. This system leverages asynchronous task processing with Celery, Redis as a message broker, and SMTP for sending alert emails.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Multi-format document parsing:** Support for PDF, DOCX, and text files.
- **Sensitive data detection:** Uses regex patterns and machine learning detectors.
- **Asynchronous processing:** Tasks are handled via Celery workers and Redis queues.
- **Email notifications:** Alerts sent automatically when sensitive data is detected.
- **Configurable:** Easy to customize SMTP, Redis, database, and scanning parameters.
- **Logging & Persistence:** Scan results and alerts are logged in SQLite database.

---

## Architecture

User Upload/Trigger Task
↓
Celery Worker ←──────── Redis Broker ─────────→ Task Queue
↓
Sensitive Data Scanner (Regex + ML)
↓
Alert Email Sender (SMTP)
↓
Scan Results Logged (SQLite)


---

## Tech Stack

- **Python 3.13+**
- **Celery:** Distributed task queue for asynchronous job processing.
- **Redis:** Message broker to queue tasks.
- **SQLite:** Lightweight database for storing scan logs and alerts.
- **SMTP:** Email protocol used for sending alert notifications.
- **Pydantic:** Configuration management with environment variable support.
- **Additional libraries:** pdfminer, python-docx for parsing documents.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Amegh3/data-loss-prevention-.git
   cd data-loss-prevention-

    Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows

Install dependencies:

pip install -r requirements.txt

Ensure Redis is installed and running:

    On Linux/macOS:

    redis-server

    On Windows, consider using Redis for Windows.

Configure environment variables or update app/config.py:

Example .env file:

    SECRET_KEY=your_super_secret_key
    SMTP_SERVER=sandbox.smtp.mailtrap.io
    SMTP_PORT=587
    SMTP_USER=your_smtp_username
    SMTP_PASSWORD=your_smtp_password
    REDIS_URL=redis://localhost:6379/0
    DATABASE_URL=sqlite+aiosqlite:///./dlp.db

Configuration

All configuration settings are managed in app/config.py using Pydantic’s BaseSettings. You can override defaults using environment variables or a .env file:
Setting	Description	Default
SECRET_KEY	Secret key for security	supersecretkey
ALGORITHM	JWT algorithm	HS256
ACCESS_TOKEN_EXPIRE_MINUTES	Token expiration time (minutes)	1440 (1 day)
SMTP_SERVER	SMTP mail server	smtp.example.com
SMTP_PORT	SMTP server port	587
SMTP_USER	SMTP authentication username	user@example.com
SMTP_PASSWORD	SMTP authentication password	emailpassword
REDIS_URL	Redis connection string	redis://localhost:6379/0
DATABASE_URL	Database connection string	sqlite+aiosqlite:///./dlp.db
Usage

    Start Redis server:

redis-server

Run the Celery worker:

celery -A celery_worker worker --loglevel=info

Trigger a scan task manually:

    python trigger_task.py

    View logs or database entries to monitor detected sensitive data and alerts.

Project Structure

.
├── app
│   ├── api
│   ├── core
│   │   ├── alerting.py          # Email alert functions
│   │   ├── detectors            # Regex and ML-based detection logic
│   │   ├── parsers             # Document parsing modules (PDF, DOCX)
│   │   ├── scanner.py           # Core scanning logic
│   │   └── tasks.py             # Celery task definitions
│   ├── config.py                # Application settings (Pydantic)
│   ├── db                      # Database models and session
│   ├── main.py                 # FastAPI app entry point (if applicable)
│   └── models.py               # Pydantic models/schema
├── celery_worker.py             # Celery worker starter
├── requirements.txt             # Python dependencies
├── trigger_task.py              # Script to trigger scan tasks
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules

Contributing

Contributions are welcome! Feel free to:

    Report issues

    Suggest new features

    Submit pull requests

Please ensure you follow the existing coding style and add tests where applicable.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

Created and maintained by Amegh3.

For questions or collaboration, please open an issue or contact via GitHub.

Thank you for using the Sensitive Data Loss Prevention System!
