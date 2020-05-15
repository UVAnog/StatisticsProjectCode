#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:08:35 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""""""

Unit 11.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

# Read in data
url = 'https://raw.githubusercontent.com/UVAnog/statprojects/master/cars.csv'
cars = pd.read_csv(url)

#%%
"""""""""""""""""""""""""""""""""""""""
Multiple linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = cars[["hp", "wt", "cyl"]]
X = sm.add_constant(X)
y = cars["qsec"]

# Apply the regression equation
model = sm.OLS(y, X).fit()
print(model.summary())

#%%
# Regression standard error
s = np.sqrt(model.mse_resid)
s = round(s, 2)
print(s)

#%%
# Coefficient of determination
r2 = model.ess/model.centered_tss
r2 = round(r2, 3)
print(r2)

r2 = model.rsquared
r2 = round(r2, 3)
print(r2)

#%%
# ANOVA F test
model_output = model.summary()
print(model_output)


#%%
"""""""""""""""""""""""""""""""""""""""
Extended multiple linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X_ext = cars[["hp", "wt", "cyl"]]
X_ext = sm.add_constant(X_ext)
y = cars["qsec"]

# Apply the regression equation
model_ext = sm.OLS(y, X_ext).fit()


#%%
# Partial F test
r2_2 = model.rsquared
r2_1 = model_ext.rsquared
 
p = 5
q = 2
n = model.nobs

# Test statistic
test_stat = ( (n-p-1) / q )*( (r2_1-r2_2) / (1-r2_1) )
test_stat = round(test_stat, 2)
print(test_stat)

#%%
# p-value
pval = 1 - stats.f.cdf(test_stat, q, n-p-1)
pval = round(pval, 4)
print(pval)


#%%
# Adjusted R-squared
print(model_output)

#%%
# Adjusted R-squared: original
adj_r2 = model.rsquared_adj
adj_r2 = round(adj_r2, 3)
print(adj_r2)

#%%
# Adjusted R-squared: extended
adj_r2_ext = model_ext.rsquared_adj
adj_r2_ext = round(adj_r2_ext, 3)
print(adj_r2_ext)


#%%

#%%

# Define the explanatory and response variables
X = cars[["hp"]]
X = sm.add_constant(X)
y = cars["qsec"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Determine the row for Florida
iFL = cars.model == 'Dodge Challenger'


# Determine the predicted value for Florida
yhat_dodge = model.fittedvalues[iFL]
yhat_dodge = round(yhat_dodge,1)
print(yhat_dodge)

#%%

seconds = cars['qsec']
average = np.mean(seconds)
# Known values
n = average

# Null hypothesis
mu0 = 16.87

#  Sample values
xbar = np.mean(cars.qsec)
s = np.std(cars.hp, ddof = 1)

# Test statistic
test_stat = (xbar - mu0)/(s/np.sqrt(n))
print(test_stat)

#%%
# p-value; test is left-tailed
pval = stats.t.cdf(test_stat, df=n-1)
print(pval)


#%%
# Determine t*
t_star = stats.t.ppf(0.975, df=n-1)
t_star = round(t_star, 3)
print(t_star)

#%%
# Determine confidence interval
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))

#%%

"""""""""""""""""""""""""""""""""""""""
T test on slopes
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = cars["hp"]
X = sm.add_constant(X)
y = cars["qsec"]

# Apply the regression equation
model = sm.OLS(y, X)
results = model_ext.fit()
slope = results.params[0]
p_value = stats.t.sf(results.tvalues[0], results.df_resid)

null_hypothesis = 1.4282
t_value = ((slope - (null_hypothesis))/results.bse) #bse = standard error
p_value = stats.t.sf(t_value, results.df_resid) #calculate p-value from t-statistic lookup tables

print("T value: ", t_value)
print("P value: ", p_value)