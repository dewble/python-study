import pandas as pd

pd.set_option('display.max_column', None)

doc = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)
# print(doc.head())



# print(doc.shape)
# print(doc.info())
#
# print(doc.columns)

# print((doc.describe()))

# doc_open = doc['단지명']
# print(doc_open.head())

# doc_apartment = doc[['단지명', '전용면적(㎡)']]
# print(doc_apartment.head())

# doc_apt = doc[['단지명', '전용면적(㎡)']].copy()
# print(doc_apt.head())


# doc_row = doc[doc['단지명'] == '신동아']
# print(doc_row)

doc_month = doc.groupby('계약년월').count()
# print(doc_month.head())
print(doc_month.columns)
print(doc_month.index)