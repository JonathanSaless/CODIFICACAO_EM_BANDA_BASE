import numpy as np
import matplotlib.pyplot as plt

def mostrar_grafico(dados, dados_saida, titulo, cor):
    if (len(dados) != len(dados_saida)):     #caso do manchester que terá uma sequencia de bits maior
        dados_repetidos = np.repeat(dados, 2)
        plt.figure(figsize=(20, 2))
        plt.yticks(np.arange(-1, 2))
        ax = plt.gca()                        
        ax.get_xaxis().set_visible(False)    #esconde eixo x
        #plt.axhline(y=0, color="gray")
        for i in range(0, len(dados_saida), 2):
            plt.axvline(i, color="black", linestyle="--")
            #plt.text(i+1, 1.1, dados_repetidos[i], ha = "center", va = "bottom")    
        plt.axvline(len(dados_repetidos), color="black", linestyle="--")        #para traçar a linha vetical no último clock  
        # Impressão em de etapas (formato digital)
        plt.step(np.arange(len(dados_saida)+1), dados_saida + [dados_saida[(len(dados_saida))-1]], where='post', color=cor)
        plt.title(titulo)
        plt.show()
    
    else:
        plt.figure(figsize=(20, 2))
        plt.yticks(np.arange(-1, 2))         #eixo y (-1, 0, 1)
        ax = plt.gca()                        
        ax.get_xaxis().set_visible(False)    #esconde eixo x
        for i in range(0, len(dados_saida), 1):      #esse for serve para colocar linha pontilhadas verticalmente e a sequencia de bits emitida acima do sinal
            plt.axvline(i, color="black", linestyle="--")    #traça linhas pontilhadas verticalmente
            #plt.text(i+0.5, 1.1, dados[i], ha = "center", va = "bottom") 
        plt.axvline(len(dados_saida), color="black", linestyle="--")        #para traçar a linha vetical no último clock    
        # Impressão em de etapas (formato digital)
        plt.step(np.arange(0, len(dados_saida)+1), dados_saida + [dados_saida[(len(dados_saida))-1]], where='post', color=cor)
        plt.title(titulo)
        plt.show()