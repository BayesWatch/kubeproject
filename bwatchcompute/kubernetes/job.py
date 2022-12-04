# Read script template, make per experiment modifications
# For each experiment script, create a job kubernetes spec file

import copy
from pathlib import Path
from typing import List, Union
import yaml
import randomname
import subprocess
import tqdm


class Job(object):
    def __init__(
        self,
        name: str,
        script_list: List[str],
        environment_variables: dict,
        secret_variables: dict,
        container_path: str,
        num_repeat_experiment: int = 5,
        kubernetes_spec_dir: Union[str, Path] = Path("generated/kubernetes/specs"),
    ):
        # to add additional features you might find these pages useful
        # https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/job-v1/#JobSpec
        # https://kubernetes.io/docs/concepts/workloads/controllers/job/
        self.name = name
        self.script_list = script_list
        self.environment_variables = environment_variables
        self.secret_variables = secret_variables
        self.container_path = container_path
        self.num_repeat_experiment = num_repeat_experiment
        self.kubernetes_spec_dir = Path(kubernetes_spec_dir)
        self.spec_file_list = None
        self.spec_dict_list = None
        self.gen_idx = 0

        if not self.kubernetes_spec_dir.exists():
            self.kubernetes_spec_dir.mkdir(parents=True)

    def generate_spec_files(self):
        spec_template = Path("bwatchcompute/templates/job.template.yaml")
        spec_dict = yaml.safe_load(spec_template.read_text())
        spec_dict["spec"]["template"]["spec"]["containers"][0]["name"] = "job-container"
        spec_dict["spec"]["template"]["spec"]["containers"][0][
            "image"
        ] = self.container_path

        spec_dict["spec"]["backoffLimit"] = self.num_repeat_experiment

        spec_dict_list = []
        for idx, script_entry in enumerate(self.script_list):
            current_dict = copy.deepcopy(spec_dict)
            current_dict["metadata"][
                "name"
            ] = f"{self.name}-{randomname.get_name()}-{idx}"
            current_dict["spec"]["template"]["spec"]["containers"][0]["command"] = list(
                script_entry.split(" ")
            )

            env_variables_list = []

            for key, value in self.secret_variables.items():
                current_dict = {
                    "name": key,
                    "valueFrom": {
                        "secretKeyRef": {
                            "name": value["namespace"],
                            "key": value["secret_name"],
                        }
                    },
                }
                env_variables_list.append(current_dict)
            
            for key, value in self.environment_variables.items():
                current_dict = {"name": key, "value": value}
                env_variables_list.append(current_dict)
            
            current_dict["spec"]["template"]["spec"]["containers"][0]["env"] = env_variables_list
            

        spec_file_list = []
        for idx, spec_dict in enumerate(spec_dict_list):
            spec_file = (
                self.kubernetes_spec_dir
                / f"{self.name}-{randomname.get_name()}-{idx}.yaml"
            )
            with open(spec_file, "w+") as spec_fp:
                yaml.safe_dump(spec_dict, spec_fp)

            spec_file_list.append(spec_file)

        self.spec_file_list = spec_file_list
        self.spec_dict_list = spec_dict_list
        self.gen_idx += 1

    def run_jobs(self):
        output_dict = {}
        with tqdm.tqdm(total=len(self.spec_file_list)) as pbar:
            for script_file in self.spec_file_list:
                result = subprocess.run(
                    f"kubectl create -f {script_file.as_posix()}",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                output_dict[script_file] = {
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                }
                pbar.update(1)
                pbar.set_description(f"Running {script_file.name}")
        return output_dict


if __name__ == "__main__":
    from rich import print
    from quote import quote

    quotes = quote("hume", limit=10)

    script_list = [f"echo {quote_instance['quote']}" for quote_instance in quotes]

    exp = Job(
        name="dummy-exp",
        script_list=script_list,
        container_path="ghcr.io/bayeswatch/compute-gpu:0.1.0",
        num_repeat_experiment=3,
    )

    exp.generate_spec_files()
    output = exp.run_jobs()
    print(output)
