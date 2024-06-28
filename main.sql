#! /usr/bin/env mysql

-- make sure to fix edit the table name to 'media'
-- name the fixed .sql with -fixed suffix

CREATE DATABASE IF NOT EXISTS media_tagging;
USE media_tagging;

DROP TABLE IF EXISTS media;

CREATE TABLE IF NOT EXISTS media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    descriptionHebrew TEXT NOT NULL,
    descriptionEnglish TEXT NOT NULL,
    tags TEXT
);

SHOW TABLES;
source ./data/kalos-media-tagging-fixed.sql;

SELECT * FROM media WHERE id < 30;
