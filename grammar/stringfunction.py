"""
문자열 함수 정리
"""
data = "Kubernetes is an open source container orchestration engine for automating deployment, " \
       "scaling, and management of containerized applications."
data2 = "123456789"

data_join = '|'

data_strip = "     data for strip      "
data2_strip = "   7777766665555444(data for strip)333322221111    "

data_split = "9,8,7,6,5,4,3,2,1"

data_replace = "(Kubernetes)"

# count()
print("특정 문자 개수 세기 - count() :", data.count('f'))

# index()
print("문자열에 있는 특정 문자 위치 찾기 - index() :", data.index('i'))

# find()
print("문자열에 있는 특정 문자 위치 찾기 - find() :", data.find('i'))
print("문자열에 있는 특정 문자 위치 찾기, 없는 문자 - find() :", data.find('none'))

if data.find('none') == -1:
    print("해당하는 문자가 없습니다")

# join()
print("문자열 사이에 다른 문자 넣기 - join() :", data_join.join(data2))

# strip()
print("문자열 앞뒤에 공백 지우기 - strip() :", data_strip.strip())
print("문자열 앞뒤에 동일한 문자 지우기 - strip() :", data2_strip.strip(" 7654()321"))

# upper(), lower()
print("소문자를 대문자로 바꾸기 - upper() :", data.upper())
print("대문자를 소문자로 바꾸기 - lower() :", data.lower())

# split()
print("문자열 나누기 - split() :", data.split())
print("문자열 나누기 - split() :", data.split()[5])
print("문자열 나누기 - split() :", data_split.split(","))

listdata = data_split.split(",")
for index, data_split in enumerate(listdata):
    listdata[index] = int(data_split)
    # print("index:", index, "value:", data_split)
print("split data to list data :", listdata)

# replace()
print("문자열을 다른 문자로 바꾸거나, 삭제하기 - replace()")
print("Kubernetes to K8s :", data.replace("Kubernetes", "K8s"))
print('() to ""',data_replace.replace("()",""))
print('() to ""',data_replace.replace("(",""))
print('() to ""',data_replace.replace(")",""))
print('() to ""',data_replace.replace("(","").replace(")",""))



