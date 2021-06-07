# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:31:32 2020

@author: DELL
"""

import pandas as pd
import config

def load_dataset(name):
    df_data = pd.read_csv(f'{config.DATASET_FOLDER}\{name}.csv')
    return df_data

def save_dataset(df_data,name):
    df_data.to_csv(f'{config.DATASET_FOLDER}\{name}.csv',index=False)
    return