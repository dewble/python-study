import pandas as pd

doc = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)

# print(doc.columns)


doc.columns = ['시군구', '번지', '본번', '부번', '단지명', '전용면적', '계약년월', '계약일', '거래금액', '층', '건축년도', '도로명']

# print(doc.columns)

doc = doc[['단지명', '전용면적', '계약년월', '계약일', '거래금액', '층', '건축년도', '도로명', '시군구', '번지', '본번', '부번']]
print(doc.head())
