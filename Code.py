import plotly.express as px
import pandas as pd
df = pd.read_csv("Data.csv")
print(df)

fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()
