import argparse
from typing import Dict

import torch
import torch.nn as nn
import torch.nn.functional as F
import wandb

# Create a parser to parse the arguments
parser = argparse.ArgumentParser(description="Sample script")

# Add the arguments
parser.add_argument("--i", type=int, default=0, help="i")
parser.add_argument("--j", type=int, default=0, help="j")
parser.add_argument("--resume", type=bool, default=False, help="resume")


args: Dict = parser.parse_args().__dict__

model = torch.nn.Parameter(
    torch.Tensor([args.i, args.j], dtype=torch), requires_grad=True
)

model.train()
for batch_idx, (data, target) in enumerate(train_loader):
    output = model(data)
    loss = F.nll_loss(output, target)
    loss.backward()
    optimizer.step()
    if batch_idx % args.log_interval == 0:
        wandb.log({"loss": loss})
    # log model gradients and parameters
    wandb.log({"gradients": wandb.Histogram(model.fc1.weight.grad)})
    wandb.log({"parameters": wandb.Histogram(model.fc1.weight)})
    # log model predictions
    wandb.log(
        {
            "predictions": [
                wandb.Image(x, caption=str(y)) for x, y in zip(data, output.argmax(1))
            ]
        }
    )

    # Save the model
    wandb.save("model.h5")
