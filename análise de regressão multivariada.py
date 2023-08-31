import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')


# com todas variaveis.
x = df[['Open', 'High', 'Low', 'Close']]
y = df['Adj Close']

x1 = sm.add.constant(x)
reg = sm.OLS(y, x1).fit()

reg.summary()

# sem o close.
x = df[['Open', 'High', 'Low']]
y = df['Adj Close']

x1 = sm.add.constant(x)
reg = sm.OLS(y, x1).fit()

reg.summary()