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

# Observation: Identifying the possible outliers in the dataset
fig2 = px.box(df, y='petal_length', title='Box Plot for Outlier Detection')

fig2.show()

# Observation: Analyzing the relationship between two features

fig_3 = px.scatter(df, x='petal_length', y='petal_width', color='species',
           title='Petal Length vs Width')          

fig_3.show()

# Observation: Insights about different species

## Different species show noticeable differences in their petal and sepal measurements, which helps in distinguishing them from each other.
## Petal length and petal width appear to be strong features, as they clearly separate some species into distinct clusters and can be useful for classification.