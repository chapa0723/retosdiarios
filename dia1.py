""""
Dado un fichero excel con nombres y correos (columna nombre y columna email), realiza un script en Python que devuelva los mails únicos de la columna email.
Consideraciones: Utiliza la librería pandas para procesar el fichero Excel (.xls).
"""
import pandas as pd
path = 'dia1.xlsx'
planilla = pd.read_excel(path)
print (planilla) # mostrará toda la hoja
columna = pd.read_excel(path, usecols=[1])
print (columna) # mostrará solo la columna 2





