#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:22:41 2020

@author: Nolan
"""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
url = 'https://raw.githubusercontent.com/UVAnog/statprojects/master/ozark.csv'
streams = pd.read_csv(url)

#%%
##scatterplots

sns.scatterplot(x="Area", y="IBI", data=streams)
plt.title("Relationship between Area and IBI")

#%%

sns.scatterplot(x="Forest", y="IBI", data=streams)
plt.title("Relationship between Forest and IBI")

#%%

#model

# Define the explanatory and response variables
X = streams[["Area", "Forest"]]
X = sm.add_constant(X)
y = streams["IBI"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

#print(model.summary())
#%%

#%%
# Determine the b0 and b1 values
model_est = model.params
print(model_est)

#%%
# Determine the regression equation
b0 = round(model_est[0], 4)
b1 = round(model_est[1], 4)

print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")

#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plots 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = streams[["Area", "Forest"]]
X = sm.add_constant(X)
y = streams["IBI"]

# Apply the regression equation
model = sm.OLS(y, X).fit()
print(model)
# Store the residuals and predicted values
m_resid = model.resid
m_pred = model.fittedvalues

#%%
# Residual Plots


# Create plot 
sns.residplot(x=m_pred, y=m_resid)
plt.title("Residual plot (predicted)")
plt.ylabel("Residuals")
plt.xlabel("Predicted values")

#%%
# Create plot 
sns.residplot(x=streams.Area, y=m_resid)
plt.title("Residual plot (Area)")
plt.ylabel("Residuals")
plt.xlabel("Area")

#%%
# Create plot 
sns.residplot(x=streams.Forest, y=m_resid)
plt.title("Residual plot (Forest)")
plt.ylabel("Residuals")
plt.xlabel("Forest")


#%%
# Determine the regression equation estimates
estimates = round(model.params,3)
print(estimates)

#%%
# Predicted value
yhat = model.fittedvalues[0]
yhat = round(yhat,1)
print(yhat)

#%%
# Specify value for prediction
Xnew = pd.DataFrame([[47, 21, 0]])

# Predict for that value
pred_new = model.predict(Xnew)
pred_new = round(pred_new, 1)
print(pred_new)

#%%
