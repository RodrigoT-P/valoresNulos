import pandas as pd
from pandas import Series, DataFrame

clientes = pd.read_excel('clientes.xlsx', index_col=0)
devoluciones = pd.read_excel('devoluciones.xlsx', index_col=0)
facturacion = pd.read_excel('facturacion.xlsx', index_col=0)
notas_credito = pd.read_excel('notas_credito.xlsx', index_col=0)
precios = pd.read_excel('precios_productos.xlsx', index_col=0)

precios.info()

facturacion.info()

facturacion=facturacion.fillna({'FECHA_CANCELA':'--','CVE_VEND':'--','FECHA_ENTREGA':'--'})
facturacion.isnull().sum()

devoluciones=devoluciones.fillna({'DOC_ANT':'--', 'CVE_PEDI':'--', 'FECHA_CANCELA':'--','CVE_VEND':'--'})
devoluciones.isnull().sum()

clientes=clientes.fillna({'RFC':'--','NOMBRE':'--'})
clientes.isnull().sum()

notas_credito=notas_credito.fillna({'CVE_PEDI':'--','FECHA_CANCELA':'--','CVE_VEND':'--'})
notas_credito.isnull().sum()

#Convertir DataFrame a CSV
devoluciones.to_csv('devoluciones_sin_nulos.csv')
clientes.to_csv('clientes_sin_nulos.csv')
facturacion.to_csv('facturacion_sin_nulos.csv')
notas_credito.to_csv('notas_credito_sin_nulos.csv')

