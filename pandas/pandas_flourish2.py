"""
1. 평당 매매가 변화율 분석
    - 기존에 만들었던 pickle을 가져와서 사용
"""

import pickle
import pandas as pd

"""1. 평당 매매가 변화율 분석
    - 기존에 만들었던 pickle을 가져와서 사용
"""
with open("apartment_data.pickle", "rb") as pickle_filename:
    apartment = pickle.load(pickle_filename)

print(apartment.head())

## 거래금액을 콤마를 뺴고 숫자로 만든다
apartment['거래금액(만원)'] = apartment['거래금액(만원)'].str.replace(',', '')
apartment = apartment.astype({'거래금액(만원)': 'int64'})

## 평당 매매가를 계산하기 위해 전용 면적을 3.3 으로 나누고 계산
apartment['평당매매가'] = apartment['거래금액(만원)'] / (apartment['전용면적(㎡)'] / 3.3)
## df 을 datetype을 바꾸고
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

apartment_gu

apartment_gu = apartment_gu.reset_index()

apartment_gu_flourish = apartment_gu[['구', '평당매매가', '계약년월']].copy()

print(apartment_gu_flourish.head())


datelist = apartment_gu_flourish['계약년월'].unique().tolist()
apartment_toflourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == 200601][['구','평당매매가']].copy()
apartment_toflourish = apartment_toflourish.set_index('구')
apartment_toflourish.columns = [200601]

for index in datelist[1:]:
    add_flourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == index][['구','평당매매가']].copy()
    add_flourish = add_flourish.set_index('구')
    add_flourish.columns = [int(index)]
    apartment_toflourish = pd.concat([apartment_toflourish, add_flourish], axis=1)


print(apartment_toflourish.head())

## csv 파일로 변환
apartment_toflourish.to_csv("seoul_aparment_avg.csv", encoding='utf-8-sig')