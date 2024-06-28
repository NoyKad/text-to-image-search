# .sql file to pandas dataframe
# head example:
# /*
# -- Query: SELECT * FROM llm_sql.copy_metadata limit 10000
# -- Date: 2024-05-05 17:56
# */
# INSERT INTO `` (`url`,`descriptionHebrew`,`descriptionEnglish`,`tags`) VALUES ('https://storage.googleapis.com/press-office-dev-storage-bucket-images/003e8fca-4741-4c5f-bdda-0c20bfdee581.jpg','ביקור ראש הממשלה יצחק רבין באנדרטה לזכר הנופלים בבקעת הירדן, ליד מושב פצאל.','P.M. YITZHAK RABIN STANDING NEXT TO THE MEMORIAL  NEAR MOSHAV PATZAEL ERECTED IN MEMORY OF THE FALLEN IN THE  BATTLES FOR THE JORDAN RIFT.','{\"tags\": [\"1.4\", \"יצחק רבין\", \"רחבעם זאבי\", \"בקעת הירדן\", \"אנדרטה\", \"ביקור\", \"סיור\", \"פצאל\", \"מושב פצאל\"]}');
# INSERT INTO `` (`url`,`descriptionHebrew`,`descriptionEnglish`,`tags`) VALUES ('https://storage.googleapis.com/press-office-dev-storage-bucket-images/00428fb4-4982-446d-bac9-297cb11ffe06.jpg','שער ציון בעיר העתיקה בירושלים.','ZION GATE IN THE OLD CITY OF JERUSALEM.            (COURTESY OF AMERICAN COLONY)','{\"tags\": [\"JERUSALEM\", \"OLD CITY\", \"CITY\", \"ZION GATE\", \"ARAB\"]}');
# INSERT INTO `` (`url`,`descriptionHebrew`,`descriptionEnglish`,`tags`) VALUES ('https://storage.googleapis.com/press-office-dev-storage-bucket-images/0064e90a-30df-46d2-adba-9305758a9b60.jpg','צילום אויר של איזור המגורים לחוף העיר אשקלון.','ASHKELON RESIDENTIAL NEIGHBORHOOD ADJACENT TO THE BEACH.','{\"tags\": [\"אשקלון\", \"עיר\", \"חוף\", \"ים\", \"צילום אויר\", \"ים התיכון\", \"נוף\"]}');
# INSERT INTO `` (`url`,`descriptionHebrew`,`descriptionEnglish`,`tags`) VALUES ('https://storage.googleapis.com/press-office-dev-storage-bucket-images/007840e9-00aa-41be-b66d-edf14eb5a3b0.jpg','','2015 Rhythmic Gymnastics Championship held in Israel, Jerusalem Sports Hall.?????? ????? ???????? ???????? ???? 2015, ???? ?????? ????????.','{\"tags\": [\"Rhytmic Gymnastics\", \"sports\", \"??????? ????????\", \"?????\", \"????\", \"ball\"]}');
# INSERT INTO `` (`url`,`descriptionHebrew`,`descriptionEnglish`,`tags`) VALUES ('https://storage.googleapis.com/press-office-dev-storage-bucket-images/0089e9ed-774e-440a-a8a5-b69b9537ddc0.jpg','','MEMBERS OF \"GUSH-EMUNIM\" OUTPOST NEAR ELKANA.','{\"tags\": [\"9.3\", \"גוש אמונים\", \"אלקנה\", \"מתפללים\", \"מתנחלים\", \"התיישבות\", \"תפילה\", \"דתיים\"]}');

import re

data = {'url': [], 'descriptionHebrew': [], 'descriptionEnglish': [], 'tags': []}

with open('./data/kalos-media-tagging.sql') as f:
    for line in f:
        if line.startswith('INSERT INTO'):
            values = re.findall(r"VALUES \((.*?)\);", line)[0].split(',')
            print(values)
            break