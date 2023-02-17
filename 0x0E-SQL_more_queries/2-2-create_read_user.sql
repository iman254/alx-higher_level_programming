--script that creates a database and a user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED BY 'User_0d_2_pwd';
GRANT SELECTED ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
