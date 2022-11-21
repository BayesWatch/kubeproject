# Using the toolset
## Intallation
To install the toolset, and get your environment ready to run Kubernetes jobs, you need to:

1. Clone repository to your local machine, or to a remote machine meant to be the job submission client

```
git clone https://github.com/BayesWatch/bwatchcompute.git
```
2. If intenting to develop new features to push to the Github repository, you need to:
   1. Log into your github account
        ```bash
        gh auth login
        ```
    2. Set up your defaul email and name in github
        ```bash
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"
        ```
3. Sign in to your gcloud account:

    ```bash
    gcloud auth login
    ```

4. Select the gcloud project to be tali-multi-modal by running:

    ```bash
    gcloud config set project tali-multi-modal
    ```
5. Sign into the gpu kubernetes cluster
   ```bash
   gcloud container clusters get-credentials gpu-cluster-1 --zone us-central1-a --project tali-multi-modal
   ```

