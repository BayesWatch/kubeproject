import copy
import itertools
from pathlib import Path
from rich import print


def get_scripts():
    template_script_path = Path("tutorial/simple.sh")
    template_script_text = template_script_path.read_text()
    script_storage_path = template_script_path.parent / "scripts"

    if not script_storage_path.exists():
        script_storage_path.mkdir(parents=True)

    script_list = []
    for i, j in itertools.product(range(1), range(1)):
        current_script_text = copy.deepcopy(template_script_text)
        current_script_text = current_script_text.replace("$args$", f"--i {i} --j {j}")
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
