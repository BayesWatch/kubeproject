#!/bin/bash
export WANDB_API_KEY="my-wandb-key"
export WANDB_ENTITY=my-wandb-group
export WANDB_PROJECT=my-simple-kubernetes-project

export EXPERIMENTS_DIR=/store/experiments
export EXPERIMENT_DIR=/store/experiments

export DATASET_DIR=/store/datasets
export MODEL_DIR=/store/models

export CLUSTER_NAME=spot-gpu-cluster-1
export CLUSTER_ZONE=us-central1-a
export CLUSTER_PROJECT=my-cluster-name

export USER_EMAIL="my@email.me"
export USER_NAME="Name Surname"

gcloud config set project $CLUSTER_PROJECT
gcloud container clusters get-credentials $CLUSTER_NAME \
    --zone $CLUSTER_ZONE --project $CLUSTER_PROJECT
