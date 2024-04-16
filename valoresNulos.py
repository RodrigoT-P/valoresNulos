import pandas as pd
import numpy as np
df=pd.read_csv("ventas_totales.csv")
#print(df.head())
#print(df.isnull().sum())

#Quitar nulos en la columna de ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Quital nulos de columna TARJETAS DE DEBITO
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Quitar nulos de columna TARJETAS DE CREDITO
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
valores_nulos=df.isnull().sum()
print(valores_nulos)