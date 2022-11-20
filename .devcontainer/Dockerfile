FROM gcr.io/deeplearning-platform-release/base-cu113

RUN conda create -n main python=3.10 -y

SHELL ["conda", "run", "-n", "main", "/bin/bash", "-c"]

RUN apt update
RUN apt install aptitude tree micro fish gh -y

RUN conda init bash
RUN conda install -c conda-forge mamba -y
RUN mamba install -c conda-forge starship -y
RUN mamba install -c conda-forge git-lfs wandb transformers -y

RUN mkdir -p /root/.config/fish/
RUN touch /root/.config/fish/config.fish
RUN echo "conda activate main" >> ~/.bashrc
RUN echo "starship init fish | source" >> ~/.config/fish/config.fish
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc


RUN echo yes | pip install nvitop
RUN git lfs install

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

