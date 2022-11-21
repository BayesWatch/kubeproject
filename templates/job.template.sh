WANDB_API_KEY=
WANDB_ENTITY=machinelearningbrewery
WANDB_PROJECT=simple-kubernetes

#######################################################################################

EXPERIMENTS_DIR=/data/experiments
EXPERIMENT_DIR=/data/experiments

DATASET_DIR=/data
MODEL_DIR=/data/models

git clone $git_repo_path$
cd $code_directory$

$python_command$ $args$

