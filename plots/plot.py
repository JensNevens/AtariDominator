import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def plot(data_dir):
    # Get all files in data_dir
    paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    paths = [path for path in paths if os.path.splitext(path)[-1].lower() == '.csv']
    # Create a huge df with MultiIndex
    inner = list(range(len(paths)))
    df = pd.read_csv(paths[0], index_col=0)
    outer = np.array(df.columns)
    iterables = [outer, inner]
    cols = pd.MultiIndex.from_product(iterables, names=['metric', 'idx'])
    df = pd.DataFrame(columns=cols)
    # Dump all the data into it
    for i, path in enumerate(paths):
        df_in = pd.read_csv(path, index_col=0)
        for column in df_in:
            df.loc[:, (column,i)] = df_in[column]
    # Compute the means and stds
    for metric in df.columns.get_level_values(0).unique():
        df.loc[:, (metric, 'mean')] = df[metric].mean(axis=1)
        df.loc[:, (metric, 'std')] = df[metric].std(axis=1)
    # Create plots for every metric
    for metric in df.columns.get_level_values(0).unique():
        fig, ax = plt.subplots()
        start = 99999
        length = len(df)
        step = 50000
        X = list(range(start, (start+(length*step)), step))
        Y = df.loc[:, (metric, 'mean')]
        Y = Y.rolling(window=10, center=True).mean()
        bars = df.loc[:, (metric, 'std')]
        label = metric.split('/')[-1]
        ax.errorbar(X, Y, yerr=bars, fmt='b', errorevery=50, label=label)
        ax.legend(loc='best')
        ax.set_xlabel('steps')
        ax.grid(linestyle='--', linewidth=1, alpha=0.1)
        out_path = os.path.join(data_dir, label) + '.pdf'
        fig.savefig(out_path)

if __name__ == '__main__':
    args = sys.argv
    data_dir = args[1]
    plot(data_dir)
