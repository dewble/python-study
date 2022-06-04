import pandas as pd
doc = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)

# string_data = "kubernetes 클러스터는 kubeadm, kubespray, rke2 등으로 구성할 수 있다"
#
# string_data2 = string_data.replace(", ","-")
#
# print(string_data2)

# doc.info()
# print(doc.head())

def func(item):
    string_data = item.replace(',', '')
    return string_data

doc['거래금액(만원)'] = doc['거래금액(만원)'].apply(func)

# print(doc.head())
doc = doc.astype({'거래금액(만원)':'int64'})
print(doc.info())