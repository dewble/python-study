def dict_with_exchange():
    '''
    다음 통화별 환율을 통화단위와 원화 환율을 가진 딕셔너리로 만들고 사용자로부터 달러, 엔, 또는 위안 금액을 입력받은 후 이를 원으로 바꿔서 계산하세요.
    사용자는 100 ~ 999 달러, 위안, 또는 엔 과 같이 금액과 통화명 사이에 공백을 넣어 입력하기로 합니다.
    '''

    exchange = {'달러':1112, '위안':171, '엔':1010}
    prices = input("금액을 입력하세요 (e.g. 100 달러) : ")
    for exchange_item in exchange.keys():
        if prices[4:] == exchange_item:
            print (int(prices[:4]) * exchange[exchange_item], '원')


def dict_with_for():

    data = {'environment': '환경', 'company': '회사', 'government': '정부, 정치', 'face': '얼굴'}

    for item in data.keys():
        print(item,":",data[item])


def dict_with_x_data():
    """
    다음 영어 사전 데이터를 딕셔너리 변수로 만들고 외움표시가 X 인 영어단어만 출력하세요
    단, key는 영어단어, value는 의미와 외움표시 두 데이터를 넣습니다.
    """

    data = {'environment': ['환경', 'X'], 'company': ['회사', 'O'], 'government': ['정부, 정치', 'X'], 'face': ['얼굴', 'X']}

    for item in data.keys():
        if (data[item][1] == 'X'):
            print(item)


def dict_merge_other_dict():
    """
    여러 dict을 하나의 dict로 합친다.
    """
    dict_all = {'environment': '환경', 'gonernment': '정부, 정치'}
    dict2 = {'company': '회사', 'face': '얼굴'}
    dict3 = {'apple': '사과'}

    for item in dict2.keys():
        dict_all[item] = dict2[item]    # 새로운 key(item)에 새로운 값 value(dict2[item])을 추가한다.

    for item in dict3.keys():
        dict_all[item] = dict3[item]

    print(dict_all)



#dict_with_exchange()
# dict_with_for()
# dict_with_x_data()
# dict_merge_other_dict()
