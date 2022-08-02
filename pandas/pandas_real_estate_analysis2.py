import pandas as pd
import pickle
import plotly.graph_objects as go

pd.set_option('display.max_column', None)

"""
1. datafile list 을 만들고
1.1. pickle 라이브러리를 사용하여 파일로 저장, 불러오기
2. apartment 에 반복문을 사용해서 데이터를 넣는다. concat 함수 사용
3. head를 보면 계약년월을 보면 월별로 그룹핑을 할 수 있다.
4 .info로 index를 확인해 보면 int64Index이다. > datetime type으로 변경해줘야 한. 아니면 그래프가 날짜를 인지 못한다
5. 그래프를 그려보면 월별 거래 건수를 확인할 수 있다.     
6. index를 삭제하고 head를 보면 index에서 계약 년월이 컬럼으로 넘어왔다. 
7. yaer, day, weekday, month, quarter 별로 정리
8. 연도별 거래 건수
~
21. 거래 금액 분석
22. 연도별 평균 거래가 계산
23. 월별로 나눠서 연도별 평균 거래가 계산 
24. 특정 지역 (구별 평균 매매가) 
"""

""" 1. apartment df 만들기 """
# datafile_list = ['아파트(매매)__실거래가_20050901_20060831.csv',
#                  '아파트(매매)__실거래가_20060901_20070831.csv',
#                  '아파트(매매)__실거래가_20070901_20080831.csv',
#                  '아파트(매매)__실거래가_20080901_20090831.csv',
#                  '아파트(매매)__실거래가_20090901_20100831.csv',
#                  '아파트(매매)__실거래가_20100901_20110831.csv',
#                  '아파트(매매)__실거래가_20110901_20120831.csv',
#                  '아파트(매매)__실거래가_20120901_20130831.csv',
#                  '아파트(매매)__실거래가_20130901_20140831.csv',
#                  '아파트(매매)__실거래가_20140901_20150831.csv',
#                  '아파트(매매)__실거래가_20150901_20160831.csv',
#                  '아파트(매매)__실거래가_20160901_20170831.csv',
#                  '아파트(매매)__실거래가_20170901_20180831.csv',
#                  '아파트(매매)__실거래가_20180901_20190831.csv',
#                  '아파트(매매)__실거래가_20190901_20200831.csv']
# apartment = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)


""" 
2. 연도별로 저장된 csv 파일을 하나의 파일로 만들기 - concat 
"""
# for filename in datafile_list[1:]:
#     doc = pd.read_csv("01_data/" + filename, encoding="utf-8-sig", error_bad_lines=False)
#     apartment = pd.concat([apartment, doc])


# def func(row):
#     """
#     format 함수를 이용하여 계약년월일 정리
#     """
#     row["계약년월일"] = str(row["계약년월"]) + "{0:02d}".format(row["계약일"])
#     return row


""" 
apply 적용 
"""
# apartment = apartment.apply(func, axis=1)


"""
1.1 pickle 라이브러리를 사용하여 파일로 저장, 불러오기
"""
## 저장
# with open("apartment_data.pickle", "wb") as picklefile:
#     pickle.dump(apartment, picklefile)

## 읽기
with open("apartment_data.pickle", "rb") as pickle_file:
    apartment = pickle.load(pickle_file)


""" 3. 정확한 분석을 위해, 연단위로 짜르기로 함 """
# print(apartment.head())
# apartment = apartment[apartment["계약년월일"] < "20200101"]
# print(apartment.sort_values(by="계약년월일").tail())


""" 4. 계약년월일 데이터 포맷 변경 """
# print(apartment.index)
# apartment['계약년월일'] = pd.to_datetime(apartment['계약년월일'], format='%Y%m%d', errors='raise')



""" 5. 15년동안 아파트 매매가 분석: 월별 거래 건수 - plotly """
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=apartment_year_month.index,
#         y=apartment_year_month['시군구']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "월별 거래건수",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 15
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "D1"
#         }
#     }
# )
# fig.show()

