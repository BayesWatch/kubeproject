# Advanced Tutorial using the MinimalMLTemplate repository and Kubernetes

This tutorial describes how one can use the bwatchcompute tools in combination with a generic ML project. We'll be using the MinimalMLTemplate that provides a stateless deep learning project template build on huggingface transformers, datasets and accelerate, as well as wandb and hydra-zen. 

## Installation

### Install the bwatchcompute toolkit

1. Install docker on your system.
2. Pull and run the bwatch controller docker by running:
   ```bash
   docker pull ghcr.io/bayeswatch/controller:0.1.0
   docker run -it ghcr.io/bayeswatch/controller:0.1.0
   ```
3. Clone the bwatchcompute repository to your container by running:
    ```
    git clone https://github.com/BayesWatch/bwatchcompute.git
    ```
4. (Optional) If intenting to develop new features to push to the Github repository, you need to:

    - Log into your github account
        ```bash
        gh auth login
        ```
    - Set up your defaul email and name in github
        ```bash
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"
        ```
5. Sign in to your gcloud account:

    ```bash
    gcloud auth login
    ```

6. Select the gcloud project to be tali-multi-modal by running:

    ```bash
    gcloud config set project tali-multi-modal
    ```

7. (Optional) If you don't already have a Kubernetes cluster with GPUs running, you can start one by running:

    ```bash
    bash bwatchcompute/gcp-helper-scripts/tali-kubecluster-spot-a100-gpu.sh
    ```

