import copy
import itertools
from pathlib import Path
from rich import print


def get_scripts():

    script_list = []
    for i, j in itertools.product(range(5), range(5)):
        current_script_text = f"/opt/conda/envs/main/bin/python /workspace/bwatchcompute/tutorial/simple.py --i {i} --j {j}"
        script_list.append(current_script_text)

    return script_list


if __name__ == "__main__":
    from bwatchcompute.kubernetes.job import Job

    script_list = get_scripts()

    exp = Job(
        name="pytorch-simple-exp",
        script_list=script_list,
        container_path="ghcr.io/bayeswatch/bwatch-tutorial:latest",
        num_repeat_experiment=1,
    )

    exp.generate_spec_files()
    output = exp.run_jobs()
    print(output)
