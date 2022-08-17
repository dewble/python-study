"""
백테스팅의 이해 / 백테스팅에 유용한 pandas 문법과 실전 알고리즘 백테스팅
1. 백테스팅의 이해
2. 상승장 전략
"""
import pandas as pd


"""2. 상승장 전략
"""
df = pd.DataFrame([[2.0],
                   [3.0],
                   [1.0],
                   [1.0],
                   [1.0],
                   [2.0],
                   [4.0],
                  ],
                   columns=['Close'])
# print(df)

# pct_change(): 칼럼의 변화률
df["변화률"] = df["Close"].pct_change()
print(df)