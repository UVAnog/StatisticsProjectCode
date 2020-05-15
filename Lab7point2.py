#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:45:57 2020

@author: Nolan
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/UVAnog/statprojects/master/rounded_stroop.csv'
stroopData = pd.read_csv(url)

