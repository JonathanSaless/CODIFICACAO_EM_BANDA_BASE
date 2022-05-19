import numpy as np
import matplotlib.pyplot as plt

def CLOCK(dados):
  clock = np.arange(1, 2*len(dados)+2) % 2
  plt.figure(figsize=(20, 2))
  plt.yticks(np.arange(0, 2))
  ax = plt.gca()                        
  ax.get_xaxis().set_visible(False)
  ay = plt.gca()                        
  ay.get_yaxis().set_visible(False)
  for i in range(0, len(dados), 1):
    plt.axvline(i, color="black", linestyle="--")
    plt.text(i+0.5, 1.1, dados[i], ha = "center", va = "bottom")
  plt.axvline(len(dados), color="black", linestyle="--")
  # Impressão em formato digital
  plt.step(np.arange(0, len(clock)/2, 0.5), clock, where="post", color="black")
  plt.show()
