import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

def plot(data_dir, mean_only=False):
    # Get all files in data_dir
    files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    # We assume the following data_dir:
    # ../../../ENV_NAME/VAL_NAME/*.csv
    # For example: tf-data/Pong-DQN/average-q/*.csv
    path = os.path.normpath(data_dir)
    head, val_name = os.path.split(path)
    _, env_name = os.path.split(head)

    # Create one big dataframe
    df = pd.DataFrame()
    row_sizes = []
    for i, f in enumerate(files):
        if 'scalars' in f:
            f_path = os.path.join(data_dir, f)
            data = pd.read_csv(f_path)
            if 'step' not in df.columns:
                df.loc[:, 'step'] = data.loc[:, 'Step']
            colname = 'run' + str(i)
            df.loc[:, colname] = data.loc[:, 'Value']
            run_length = len(data['Value'])
            row_sizes.append(run_length)

    # Compute mean and std, ommit 'step' column
    df1 = df.drop(['step'], axis=1)
    df.loc[:, 'mean'] = df1.mean(axis=1)
    df.loc[:, 'std'] = df1.std(axis=1)

    # Create the plot
    fig, ax = plt.subplots()
    for column in df:
        if 'run' in column:
            col_data = np.array(df.loc[:, column])
            if not mean_only:
                ax.plot(df.loc[:, 'step'], col_data, 'b--', alpha=0.3, label=None)
    rolling_mean = df.loc[:, 'mean'].rolling(window=10, center=True).mean()
    ax.errorbar(df.loc[:, 'step'], rolling_mean, yerr=df.loc[:, 'std'], fmt='b', errorevery=10, label=val_name)
    ax.legend(loc='best')
    ax.set_xlabel('steps')
    ax.set_ylabel(val_name)
    # ax.set_title('Average score per episode')
    ax.grid(linestyle='--', linewidth=1, alpha=0.1)
    # plt.show()

    fig.savefig(env_name + '-' + val_name + '.pdf')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot tensorboard csv data.')
    parser.add_argument('dir', type=str, help='The directory that contains the CSV files')
    parser.add_argument('-m', '--meanonly', action='store_true', help='Bool to indicate to plot the mean only')
    args = parser.parse_args()
    plot(args.dir, mean_only=args.meanonly)
