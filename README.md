# Online Gym Management System

A web-based Online Gym Management System developed using Python and Django to simplify and automate gym operations such as member management, trainer management, membership plans, and payment tracking. The system provides secure role-based authentication for Admin, Trainer, and Member users along with responsive dashboards and database management using SQL . Designed with HTML, CSS, Bootstrap, and Django ORM, the project offers an efficient, user-friendly, and scalable solution for modern fitness centers.

## Technology Stack and Tools Used 

### Programming Language 
Python 3.x
### Framework 
Django
### Frontend Technologies
HTML5, CSS, Bootstrap, JavaScript
### Database 
SQLite , MySQL
### Development Tools 
Visual Studio Code (VS Code), PyCharm
### Version Control 
Git & GitHub

## Features and Functionalities

1. **User Registration & Login Authentication**  
   Allows users to securely register, log in, and access the system using authenticated credentials.

2. **Role-Based Dashboards (Admin, Trainer, Member)**  
   Provides separate dashboards and functionalities based on user roles for better access control and management.

3. **Member Management System**  
   Enables adding, updating, viewing, and deleting member records efficiently.

4. **Trainer Management**  
   Allows management of trainer details, assignments, and related information.

5. **Membership Plan Management**  
   Supports creation and management of different gym membership plans with pricing and duration.

6. **Payment Tracking & Records**  
   Maintains payment history, transaction details, and membership payment status.

7. **Secure Database Management using Django ORM**  
   Uses Django ORM for secure and efficient database operations without complex SQL queries.

8. **Responsive and User-Friendly Interface**  
   Provides a clean, modern, and mobile-friendly user interface for smooth user experience.

9. **CRUD Operations (Add, Update, Delete, View)**  
   Implements complete CRUD functionality for managing gym-related data dynamically.

## Installation / Execution Steps to Run the Project

### 1. Clone the Repository
Open terminal or command prompt and clone the GitHub repository:

```bash
git clone <repository-link>
```

---

### 2. Navigate to the Project Directory

```bash
cd GYM_Management_System
```

---

### 3. Open the Project
Open the project folder in any IDE such as:
- Visual Studio Code (VS Code)
- PyCharm

---

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 5. Activate the Virtual Environment

#### For Windows:
```bash
venv\Scripts\activate
```

#### For Linux/macOS:
```bash
source venv/bin/activate
```

---

### 6. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

### 7. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 8. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Enter username, email, and password for admin access.

---

### 9. Run the Django Development Server

```bash
python manage.py runserver
```

---

### 10. Open the Application
Open any web browser and visit:

```bash
http://127.0.0.1:8000/
```

---

### 11. Login to the System
- Register a new account or
- Login using admin/member credentials to access dashboards and features.

## Academic Team and Project Guidance
This project was developed as a B.Tech III-Year Minor Project in Computer Science and Engineering at Medi-Caps University, Indore.

## Project Mentors and Guides
- Prof. Arjun Dixit
- Prof. Rashmi Vijayvargiya

## Team Member 
Tanvi Patil (Enrollment Number: EN23CS3011077)

## Institution Details
- Department of Computer Science and Engineering
- Faculty of Engineering, Medi-Caps University, Indore - 453331
- Date of Submission: April 2026

