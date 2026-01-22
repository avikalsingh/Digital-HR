# Digital-HR

Digital-HR is a Django-based HR management web application that provides an admin-driven interface for managing employees, jobseekers, master data, contact inquiries, and email communication.

The project emphasizes **backend correctness, authentication, environment-based configuration, and secure handling of credentials**, making it suitable as a portfolio project for backend / full-stack software engineering roles.

---

## Features

### Authentication & Admin Access
- Admin login and logout
- Password change functionality
- Admin-only protected routes

### Employee Management
- Employee registration
- View, update, and delete employee records

### Master Data Management
- City management
- Qualification management

### Jobseeker Module
- Jobseeker registration and management
- Admin review and deletion

### Contact & Email
- Contact form handling
- Admin contact inbox
- Email generation and sending using SMTP

### Configuration & Security
- Environment-based configuration using `.env`
- No secrets committed to version control
- SQLite used for local development

---

## Screenshots

<p align="center">
  <img src="./screenshots/Home Page.png" width="800" alt="Home Page"/>
</p>

<p align="center">
  <img src="./screenshots/Admin Login.png" width="800" alt="Admin Login"/>
</p>

<p align="center">
  <img src="./screenshots/Admin Home.png" width="800" alt="Admin Dashboard"/>
</p>

<p align="center">
  <img src="./screenshots/Employee Mgmt.png" width="800" alt="Employee Management"/>
</p>

<p align="center">
  <img src="./screenshots/Employee Registration.png" width="800" alt="Employee Registration"/>
</p>

<p align="center">
  <img src="./screenshots/Send Email.png" width="800" alt="Email Generation"/>
</p>

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates (HTML, CSS)
- **Database:** SQLite (development)
- **Authentication:** Django Auth
- **Email:** SMTP (Gmail App Password supported)
- **Configuration:** Environment variables via `python-dotenv`

---

## Project Structure

```text
Digital-HR/
├── Training_Project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── static/
├── screenshots/
├── .env.example
├── requirements.txt
└── manage.py
