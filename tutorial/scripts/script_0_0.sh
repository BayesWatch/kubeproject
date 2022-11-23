#!/bin/bash
export WANDB_API_KEY=9a295b91cf65c412f681e492d6b92fe4be4b000b
export WANDB_ENTITY=machinelearningbrewery
export WANDB_PROJECT=simple-kubernetes

export EXPERIMENTS_DIR=/data/experiments
export EXPERIMENT_DIR=/data/experiments

export DATASET_DIR=/data
export MODEL_DIR=/data/models

git clone https://github.com/BayesWatch/bwatchcompute.git
cd bwatchcompute
python tutorial/simple.py --i 0 --j 0
