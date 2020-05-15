#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:41:06 2020

@author: Nolan
"""

# Install needed packages
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

#%%

# Null hypothesis
p0 = 0.8

# Sample and known values of 60 coin flips 
n = 60
tails = 25
phat = tails/n  

# Test statistic
test_stat = (tails - p0)/np.sqrt(p0*(1-p0)/n)
print(test_stat)



#%%
# p-value; test is right-tailed
pval = 1 - stats.norm.cdf(test_stat)
if pval < 0.05:
    print(pval)
    print("Reject the null hypothesis")
else:
    print("Accept possibility null hypothesis could be true")

#%%
#%%
# Determine z*
z_star = stats.norm.ppf(0.95)
z_star = round(z_star, 3)
print(z_star)

#%%
# Determine confidence interval

LL = phat - z_star * np.sqrt(phat*(1-phat)/n)
UL = phat + z_star * np.sqrt(phat*(1-phat)/n)

print("Lower level: ", round(LL,3))
print("Upper level: ", round(UL,3))
#%%