""" 6. index를 삭제하고 head를 보면 index에서 계약 년월이 컬럼으로 넘어왔다. """
# doc_count = apartment.reset_index()
# print(doc_count.head())


""" 7. yaer, day, weekday, month, quarter 별로 정리 - 이후 plotly에서 사용 """
# apartment['year'] = apartment['계약년월일'].dt.year
# apartment['monthday'] = apartment['계약년월일'].dt.day
# apartment['weekday'] = apartment['계약년월일'].dt.weekday
# apartment['month'] = apartment['계약년월일'].dt.month
# apartment['quarter'] = apartment['계약년월일'].dt.quarter
#
# apartment_monthday = apartment.groupby('monthday').count()
# apartment_weekday = apartment.groupby('weekday').count()
# apartment_year_month = apartment.groupby(['year', 'month']).count()
# apartment_quarter = apartment.groupby('quarter').count()



""" 멀티 컬럼으로 그룹핑하기 """
# apartment_year_month = apartment.groupby(['year', 'month']).count()
# print(apartment_year_month.head())


""" 최신 문법: query() - 직관적으로 내가 원하는 데이터를 가져오는 문법 """
# apartment_year_month_3 = apartment_year_month.query("month == 3")
# print(apartment_year_month_3)


""" query()를 사용하여 연도별 거래건수 가져오기 - plotly """
# # reset index
# apartment_year_month_3 = apartment_year_month_3.reset_index()
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=apartment_year_month_3['year'],
#         y=apartment_year_month_3['시군구']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "<b>연도별 거래건수(3월)</b>",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 18
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "D1"
#         }
#     }
# )
#
# fig.show()



""" 월별 트랜드 확인하기 """
# print(apartment_year_month.head())
# for index in range(1, 13):
#     apartment_year_month_each = apartment_year_month.query("month == "+ str(index))
#     apartment_year_month_each = apartment_year_month_each.reset_index()
#
#     fig = go.Figure()
#     fig.add_trace(
#         go.Bar(
#             x=apartment_year_month_each['year'],
#             y=apartment_year_month_each['시군구']
#         )
#     )
#
#     fig.update_layout(
#         {
#             "title": {
#                 "text": "특정 월의 년도별 거래건수 (" + str(index) + "월)",
#                 "x": 0.5,
#                 "y": 0.9,
#                 "font": {
#                     "size": 15
#                 }
#             },
#             "xaxis": {
#                 "showticklabels":True,
#                 "dtick": "D1"
#             }
#         }
#     )
#
#     fig.show()


""" 막대그래프 합쳐서 확인하기 """
""" 
연도별 월 그래프 
"""
# fig = go.Figure()
# for index in range(1, 13):
#     apartment_year_month_each = apartment_year_month.query('month == ' + str(index))
#     apartment_year_month_each = apartment_year_month_each.reset_index()
#
#
#     fig.add_trace(
#         go.Bar(
#             x=apartment_year_month_each['year'],
#             y=apartment_year_month_each['시군구'],
#             # name=str(index) + "월"
#         )
#     )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "특정 월의 년도별 거래건수",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 15
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "D1"
#         }
#     }
# )
#
# fig.show()

"""
월별 연도 그래프
"""
# fig = go.Figure()
# for index in range(2006, 2020):
#     apartment_year_month_each = apartment_year_month.query('year == ' + str(index))
#     apartment_year_month_each = apartment_year_month_each.reset_index()
#
#
#     fig.add_trace(
#         go.Bar(
#             x=apartment_year_month_each['month'],
#             y=apartment_year_month_each['시군구'],
#             name=str(index) + "년"
#         )
#     )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "특정 월의 년도별 거래건수",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 15
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "D1"
#         }
#     }
# )
#
# fig.show()


""" 월별 거래건수에서 최대/최소 거래건수 삭제 후, 평균으로 파악해보기 """
# print(apartment_year_month.head())
# apartment_year_month = apartment_year_month.reset_index()

"""
슬라이싱, 가장작은수, 가장 큰 수를 뺀다"""
# apartment_year_month_each = apartment_year_month[apartment_year_month['month'] == 1].sort_values(by='시군구')[1:-1]

