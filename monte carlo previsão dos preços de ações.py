import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 
from scipy.stats import norm
%matplotlib inline 

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')

log_returns = np.log(1+df['Adj Close'].pct_change())
log_returns.tail()

df['Adj Close'].plot(figsize=(10,6))

log_returns.plot(figsize=(10,6))

u = log_returns.mean()

var = log_returns.var()

#melhor aproximação das taxas futuras de uma ação.
drift = u -(0.5 * var)

#desvio padrão.
stdev = log_returns.std()

#transformando os valores em arrays do numpy.
np.array(drift)

#para retornar os valores como arreys.
drift.values
stdev.values

#corresponde a distância entre a média e os eventos, expresso pelo número de desvio padrão.
norm.ppf(0.95)

#implementando o segundo elemento.
x = np.random.rand(10,2)
norm.ppf(x)

z = norm.ppf(np.random.rand(10,2))

#
t_intervals = 1000
interations = 10

#retorno diário.
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, interations)))

#ponto de partida do preço da ação.
s0 = df['Adj Close'].iloc[-1]

#definindo o preço final das ações.
price_list = np.zeros_like(daily_returns)

price_list[0] = s0

for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
    
plt.figure(figsize=(10,6))
plt.plot(price_list);

