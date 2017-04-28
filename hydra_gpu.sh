#!/bin/bash -l

#PBS -l nodes=1:ppn=4:gpus=1:gpgpu
#PBS -l mem=16gb
#PBS -l walltime=120:00:00
#PBS -o Pong.out
#PBS -e Pong.err
#PBS -N Pong
#PBS -V

module add imkl
module add CUDA/8.0.61
module add cuDNN/6.0-CUDA-8.0.61

cd $HOME
source .bashrc
source activate dqn
cd dev/AtariDominator
python main.py --use_gpu 1 --is_train True --env_name Pong-v0 --model base
