-- =====================================================
--  Run this file FIRST before starting app.py
--  In MySQL Workbench: File > Open SQL Script > Run
-- =====================================================

CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id      INT          NOT NULL AUTO_INCREMENT,
    name    VARCHAR(100) NOT NULL,
    roll_no VARCHAR(20)  NOT NULL UNIQUE,
    course  VARCHAR(50)  NOT NULL,
    email   VARCHAR(100) NOT NULL,
    phone   VARCHAR(15)  NOT NULL,
    PRIMARY KEY (id)
);

-- Sample data (optional — delete if not needed)
INSERT IGNORE INTO students (name, roll_no, course, email, phone) VALUES
('Prajwal Sharma',  'CS2024001', 'B.Tech CSE', 'prajwal@example.com', '9876543210'),
('Ananya Desai',    'CS2024002', 'B.Tech IT',  'ananya@example.com',  '9876543211'),
('Rohan Patil',     'EC2024001', 'B.Tech ECE', 'rohan@example.com',   '9876543212');

SELECT * FROM students;
