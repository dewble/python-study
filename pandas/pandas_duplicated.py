import pandas as pd

df = pd.DataFrame({
    '영어': [60, 60],
    '수학': [60, 80],
}, index = ['Dave', 'David'])


# print( df.duplicated(['영어']))
print(df.drop_duplicates(subset='영어', keep='last'))