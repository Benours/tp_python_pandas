import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@localhost:8889/fromagerie")
sql_select_query = "select * from dataw_fro where qte > 5 and timbrecli > 0"
df = pandas.read_sql(sql_select_query, engine)
df_cp_cc_dc = df.groupby(['cpcli', 'codcli', 'timbrecde'])

print(df.columns)
print(df.head())
print(df_cp_cc_dc.agg({'prixcond': 'mean'}))
print(df_cp_cc_dc.agg({'qte': 'sum'}))
print(df_cp_cc_dc.describe())