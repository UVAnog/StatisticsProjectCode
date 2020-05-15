#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:24:43 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""""""

Unit 4.4 examples

"""""""""""""""""""""""""""""""""""""""
# Import packages
import numpy as np

# Fill in the amounts associated with spaces A' through I'
X = np.array([100, 500, 1000, 0, 10000, 0, 1000, 500, 100])

# Fill in the probabilities that the chip falls into spaces A' through I' when starting at each location
P_A = np.array([0.226])
P_B = np.array([0.193 ])
P_C = np.array([0.121])
P_D = np.array([0.054])
P_E = np.array([0.016])
P_F = np.array([0.003])
P_G = np.array([0])
P_H = np.array([0])
P_I = np.array([0])


#%%
# Calculate the mean starting at each location
mu_A = np.sum(X * P_A)
mu_B = np.sum(X * P_B)
mu_C = np.sum(X * P_C)
mu_D = np.sum(X * P_D)
mu_E = np.sum(X * P_E)
mu_F = np.sum(X * P_F)
mu_G = np.sum(X * P_G)
mu_H = np.sum(X * P_H)
mu_I = np.sum(X * P_I)

# Print each mean with this statement modified appropriately
# Round to two decimal places where needed
print("Expected winnings starting at location A is $" + str(mu_A))
print("Expected winnings starting at location B is $" + str(mu_B))
print("Expected winnings starting at location C is $" + str(mu_C))
print("Expected winnings starting at location D is $" + str(mu_D))
print("Expected winnings starting at location E is $" + str(mu_E))
print("Expected winnings starting at location F is $" + str(mu_F))
print("Expected winnings starting at location G is $" + str(mu_G))
print("Expected winnings starting at location H is $" + str(mu_H))
print("Expected winnings starting at location I is $" + str(mu_I))



#%%
# Calculate the standard deviation of winnings starting at each location
sigma_A = np.sqrt(np.sum((X-mu_A)**2 * P_A))
sigma_B = np.sqrt(np.sum((X-mu_B)**2 * P_B))
sigma_C = np.sqrt(np.sum((X-mu_C)**2 * P_C))
sigma_D = np.sqrt(np.sum((X-mu_D)**2 * P_D))
sigma_E = np.sqrt(np.sum((X-mu_E)**2 * P_E)) 
sigma_F = np.sqrt(np.sum((X-mu_F)**2 * P_F))
sigma_G = np.sqrt(np.sum((X-mu_G)**2 * P_G))
sigma_H = np.sqrt(np.sum((X-mu_H)**2 * P_H))
sigma_I = np.sqrt(np.sum((X-mu_I)**2 * P_I))

# Print each standard deviation with this statement modified appropriately
# Round to two decimal places where needed
print("Standard deviation of winnings starting at location A is $" + str(sigma_A))
print("Standard deviation of winnings starting at location B is $" + str(sigma_B))
print("Standard deviation of winnings starting at location C is $" + str(sigma_C))
print("Standard deviation of winnings starting at location D is $" + str(sigma_D))
print("Standard deviation of winnings starting at location E is $" + str(sigma_E))
print("Standard deviation of winnings starting at location F is $" + str(sigma_F))
print("Standard deviation of winnings starting at location G is $" + str(sigma_G))
print("Standard deviation of winnings starting at location H is $" + str(sigma_H))
print("Standard deviation of winnings starting at location I is $" + str(sigma_I))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:45:15 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""

Unit 4.1 lab activity









"""""""""""""""""""""""""""""""""""
# Install needed packages
import random

# Define the sample space with all possible outcomes of a flip
SS = ['H','T']

# Define the number of flips
my_n = 75

# Generate the outcomes
outcomes = random.choices(SS, k=my_n)
print(outcomes)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:07:07 2020

@author: Nolan
"""


import numpy as np
print((1+2+4)/3)
print(np.sqrt)




#%%

"""""""""""""""""""""""""""""""""""""""

Unit 6.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats


# Population parameters
mu = 405.17
sigma = 210.59

#%%
"""""""""""""""""""""""""""""""""""""""
Sampling distribution parameters
"""""""""""""""""""""""""""""""""""""""
sigma_xbar25 = sigma/np.sqrt(25)
sigma_xbar50 = sigma/np.sqrt(50)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that the 
sample mean of a sample of 25 is less 
than $350?
"""""""""""""""""""""""""""""""""""""""
xbar = 350
z = (xbar - mu)/(sigma/np.sqrt(25))

P1 = stats.norm.cdf(z)
P1 = round(P1, 4)
print(P1)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that the 
sample mean of a sample of 50 is less 
than $350?
"""""""""""""""""""""""""""""""""""""""
xbar = 350
z = (xbar - mu)/(sigma/np.sqrt(50))

P2 = stats.norm.cdf(z)
P2 = round(P2, 4)
print(P2)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 6.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

text = pd.read_csv(r"C:\Users\rr3pp\Box\stat2120\Rich\Course materials\Data\textbook.csv")


#%%
"""""""""""""""""""""""""""""""""""""""
Create population histogram
"""""""""""""""""""""""""""""""""""""""
sns.distplot(text.Amount, bins=8, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of amount spent on textbooks")
plt.ylabel("Frequency")
plt.xlabel("Amount in dollars")


#%%
"""""""""""""""""""""""""""""""""""""""
Create sampling distribution histogram
"""""""""""""""""""""""""""""""""""""""
# Define sample size
my_n = 25 

# Create list to store sample means
means25_list = []

# Draw a sample, calculate and store the sample mean of that sample
# Repeat this process 10,000 times
for i in range(0, 10000):
    samp = text.sample(n=my_n)
    samp_mean = np.mean(samp.Amount)
    means25_list.append(samp_mean)
    
# Display the 10,000 sample means in a histogram
sns.distplot(means25_list, bins=10, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of sample means with n=25")
plt.ylabel("Frequency")
plt.xlabel("Amount in dollars")
plt.xlim(250,600)


#%%
# Define sample size
my_n = 50 

# Create list to store sample means
means50_list = []

# Draw a sample, calculate and store the sample mean of that sample
# Repeat this process 10,000 times
for i in range(0, 10000):
    samp = text.sample(n=my_n)
    samp_mean = np.mean(samp.Amount)
    means50_list.append(samp_mean)

# Display the 10,000 sample means in a histogram
sns.distplot(means50_list, bins=10, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of sample means with n=50")
plt.ylabel("Frequency")
plt.xlabel("Amount in dollars")
plt.xlim(250,600)




#%%

X = np.array([1, 3/2, 2, 5/2, 3, 4])
P = np.array([1/9, 2/9, 1/9, 2/9, 2/9, 1/9])

mu_X = np.sum(X * P)
print(mu_X)

sigma2_X = np.sum((X-mu_X) ** 2 * P)
print(sigma2_X)

sigma_X = np.sqrt(sigma2_X)
sigma_X = round(sigma_X, 4)
print(sigma_X)


#%%

mu_p = 1.25
k = 0

p = stats.poisson.pmf(k, mu_p)
p = round(p, 4)
print(p)

#%%

n = 10000
k = 1
p = 0.00005

print(str(1 - stats.binom.cdf(k, n, p)))

#%%

mu_p = 0.1078
k = 2
p1 = stats.poisson.cdf(k-1, mu_p)
print(1 - p1)

#%%

n = 182
k = 1
p = 0.0054

p = stats.binom.cf(k-1, n, p)
print(1-p)

