# Script de Preparación de Datos
###################################

import pandas as pd
import numpy as np
import lifetimes
import os

# Leemos los archivos csv

def read_file_csv(filename):
    df = pd.read_csv(os.path.join('../data/raw/', filename))
    print(filename, ' cargado correctamente')
    return df

# Funciones para manejon de outliers

def find_boundaries(df, variable, q1=0.05, q2=0.95):

    # the boundaries are the quantiles
    lower_boundary = df[variable].quantile(q1)
    upper_boundary = df[variable].quantile(q2)
    return upper_boundary, lower_boundary

def capping_outliers(df, variable):

    # aplica los límites de los quantiles
    upper_boundary,lower_boundary =  find_boundaries(df,variable)
    df[variable] = np.where(df[variable] > upper_boundary, upper_boundary,
                            np.where(df[variable] < lower_boundary, lower_boundary, df[variable]))

# Generación del archivo rfm

def data_preparation(df):

    # Nos quedamos los valores de Precio y Cantidad mayores a cero
    df = df[df['Quantity'] > 0 ]
    df = df[df['UnitPrice'] > 0]
    df = df[~df['InvoiceNo'].str.contains("C",na=False)] # drop returned items

    # Eliminación de outliers
    df.dropna(inplace=True)

    # Aplicando las reglas para manejo de outliers
    capping_outliers(df,'UnitPrice')
    capping_outliers(df,'Quantity')

    # Filtra valores 'Usamos solo del Reino Unido'
    df = df[df.Country == 'United Kingdom']

    # Se crea la columna 'Total Price'
    df['Total Price'] = df['UnitPrice'] * df['Quantity']

    # Creating Summary Dataset
    clv = lifetimes.utils.summary_data_from_transaction_data(df,'CustomerID',
                                                             'InvoiceDate',
                                                             'Total Price',
                                                             observation_period_end='2011-12-09')

    # we want only customers shopped more than 2 times
    clv = clv[clv['frequency']>1]

    print('Archivo de frecuencia, recencia, value correctamente generado')
    return clv

# Exportamos la tabla rfm

def data_exporting(df, filename):
    
    df.to_csv(os.path.join('../data/processed/', filename))
    print(filename, 'exportado correctamente en la carpeta processed')


def main():
    # Lectura del archivo original
    df1 = read_file_csv('Online_Retail.csv')

    # Generación del archivo clv  customer lifetime value
    clv1 = data_preparation(df1)

    # Exporta clv1
    data_exporting(clv1, 'rfm_data.csv')
 