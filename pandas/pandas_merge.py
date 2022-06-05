import pandas as pd

pd

df_1 = pd.DataFrame({
    "id":[1,2,3],
    "customer_id": [1,2,3],
    "customer_name":["JM","Rucia","Dewble"]
}, columns=["id","customer_id", "customer_name"]
)

df_2 = pd.DataFrame({
    "id": [1,2,4],
    "order_id": [100,200,300],
    "order_date": ["2021-01-21", "2021-02-03", "2020-10-01"]
}, columns=['id', 'order_id', 'order_date']
)

# print(pd.concat([df_1,df_2], axis=1))

# print(pd.merge(df_1, df_2, on="id"))
# print(pd.merge(df_1, df_2, on='id', how='outer'))
# print(pd.merge(df_1, df_2, on='id', how='left'))
# print(pd.merge(df_1, df_2, on='id', how='right'))

df_1 = df_1.set_index("id")
df_2 = df_2.set_index("id")

print(pd.merge(df_1, df_2, how="outer", left_index=True, right_index=True))