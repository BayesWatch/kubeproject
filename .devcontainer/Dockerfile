FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest

SHELL ["/bin/bash", "-c"]

# install basic dev tools and beautiful shell stuff
RUN apt update
RUN apt install micro bat git tmux fish curl aptitude -y

RUN apt update
RUN apt install -y ca-certificates curl
RUN apt install -y apt-transport-https
RUN curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list

RUN apt update
RUN aptitude install kubelet kubeadm kubectl -y

RUN type -p curl >/dev/null || apt install curl -y
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& apt update \
&& apt install gh -y

# RUN mkdir -p /root/.config/fish/
# RUN touch /root/.config/fish/config.fish
# RUN echo "starship init fish | source" >> ~/.config/fish/config.fish
# RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc

ENTRYPOINT ["/bin/bash"]

# The Dockerfile is pretty straightforward. It starts with the base image,
# which is the mambaforge image. Then, it installs fish and creates a conda environment.
# It clones the TALI-collector repository and installs the dependencies.
# Finally, it sets the working directory to the TALI-collector repository and sets the
# entrypoint to the entrypoint.sh script.