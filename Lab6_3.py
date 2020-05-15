#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:17:25 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""

Unit 6.3 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import numpy as np
import scipy.stats as stats

# Read in the data
# Read in the data
url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/coins_collection.csv"
coins = pd.read_csv(url)

#%%
# Draw your simple random sample
import random
n = 35
outcomes = random.choices(coins['Age'], k=n)
print(outcomes)

#%%
# Calculate sample mean
xbar = np.mean(outcomes).round(4)
print(xbar)

#%%
# Calculate test statistic
sigma = 3.059924
mu0 = 2.5
n = 35
z = (xbar - mu0)/(sigma/np.sqrt(n))
print(z)
#%%
# Determine p-value
pval = 1 - stats.norm.cdf(z)
print(pval)




