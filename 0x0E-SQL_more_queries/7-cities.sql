-- create database and table simultaneously with foreugn key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
  id INTEGER AUTO_INCREMENT,
  state_id INTEGER NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (state_id)
  REFERENCES states(id));
