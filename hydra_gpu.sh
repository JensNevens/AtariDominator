#!/bin/bash -l

#PBS -l nodes=1:ppn=4
#PBS -l feature=gpgpu
#PBS -l mem=16gb
#PBS -l walltime=72:00:00
#PBS -o dqn-gpu.out
#PBS -e dqn-gpu.err
#PBS -N dqn-gpu
#PBS -V

module add OpenBLAS
module add CUDA/8.0.61
#module add cuDNN/4.0
module add cuDNN/6.0-CUDA-8.0.61

cd $HOME
source .bashrc
source activate dqn
<<<<<<< HEAD
cd dev/AtariDominator
python main.py --use_gpu 1

