# 💇‍♂️ SalonHub — Real-Time Salon Appointment Booking System

SalonHub is a **production-ready Salon Appointment Booking Web Application** built with **Django REST Framework (Backend)** and **React.js (Frontend)**.  

It supports **real-time booking workflows**, **JWT-based authentication**, **role-based access control**, and **asynchronous background processing using Celery**.

---

## 🚀 Key Highlights 

- 🔐 Secure Authentication using **JWT (SimpleJWT)**
- ⚡ Real-time booking & slot management
- 📧 Automated Email Notifications (Booking Confirmation / Updates)
- ⏰ Background Task Processing using **Celery + Celery Beat**
- 👨‍💼 Role-Based Access Control (Admin/User)
- 🧩 Scalable REST API Architecture
- 🗂 Clean Modular Django App Structure

---

## 🚀 Features

### 👤 User Side
- Register & Login (JWT Authentication)
- Browse services by **Male / Female categories**
- Explore subcategories (Hair, Facial, etc.)
- Add services to cart & dynamic price calculation
- Book appointments with **date & time slot selection**
- Receive **email confirmation after booking**
- View booking history (past & upcoming)

---

### 👨‍💼 Admin Side
- Custom Admin Panel (API-based, no default Django admin)
- Manage:
  - Gender Categories
  - Subcategories
  - Services
- Full CRUD operations via REST APIs
- View & manage all bookings
- Role-based secure endpoints

---

## ⚙️ Background Processing (Celery)

- 📅 Automated scheduling using **Celery Beat**
- ⏰ Tasks handled:
  - Appointment reminders
  - Booking status updates
  - Background email sending
- ⚡ Improves performance by offloading heavy tasks

---

## 📧 Email Integration

- Integrated Django Email Backend
- Features:
  - Booking confirmation emails
  - Appointment reminders
  - Admin notifications
- Supports SMTP configuration (Gmail / custom providers)

---

## 🏗️ Project Structure

SalonHub/
│
├── accounts/        # Authentication & user roles (JWT)
├── services/        # Category & service management APIs
├── booking/         # Appointment booking logic
├── scheduler/       # Celery & background tasks
├── backend/         # Django core (settings, urls)
├── media/           # Uploaded files
│
├── manage.py
├── requirements.txt
├── db.sqlite3
├── celerybeat-schedule
├── README.md

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Python 3.13, Django 5.2, Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Database | SQLite (Dev) / MySQL (Production) |
| Frontend | React.js |
| Async Tasks | Celery + Redis |
| Email | Django SMTP |
| Image Handling | Pillow |

---
1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/salon-management-system.git
cd salon-management-system
## 🧩 Installation & Setup

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver

⚡ Run Celery (Important)
celery -A backend worker --loglevel=info
celery -A backend beat --loglevel=info

🔐 Environment Variables (.env)
SECRET_KEY=your_secret_key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password

REDIS_URL=redis://127.0.0.1:6379/0


