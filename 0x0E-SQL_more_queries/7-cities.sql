-- create database and table simultaneously with foreugn key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INTEGER NOT NULL AUTO_INCREMENT, state_id INTEGER NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY (state_id) REFERENCES states(id));
