import pandas as pd

doc = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)

df = pd.DataFrame({
    '영어': [60, 70],
    '수학': [100, 50]
}, index = ['Dave', 'David'])
# print(df)


# def func(df_data):
#     print (type(df_data))
#     print (df_data.index)
#     print (df_data.values)
#     return df_data
#
#
# df_func = df.apply(func, axis=1)


def func(df_data):
    df_data['영어'] = 80
    return df_data

df_func = df.apply(func, axis=1)
print(df_func)