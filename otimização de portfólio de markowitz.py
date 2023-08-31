import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 
%matplotlib inline 

df = pd.read_csv('C:/Users/mathe/Downloads/PETR4.SA.csv')
df = df.set_index('Date')

(df / df.iloc[0] * 100).plot(figsize=(10,5))

#retorno logaritmo.

log_return = np.log(df/df.shift(1))

log_return.mean()

log_return.cov()

log_return.corr()

# variavel que vai contar o número de ativos.
num_assets = len(assets)

#criando dois número aleatorios.
arr = np.random.random(2)

arr[0] + arr[1]

weigths = np.random.random(num_assets)
weigths /= np.sum(weighs)

weights[0] + weights[1]

#%% retorno esperado de um portifolio.

np.sum(weights * log_returns.mean()) * 250 

# variancia esparada de um portifolio.

np.dot(weghts.T, np.dot(log_returns.cov() * 250, weights))

# volatividade esparada de um portifolio.

np.sqrt(np.dot(weghts.T, np.dot(log_returns.cov() * 250, weights)))

# gráfico 
pfolio_retuns = []
pfolio_volatilities = []

for x in range(1000):
    weights = np.random(num_assents)
    weigths /= np.sum(weighs)
    pfolio_returns.append(np.sum(weights * log_returns.mean( ))*250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.araay(pfolio_volatilities)

portifolios = pd.DataFrame({'Return':pfolio_returns, 'Volatility': pfolio_volatilities})

portifolios.plot(x='Volatility', y='Return', kind='scatter',figsize=(10,6));
plt.xlabel('Explored Volstility')
plt.ylabel('Expected Return')
    