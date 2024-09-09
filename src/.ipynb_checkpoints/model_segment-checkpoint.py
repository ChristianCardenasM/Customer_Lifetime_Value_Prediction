# Cogigo que aplica los modelos y genera la data de segmentación

import pandas as pd
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
import dill
import pickle
import os

#from mkdata_rfm import read_file_csv

def model_segmentation(file_rfm, file_segmento, t=180):

    # Lectura del archivo rfm recency, frecuencia value.

    clv = pd.read_csv(os.path.join('../data/processed', file_rfm))
    print(file_rfm, ' cargado correctamente')

    # Leemos los modelos entrenados para usarlo
    
    bgf_package = '../models/bgf_model.pkl'
    bgf_loaded = pickle.load(open(bgf_package, 'rb'))

    ggf_package = '../models/ggf_model.pkl'
    ggf_loaded = pickle.load(open(ggf_package, 'rb'))
    
    print('Modelos importado correctamente')

    # Number of purchases
    # t = 180 # 30 day period
    
    clv['expected_purc_6_months'] = \
    bgf_loaded.conditional_expected_number_of_purchases_up_to_time(t, clv['frequency'], clv['recency'], clv['T'])

    # Customer Lifetime Value
    clv['6_Months_CLV']=ggf_loaded.customer_lifetime_value(bgf_loaded,
                                                    clv["frequency"],
                                                    clv["recency"],
                                                    clv["T"],
                                                    clv["monetary_value"],
                                                    time=t/30,
                                                    freq='D',
                                                    discount_rate=0.01)

    clv.to_csv(f'../data/segments/{file_segmento}')
    print(f'Archivo de segmentación {file_segmento} generado y guardado')

    return clv


def main():
    
    df = model_segmentation(file_rfm='rfm_data.csv', file_segmento='segmentos.csv')
    print('Finalizó la segmentación de la base')


if __name__ == "__main__":
    main()