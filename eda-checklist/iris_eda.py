import pandas as pd
import plotly.express as px

df = pd.read_csv("eda-checklist/iris.csv")

# Observation: Inspect the dataset structure
print(df.head())

print(df.tail())

print(df.shape)

print(df.describe())

# Observation: Checking column information and missing values
print(df.info())

print(df.isnull().sum())

print(df.dtypes)

print(df.columns)
