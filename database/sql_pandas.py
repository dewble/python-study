import sqlite3
import pandas as pd

# conn = sqlite3.connect('class_sakila.db')
# cur = conn.cursor()
#
# with open('sqlite-sakila-schema.sql', 'r', encoding='utf-8') as create_file:
#     create_query = create_file.read()
# with open('sqlite-sakila-insert-data.sql', 'r', encoding='utf-8') as insert_file:
#     insert_query = insert_file.read()
#
# # cur.executescript(create_query)
# # cur.executescript(insert_query)
#
# conn.commit()
# # conn.close()
#
# # # 테이블 확인하기
# # cur.execute("SELECT tbl_name, sql FROM sqlite_master WHERE type = 'table'")
# # rows = cur.fetchall()
# #
# # for row in rows:
# #     print(row)
#
# # 테이블 확인하기
# cur.execute("SELECT * from actor")
# rows = cur.fetchall()
#
# for row in rows:
#     print(row)

## pandas Dataframe 으로 데이터 가져오기
conn = sqlite3.connect('class_sakila.db')
SQL = "SELECT tbl_name, sql FROM sqlite_master WHERE type = 'table'"
df = pd.read_sql(SQL, conn)
conn.close()

# print(df)

for item in range(len(df['sql'])):
    print (df['sql'][item])
