import numpy as np
import matplotlib.pyplot as plt

#prevendo o lucro bruto.
#rev = receita.
rev_m = 170
rev_stdev = 20
interations = 1000

rev = np.random.normal(rev_m, rev_stdev, interations)

plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

#cmv
cogs = - (rev * np.random.normal(0.6,0.1))

plt.figure(figsize=(15, 6))
plt.plot(cogs)
plt.show()

cogs.mean()
cogs.std()


gross_profit = rev + cogs

plt.figure(figsize=(10.6));
plt.hist(gross_profit, bins = [40, 50, 60, 70, 80, 90, 100, 110, 120]);
plt.show()

plt.figure(figsize=(10.6));
plt.hist(gross_profit, bins = 20);
plt.show()

max(gross_profit)
min(gross_profit)
gross_profit.mean()
gross_profit.std()



