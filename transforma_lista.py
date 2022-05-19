def transforma_lista(dados):
  for i in range(len(dados)):
    if dados[i] == 1:
      dados[i] = "+"
    elif dados[i] == -1:
      dados[i] = "-"
    else:
      dados[i] = "0"
  strDADOS = " ".join(dados)
  return strDADOS
