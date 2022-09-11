'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Bruno Penteado Carrara

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

12/09/2022
===================================================='''

import sys
from igraph import *
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from Metodos import (caracteristicas as car)

'''Core do programa'''
def main(instancia):
    matriz = ds.criaMatrizAdjacencias(instancia)
    print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    G = g.criaGrafo(matriz)
    print(G, '\n') # Mostra as características do grafo.

    vis.visualizarGrafo(True, G)  # True para visualização do grafo ou False.
    funcao0 = car.tipoGrafo(matriz)
    match funcao0:
        case 0:
            print('Grafo simples', '\n')
        case 1:
            print('Digrafo', '\n')
        case 2:
            print('Multigrafo', '\n')
        case 3:
            print('Pseudografo', '\n')
    funcao1 = car.verificaAdjacencia(matriz, 0, 1)
    funcao2 = car.calcDensidade(matriz)

    resultado = [instancia, funcao0, funcao1, funcao2] # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado) # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

