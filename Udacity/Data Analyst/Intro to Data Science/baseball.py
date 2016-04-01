# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:39:06 2016

@author: Todd
"""

import pandas as pd


def add_full_name(path_to_csv, path_to_new_csv):
    dataframe = pd.read_csv('./baseballDB/Master.csv')
    dataframe['nameFull'] = dataframe['nameFirst'] + ' ' + dataframe['nameLast']
    dataframe.to_csv('./baseballDB/fullName')
    print(dataframe['nameFull'])

add_full_name('./baseballDB/Master.csv', './baseballDB/fullName.csv')