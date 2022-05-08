'''
다음 통화별 환율을 통화단위와 원화 환율을 가진 딕셔너리로 만들고 사용자로부터 달러, 엔, 또는 위안 금액을 입력받은 후 이를 원으로 바꿔서 계산하세요.
사용자는 100 ~ 999 달러, 위안, 또는 엔 과 같이 금액과 통화명 사이에 공백을 넣어 입력하기로 합니다.
'''

exchange = {'달러':1112, '위안':171, '엔':1010}
prices = input("금액을 입력하세요 (e.g. 100 달러) : ")
for exchange_item in exchange.keys():
    if prices[4:] == exchange_item:
        print (int(prices[:4]) * exchange[exchange_item], '원')