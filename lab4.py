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

