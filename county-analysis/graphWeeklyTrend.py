# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:29:40 2020

@author: Madeleine
"""

import pandas as pd
import matplotlib.pyplot as plt

# generates a trend graph of COVID cases for the past week
dataFrame = pd.read_csv('NumCases_Nassau.csv')
x = dataFrame['Date']
y = dataFrame['NoOfCases']
plt.plot(x, y, 'ro-')
dataFrame[['Date','NoOfCases','NoOfCases']].apply(lambda row: plt.text(*row, va='top'),axis=1)
plt.title('Confirmed COVID-19 Cases in Nassau County from the Past 7 Days')
plt.xlabel('Date')
plt.ylabel('No. Of Cases')
plt.show()


