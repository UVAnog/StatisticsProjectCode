#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:06:47 2020

@author: Nolan
"""
"""""""""""""""""""""""""""""""""""

Unit 2.2 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
q# Read in the data
url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/OSU_beer.csv"
osu_data = pd.read_csv(url)

#%%
# Define the explanatory and response variables
X = osu_data['Beers']
X = sm.add_constant(X)
y = osu_data['BAC']

# Apply the regression equation
model = sm.OLS(y, X).fit()

model_est = model.params
# Determine the regression equation
b0 = round(model_est[0], 4)
b1 = round(model_est[1], 4)
print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")

#%%
# Determine the coefficient of determination

#square of corr coefficient 
#so... square the corr coef ..

r2 = model.rsquared
r2 = round(r2,4)
print("The coefficient of determination is " + str(r2) + ".")

#%%
# Determine the predicted BAC for 15 beers
#The regression equation is: y = -0.0127 + 0.018x.

bac15 = -0.0127 + (0.018 * 15)
print(bac15)
#%%
# Determine the row for the participant who drank 6
#six = osu_data['Beers' == 6]
six = osu_data.Beers == 6
bacsix = model.resid[six]
bacsix = round(bacsix,4)
print("The residual for the participant who drank 6 is " + str(bacsix))

#%%






