# Appointment Booking System

This project is a web-based appointment booking system with a **Django REST API** backend and a **vanilla JavaScript**, **HTML**, and **CSS** frontend. It allows users to check available time slots for a given date and book appointments, demonstrating a full-stack application built without relying on heavy frontend frameworks.

---

## Project Overview

The goal of this project was to create a functional booking system using minimal dependencies, showcasing my skills in **backend development (Django REST Framework)**, **frontend development (vanilla JS)**, and integrating the two via **RESTful APIs**. The system is lightweight, easy to set up, and includes basic error handling and validation.

---

## Key Features

- **Check Available Slots**: Users can input a date to view available 30-minute time slots (10:00 AM–5:00 PM, excluding a 1:00 PM–2:00 PM break).
- **Book an Appointment**: Submit a form with name, phone number, date, and time to reserve a slot, with validation to prevent double-booking.
- **Real-Time Feedback**: The frontend dynamically updates available slots based on existing bookings.
- **Simple, Responsive UI**: Built with pure HTML/CSS/JS for a clean, framework-free experience.
- **RESTful API**: Backend provides endpoints for slot availability and booking operations.

---

## Tech Stack

- **Backend**: Django 4.2.7, Django REST Framework, SQLite
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Tools**: Python 3.12, Git

---

## Project Structure

BOOKING-SYSTEM/ ├── backend/ # Django backend │ ├── appointments/ # Main app (settings, URLs) │ ├── booking/ # Booking app (models, views, URLs) │ ├── db.sqlite3 # SQLite database │ ├── manage.py # Django management script │ └── requirements.txt # Python dependencies ├── frontend/ # Frontend files │ ├── index.html # Main page │ ├── styles.css # Styling │ └── script.js # Logic for API calls and UI updates └── README.md # This documentation

yaml
Copy

---

## Prerequisites

- **Python 3.12+**: Required for the Django backend.
- **pip**: To install dependencies.
- **Git**: For cloning and version control.
- **Web Browser**: Chrome recommended (see Known Issues for Brave).

---

## How to Run Locally

Follow these steps to set up and run the application on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/booking-system.git
cd booking-system
2. Set Up the Backend
Create a Virtual Environment (optional but recommended):
bash
Copy
python -m venv venv
source venv/bin/activate  
Install Dependencies:
bash
Copy
cd backend
pip install -r requirements.txt
Apply Database Migrations:
bash
Copy
python manage.py makemigrations
python manage.py migrate
Start the Backend Server:
bash
Copy
python manage.py runserver
The backend will run at http://127.0.0.1:8000/.

3. Running the Frontend
To test the frontend, open the frontend folder and start an HTTP server:

bash
Copy
cd frontend
python3 -m http.server 8001
This will run the frontend at http://127.0.0.1:8001/.