import plotly.graph_objects as go
import pandas as pd



# ## plotly.graph_objects
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=[1, 2, 3], y=[1, 2, 3]
#     )
# )
# # fig.show()
#
# print(dir(go))

## 라인 그래프 테스트

df = pd.DataFrame({
    "A": [2.1, 2.2, 2.3, 2, 3],
    "B": [0.4, 0.5, 0.45, 0.3, 1]
})
# print(df.head())
#
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=df.index, y=df["A"]
#     )
# )
# fig.show()

# ## 복합 라인 그래프 그리기
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=df.index, y=df['B'], mode='lines', name='B'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=df.index, y=df['A'], mode='lines+markers+text', name='A', text=df['A'], textposition='top center'
#     )
# )
#
# fig.update_layout(
#     {
#         "title": {
#             "text": "Graph with go.Scatter",
#             "font": {
#                 "size": 15
#             }
#         },
#         "showlegend": True,
#         "xaxis": {
#             "title": "random number"
#         },
#         "yaxis": {
#             "title": "A"
#         }
#     }
# )
#
# fig.show()

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=df.index, y=df['A'], name='A', text=df['A'], textposition='auto'
    )
)

fig.add_trace(
    go.Bar(
        x=df.index, y=df['B'], name='B', text=df['B'], textposition='auto'
    )
)

fig.update_layout(
    {
        "title": {
            "text": "Graph with <b>go.Bar</b>",
            "x": 0.5,
            "y": 0.9,
            "font": {
                "size": 20
            }
        },
        "showlegend": True,
        "xaxis": {
            "title": "random number",
            "showticklabels": False,
            "dtick": 1

        },
        "yaxis": {
            "title": "A"
        },
        "autosize": False,
        "width": 800,
        "height": 340

    }
)

fig.show()