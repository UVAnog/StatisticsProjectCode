#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:36:00 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""""""

Unit 11.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import pandas as pd
import statsmodels.api as sm

# Read in data
hospital = pd.read_csv(r"C:\Users\gaf9f\Documents\2120 Fall 2019\Course materials\Data\hospital.csv")

#%%
"""""""""""""""""""""""""""""""""""""""
Multiple linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = hospital[["Stay", "Age", "Xray"]]
X = sm.add_constant(X)
y = hospital["Risk"]

# Apply the regression equation
model = sm.OLS(y, X).fit()





#%%
# Determine the regression equation estimates
bj = round(model.params,3)
print(bj)

#%%
# Predicted value
yhat = model.fittedvalues[0]
yhat = round(yhat,1)
print(yhat)

#%%
# Specify value for prediction
Xnew = pd.DataFrame([[1,  7.13, 55.7, 39.6]])

# Predict for that value
pred_new = model.predict(Xnew)
pred_new = round(pred_new, 1)
print(pred_new)

#%%
# t-test and confidence interval for the slope
model_output = model.summary()
print(model_output)



#%%
############
# SLR
############
# Define the explanatory and response variables
X2 = hospital["Age"]
X2 = sm.add_constant(X2)
y = hospital["Risk"]

# Apply the regression equation
model2 = sm.OLS(y, X2).fit()

# t-test for slope
model2_output = model2.summary()
print(model2_output)


#%%
# Correlation matrix
exp_var = hospital[["Stay", "Age", "Xray"]]
corr = exp_var.corr()
print(corr)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 11.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url = 'https://raw.githubusercontent.com/UVAnog/statprojects/master/cars.csv'
cars = pd.read_csv(url)

#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplots
"""""""""""""""""""""""""""""""""""""""
sns.scatterplot(x="Stay", y="Risk", data=hospital)
plt.title("Infection risk and average length of stay")

#%%
sns.scatterplot(x="Age", y="Risk", data=hospital)
plt.title("Infection risk and average patient age")

#%%
sns.scatterplot(x="Xray", y="Risk", data=hospital)
plt.title("Infection risk and number of x-rays given")



#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plots 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = cars[["wt", "cyl", "hp"]]
X = sm.add_constant(X)
y = cars["qsec"]

# Apply the regression equation
model = sm.OLS(y, X).fit()
print(model)
# Store the residuals and predicted values
m_resid = model.resid
m_pred = model.fittedvalues

#%%
# Create plot 
sns.residplot(x=m_pred, y=m_resid)
plt.title("Residual plot (predicted)")
plt.ylabel("Residuals")
plt.xlabel("Predicted values")

#%%
# Create plot 
sns.residplot(x=cars.wt, y=m_resid)
plt.title("Residual plot (weight)")
plt.ylabel("Residuals")
plt.xlabel("weight")

#%%
# Create plot 
sns.residplot(x=cars.hp, y=m_resid)
plt.title("Residual plot (horsepower)")
plt.ylabel("Residuals")
plt.xlabel("horsepower")

#%%
# Create plot 
sns.residplot(x=cars.cyl, y=m_resid)
plt.title("Residual plot (number of cylinders)")
plt.ylabel("Residuals")
plt.xlabel("cylinders")



