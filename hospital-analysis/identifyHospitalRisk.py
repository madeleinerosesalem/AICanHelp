# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:17:54 2020

@author: Madeleine
"""
import pandas as pd

#generate graphs for classifying risk of all hospitals in a county
df = pd.read_csv('Nassau_HospitalData.csv')
ax = df.plot(kind='scatter',
             x='Number of Confirmed Cases in City',
             y='Number of ICU Beds', 
             c='Risk Index', 
             colormap='autumn', 
             title='Risk Classification of Hospitals in Nassau County Based on Supply and Demand',
             s=120, 
             linewidth=0)
df[['Number of Confirmed Cases in City','Number of ICU Beds','Hospital']].apply(lambda row: ax.text(*row, va='top'),axis=1)
