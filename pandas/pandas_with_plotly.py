import pandas as pd
import plotly.graph_objects as go

pd.set_option('display.max_column', None)

datafile_list = ['아파트(매매)__실거래가_20050901_20060831.csv',
'아파트(매매)__실거래가_20060901_20070831.csv',
'아파트(매매)__실거래가_20070901_20080831.csv',
'아파트(매매)__실거래가_20080901_20090831.csv',
'아파트(매매)__실거래가_20090901_20100831.csv',
'아파트(매매)__실거래가_20100901_20110831.csv',
'아파트(매매)__실거래가_20110901_20120831.csv',
'아파트(매매)__실거래가_20120901_20130831.csv',
'아파트(매매)__실거래가_20130901_20140831.csv',
'아파트(매매)__실거래가_20140901_20150831.csv',
'아파트(매매)__실거래가_20150901_20160831.csv',
'아파트(매매)__실거래가_20160901_20170831.csv',
'아파트(매매)__실거래가_20170901_20180831.csv',
'아파트(매매)__실거래가_20180901_20190831.csv',
'아파트(매매)__실거래가_20190901_20200831.csv']

## 아래 df가 기준
doc_merge = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)

## datafile의 리스트를 받아 기준 df에 합친다
for filename in datafile_list[1:]:
    doc = pd.read_csv("01_data/" + filename, encoding='utf-8-sig', error_bad_lines=False)
    doc_merge = pd.concat([doc_merge, doc])

# print(doc_merge.shape)
# print(doc_merge.head())


## replace, apply() 작성
def func(item):
    string_data = item.replace(",", "")
    return string_data


doc_merge['거래금액(만원)'] = doc_merge['거래금액(만원)'].apply(func)
# print(doc_merge.info())


# ## 컬럼명 변경하기
# doc_merge = doc_merge.astype({"거래금액(만원)":"int64"})
# print(doc_merge.info())


## 컬럼명 변경하기
doc_merge.columns = ['시군구', '번지', '본번', '부번', '단지명', '전용면적(㎡)', '계약년월', '계약일', '거래금액', '층', '건축년도', '도로명']
# print(doc_merge.info())

## 그룹핑
doc_count = doc_merge.groupby('계약년월').count()

# print(doc_count.head())


## datatype 변경
doc_count.index = pd.to_datetime(doc_count.index, format='%Y%m', errors='raise')
# print(doc_count.info())


## 바 그래프 그리기
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=doc_count.index, y=doc_count['시군구']
    )
)
fig.show()