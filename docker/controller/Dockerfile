FROM condaforge/mambaforge:latest

SHELL ["/bin/bash", "-c"]

# install basic dev tools and beautiful shell stuff
RUN apt update
RUN apt install micro bat git tmux fish curl -y

# install gcloud dependencies
RUN apt-get software-properties-common rsync install apt-transport-https ca-certificates gnupg ssh -y
RUN apt-get update
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get update && apt-get install google-cloud-cli

RUN apt-get install google-cloud-cli kubectl google-cloud-cli-app-engine-python google-cloud-cli-app-engine-python-extras

# install kubernetes dependencies

RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN add-apt-repository 'deb http://apt.kubernetes.io/ kubernetes-xenial main'
RUN apt-get install kubelet kubeadm kubectl kubernetes-cnisudo google-cloud-sdk-gke-gcloud-auth-plugin -y
RUN systemctl enable kubelet

RUN mkdir -p /root/.config/fish/
RUN touch /root/.config/fish/config.fish
RUN echo "starship init fish | source" >> ~/.config/fish/config.fish
RUN  echo 'eval "$(starship init bash)"' >> ~/.bashrc

ENTRYPOINT ["/bin/bash"]

# The Dockerfile is pretty straightforward. It starts with the base image,
# which is the mambaforge image. Then, it installs fish and creates a conda environment.
# It clones the TALI-collector repository and installs the dependencies.
# Finally, it sets the working directory to the TALI-collector repository and sets the
# entrypoint to the entrypoint.sh script.