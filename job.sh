#!/bin/bash -l

#PBS -l nodes=1:ppn=8
#PBS -l mem=20gb
#PBS -l walltime=10:00:00
#PBS -o logs-912.out
#PBS -e logs-912.err
#PBS -N LOGS-912
#PBS -V

cd $HOME
source .bashrc
source activate dqn
cd dev/AtariDominator
python logs.py /u/jnevens/dev/AtariDominator/logs/Pong-v0/min_delta--1/max_delta-1/history_length-4/train_frequency-4/target_q_update_step-10000/double_q-False/memory_size-250000/action_repeat-4/ep_end_t-1000000/dueling-False/min_reward--1.0/backend-tf/random_start-30/scale-10000/env_type-detail/learning_rate_decay_step-50000/ep_start-1.0/random_seed-912/screen_width-84/learn_start-50000.0/cnn_format-NHWC/learning_rate-0.00025/batch_size-32/discount-0.99/max_step-50000000/max_reward-1.0/learning_rate_decay-0.96/learning_rate_minimum-0.00025/env_name-Pong-v0/ep_end-0.01/nb_heads-10/model-base/screen_height-84/events.out.tfevents.1496047205.nic141 /u/jnevens/Pong-seed-912.csv
