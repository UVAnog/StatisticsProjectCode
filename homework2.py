#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:22:28 2020

@author: Nolan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns


url = 'https://raw.githubusercontent.com/UVAnog/statprojects/master/fastfood.csv'

fastfood_data = pd.read_csv(url)







sns.scatterplot(x = 'Restaurants', y = 'Obesity', data=fastfood_data)

#%%

x = fastfood_data['Restaurants']
y = fastfood_data['Obesity']

cor = np.corrcoef(x, y)
print(cor)
#%%

# Define the explanatory and response variables
X = fastfood_data['Restaurants']
y = fastfood_data['Obesity']
X = sm.add_constant(X)

# Apply the regression equation
model = sm.OLS(y, X).fit()

model_est = model.params
# Determine the regression equation
b0 = round(model_est[0], 4)
b1 = round(model_est[1], 4)
print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")

#%%

vaSix = 22.4026 + (1.8995 * 4.3)
print(vaSix)

#%%

r2 = model.rsquared
r2 = round(r2,4)
print("The coefficient of determination is " + str(r2) + ".")

