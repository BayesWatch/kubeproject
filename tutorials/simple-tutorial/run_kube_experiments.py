import copy
import itertools
from pathlib import Path
from rich import print


def get_scripts():

    script_list = []
    for i, j in itertools.product(range(1), range(1)):
        current_script_text = (
            f"python /workspace/bwatchcompute/tutorial/simple.py --i {i} --j {j}"
        )
        script_list.append(current_script_text)

    return script_list


if __name__ == "__main__":
    from bwatchcompute.kubernetes.job import Job

    script_list = get_scripts()

    exp = Job(
        name="pytorch-simple-exp",
        script_list=script_list,
        container_path="ghcr.io/bayeswatch/bwatch-tutorial:latest",
        num_repeat_experiment=3,
    )

    exp.generate_spec_files()
    output = exp.run_jobs()
    print(output)