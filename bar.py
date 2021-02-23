import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")

fig=px.bar(df,x="Country",y="Internet Users",title="Country VS Internet Users",color="Country")

fig.show()