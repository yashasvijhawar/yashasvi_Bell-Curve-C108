import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
Avg_df = df["Avg Rating"].tolist()

fig = ff.create_distplot([Avg_df],["Average Rating"],show_hist=False)
fig.show()
