import pkg_resources as pkg
import bwatchcompute
from rich import print as pprint
from rich.traceback import install
import os
import wandb

install()
pprint(os.getenv("WANDB_API_KEY"))

wandb.login(key=os.getenv("WANDB_API_KEY"))

wandb.init()
