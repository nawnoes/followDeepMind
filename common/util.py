import torch
import numpy as np
from matplotlib import animation
from JSAnimation.IPython_display import display_animation
from IPython.display import display
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

def seed_torch(seed):
  torch.manual_seed(seed)
  if torch.backends.cudnn.enabled:
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

def display_frames_as_gif(frames: List[np.ndarray]) -> None:
  """Displays a list of frames as a gif, with controls."""
  patch = plt.imshow(frames[0])
  plt.axis('off')

  def animate(i):
    patch.set_data(frames[i])

  anim = animation.FuncAnimation(
    plt.gcf(), animate, frames=len(frames), interval=50
  )
  # display(display_animation(anim, default_mode='loop'))