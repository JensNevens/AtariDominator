#!/bin/bash -l

#PBS -l nodes=1:ppn=4
#PBS -l mem=16gb
#PBS -l walltime=72:00:00
#PBS -o dqn.out
#PBS -e dqn.err
#PBS -N dqn
#PBS -V

module add openblas
module add CUDA/8.0.61
module add cuDNN/4.0

cd $HOME
source .bashrc
source activate dqn
cd AtariDominator
python main.py --use_gpu 0

