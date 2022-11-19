For Kubernetes jobs

```bash
bwatchcompute batch "python3 examples/bayescompute.py -i 0 -j 0" "python3 examples/bayescompute.py -i 1 -j 0"
```

```bash
bwatchcompute accelerator_list
```

```bash
bwatchcompute num_accelerators_per_type
```

... and so on.

For local dev machine creation and access

```bash
bwatchcompute start dev-machine --name dev-0 --accelerator-type "nvidia-a100" --accelerator-count 1 \ --container_name "dev-0" --container_image "nvidia/cuda:11.0-devel-ubuntu18.04" --container_command "bash" --container_mounts "/home/ubuntu:/home/ubuntu" --container_env "API_KEY=balablasbasdahs"
```

```bash
bwatchcompute ssh dev-0
```
