-- create database and table simultaneously
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXITS hbtn_0d_usa.states(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
