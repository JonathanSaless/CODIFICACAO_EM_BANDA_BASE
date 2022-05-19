import numpy as np
import matplotlib.pyplot as plt

def mostrar_grafico(dados, titulo, cor):
  plt.figure(figsize=(20, 2))
  plt.yticks(np.arange(-1, 2))
  if titulo == "MANCHESTER":
    plt.xticks(np.arange(0, (len(dados)/2)+1))
    for i in range(0, int((len(dados)/2)), 1):
      plt.axvline(i, color="black", linestyle="--")
    plt.axvline(len(dados)/2, color="black", linestyle="--")
    # Impressão em etapas (formato digital)
    plt.step(np.arange(0, (len(dados)/2)+0.5, 0.5), dados + [dados[len(dados)-1]], where="post", color=cor)
    plt.title(titulo)
    plt.show()
  else:
    plt.xticks(np.arange(0, len(dados)+1))
    for i in range(0, len(dados), 1):
      plt.axvline(i, color="black", linestyle="--")
    plt.axvline(len(dados), color="black", linestyle="--")
    # Impressão em formato digital
    plt.step(np.arange(0, len(dados)+1, 1), dados + [dados[(len(dados))-1]], where="post", color=cor)
    plt.title(titulo)
    plt.show()
