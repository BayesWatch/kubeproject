FROM gcr.io/deeplearning-platform-release/base-cpu

RUN conda create -n main python=3.10 -y

SHELL ["conda", "run", "-n", "main", "/bin/bash", "-c"]

RUN apt update
RUN apt install aptitude -y

RUN conda init bash
RUN conda install -c conda-forge mamba -y
RUN mamba install -c conda-forge wandb transformers -y
RUN mamba install pytorch torchvision torchaudio cpuonly -c pytorch -y
RUN mamba install -c conda-forge google-cloud-storage -y
RUN mamba install -c conda-forge google-api-python-client -y
RUN mamba install -c conda-forge gh -y
RUN mamba install -c conda-forge git -y
RUN mamba install -c conda-forge git-lfs -y

RUN git lfs install

RUN echo "conda activate main" >> ~/.bashrc
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc

COPY entrypoint.sh .

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

