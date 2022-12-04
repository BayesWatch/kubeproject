#!/bin/bash
kubectl create secret generic wandb-vars \
    --from-literal=WANDB_API_KEY=$WANDB_API_KEY
