# 🔐 User Authentication System

A Flask-based User Authentication System with secure user login and password reset functionality using OTP verification. This project demonstrates user authentication, email verification, password reset workflow, and database integration.

---

## 🌐 Live Demo

**Application:** https://user-authentication-system-oa3s.onrender.com

---

## 🚀 Features

- User Login Authentication
- Forgot Password Functionality
- OTP Verification via Email
- Reset Password
- SQLAlchemy Database Integration
- Bootstrap Responsive UI
- Flask-Mail Email Support
- Environment Variable Configuration using `.env`

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Mail
- SQLite / MySQL
- HTML5
- CSS3
- Bootstrap 5
- SQLAlchemy
- python-dotenv
- Gunicorn

---

## 📂 Project Structure

```
User-Authentication-System/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── login.html
│   ├── forgot_password.html
│   ├── verify_otp.html
│   ├── reset_password.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── utils/
    └── email_utils.py
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Aryan457-dev/User-Authentication-System.git
```

Navigate to the project directory

```bash
cd User-Authentication-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

DB_HOST=localhost
DB_NAME=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

---

## ▶️ Run the Application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

---

## 🔄 Password Reset Workflow

1. User enters registered email.
2. OTP is sent to the email.
3. User verifies the OTP.
4. User sets a new password.
5. User logs in with the updated password.

---

## 📸 Screenshots

- Login Page
- Forgot Password
- OTP Verification
- Reset Password
- Dashboard

---

## 📌 Future Improvements

- Password hashing using Werkzeug
- User Registration
- JWT Authentication
- Session Management
- Password Strength Validation
- Profile Management

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Aryan Dabholkar**
