Student Database Management System (SDMS)

A web-based Student Database Management System built using Python, Flask, MySQL, HTML, and CSS. This application helps manage student records efficiently through a simple and user-friendly interface. It allows users to perform complete CRUD (Create, Read, Update, Delete) operations on student data stored in a MySQL database.

Features

Add new student records
View all students in a structured table
Search students by name or roll number
Update existing student information
Delete student records
MySQL database integration
Responsive and easy-to-use interface
Flask-based backend with secure database operations

Tech Stack

Backend: Python, Flask
Database: MySQL
Frontend: HTML, CSS
Database Connector: mysql-connector-python

Project Structure
StudentDBMS/
│
├── app.py
├── database.sql
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
└── static/
    └── style.css
    
Installation

Clone the repository
Install dependencies
pip install -r requirements.txt
Create the MySQL database using database.sql
Update database credentials in app.py
Run the application
python app.py
Open your browser and visit:
http://localhost:5000

Learning Outcomes

Flask web development
CRUD operations with MySQL
Database connectivity using Python
Form handling and validation
Web application development fundamentals
