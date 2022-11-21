import argparse
import os
from typing import Dict
from rich import print
from rich.traceback import install
import dotenv

import torch
import torch.nn as nn
import torch.nn.functional as F
import wandb

os.environ[
    "HYDRA_FULL_ERROR"
] = "1"  # Makes sure that stack traces produced by hydra instantiation functions produce
# traceback errors related to the modules they built, rather than generic instantiate related errors that
# are generally useless for debugging

os.environ[
    "TORCH_DISTRIBUTED_DEBUG"
] = "DETAIL"  # extremely useful when debugging DDP setups

install()  # beautiful and clean tracebacks for debugging
dotenv.load_dotenv(override=True, verbose=True)
# Create a parser to parse the arguments
parser = argparse.ArgumentParser(description="Sample simple script")

# Add the arguments
parser.add_argument("--i", type=int, default=0, help="i")
parser.add_argument("--j", type=int, default=0, help="j")


args: Dict = parser.parse_args()

wandb.init(project="simple", entity="machinelearningbrewery", config=args.__dict__)

model = torch.nn.Parameter(
    torch.Tensor([args.i, args.j], dtype=torch), requires_grad=True
)

model.train()

loss = torch.sum(model - float(args.i))
loss.backward()

wandb.log({"loss": loss})
# log model gradients and parameters
wandb.log({"gradients": wandb.Histogram(model.grad)})
wandb.log({"parameters": wandb.Histogram(model)})
