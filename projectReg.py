#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:11:05 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""""""

Unit 2.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Read in data
#spending = pd.read_csv(r"C:\Users\rjr85\Box\stat2120\Rich\Course materials\Data\edu_spending.csv")
#opinion = pd.read_csv(r"C:\Users\rjr85\Box\stat2120\Rich\Course materials\Data\gov_opinion.csv")
url = 'https://raw.githubusercontent.com/UVAnog/statprojects/master/cars.csv'
cars = pd.read_csv(url)

#%%
"""""""""""""""""""""""""""""""""""""""
Linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = spending["Population"]
X = sm.add_constant(X)
y = spending["Spending"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

#%%
# Determine the coefficient of determination
r2 = model.rsquared
r2 = round(r2,4)
print("The coefficient of determination is " + str(r2) + ".")

#%%
# Determine the correlation coefficient
r = np.sqrt(r2)
r = round(r,4)
print("The correlation is " + str(r) + ".")

#%%
# Verify that this is indeed the correlation coefficient
r_check = np.corrcoef(x=spending.Population, y=spending.Spending)
print(r_check) 

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
# Determine the row for Florida
iFL = spending.State == 'Florida'

# Determine the predicted value for Florida
yhat_FL = model.fittedvalues[iFL]
yhat_FL = round(yhat_FL,1)
print(yhat_FL)

#%%
# Determine the residual for Florida
resid_FL = model.resid[iFL]
resid_FL = round(resid_FL,4)
print(resid_FL)

#%%
"""""""""""""""""""""""""""""""""""""""
Two-way tables
"""""""""""""""""""""""""""""""""""""""
# Create the two-way table
op_tbl = pd.crosstab(index=opinion.Generation, columns=opinion.Opinion,
                            margins=True)
print(op_tbl)

#%%
# Display proportions 
op_tbl_prop = op_tbl/op_tbl.loc["All","All"]
print(op_tbl_prop)

#%%
# Display conditional proportions
# Conditioned on the columns
op_tbl_cond_gen = op_tbl/op_tbl.loc["All",]
print(op_tbl_cond_gen)

# Conditioned on the rows
op_tbl_cond_op = op_tbl.div(op_tbl["All"], axis=0)
print(op_tbl_cond_op)

#%%
"""""""""""""""""""""""""""""""""""""""
Two-way tables without external data
"""""""""""""""""""""""""""""""""""""""
# Table values for 2x3 table
tbl_data = {'Column 1 name': [1,2],
            'Column 2 name': [3,4],
            'Column 3 name': [5,6]}
tbl = pd.DataFrame(tbl_data, 
                   columns=['Column 1 name','Column 2 name','Column 3 name'], 
                   index=['Row 1 name','Row 2 name'])

tbl.loc['All']= tbl.sum(axis=0)
tbl.loc[:,'All'] = tbl.sum(axis=1)

print(tbl)



#%%
"""""""""""""""""""""""""""""""""""""""

Unit 2.2 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplot
"""""""""""""""""""""""""""""""""""""""
sns.scatterplot(x="cyl", y="hp", data=cars)
plt.title("Correlation of Number of Cylinders to Horse Power")
plt.ylabel("Horsepower")
plt.xlabel("Number of Cylinders")

#%%

"""""""""""""""""""""""""""""""""""""""
Create scatterplot
"""""""""""""""""""""""""""""""""""""""
sns.scatterplot(x="cyl", y="wt", data=cars)
plt.title("Correlation of Weight to Number of Cylinders")
plt.ylabel("Weight")
plt.xlabel("Number of Cylinders")

#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplot with regression line
"""""""""""""""""""""""""""""""""""""""
sns.regplot(x="Population", y="Spending", data=spending, ci=0)
plt.title("State education spending")
plt.ylabel("Total spending (billion $)")
plt.xlabel("Population (millions)")

#%%
"""""""""""""""""""""""""""""""""""""""
Create bar graph
"""""""""""""""""""""""""""""""""""""""
sns.countplot(x="Generation", hue="Opinion", data=opinion)
plt.title("Opinion on federal government spending")

#%%

# Define the explanatory and response variables
X = cars["hp"]
X = sm.add_constant(X)
y = cars["qsec"]

# Apply the regression equation
model = sm.OLS(y, X).fit()


#%%
# Determine the coefficient of determination
r2 = model.rsquared
r2 = round(r2,4)
print("The coefficient of determination is " + str(r2) + ".")

#%%
# Determine the correlation coefficient
r = np.sqrt(r2)
r = round(r,4)
print("The correlation is " + str(r) + ".")
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

model.summary()