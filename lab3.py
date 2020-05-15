"""""""""""""""""""""""""""""""""""

Unit 3 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd

# Read in the data
url = "https://raw.githubusercontent.com/UVAnog/statprojects/master/buildings.csv"
build = pd.read_csv(url)

#%%









# Draw your simple random sample
# Define the sample size
s = 4

# Draw the random sample
samp_builds = build.sample(n=s)
print(samp_builds)
