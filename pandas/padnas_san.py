import san
import plotly.graph_objects as go
import plotly.offline as pyo # jupyter notebook 에서 보여지도록 설정하는 부분 (가끔 안나올 때, 이 명령을 하면 됨)


bitcoin_data = san.get("ohlcv/bitcoin")

# print(bitcoin_data.head())
# print(bitcoin_data.tail())

# print(bitcoin_data.shape)
# print(bitcoin_data.info())

# print(bitcoin_data.columns)

# print(bitcoin_data.describe())

data = bitcoin_data.copy()
data['MA'] = data['closePriceUsd'].rolling(window=5, min_periods=1).mean()
data["trades"] = data['MA'] < data['closePriceUsd']
data["returns"] = data['closePriceUsd'].pct_change()
data['BACKTEST'] = (data["returns"].shift(-1) * data["trades"] + 1).cumprod()

print(data['BACKTEST'])

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data.index, y=data['BACKTEST'], mode='lines'
    )
)
fig.show()