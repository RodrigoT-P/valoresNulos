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
#print(valores_nulos)

#Eliminar nulos columna OTROS MEDIO
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#ELIMINAR NULOS EN LA COLUMNA SUBTOTAL VENTAS
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Eliminar nulos en la columna BEBIDAS
df['bebidas'] =df['bebidas'].fillna(round(df['bebidas'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Eliminar nulos columna ALMACEN
df['almacen'] =df['almacen'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Eliminar duplicados de la columna panaderia
df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Eliminar nulos en columna LACTEOS
df['lacteos'] =df['lacteos'].fillna(0)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Eliminar nulos en columna carne
df['carnes'] =df['carnes'].fillna(round(df['carnes'].median(),1))

#Eliminar nulos en la columna verduleria_fruteria
df['verduleria_fruteria'] =df['verduleria_fruteria'].fillna(method='bfill')

#Elimar nulos en columna alimentos_preparados
df['alimentos_preparados_rotiseria'] =df['alimentos_preparados_rotiseria'].fillna(method='ffill')

print(valores_nulos)
df.to_csv("Ventas_totales_limpio")
