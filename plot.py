import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def correct_df(df):
   rows = len(df)
   half = (rows/2)-1
   return df.loc[:half, :]

df = pd.DataFrame()

# Collect all scores in a single dataframe
for i in range(1,11):
     filename = 'scalars' + str(i) + '.csv'
     run = pd.read_csv(filename)
     if i == 1:
         # There is something wrong with the 1st run
         run = correct_df(run)
         df.loc[:, 'step'] = run['Step']
     colname = 'run' + str(i)
     df.loc[:, colname] = run['Value']

# Compute mean and std
df1 = df.drop(['step'], axis=1)
df.loc[:, 'mean'] = df1.mean(axis=1)
df.loc[:, 'std'] = df1.std(axis=1)

# Create plot
fig, ax = plt.subplots()
for i in range(1,11):
     colname = 'run' + str(i)
     col = np.array(df.loc[:, colname])
     ax.plot(df.loc[:, 'step'], col, 'b--', alpha=0.3, label=None)
rolling_mean = df.loc[:, 'mean'].rolling(window=10, center=True).mean()
ax.errorbar(df.loc[:, 'step'], rolling_mean, yerr=df.loc[:, 'std'], fmt='b', errorevery=10, label='Pong')
ax.legend(loc='best')
ax.set_xlabel('Steps')
ax.set_ylabel('Score')
ax.set_title('Average score per episode')
ax.grid(linestyle='--', linewidth=1, alpha=0.1)
plt.show()

fig.savefig('plot-test.pdf')
