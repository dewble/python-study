import sqlite3

# ## create table
# conn = sqlite3.connect('class.db')
# cur = conn.cursor()
# cur.execute("CREATE TABLE private(name TEXT, phone TEXT, address TEXT)") # 여기에 SQL 구문만 변경하면, 데이터베이스 제어 가능
# conn.commit()
# conn.close()

# ## insert data
# conn = sqlite3.connect('class.db')
# cur = conn.cursor()
# cur.execute("INSERT INTO private (name, phone, address) VALUES ('Dave', '01000001111', '서울시')")
# conn.commit()
# conn.close()


# ## select문 사용하기
# conn = sqlite3.connect('class.db')
# cur = conn.cursor()
# cur.execute("select * from private")
#
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# for row in rows:
#     print(row[0],row[1] )
#
# print(rows)
# conn.close()

# ## update문 사용하기
# conn = sqlite3.connect("class.db")
# cur = conn.cursor()
# cur.execute("UPDATE private SET name='JM' WHERE name = 'Dave' AND address = '서울시'")
# conn.commit()
#
# cur.execute("select * from private")
#
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# ## delete문 사용하기
# conn = sqlite3.connect('class.db')
# cur = conn.cursor()
# cur.execute("DELETE FROM private")
# conn.commit()    # 데이터 변경이므로 conn.commit() 를 해줌
#
# cur.execute("select * from private")
#
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# conn.close()

# ## 테이블 정보 조회
# conn = sqlite3.connect('class.db')
# cur = conn.cursor()
# cur.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.close()

# ## 제약조건과 함께 테이블 만들기
# import sqlite3
#
# conn = sqlite3.connect('class.db')
# cur = conn.cursor()
# # cur.execute("CREATE TABLE grade3 (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT, address TEXT)") # 여기에 SQL 구문만 변경하면, 데이터베이스 제어 가능
# # cur.execute("INSERT INTO grade3 (name, phone, address) VALUES ('Dave', '01000001111', '서울시')")
# conn.commit()
#
# cur.execute("SELECT * FROM grade3")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#
# conn.close()

## sqlite와 pandas
import sqlite3
import pandas as pd

conn = sqlite3.connect('class.db')

SQL = "SELECT * FROM grade3"
df = pd.read_sql(SQL,conn)

print(df)