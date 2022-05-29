import sqlite3
import pandas as pd

def save_to_csv(table_name, file_name):
    conn = sqlite3.connect('class_sakila.db')
    SQL = "SELECT * FROM " + table_name
    dataframe = pd.read_sql(SQL, conn)
    conn.close()
    dataframe.to_csv(file_name + ".csv", encoding='utf-8-sig', index=False)
    return True

save_to_csv('film_category', 'film_category')