#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:03:53 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""

Unit 6.2 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/coins_collection.csv"
coins = pd.read_csv(url)

#%%
# Create population histogram

plt.title("Histogram of age of coins")
plt.ylabel("Frequency")
plt.xlabel("Age")
sns.distplot(coins, bins=11, kde=False, color="white", hist_kws=dict(edgecolor="black"))


#%%
# Draw your simple random sample
import random
n = 35
outcomes = random.choices(coins['Age'], k=n)
print(outcomes)


#%%
# Calculate your sample mean
xbar = np.mean(outcomes).round(4)
print(xbar)

#%%
# Determine z*
z_star = stats.norm.ppf(0.90)
z_star = round(z_star, 3)
print(z_star)


#%%
# Calculate your CI
sigma = 3.059924
average = 4.0857
UP = (xbar + z_star * sigma/np.sqrt(35)).round(4)
LL = (xbar - z_star * sigma/np.sqrt(35)).round(4)
print("UP: ", UP)
print("LOW: ", LL)


#%%
# Margin of error. z score * standard deviation

marginError = (z_star * sigma).round(4)
print(marginError)

#%%
# Confidence Interval 

