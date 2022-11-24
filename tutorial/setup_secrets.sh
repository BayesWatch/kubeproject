#!/bin/bash
kubectl create namespace wandb-secrets

kubectl create secret generic wandb-vars \
    --from-literal=WANDB_API_KEY=$WANDB_API_KEY \
    --namespace=wandb-secrets
