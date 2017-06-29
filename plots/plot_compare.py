import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def plot(data1, data2):
    dataname1 = data1.split('/')[-1]
    dataname2 = data2.split('/')[-1]
    # Get all files in data_dir
    paths1 = [os.path.join(data1, f) for f in os.listdir(data1)]
    paths1 = [path for path in paths1 if os.path.splitext(path)[-1].lower() == '.csv']
    paths2 = [os.path.join(data2, f) for f in os.listdir(data2)]
    paths2 = [path for path in paths2 if os.path.splitext(path)[-1].lower() == '.csv']
    # Create a huge df with MultiIndex
    inner1 = list(range(len(paths1)))
    df = pd.read_csv(paths1[0], index_col=0)
    outer1 = np.array(df.columns)
    outer1 = list(map(lambda col: col.split('/')[-1], outer1))
    iterables1 = [outer1, inner1]
    cols1 = pd.MultiIndex.from_product(iterables1, names=['metric', 'idx'])
    df1 = pd.DataFrame(columns=cols1)
    inner2 = list(range(len(paths2)))
    df = pd.read_csv(paths2[0], index_col=0)
    outer2 = np.array(df.columns)
    outer2 = list(map(lambda col: col.split('/')[-1], outer2))
    iterables2 = [outer2, inner2]
    cols2 = pd.MultiIndex.from_product(iterables2, names=['metric', 'idx'])
    df2 = pd.DataFrame(columns=cols2)
    # Dump all the data into it
    for i, path in enumerate(paths1):
        df_in = pd.read_csv(path, index_col=0)
        for column in df_in:
            normalized_col = column.split('/')[-1]
            df1.loc[:, (normalized_col,i)] = df_in[column]
    for i, path in enumerate(paths2):
        df_in = pd.read_csv(path, index_col=0)
        for column in df_in:
            normalized_col = column.split('/')[-1]
            df2.loc[:, (normalized_col,i)] = df_in[column]
    # Compute the means and stds
    for metric in df1.columns.get_level_values(0).unique():
        df1.loc[:, (metric, 'mean')] = df1[metric].mean(axis=1)
        df1.loc[:, (metric, 'std')] = df1[metric].std(axis=1)
    for metric in df2.columns.get_level_values(0).unique():
        df2.loc[:, (metric, 'mean')] = df2[metric].mean(axis=1)
        df2.loc[:, (metric, 'std')] = df2[metric].std(axis=1)
    # Create plots for every metric
    for metric in df1.columns.get_level_values(0).unique():
        fig, ax = plt.subplots()
        start = 99999
        step = 50000
        length1 = len(df1)
        length2 = len(df2)
        X1 = list(range(start, (start+(length1*step)), step))
        X2 = list(range(start, (start+(length2*step)), step))
        Y1 = df1.loc[:, (metric, 'mean')]
        Y1 = Y1.rolling(window=10, center=True).mean()
        Y2 = df2.loc[:, (metric, 'mean')]
        Y2 = Y2.rolling(window=10, center=True).mean()
        bars1 = df1.loc[:, (metric, 'std')]
        bars2 = df2.loc[:, (metric, 'std')]
        title = metric.split('/')[-1]
        ax.errorbar(X1, Y1, yerr=bars1, fmt='b', errorevery=50, capsize=5, label=dataname1)
        ax.errorbar(X2, Y2, yerr=bars2, fmt='g', errorevery=50, capsize=5, label=dataname2)
        ax.legend(loc='best')
        ax.set_xlabel('steps')
        ax.set_title(title)
        ax.grid(linestyle='--', linewidth=1)
        out_path = './' + title + '.pdf'
        fig.savefig(out_path)
        fig.clf()

if __name__ == '__main__':
    args = sys.argv
    data1 = args[1]
    data2 = args[2]
    plot(data1, data2)
