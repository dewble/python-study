import plotly.graph_objects as go
import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5, 6],
#     'C': [1, 2, 3, 4, 5, 100]
# })
# print(df)

"""
수치형 데이터 boxplot
"""
# fig = go.Figure()
# fig.add_trace(
#     go.Box(
#         y=df['A'], name='A'
#     )
# )
#
# fig.add_trace(
#     go.Box(
#         y=df['C'], name='C'
#     )
# )
# fig.show()


"""
분포 그래프 확인 - 도수분포표, 히스토그램
"""
# df = pd.DataFrame(np.random.rand(100000, 1), columns=['A'])
# # print(df.head())
#
# fig = go.Figure()
# fig.add_trace(
#     go.Histogram(
#         x=df['A'], name='A',
#             xbins=dict( # bins used for histogram
#                 start=0, # 각 구간을 어느정도로 나눌것인지 설정
#                 end=1.0,
#                 size=0.05
#             ),
#         marker_color='#F50057'
#     )
# )
#
# fig.update_layout(
#     title_text='Sampled Results', # title of plot
#     xaxis_title_text='Value', # xaxis label
#     yaxis_title_text='Count', # yaxis label
#     bargap=0.1, # gap between bars of adjacent location coordinates
#
# )
# fig.show()

"""
바, 원 그래프 예제 데이터
"""
# data = {
#     'year': ['2017', '2017', '2019', '2020', '2021', '2021'],
#     'grade': ['C', 'C', 'B', 'A', 'B', 'E'],
# }
#
# df = pd.DataFrame(data)
# df1 = df.groupby("grade").count()
# df2 = df.groupby("year").count()

# fig = go.Figure()
# fig.add_trace(
#     go.Bar(
#         x=df1.index, y=df1['year'], name='A'
#     )
# )
#
# fig.show()

"""
원그래프
"""
# fig = go.Figure()
# fig.add_trace(
#     go.Pie(
#         labels=df1.index, values=df1['year']
#     )
# )
#
# fig.show()


