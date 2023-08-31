import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt 
%matplotlib inline 

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')

# s-preço da ação.
# k-preço de exercício.
# r-taxa livre de risco.
# stdev - desvio padrão.
# t-intervalo de tempo (anos

log_returns = np.log(1 + df['Adj Close'].pct_change())

r = 0.025

stdev = log_returns.std() * 250 ** 0.5
stdev = stdev.values

t = 1.0
t_intervals = 250
delta_t = t / t_intervals

interations t_intervals= 10000

#matriz com elementos aleatorios extraidos de uma distribuição normal.

np.random.standard_normal((t_intervals + 1, interations))
s = np.zeros_like(z)
s0 = df['Adj Close'].iloc[-1]
s[0] = s0

# criando uma matriz completa com os valores das ações.
for t in range(1,t_intervals + 1):
    s[t] = s[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * z[t])
    
s.shape

plt.figure(figsize=(10,6))
plt.plot(s[:, :10]);

#como saber se compra ou não.
#se positivo é comprado, em casa contario não.

p = np.maximum(s[-1] - 110, 0)

p.shape

c = np.exp(-r * t) * np.sum(p) / iterations