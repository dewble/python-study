import re


"""
match, search 함수 사용법
"""
# pattern = re.compile('[a-z]+')
# matched = pattern.match('Dave Dave Kate JM')
# searched = pattern.search("Dave Kate JM")
# findall = pattern.findall("Dave Kate JM")
#
# print(matched)
# print(searched)
# print(findall)


# ## ? 는 앞 문자가 0 or 1 번 반복되는 패턴
# pattern2 = re.compile('d?t')
#
# res1 = pattern2.search("date")
# res2 = pattern2.search("ddddddtte")
#
# print(res1)
# print(res2)
#
# ## * 는 앞 문자가 0 or 그 이상 반복되는 패턴
# pattern3 = re.compile('d*t')
#
# res3 = pattern3.search("date")
# res4 = pattern3.search("ddddddtte")
#
# print(res3)
# print(res4)
#
# ## + 는 앞 문자가 1번 또는 그 이상 반복되는 패턴
# pattern4 = re.compile('d+t')
#
# res5 = pattern4.search("date")
# res6 = pattern4.search("ddddddtte")
#
# print(res5)
# print(res6)


## {n} : 앞 문자가 n 번 반복되는 패턴
pattern5 = re.compile('AE{3}A')

res7 = pattern5.search("AEEA")
res8 = pattern5.search("AEEEA")
res9 = pattern5.search("AEEEEA")

print(res7)
print(res8)
print(res9)

## {m, n} : 앞 문자가 m 번 반복되는 패턴부터 n 번 반복되는 패턴까지
pattern6 = re.compile('AE{3,5}A')

res10 = pattern6.search("AEEA")
res11 = pattern6.search("AEEEA")
res12 = pattern6.search("AEEEEA")
res13 = pattern6.search("AEEEEEA")

print(res10)
print(res11)
print(res12)
print(res13)