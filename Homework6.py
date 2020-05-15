#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:44:03 2020

@author: Nolan
"""

# Install needed packages
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/cholesterol.csv"
data = pd.read_csv(url)


#%%
# getting data 
level = data['level']
xbar = np.mean(level)
print("Mean: ", mean)


#%%
z_star = stats.norm.ppf(0.99)
z_star = round(z_star, 3)
print(z_star)

#%%
# creating confidence interval 
sigma = 47.7
average = xbar

UP = (xbar + z_star * sigma/np.sqrt(37)).round(4)
LL = (xbar - z_star * sigma/np.sqrt(37)).round(4)
print("UP: ", UP)
print("LOW: ", LL)



