import pandas as pd

# ## create Series
# szdata = pd.Series([11,22,33])
# print(szdata)
#
# ## index 변경
# szdata2 = pd.Series([11,22,33], index=['A','B','C'])
# print(szdata2)

# ## read series
# szdata3 = pd.Series([11,22,33], index=['가','나','다'])
# print(szdata3)
#
# ## update Series
# szdata3.index = ['가', '나', '다']
# print(szdata3)

# ## Series value 가져오기
# print(szdata3.values)
# print(szdata3['가'])
# print(szdata3[0])
#
# ## value update 하기
# szdata3['가'] = 55
# print(szdata3['가'])
#
# szdata3[0] = 66
# print(szdata3['가'])

# ## delete Series
# szdata4 = pd.Series([11,22,33], index=['가','나','다'])
# print(szdata4)
#
# del szdata4['나']
# print(szdata4)
#
# ## change data type in Series
# data_type = pd.Series([1,2,3])
# print(data_type)
# print(data_type.astype('float'))

# ## create df
# df = pd.DataFrame({
#     "bench": [175, 185, 195],
#     "squat": [325, 335, 355],
#     "dead": [345, 355, 365]
# })
# print(df)

# ## create df with index
# df = pd.DataFrame({
#     "bench": [175, 185, 195],
#     "squat": [325, 335, 355],
#     "dead": [345, 355, 365]},
#     index=['1차','2차','3차']
# )
#
# ## read and update df
# print(df.index)
#
# # 행 방향 index 변경
# df.index=['4차','5차','6차']
# print(df)
#
# # 열 방향 index 변경
# print(df.columns)
# df.columns=["clean","snatch","shoulder press"]
# print(df)
#
# # read value
# print(df.values)


## index로 특정 컬럼 선택하기
df = pd.DataFrame({
    "이름": ["A","B","C"],
    "bench": [175, 185, 195],
    "squat": [325, 335, 355],
    "dead": [345, 355, 365]},
)
# print(df)

# df = df.set_index("이름")
# # print(df)
#
# print(df.index.name)
#
# df.index.name = 'athlete'
# print(df)
#
# print(df)
#
# df = df.reset_index("이름")
# print(df)

## 데이터프레임 특정 행 가져오기
# df = df.set_index("이름")
# print(df.loc["A"])
#
# df = df.reset_index("이름")
# print(df.iloc[0])

# ## 데이터프레임 특정 칼럼 가져오기
# print(df)
# print(type(df['bench']))
# print(df['bench'])
# print(df['bench'][0])
# print(df.loc[0]['bench'])

# ## Dataframe 컬럼 추가 - Update
# print(df)
# df['shoulder'] = [135,145,155]
# print(df)
#
# ## Dataframe 컬럼 삭제 - Delete
# del df['bench']
# print(df)

# ## Dataframe 행 추가 - Update
# df = df.set_index("이름")
# df.loc["A"] = [135, 235, 300]
# print(df)
#
# ## Dataframe 행 삭제 - Delete
# df = df.drop(["C"])
# print(df)

## Dataframe 특정 컬럼 복사(선택) - copy()
print(df)
df = df.set_index("이름")

df2 = df[['squat','dead']].copy()
print(df2)