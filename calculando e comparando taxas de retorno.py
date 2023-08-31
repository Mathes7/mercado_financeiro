import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
import numpy as np

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')

df = df.set_index('Date')

# calculando a taxa de retorno de um ativo.

#taxa simples de um retorno
df['simple_return'] = (df['Adj Close']/df['Adj Close'].shift(1))-1
print(df['simple_return'])

df['simple_return'].plot(figsize=(8, 5))

#média diaria de retorno
avg_return_d = df['simple_return'].mean()

#média anual de retorno
avg_return_a = df['simple_return'].mean() * 250
print (str(round(avg_return_a, 5) * 100) + '%')

#retornos logarimos
df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))

df['log_return'].plot(figsize=(8, 5))

#retornos logarimos diario
log_return_d = df['log_return'].mean()

#retornos logarimos anual
log_return_a = df['log_return'].mean() * 250

#calculando a taxa de retorno dos índices
(df['Adj Close'] / df['Adj Close'].iloc[0] * 100).plot(figsize=(15, 6));

ind_returns = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
annual_ind_returns = ind_returns.mean() * 250






# trabalhando com varias ações
tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']
    
(mydata / mydata.iloc[0] * 100).plot(figsize = (15,6));
plt.show()

#retorno simples
returns = (mydata / mydata.shift(1)) - 1
weights = np.array([0.25, 0.25, 0.25, 0.25])
np.dot(returns, weights)

annual_returns = returns.mean() * 250
pfolio_1 = str(round(np.dot(annual_returns, weights),5) * 100) +' %'

#comparando com outra carteira
weights_2 = np.array([0.4, 0.4, 0.15, 0.15])
pfolio_2 = str(round(np.dot(annual_returns, weights_2),5) * 100) +' %'
print (pfolio_1)
print (pfolio_1)

