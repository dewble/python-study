import pickle
import pandas as pd

"""
1. 사전준비
2. 각각의 구별로 연도에 따라 어떻게 거래금액이 변화해왔는지 보고 싶다.
3. 코드 정리
4. 컬럼을 하나씩 가져와서 이어 붙인다. (위에서 진행했던 내용을 for문으로 반복)
5. csv 파일로 저장
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

## df 만들기 - 각 구별 특정 계약 년월(200601)
apartment_toflourish = apartment_gu_flourish[apartment_gu_flourish["계약년월"] == 200601.0][["구","거래금액(만원)"]].copy()
# print(apartment_toflourish)

## index를 “구"로 변경
apartment_toflourish = apartment_toflourish.set_index("구")
# print(apartment_toflourish)

## column을 다시 써준다
apartment_toflourish.columns = ['200601']
# print(apartment_toflourish)

## 내가 원하는 column(200602)을 하나 더 추가해준다.
add_flourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == 200602.0][['구','거래금액(만원)']].copy()
## index를 “구"로 변경
add_flourish = add_flourish.set_index("구")
## column을 다시 써준다
add_flourish.columns = ['200602']
# print(add_flourish.head())

## concat - 두 column 합치기
apartment_toflourish = pd.concat([apartment_toflourish, add_flourish], axis=1)
# print(apartment_toflourish.head())

"""3. 코드 정리
위에서 부터 진행한 내용을 아래에 정리


apartment_gu_flourish = apartment_gu[['구', '거래금액(만원)', '계약년월', 'year', 'month']].copy()

# 컬럼 명을 list로 뽑아서 저장
datelist = apartment_gu_flourish['계약년월'].unique().tolist()

# 맨 처음 df를 만든다. 200601dnjf
apartment_toflourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == 200601][['구','거래금액(만원)']].copy()
apartment_toflourish = apartment_toflourish.set_index('구')
apartment_toflourish.columns = [200601]
"""

"""4. 컬럼을 하나씩 가져와서 이어 붙인다. (위에서 진행했던 내용을 for문으로 반복)
"""
## 하나씩 컬럼을 가져와서 이어 붙인다.
for index in datelist[1:]:
    add_flourish = apartment_gu_flourish[apartment_gu_flourish['계약년월'] == index][['구','거래금액(만원)']].copy()
    add_flourish = add_flourish.set_index('구')
    add_flourish.columns = [int(index)]
    apartment_toflourish = pd.concat([apartment_toflourish, add_flourish], axis=1)

# print(apartment_toflourish.head())

"""5. csv 파일로 저장
"""
# apartment_toflourish.info()
apartment_toflourish.to_csv("seoul_apartment.csv", encoding="utf-8-sig")