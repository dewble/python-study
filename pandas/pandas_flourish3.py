"""
1. grammar - cumprod, pct_change
2. 사전 준비
    - 기존에 만들었던 pickle을 가져와서 사용
3. 누적 수익률 계산하기
4. 시각화 하기
5. 추가 문법 이해 (정렬, sort_values(), sort_index())
"""

import pickle
import pandas as pd


"""1. grammar - cumprod, pct_change

"""
# # cumprod() > 누적곱 계산, 위에서 부터 각 칼럼 값이 곱해진다.
# df = pd.DataFrame([[2.0,1.0],
#                    [3.0,1.0],
#                    [1.0,0.0]],
#                    columns=["A","B"])
# print(df)
# # 2.0 x 3.0, (2.0 x 3.0) x 1.0
# print(df.cumprod())
#
# # pct_change > 변화률, df 보단 시리즈에 적용
# df = pd.DataFrame([[2.0,1.0],
#                    [3.0,1.0],
#                    [1.0,0.0]],
#                    columns=["A","B"])
# print(df)
# df["A"].pct_change()
# # 2.0 에서 3.0 으로의 변화율, 3.0에서 1.0으로의 변화율
# print(df["A"].pct_change())



"""2. 사전 준비
    - 기존에 만들었던 pickle을 가져와서 사용
"""
# 기존 pickle 가져와서 진행
with open('apartment_data.pickle', 'rb') as pickle_filename:
    apartment = pickle.load(pickle_filename)

apartment['거래금액(만원)'] = apartment['거래금액(만원)'].str.replace(',', '')
apartment = apartment.astype({'거래금액(만원)': 'int64'})
apartment['평당매매가'] = apartment['거래금액(만원)'] / (apartment['전용면적(㎡)'] / 3.3)
apartment['계약년월일'] = pd.to_datetime(apartment['계약년월일'], format='%Y%m%d', errors='raise')

apartment['year'] = apartment['계약년월일'].dt.year
apartment['monthday'] = apartment['계약년월일'].dt.day
apartment['weekday'] = apartment['계약년월일'].dt.weekday
apartment['month'] = apartment['계약년월일'].dt.month
apartment['quarter'] = apartment['계약년월일'].dt.quarter

apartment['시'] = apartment['시군구'].str.split().str[0]
apartment['구'] = apartment['시군구'].str.split().str[1]
apartment['동'] = apartment['시군구'].str.split().str[2]

apartment_gu = apartment.groupby(['year', 'month', '구']).mean()
apartment_gu = apartment_gu.reset_index()
apartment_gu_flourish = apartment_gu[['구', '평당매매가', '계약년월']].copy()

datelist = apartment_gu_flourish['계약년월'].unique().tolist()
apartment_toflourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == 200601][['구','평당매매가']].copy()
apartment_toflourish = apartment_toflourish.set_index('구')
apartment_toflourish.columns = [200601]


for index in datelist[1:]:
    add_flourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == index][['구','평당매매가']].copy()
    add_flourish = add_flourish.set_index('구')
    add_flourish.columns = [int(index)]
    apartment_toflourish = pd.concat([apartment_toflourish, add_flourish], axis=1)

# print(apartment_toflourish.head())


"""3. 누적 수익률 계산하기 - 강남구
"""
gu_list = list(apartment_toflourish.index)
# print(gu_list)
# 위 df에서 series를 만든다.
each_gu = apartment_toflourish.loc[gu_list[0]]
# print(each_gu)

# series name 변경, pct_change() 함수 적용
changerate = each_gu.pct_change()
changerate.name = "change_rate"
# print(changerate)

# 처음 만든 series(강남구)에 변화률 series를 붙인다.
each_gu_changerate = pd.concat([each_gu,changerate], axis=1)
# print(each_gu_changerate)

# 변화률의 누적곱을 이용하여 수익률을 구한다.
each_gu_changerate["profit_rate"] = (each_gu_changerate["change_rate"] + 1).cumprod()
# print(each_gu_changerate)

# 수익률을 따로 copy하고 series를 df로 변경, column을 강남구로 변경
gu_profitrate = each_gu_changerate[["profit_rate"]].copy()
# print(type(gu_profitrate))

gu_profitrate.columns = ["강남구"]
# print(gu_profitrate)

# gu_list의 각 구들도 위 내용을 반복해서 수익률을 계산하고, concat으로 이어 나간다.
for gu in gu_list[1:]:
    each_gu = apartment_toflourish.loc[gu]
    changerate = each_gu.pct_change()
    changerate.name = 'change_rate'
    each_gu_changerate = pd.concat([each_gu, changerate], axis=1)
    each_gu_changerate['profit_rate'] = (each_gu_changerate["change_rate"] + 1).cumprod()
    gu_profitrate_each = each_gu_changerate[['profit_rate']].copy()
    gu_profitrate_each.columns = [gu]
    gu_profitrate = pd.concat([gu_profitrate, gu_profitrate_each], axis=1)

# print(gu_profitrate.head())

# 없는 데이터(NaN)을 특정값으로 일괄 변경하기
gu_profitrate = gu_profitrate.fillna(1)
# print(gu_profitrate.head())

"""4. 시각화 하기
"""
gu_profitrate.index = pd.to_datetime(gu_profitrate.index, format='%Y%m', errors='raise')
import plotly.graph_objects as go

# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=gu_profitrate.index, y=gu_profitrate['강남구']
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "강남구",
#             "x": 0.5,
#             "y": 0.9,
#             "font": {
#                 "size": 20
#             }
#         },
#         "xaxis": {
#         },
#         "yaxis": {
#             "tickformat": "%"
#         },
#         "template": 'none'
#
#     }
# )
# fig.show()

# # 여러 그래프 한번에 그리 - add trace
# gu_profitrate.columns
#
# gu_list = list(gu_profitrate.columns)
#
# import plotly.graph_objects as go
#
# fig = go.Figure()
#
# for gu in gu_list:
#     fig.add_trace(
#         go.Scatter(
#             x=gu_profitrate.index, y=gu_profitrate[gu], name=gu
#         )
#     )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "서울시 구별 아파트 수익률",
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
#             "tickformat": "%"
#         },
#         "template": 'none'
#
#     }
# )
#
# fig.show()

"""5. 추가 문법 이해 (정렬, sort_values(), sort_index())
"""
