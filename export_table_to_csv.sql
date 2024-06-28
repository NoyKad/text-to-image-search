-- export "media" table to csv file and add header
USE media_tagging;

SELECT 'url', 'descriptionHebrew', 'descriptionEnglish', 'tags'
UNION ALL
SELECT url, descriptionHebrew, descriptionEnglish, tags
    FROM media
    INTO OUTFILE '/var/lib/mysql-files/media.csv';