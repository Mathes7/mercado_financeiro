import numpy as np
import pandas as pd

from scipy import stats 
import statsmodels.api as sm

import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')

df[['Open', 'Close']]

#%% regressão univariada.

x = df['Open']
y = df['Close']

plt.scatter(x, y)         

x1 = sm.add_constant(x)

reg = sm.OLS(y, x1).fit()
reg.summary()                  

# calculando alfa, beta e r ao quadrado.

slope, intercep, r_value, p_value, sdr_err = stats.linregress(x,y)

