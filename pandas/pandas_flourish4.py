"""
특정 년도에 건축된 아파트의 구별 평균매매가 분석
1. pickle로 가공한 데이터 불러오기, 저장하기
2. query() 문법 복습
3. 특정 건축년도의 구별 아파트 거래가 비교
4. 특정 아파트 찾기
"""

"""1. pickle로 가공한 데이터 불러오기, 저장하기
"""
import pickle
import pandas as pd

# # apartment_data.pickle의 데이터 가져와서 가공한 데이터 업데이트
# with open('apartment_data.pickle', 'rb') as pickle_filename:
#     apartment = pickle.load(pickle_filename)
#
# apartment['거래금액(만원)'] = apartment['거래금액(만원)'].str.replace(',', '')
# apartment = apartment.astype({'거래금액(만원)': 'int64'})
# apartment['평당매매가'] = apartment['거래금액(만원)'] / (apartment['전용면적(㎡)'] / 3.3)
# apartment['계약년월일'] = pd.to_datetime(apartment['계약년월일'], format='%Y%m%d', errors='raise')
#
# apartment['year'] = apartment['계약년월일'].dt.year
# apartment['monthday'] = apartment['계약년월일'].dt.day
# apartment['weekday'] = apartment['계약년월일'].dt.weekday
# apartment['month'] = apartment['계약년월일'].dt.month
# apartment['quarter'] = apartment['계약년월일'].dt.quarter
#
# apartment['시'] = apartment['시군구'].str.split().str[0]
# apartment['구'] = apartment['시군구'].str.split().str[1]
# apartment['동'] = apartment['시군구'].str.split().str[2]
#
# # pickle 사용해서 apartment_data_update.pickle에 가공한 데이터 저장
# with open("apartment_data_update.pickle", "wb") as picklefile:
#     pickle.dump(apartment, picklefile)

# 가공한 데이터 읽기
with open('apartment_data_update.pickle', 'rb') as pickle_filename:
    apartment = pickle.load(pickle_filename)


"""2. query() 문법 복습
"""
# 방법 1
# print(apartment[(apartment["건축년도"] >= 2010) & (apartment["구"] == "송파구")].count())

# 방법 2
# print(apartment.query("(건축년도 >= 2010) & (구== '송파구')").count())

"""3. 특정 건축년도의 구별 아파트 거래가 비교
"""
# # copy df
# doc = apartment.query("(건축년도 >= 2010) & (구== '송파구')").copy()
# # print(doc.head())
#
# # 계약년월로 평균을 만든다
# doc = doc.groupby(["계약년월"]).mean()
# doc.index = pd.to_datetime(doc.index, format="%Y%m", errors="raise")
# # print(doc.head())
#
# # 특정 건축년도의 구별 아파트 거래가 비교, 각각의 df를 따로 만든다
# doc_songpa = apartment.query("(건축년도 == 2008) & (구 == '송파구')").copy()
# doc_songpa = doc_songpa.groupby(['계약년월']).mean()
# doc_songpa.index = pd.to_datetime(doc_songpa.index, format='%Y%m', errors='raise')
#
# doc_gangnam = apartment.query("(건축년도 == 2008) & (구 == '강남구')").copy()
# doc_gangnam = doc_gangnam.groupby(['계약년월']).mean()
# doc_gangnam.index = pd.to_datetime(doc_gangnam.index, format='%Y%m', errors='raise')
#
# doc_serngdong = apartment.query("(건축년도 == 2008) & (구 == '동대문구')").copy()
# doc_serngdong = doc_serngdong.groupby(['계약년월']).mean()
# doc_serngdong.index = pd.to_datetime(doc_serngdong.index, format='%Y%m', errors='raise')
#
# # print(doc_songpa)
#
# # plotly - 송파구/강남구/동대문구 12년차 아파트 평당매매가
# import plotly.graph_objects as go
#
# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=doc_songpa.index, y=doc_songpa['평당매매가'], name='송파구'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=doc_gangnam.index, y=doc_gangnam['평당매매가'], name='강남구'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=doc_serngdong.index, y=doc_serngdong['평당매매가'], name='동대문구'
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "송파구/강남구/동대문구 12년차 아파트 평당매매가",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 20
#             }
#         },
#         "showlegend": True,
#         "xaxis": {
#         },
#         "yaxis": {
#             "tickformat": ","
#         },
#         "template": 'none'
#
#     }
# )
#
# fig.show()


"""4. 특정 아파트 찾기
"""
# print(apartment[apartment['단지명'].str.contains('북한산시티')]['단지명'].unique())
print(apartment[apartment["단지명"] == "에스케이북한산시티"].head())

# 특정 아파트를 copy()
doc_pick1 = apartment[apartment['단지명'] == '강남한양수자인(4단지)'].copy()
doc_pick1 = doc_pick1.groupby(['계약년월']).mean()
doc_pick1.index = pd.to_datetime(doc_pick1.index, format='%Y%m', errors='raise')

doc_pick2 = apartment[apartment['단지명'] == '주공아파트 5단지'].copy()
doc_pick2 = doc_pick2.groupby(['계약년월']).mean()
doc_pick2.index = pd.to_datetime(doc_pick2.index, format='%Y%m', errors='raise')

doc_pick3 = apartment[apartment['단지명'] == '에스케이북한산시티'].copy()
doc_pick3 = doc_pick3.groupby(['계약년월']).mean()
doc_pick3.index = pd.to_datetime(doc_pick3.index, format='%Y%m', errors='raise')

# # plotly
# import plotly.graph_objects as go
#
# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=doc_pick1.index, y=doc_pick1['평당매매가'], name='강남한양수자인(4단지)'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=doc_pick2.index, y=doc_pick2['평당매매가'], name='주공아파트 5단지'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=doc_pick3.index, y=doc_pick3['평당매매가'], name='에스케이북한산시티'
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "특정 단지 아파트 평당매매가 트렌드",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 20
#             }
#         },
#         "showlegend": True,
#         "xaxis": {
#         },
#         "yaxis": {
#             "tickformat": ","
#         },
#         "template": 'none'
#
#     }
# )
#
# fig.show()

# 수익률 확인
print (int(doc_pick1.loc['2017-01-01']['거래금액(만원)']), int(doc_pick1.iloc[-1]['거래금액(만원)']), int(doc_pick1.iloc[-1]['거래금액(만원)']/doc_pick1.loc['2017-01-01']['거래금액(만원)']*100), '%')
print (int(doc_pick2.loc['2017-01-01']['거래금액(만원)']), int(doc_pick2.iloc[-1]['거래금액(만원)']), int(doc_pick2.iloc[-1]['거래금액(만원)']/doc_pick2.loc['2017-01-01']['거래금액(만원)']*100), '%')
print (int(doc_pick3.loc['2017-01-01']['거래금액(만원)']), int(doc_pick3.iloc[-1]['거래금액(만원)']), int(doc_pick3.iloc[-1]['거래금액(만원)']/doc_pick3.loc['2017-01-01']['거래금액(만원)']*100), '%')