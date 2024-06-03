-- Active: 1716681595456@@127.0.0.1@3306
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL
);

-- SQL for creating the Task table
CREATE TABLE Task (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    date VARCHAR(10) NOT NULL,
    user_id INTEGER NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY(user_id) REFERENCES user(id)
);