"""
월별 평균값 구하기"""
# apartment_year_month_each['시군구'].mean()

"""
각 월별 평균값 구하기"""
# mean_per_month = list()
# for index in range(1, 13):
#     apartment_year_month_each = apartment_year_month[apartment_year_month['month'] == index].sort_values(by='시군구')[1:-1]
#     mean_per_month.append(apartment_year_month_each['시군구'].mean())
#
# print(mean_per_month)


""" 그래프 - 특정 월의 년도별 평균 거래건수 (최대 및 최소 거래건수 삭제) """
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=list(range(1, 13)),
#         y=mean_per_month,
#         text=mean_per_month, textposition='auto', texttemplate='%{y:.2f}'
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "<b>특정 월의 년도별 평균 거래건수 (최대 및 최소 거래건수 삭제)</b>",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 18
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "D1"
#         }
#     },
#     template='presentation'
# )
#
# fig.show()

## 날짜별 거래 건수 그래프로 확인하기
## Plotly로 데이터 확인하기

"""  15년동안의 아파트 매매가 분석: 분기별 거래건수 """
# # print(apartment_quarter.index)
#
# # index 변경
# apartment_quarter.index = ['1Q', '2Q', '3Q', '4Q']
#
# print(apartment_quarter.index)
#
# print(apartment_quarter.head())

# # plotly로 분석
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=apartment_quarter.index,
#         y=apartment_quarter['시군구']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "<b>분기별 거래건수</b>",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 18
#             }
#         },
#         "xaxis": {
#             "showticklabels":True
#         },
#         "template":'ggplot2'
#     }
# )
#
# fig.show()

""" 15년동안의 아파트 매매가 분석: 요일별 거래건수 """
# print(apartment_weekday.head())

# print(apartment.groupby('weekday').tail())
# print(apartment.tail())
# apartment_weekday.index = ['월', '화', '수', '목', '금', '토', '일']
# print(apartment_weekday.index)
#
# # plotly로 분석
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=apartment_weekday.index,
#         y=apartment_weekday['시군구']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "요일별 거래건수",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 18
#             }
#         },
#         "xaxis": {
#             "showticklabels":True
#         },
#         "template":"ggplot2"
#     }
# )
#
# fig.show()

""" 21. 거래 금액 분석 """
# print(apartment.head())
# replace
apartment['거래금액(만원)'] = apartment['거래금액(만원)'].str.replace(',','')
# apartment.info()

# change type object to int64
apartment = apartment.astype({'거래금액(만원)': 'int64'})
# change 계약년월일 type int64 to datetime
apartment["계약년월일"] = pd.to_datetime(apartment["계약년월일"], format="%Y%m%d", errors="raise")
# apartment.info()

# 연도별 평균 거래가
apartment['year'] = apartment['계약년월일'].dt.year
apartment_year = apartment.groupby('year').mean()
# print(apartment_year.head())

"""22. 연도별 평균 거래가 계산"""
# # ploty - 연도별 평균 거래가
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=apartment_year.index,
#         y=apartment_year['거래금액(만원)']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "연도별 아파트 평균 매매가",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 18
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "1"
#         },
#         "template":'ggplot2'
#     }
# )
#
# fig.show()

"""23. 월별로 나눠서 연도별 평균 거래가 계산"""
# apartment.head()
apartment_month = apartment.groupby('계약년월').mean()
apartment_month.index = pd.to_datetime(apartment_month.index, format='%Y%m', errors='raise')

# # 월별로 나눠서 연도별 평균 거래가 계산
# # plotly
# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=apartment_month.index,
#         y=apartment_month['거래금액(만원)']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "월별 아파트 평균 매매가",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 18
#             }
#         },
#         "xaxis": {
#             "showticklabels":True,
#             "dtick": "M3"
#         },
#         "template":'ggplot2'
#     }
# )
#
# fig.show()


""" 24. 특정 지역 (구별 평균 매매가) """
print(apartment.head())