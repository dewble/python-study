import sqlite3
import pandas as pd

def get_data_join(SQL):
    conn = sqlite3.connect('class_join.db')
    cur = conn.cursor()
    dataframe = pd.read_sql(SQL, conn)
    conn.close()
    return dataframe



print(get_data_join("SELECT * FROM customer_table"))
print(get_data_join("SELECT * FROM order_table"))
print(get_data_join("""
select * 
from customer_table as ct 
LEFT OUTER JOIN order_table as ot 
ON ct.customer_id = ot.customer_id
"""))

