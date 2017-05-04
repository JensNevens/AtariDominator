#!/bin/bash -l

#PBS -t 1-10

#PBS -l nodes=1:ppn=4:gpus=1:gpgpu
#PBS -l mem=16gb
#PBS -l walltime=120:00:00
#PBS -o Pong-base.out
#PBS -e Pong-base.err
#PBS -N Pong
#PBS -V

module add imkl
module add CUDA/8.0.61
module add cuDNN/6.0-CUDA-8.0.61

# Launch the matching script file
bash $HOME/dev/AtariDominator/jobs/Pong-run-${PBS_ARRAYID}.cmds
