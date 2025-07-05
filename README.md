# 🔐 Secure Incident Reporting & Response System

A secure, encrypted digital platform for **anonymous reporting**, **sentiment analysis**, and **case tracking** of harassment, abuse, or misconduct incidents in educational institutions, workplaces, or communities.

---

## 🎯 Key Features

- ✅ **User Authentication** — Secure signup/login for institution members.
- ✅ **End-to-End Encryption** — Users submit reports which are encrypted with a fernet key.
- ✅ **Sentiment Analysis** — Automated sentiment scoring to detect urgency/distress.
- ✅ **Location Tagging** — Adds location data for context.
- ✅ **Personal Report History** — Users can view only their own reports.
- ✅ **Reviewer Dashboard (Admin)** — Staff can decrypt & review all reports, update status.
- ✅ **Status Tracking** — Track case progress via status field.
- ✅ **Future Scope** — 24/7 AI chatbot, predictive analytics, notifications.

---

## 💡 Why This Project?

This project tackles the *real-world need* for a **safe, private, and structured channel** for reporting harassment or misconduct within institutions.  
It empowers victims or witnesses to **speak up securely** and ensures staff can respond responsibly and effectively.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Django REST Framework |
| **Frontend** | Flutter |
| **Database** | SQLite / PostgreSQL (configurable) |
| **Authentication** | Token-based, role-based access |
| **Encryption** | AES / Fernet for sensitive fields |

---

## 📍 How It Works

**1️⃣ Users**
- Register & login
- Submit reports with title, description, and location
- View only *their* submitted reports & statuses

**2️⃣ Reviewers/Admins**
- Login via Django Admin
- Decrypt & view all reports
- See sentiment scores & locations
- Update report status manually

---

## 🗂️ Project Structure

gbv_system/
├── accounts/ # User auth: signup, login
├── reports/ # Models, encryption, sentiment analysis
├── api/ # Django REST API
├── flutter_app/ # Flutter frontend (submit & view reports)
├── manage.py
├── requirements.txt
├── README.md

## 🚀 Setup Instructions
1️⃣ Backend

```
# Clone the repo
git clone <your_repo_url>
cd gbv_system

# Create & activate virtualenv
python -m venv env
source env/bin/activate  # Or `env\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Make migrations & run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 2️⃣ Frontend

```
# Go to your Flutter app directory
cd flutter_app

# Install dependencies
flutter pub get

# Run the app
flutter run
```

## 🔐 Environment Variables
- Create a .env file or use settings.py for sensitive configs:

- SECRET_KEY

- FERNET_KEY (for encryption)

- Database config

---

## 🚀 Future Enhancements
- 🤖 AI-powered chatbot for real-time counseling & FAQ

- 📲 Push notifications for reviewers/admins

- 📈 Analytics dashboard for institutions

- 📧 Institution-only email sign-up

## 📜 License
This project is licensed under the MIT License — feel free to use and modify it!

## ✨ Author
Nikita Sanganeria
nikitasanganeria1@gmail.com

