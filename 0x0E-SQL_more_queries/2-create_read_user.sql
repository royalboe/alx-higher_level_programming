-- create the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- create read-only user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant user_0d_2 read-only permissions
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
