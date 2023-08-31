import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')

df_returns = np.log(df['Adj Close']/df['Adj Close'].shift(1))
cov = df_returns.cov() * 250
cov_with_market = cov.ioloc[0,1]
market_var = df['Adj Close']

#beta.
df_beta = cov_with_market / market_var

# calculando o capm.
df_er = 0.025 + df_beta * 0.05

# calculando o indice de charpe.
sharpe = (df_er - 0.025) / (df_returns.std() * 250 **0.5)




