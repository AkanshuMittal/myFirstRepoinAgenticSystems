import pandas as pd
import plotly.express as px

df = pd.read_csv("eda-checklist/iris.csv")

# Observation: Inspect the dataset structure
print(df.head())

print(df.tail())

print(df.shape)

print(df.info())

print(df.describe())
