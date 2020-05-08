# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:00:26 2020

@author: Sudham Hebbar
"""


import numpy as np
import pandas as pd


data = np.zeros((200,5), dtype=float)

np.random.seed(42)
data[:100,4] = 0
data[100:,4] = 1



for i in range(data.shape[1]-1):
    data[:100, i] = np.random.random((1,100))*15
    data[100:, i] = np.random.random((1,100))*75

df = pd.DataFrame(data, columns= ['Feature'+str(i) for i in range(1,5)]+['label'])
df.to_csv("RandomDataSet.csv", index=False)


df = pd.read_csv('RandomDataSet.csv')
df.head()
