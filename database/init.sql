-- Create Database
CREATE DATABASE IF NOT EXISTS taskdb;

USE taskdb;

-- Create Tasks Table
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample Data
INSERT INTO tasks (title) VALUES
('Learn Docker'),
('Build Flask API'),
('Practice Docker Compose'),
('Deploy with Kubernetes');
