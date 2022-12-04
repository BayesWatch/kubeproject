#!/bin/bash
kubectl create secret generic wandb-vars \
    --from-literal=KEY_NAME=VALUE
