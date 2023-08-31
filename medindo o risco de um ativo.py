import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
import numpy as np


df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')

df = df.set_index('Date')

#retorno logaritimo.

df_returns = np.log(df['Adj Close'] / df['Adj Close'].shift(1))

#%%média.

# retorno médio diario.
df_returns.mean()

#retorno médio anual.
df_returns.mean() * 250

#%% desvio padrão.

df_returns.std()

df_returns.std() * 250 ** 0.5

#%% covariância e correlação.

#variancias.

df_var = df_returns.var()

df_var_ano = df_returns.var() * 250

#covariância.
df_cov = df_returns.cov()

df_cov_ano = df_returns.cov() * 250

# correlação.
df_corr = df_returns.corr()

#%% calculando o risco de um portifolio.

#esquema de peso igual
weights = np.array([0.5, 0.5])

#variancia do portifolio.
pfolio_vari = np.dot(weights.T,np.dot(df_returns)*250,weights))

#volatividade do portifolio.
pfolio_vari = (np.dot(weights.T,np.dot(df_returns)*250,weights))) ** 0.5

print(str(round(pfolio_vol, 5) * 100)) + '%'

#%%calculando o risco diversificável e não diversicável.
#risco divesificavel.
df_div_a = df_returns.var() * 250

dr = df_var - (weights[0] ** 2 * df_1_var_a) - (weights[1] ** 2 * df_2_var_a)

#não diversificavel.
n_dr = df_var - dr
