#!/bin/bash -l

#PBS -l nodes=1:ppn=4
#PBS -l mem=16gb
#PBS -l walltime=72:00:00
#PBS -o dqn-cpu.out
#PBS -e dqn-cpu.err
#PBS -N dqn-cpu
#PBS -V

cd $HOME
source .bashrc
source activate dqn
cd dev/AtariDominator
python main.py --use_gpu 0
