#!/bin/bash
export WANDB_API_KEY=9a295b91cf65c412f681e492d6b92fe4be4b000b
export WANDB_ENTITY=machinelearningbrewery
export WANDB_PROJECT=simple-kubernetes-tutorial

export EXPERIMENTS_DIR=/volume/experiments
export EXPERIMENT_DIR=/volume/experiments

export DATASET_DIR=/volume/datasets
export MODEL_DIR=/volume/models

export CLUSTER_NAME=spot-gpu-cluster-1
export CLUSTER_ZONE=us-central1-f
export CLUSTER_PROJECT=tali-multi-modal

export USER_EMAIL="iam@antreas.io"
export USER_NAME="Antreas Antoniou"

gcloud config set project $CLUSTER_PROJECT
gcloud container clusters get-credentials $CLUSTER_NAME \
    --zone $CLUSTER_ZONE --project $CLUSTER_PROJECT
