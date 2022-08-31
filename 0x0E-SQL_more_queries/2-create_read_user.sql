-- create database and user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXITS 'hbtn_0d_2'
GRANT SELECT on 'hbtn_0d_2' to 'user_0d_2'@'localhost';
