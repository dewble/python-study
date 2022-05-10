def swapping():
    """
    tuple을 사용하면 swaping 이 가능하다.
    """
    x = 1
    y = 2

    x, y = y, x
    print(x)
    print(y)


def delete_tuple():
    """
    tuple을 수정하기 위해서 list로 변환 후 다시 tuple로 변경한다.
    """
    tupledata = ('tupledata1', 'tupledata2', 'tupledata3', 'tupledata4', 'tupledata5')
    tuple_data = list(tupledata)
    del tuple_data[0]
    tuple(tuple_data)
    print(tuple_data)
    

def append_tuple():
    """
    tuple을 수정하기 위해서 list로 변환 후 다시 tuple로 변경한다.
    """
    tupledata = ('tupledata2', 'tupledata3', 'tupledata4', 'tupledata5')
    tuple_data = list(tupledata)
    tuple_data.append('tupledata6')
    print(tuple(tuple_data))


def insert_tuple():
    """
    tuple을 list로 변경한 뒤 맨 앞에 원하는 내용을 추가한다.
    """
    tupledata = ('tupledata2', 'tupledata3', 'tupledata4', 'tupledata5')
    tuple_data = list(tupledata)
    tuple_data.insert(0,'tupledata1')
    print(tuple(tuple_data))


#swapping()
#delete_tuple()
#append_tuple()
insert_tuple()