import torch
import torch.nn as nn

class FNN(nn.Module):
  def __init__(self, in_dim: int, out_dim: int):
    """Initialization."""
    super(FNN, self).__init__()

    self.layers = nn.Sequential(
      nn.Linear(in_dim, 128),
      nn.ReLU(),
      nn.Linear(128, 128),
      nn.ReLU(),
      nn.Linear(128, out_dim)
    )

  def forward(self, x: torch.Tensor) -> torch.Tensor:
    """Forward method implementation."""
    return self.layers(x)
