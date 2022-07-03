import pandas as pd
import plotly.graph_objects as go

pd.set_option('display.max_column', None)

doc = pd.read_csv("01_data/아파트(매매)__실거래가_20050901_20060831.csv", encoding='utf-8-sig', error_bad_lines=False)


def func(row):
    row["계약년월일"] = str(row["계약년월"]) + "{0:02d}".format(row["계약일"])
    return row


doc = doc.apply(func, axis=1)


doc["계약년월일"] = pd.to_datetime(doc["계약년월일"], format="%Y%m%d", errors='raise')
# print(doc.head())

# print(dir(doc['계약년월일'].dt))

doc["year"] = doc["계약년월일"].dt.year
doc["day"] = doc["계약년월일"].dt.day
doc["weekday"] = doc["계약년월일"].dt.weekday
doc["month"] = doc["계약년월일"].dt.month
doc["quarter"] = doc["계약년월일"].dt.quarter

# print(doc["year"])

doc_day = doc.groupby('day').count()
doc_weekday = doc.groupby('weekday').count()
doc_month = doc.groupby('month').count()
doc_quarter = doc.groupby('quarter').count()

# print(doc_quarter.head())

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=doc_day.index,
        y=doc_day['시군구']
    )
)

fig.update_layout(
    {
        "title": {
            "text": "날짜별 거래건수",
            "x": 0.5,
            "y": 0.9,
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "showticklabels":True,
            "dtick": "1",
            "tickfont": {
                "size": 10
            }
        }
    }
)

# fig.show()

print(doc.info())