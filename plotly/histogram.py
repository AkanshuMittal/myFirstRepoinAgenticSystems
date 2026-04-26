import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "age": [22, 25, 26, 28, 30, 31, 35, 36, 40, 42]
})

fig = px.histogram(
    df,
    x="age",
    title='Age distribution of App users'
    #nbins=4
)

fig.update_traces(
    xbins = dict(
        start = 18,
        end = 50,
        size = 8
    )
)

fig.show()