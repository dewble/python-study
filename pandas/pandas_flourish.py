import pickle
import pandas as pd

"""
1. 사전준비
2. 각각의 구별로 연도에 따라 어떻게 거래금액이 변화해왔는지 보고 싶다.
"""

"""1. 사전준비
"""
with open('apartment_data.pickle', 'rb') as pickle_filename:
    apartment = pickle.load(pickle_filename)
apartment['거래금액(만원)'] = apartment['거래금액(만원)'].str.replace(',', '')
apartment = apartment.astype({'거래금액(만원)': 'int64'})
apartment['계약년월일'] = pd.to_datetime(apartment['계약년월일'], format='%Y%m%d', errors='raise')
apartment['year'] = apartment['계약년월일'].dt.year
apartment['month'] = apartment['계약년월일'].dt.month
apartment['시'] = apartment['시군구'].str.split().str[0]
apartment['구'] = apartment['시군구'].str.split().str[1]
apartment['동'] = apartment['시군구'].str.split().str[2]
# groupby > index로 만들어진다, index reset 필요
apartment_gu = apartment.groupby(['year', 'month', '구']).mean()
apartment_gu = apartment_gu.reset_index()
apartment_gu_flourish = apartment_gu[['구', '거래금액(만원)', '계약년월', 'year', 'month']].copy()

# print(apartment_gu_flourish.head())

"""2. 각각의 구별로 연도에 따라 어떻게 거래금액이 변화해왔는지 보고 싶다.
"""
## 리스트로 계약년월을 뽑기 - .tolist
datelist = apartment_gu_flourish["계약년월"].unique().tolist()
# print(datelist)

## df 만들기 - 각 구별 특정 계약 년월
apartment_toflorish = apartment_gu_flourish[apartment_gu_flourish["계약년월"] == 200601.0][["구","거래금액(만원)"]].copy()
# print(apartment_toflorish)
apartment_toflorish = apartment_toflorish.set_index("구")
print(apartment_toflorish)