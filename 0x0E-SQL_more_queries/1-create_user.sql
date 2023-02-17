--create and assign priveleges for user_0d_0
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVELAGE ON "." TO 'user_0d_1'@'localhost';
