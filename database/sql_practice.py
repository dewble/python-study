import sqlite3
import pandas as pd

# ## 쿼리로 데이터 가져오가
# conn = sqlite3.connect('class_sakila.db')
# cur = conn.cursor()
# cur.execute("SELECT tbl_name FROM sqlite_master WHERE type = 'table'")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# conn.close()
#

## pandas DataFrame으로 데이터 가져오기

# conn = sqlite3.connect('class_sakila.db')
#
# SQL = "SELECT tbl_name FROM sqlite_master WHERE type = 'table'"
# df = pd.read_sql(SQL, conn)

# print(df)


def get_data(SQL):
    conn = sqlite3.connect('class_sakila.db')
    dataframe = pd.read_sql(SQL, conn)
    conn.close()
    return dataframe

print(get_data("SELECT * FROM film LIMIT 1"))