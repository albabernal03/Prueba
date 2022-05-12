#importamso libreria
import pandas as pd
import os
import re

#PASO 1: unir los archivos de las carpetas ETFs y Stock en un solo csv

def ruta_carpeta_ETFs():
    path= '/Users/hectorbernaltrujillo/Documents/informática/Programación python/Prueba/archive (3)/ETFs'
    os.chdir(path)
ruta_carpeta_ETFs()

def unir_archivos_ETFs(path):
    archivos= [x for x in os.listdir() if re.search('.txt',x)]
    print(archivos)
    df= pd.DataFrame()
    for i in archivos:
        archivo=pd.read_csv(i)
        df= pd.concat([df,archivo])
    df.to_csv('datos_unidos_ETFs.csv')
    return df
unir_archivos_ETFs((ruta_carpeta_ETFs()))

