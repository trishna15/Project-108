import csv
import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("108.csv")

fig = pf.create_distplot([df["Avg Rating"].tolist()], ["Rating"])

fig.show()