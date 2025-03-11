import sqlite3
from contextlib import closing


db_path="sqlite.db"

try:
    with closing(sqlite3.connect(db_path)) as db_con:
        db_con.row_factory = sqlite3.Row
        with closing(db_con.cursor()) as cursor:
        try:
            query_1 = "SELECT * FROM demo where id > 14:"
            cursor.execute(query_1)
            rows = cursor.fetchall()
            for row in rows:
                print(row["name"])
        except Exception as e:
            print(f"Error excuting query_1: {e}")
        try:
            del_row=input("Enter the row ID threshold for deletion:")
            
        except:    
except ValueError as e:
    print("--")
