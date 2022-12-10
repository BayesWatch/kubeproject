#!/bin/bash
kubectl create secret generic antreas-vars \
    --from-literal=WANDB_API_KEY=$WANDB_API_KEY
