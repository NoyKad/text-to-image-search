-- export "media" table to csv file
USE media_tagging;
SELECT * FROM media
INTO OUTFILE '/var/lib/mysql-files/media.csv'
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n';
