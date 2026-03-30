import pandas as pd
import plotly.express as px

df = pd.read_csv("eda-checklist/iris.csv")

# Observation: Inspect the dataset structure
print(df.head())

print(df.tail())

print(df.info())

print(df.shape)

print(df.describe())

# Observation: Checking column information and missing values
print(df.info())

print(df.isnull().sum())

print(df.dtypes)

print(df.columns)

# Observation: Analyzing the distribution of one feature
import plotly.express as px

fig = px.histogram(df, x='petal_length', title='Distribution of Petal Length')

fig.show()

# Observation: Analyzing the distribution of one feature
fig2 = px.box(df, y='petal_length', title='Box Plot for Outlier Detection')

fig2.show()