#!/bin/bash -l

#PBS -l nodes=1:ppn=4:gpus=1:gpgpu
#PBS -l mem=8gb
#PBS -l walltime=60:00:00
#PBS -o dqn.out
#PBS -e dqn.err
#PBS -N dqn
#PBS -V

module add openblas
module add CUDA/7.5.18
module add cuDNN/4.0

cd $HOME
source .bashrc
source activate dqn
cd DQN-agent
python main.py --use_gpu 1