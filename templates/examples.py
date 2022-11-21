from bwatch_compute import batch_job


def generate_experiment_scripts(args, **kwargs):
    """Generate a list of experiment scripts to run."""
    scripts = []
    for i in range(10):
        for j in range(10):
            scripts.append(f"python3 experiment.py --i {i} --j {j}")
    return scripts


# start a __main__ block
if __name__ == "__main__":
    container_path = "gcr.io/bayescompute-275117/bayescompute:latest"
    experiment_runner = batch_job.BatchJob(
        script_list=generate_experiment_scripts,
        accelerator_type="NVIDIA_A100",
        container_path=container_path,
        num_gpus_per_experiment=1,
        num_repeat_experiment=3,
    )
