FROM ghcr.io/bayeswatch/compute-gpu:0.1.0

RUN mkdir -p /workspace/

RUN git clone https://github.com/BayesWatch/bwatchcompute.git /workspace/bwatchcompute

COPY entrypoint.sh /workspace/

ENTRYPOINT ["/bin/bash", "/workspace/entrypoint.sh"]
