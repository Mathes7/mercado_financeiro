import pandas as pd
import numpy as np
from scipy.stats import norm

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')

# s-preço da ação.
# k-preço de exercício.
# r-taxa livre de risco.
# stdev - desvio padrão.
# t-intervalo de tempo (anos)

# funções para os valores que vão entrar na função de black sholes merton.
def d1(s, k, stdev, t):
    return (np.log(s / k) + (r + stdev ** 2 / 2) * t) / (stdev * np.sqrt(t))

def d2(s, k, stdev, t):
    return (np.log(s / k) + (r + stdev ** 2 / 2) * t) / (stdev * np.sqrt(t))

norm.cdf(0)
norm.cdf(0.25)
norm.cdf(0.75)
norm.cdf(9)

#função de black sholes merton.
def bsm(s, k, r, stdev, t):
    return (s * norm.cdf(d1(s, k, r, stdev, t))) - (k * np.exp(-r * t) * norm.cdf(d2(s, k, r, stdev, t)))

s = df['Adj Close'].iloc[-1]

log_returns = np.log(1 + df['Adj Close'].pct_change())

stdev = log_returns.std() * 250 ** 0.5

r = 0.025
k = 110.0
t = 1

d1(s, k, stdev, t)
d2(s, k, stdev, t)

# preço da opção de compra.
bsm(s, k, r, stdev, t)