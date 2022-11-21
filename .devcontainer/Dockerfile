FROM gcr.io/deeplearning-platform-release/base-cu113

RUN conda create -n main python=3.10 -y

SHELL ["conda", "run", "-n", "main", "/bin/bash", "-c"]

RUN apt update
RUN apt install aptitude tree micro fish -y

RUN conda init bash
RUN conda install -c conda-forge mamba -y
RUN mamba install -c conda-forge starship -y
RUN mamba install -c conda-forge wandb transformers rich python-dotenv -y
RUN mamba install -c conda-forge bash htop jupyterlab -y
RUN mamba install -c conda-forge micro bat -y
RUN mamba install -c conda-forge google-cloud-storage -y
RUN mamba install -c conda-forge google-api-python-client -y
RUN mamba install -c conda-forge gh -y
RUN mamba install -c conda-forge git -y
RUN mamba install -c conda-forge git-lfs -y
RUN mamba install -c conda-forge black -y
RUN mamba install -c conda-forge tmux -y

RUN echo yes | pip install pytest-pretty-terminal
RUN echo yes | pip install glances
RUN echo yes | pip install loguru
RUN echo yes | pip install nvitop
RUN git lfs install


RUN mkdir -p /root/.config/fish/
RUN touch /root/.config/fish/config.fish
RUN echo "conda activate main" >> ~/.bashrc
RUN echo "starship init fish | source" >> ~/.config/fish/config.fish
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc
RUN git config --global --add safe.directory /workspaces/bwatchcompute

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

