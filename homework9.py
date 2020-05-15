#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:48:36 2020

@author: Nolan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:38:27 2020

@author: Nolan
"""

"""""""""""""""""""""""""""""""""""""""

Unit 8.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import scipy.stats as stats
import pandas as pd

#%%
"""""""""""""""""""""""""""""""""""""""
Venmo
"""""""""""""""""""""""""""""""""""""""
# Null hypothesis
p0 = 0.5

#  Sample and known values
n = 52
X = 42
phat = X/n  

# Test statistic
test_stat = (phat - p0)/np.sqrt(p0*(1-p0)/n)
print(test_stat)

#%%
# p-value; test is right-tailed
pval = 1 - stats.norm.cdf(test_stat)
print(pval)


#%%
# Determine z*
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

#%%
# Determine confidence interval
LL = phat - z_star * np.sqrt(phat*(1-phat)/n)
UL = phat + z_star * np.sqrt(phat*(1-phat)/n)

print(round(LL,3))
print(round(UL,3))


#%%
"""""""""""""""""""""""""""""""""""""""
Sample size
"""""""""""""""""""""""""""""""""""""""
m_star = 0.05
p_star = 0.5

n = (z_star / m_star)**2 * p_star*(1-p_star)
n = np.ceil(n)
print(n)

#%%

url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/morning.csv"
morning = pd.read_csv(url)

#%%

xbar = np.mean(morning.Morning_time)
s = np.std(morning.Morning_time)
n = 473
test = (xbar - 55)/(s/np.sqrt(n))
print(test)
pval = stats.t.cdf(test, df = n-1)
print(pval)

#%%

t_star = stats.t.ppf(.975, df = n - 1)
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)
print(round(LL,3))
print(round(UL,3))

#%%

# 1 = female 
# 2 = male
print('----------- FEMALES -----------')
xbar1 = np.mean(morning.loc[morning['Identified_gender'] == 'Female'].Morning_time) 

s1 = np.std(morning.Morning_time)
n1 = 473
test1 = (xbar1 - 55)/(s1/np.sqrt(n1))
print(test1.round(4))
pval1 = stats.t.cdf(test, df = n-1)
print(pval1.round(4))
print('----------- MALES -----------')
xbar2 = np.mean(morning.loc[morning['Identified_gender'] == 'Male'].Morning_time) 

s2 = np.std(morning.Morning_time)
n2 = 473
test2 = (xbar2 - 55)/(s2/np.sqrt(n2))
print(test2.round(4))
pval2 = stats.t.cdf(test, df = n-1)
print(pval2.round(4))

print('----------- FEMALES -----------')

t_star1 = stats.t.ppf(.95, df = n1 - 1)
LL1 = xbar1 - t_star1 * s1/np.sqrt(n1)
UL1 = xbar1 + t_star1 * s1/np.sqrt(n1)
print(round(LL1,3))
print(round(UL1,3))

print('----------- MALES -----------')


t_star2 = stats.t.ppf(.95, df = n2 - 1)
LL2 = xbar2 - t_star2 * s2/np.sqrt(n2)
UL2 = xbar2 + t_star2 * s2/np.sqrt(n2)
print(round(LL2,3))
print(round(UL2,3))
#%%


print(np.mean(morning.Morning_time))
print(np.std(morning.Morning_time))

#%%

url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/social_media.csv"
media = pd.read_csv(url)

