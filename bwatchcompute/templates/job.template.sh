export WANDB_API_KEY=
export WANDB_ENTITY=machinelearningbrewery
export WANDB_PROJECT=simple-kubernetes

export EXPERIMENTS_DIR=/data/experiments
export EXPERIMENT_DIR=/data/experiments

export DATASET_DIR=/data
export MODEL_DIR=/data/models

git clone $git_repo_path$
cd $code_directory$

$python_command$ $args$

