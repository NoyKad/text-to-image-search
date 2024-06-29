import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(
            host="127.0.0.1", 
            user="root",
            password="5019",
            database='media_tagging',
            use_pure=True
            )
    
    query = "Select * from media;"
    result_dataFrame = pd.read_sql(query, mydb)

    result_dataFrame.to_csv('../data/media.csv')

    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))
