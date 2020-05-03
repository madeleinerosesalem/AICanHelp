# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:06:00 2020

@author: Madeleine
"""
import pandas as pd
import numpy as np
from scipy import interpolate

# outputs the predicted number of cases and the percent increase in cases for the next 3 days
dataFrame = pd.read_csv('NumCases_Nassau.csv')
x = np.arange(0,5)
y = [dataFrame.iloc[2,1], dataFrame.iloc[3, 1], dataFrame.iloc[4, 1], dataFrame.iloc[5, 1], dataFrame.iloc[6, 1]]
f = interpolate.interp1d(x, y, fill_value='extrapolate')
print('The predicted number of COVID-19 cases in Nassau County for the next 3 days are:')
print(f(5), f(6), f(7))
z = ((f(7)-f(4))/f(4))*100
print('The predicted percent increase in COVID-19 cases in Nassau County over the next 3 days is:')
print(z)