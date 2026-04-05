import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('gapminder(2007) (1).csv')
print(df.head())

print(df.info())

print(df.isnull().any())

labels=['population','life_exp','gdp_cap']

for l in labels:
    sns.boxplot(y=df[l],palette='winter')
    plt.show()

sns.boxplot(x='continent',y='gdp_cap',data=df,palette='viridis')
plt.show()

sns.boxplot(x='continent',y='life_exp',data=df,palette='viridis')
plt.show()

sns.violinplot(x='continent',y='gdp_cap',data=df,palette='bright')
plt.show()

sns.violinplot(x='continent',y='life_exp',data=df,palette='bright')
plt.show()

for l in labels:
    sns.kdeplot(df[l])
    plt.show()

for l in labels:
    plt.hist(df[l])
    plt.xlabel(l)
    plt.show()

for l in labels:
    sns.distplot(df[l])
    plt.show()
    print('Skewness is:',df[l].skew())