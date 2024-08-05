import os

from dotenv import load_dotenv
import mysql.connector as connection
import pandas as pd

load_dotenv()

try:
    mydb = connection.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        use_pure=True
    )
    
    query = "Select * from media;"
    result_dataFrame = pd.read_sql(query, mydb)

    result_dataFrame.to_csv('../data/media.csv')

    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))
