# Cogigo que aplica los modelos y genera la data de segmentación

import pandas as pd
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
import dill
import pickle
import os


def model_segmentation(filename, t=180):

    clv = pd.read_csv(os.path.join('../data/processed', filename))
    print(filename, ' cargado correctamente')

    # Leemos los modelo entrenado para usarlo
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

    return clv
