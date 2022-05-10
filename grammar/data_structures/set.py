def set_delete():
    """
    리스트에서 중복을 제거한다.
    """
    number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]
    number_list1 = set(number_list)
    print (number_list1)



def set_add_remove():
    number_list2 = {1, 2, 3}
    number_list2.add(4)  # 하나의 데이터를 추가할 때는 add
    number_list2.update([5, 6])  # 여러 데이터를 추가할 때는 리스트 형태로 update 함수를 사용
    number_list2.remove(2)  # 특정 데이터를 삭제할 때는 remove
    number_list2



set_delete()
set_add_remove()