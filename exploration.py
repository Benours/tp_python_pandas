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
'''
print(df.dtypes)
for column in df.columns:
    try:
        df[column] = df[column].astype(float)
    except Exception as e:
        print("An error occurred:", str(e))
for column in df_city.columns:
    try:
        df_city[column] = df_city[column].astype(float)
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

double = df_city[df_city['CODGEO'].isin(x)]
print(double)
invdouble = df_city[~df_city['CODGEO'].isin(x)]
print(invdouble)

double = double.sort_values('LIBGEO')
print(double)
invdouble = invdouble.sort_values('LIBGEO')
print(invdouble)

print(double.describe())
print(invdouble.describe())

print(invdouble)
print(double[double['NBPERSMENFISC16'] > 100000])

print(df_city[df_city['LIBGEO'].isin(['Montreuil', 'Saint-Denis'])])
'''

# Exercice 3
'''
df = df.set_index('INSEE commune')
df_city = df_city.set_index('CODGEO')
print(df)
print(df_city)
df['dep'] = df.index.str.slice(stop=2)
df_city['dep'] = df_city.index.str.slice(stop=2)

print(df)
print(df_city)

df_log = df.groupby('dep').count()[:5]

print(df_log)
df_log.plot(kind='bar')
plt.show()

df_sorted = df.groupby('dep').count().sort_values('CO2 biomasse hors-total')[:10]
print(df_sorted)
'''

# Exercice 4
'''
df_copy = df.copy()
df_copy2 = df.copy()

df_copy = df_copy.set_index('dep')
df_copy2 = df_copy2.reset_index()

import timeit
def somme_func_copy():
    somme = df_copy.groupby('dep')['CO2 biomasse hors-total'].sum()
    return somme
def somme_func_copy2():
    somme = df_copy2.groupby('dep')['CO2 biomasse hors-total'].sum()
    return somme

temps_copy = timeit.timeit(somme_func_copy, number=1)
temps_copy2 = timeit.timeit(somme_func_copy2, number=1)

print(str(temps_copy) + " secondes")
print(str(temps_copy2) + " secondes")
'''

# Exercice 5
'''
df_wide = df.copy()
print(df_wide.columns)

id_vars = ['Commune', 'dep']
df_wide = df_wide.drop(['INSEE commune'], axis=1)

df_long = pd.melt(df_wide, id_vars='Commune', var_name='Secteur', value_name='Emissions')

print(df_long)

df_long_sum = df_long.groupby('Secteur')['Emissions'].sum().reset_index()

print(df_long_sum)

plt.bar(df_long_sum['Secteur'], df_long_sum['Emissions'])
plt.show()
'''

# Exercice 6