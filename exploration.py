import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download

df = pd.read_csv("data/IGT - Pouvoir de réchauffement global.csv", sep=",")

df_city = pynsee.download.download_file("FILOSOFI_COM_2016")
meta = pynsee.get_file_list()
meta.loc[meta['label'].str.contains(r"Filosofi.*2016")]

# Exercice 1

'''
print(df.head(10))
print(df.tail(15))
print(df.sample(10))
print(df.sample(int(0.05 * len(df)), replace=False))
head = df.head(10)
sample = head.sample(100, replace=True)
print(sample)

head = df.head(6)
weights = [0.5] + [0.1]*(len(head) - 1)
draws = head.sample(100, replace=True, weights=weights)

print(draws)
'''
'''
print(df_city.head(10))
print(df_city.tail(15))
print(df_city.sample(10))
print(df_city.sample(int(0.05 * len(df_city)), replace=False))
head = df_city.head(10)
sample = head.sample(100, replace=True)
print(sample)

head = df_city.head(6)
weights = [0.5] + [0.1]*(len(head) - 1)
draws = head.sample(100, replace=True, weights=weights)

print(draws)
'''

# Exercice 2

print(df.dtypes)
for column in df.columns:
    try:
        df[column] = df[column].astype('float64')
    except Exception as e:
        print("An error occurred:", str(e))

print(df_city.dtypes)

print(df.ndim)
print(df_city.ndim)

print(df['Commune'].count())
print(df_city['LIBGEO'].count())

grouped = df_city.groupby('LIBGEO')['CODGEO'].nunique()
duplicates = grouped[grouped > 1]
x = df_city[df_city['LIBGEO'].isin(duplicates.index)]['CODGEO'].unique()
print(len(x))

double = df_city[df_city['CODGEO'].isin(x)].nunique()
print(double)
invdouble = df_city[~df_city['CODGEO'].isin(x)]
print(invdouble)

double = double.sort_values('LIBGEO')
print(double)
invdouble = invdouble.sort_values('LIBGEO')
print(invdouble)

print(double.describe())
print(invdouble.describe())
