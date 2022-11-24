# BWatch Compute Toolkit
## Installation
To install the toolset, and get your environment ready to run Kubernetes jobs, you need to:
1. Log into a machine to be used as the job generator and submission terminal. We recommend that this is a google cloud VM with at least 4 CPU cores, or, your local machine -- although doing this on a google cloud VM generally has less probability of issues. 
2. Pull and run the controller docker by running:
   ```bash
   docker pull ghcr.io/bayeswatch/controller:0.1.0
   docker run -it ghcr.io/bayeswatch/controller:0.1.0
   ```
3. Clone repository to your local machine, or to a remote machine meant to be the job submission client

    ```
    git clone https://github.com/BayesWatch/bwatchcompute.git
    ```
4. If intenting to develop new features to push to the Github repository, you need to:
   1. Log into your github account
        ```bash
        gh auth login
        ```
    2. Set up your defaul email and name in github
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
7. Sign into the gpu kubernetes cluster
   ```bash
   gcloud container clusters get-credentials gpu-cluster-1 --zone us-central1-a --project tali-multi-modal
   ```

## Cheatsheet

Listing VM nodes of the cluster
```bash
kubectl get nodes
```

Listing pods of the cluster
```bash
kubectl get pods
```

Listing jobs of the cluster
```bash
kubectl get jobs
```

Read logs of a particular pod
```bash
kubectl logs <pod_id>
```

Read meta logs of a particular pod
```bash
kubectl describe pod <pod_id>
```

Submit a job to the cluster
```bash
kubectl create -f job.yaml
```
