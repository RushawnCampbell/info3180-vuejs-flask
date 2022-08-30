DROP DATABASE IF EXISTS skiptrace;
CREATE DATABASE skiptrace;

USE skiptrace;

GRANT ALL PRIVILEGES on *.* to skipuser1@localhost;

CREATE TABLE Users(
    user_id VARCHAR(255) PRIMARY KEY NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE accesskeys (
    user_id VARCHAR(255) PRIMARY KEY NOT NULL,
    password BLOB,
    CONSTRAINT user_access FOREIGN KEY (user_id) REFERENCES Users(user_id)
);