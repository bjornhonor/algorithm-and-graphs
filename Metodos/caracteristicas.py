'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Bruno Penteado Carrara

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

12/09/2022  
===================================================='''

from asyncio.windows_events import NULL
import numpy as np

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

'''Descrição: Retorna se uma dada matriz é simetrica.
Entrada: matriz de adjacências
Saída: Boolean(True - matriz simetrica; False - matriz assimetrica)'''
def isSimetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]!=matriz[j][i]:
                return False
    return True

'''Descrição: Retorna se uma dada matriz possui aresta em um unico vertice (tem valor na diagonal).
Entrada: matriz de adjacências
Saída: Boolean(True - possui aresta em um so vertice; False - nao possui aresta em um so vertice)'''
def temDiagonal(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] > 0:
            return True
    return False

'''Descrição: Retorna se uma dada matriz é simples ou representa um multigrafo.
Entrada: matriz de adjacências
Saída: Boolean(True - possui uma aresta por conexao entre vertices; False - possui mais de uma aresta por conexao de vertices)'''
def isSimple(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 1 or matriz[j][i] > 1:
                return False
    return True

'''Descrição: Retorna o tipo do grafo representado por uma dada matriz de adjacências.
Entrada: matriz de adjacências
Saída: Integer (0 – simples; 1 – dígrafo; 2 – multigrafo; 3 – pseudografo)'''
def tipoGrafo(matriz):
    tipo = 0
    simetrica = isSimetrica(matriz)
    diagonal = temDiagonal(matriz)
    simples = isSimple(matriz)
    if simetrica == False:
        tipo = 1
    elif diagonal == True:
        tipo = 3
    elif simples == False:
        tipo = 2
    return tipo

'''Descrição: Retorna quantas arestas possui um dado grafo.
Entrada: matriz de adjacências
Saída: Float(quantidade de arestas de um grafo)'''
def contaArestas(matriz):
    tipo = tipoGrafo(matriz)
    if tipo == 1: # para grafos direcionados, apenas somamos os valores da matriz
        numArestas = matriz.sum()

    elif tipo == 3: # para pseudografos, calculamos o valor da diagonal e retiramos da soma total, entao dividimos por 2
        soma = 0 # para tirar a simetria e apos isso somamos o valor da diagonal novamente

        for i in range(len(matriz)):
            if matriz[i][i] > 0:
                soma += matriz[i][i]
        numArestas = (matriz.sum() - soma) / 2
        numArestas += soma

    else: # para os outros tipos de grafos, basta somarmos os valores das posicoes da matriz e dividir por 2 para tirar a simetria
        numArestas = matriz.sum()/2

    return numArestas

'''Descrição: Retorna o valor da densidade do grafo.
Entrada: matriz de adjacências
Saída: Float (valor da densidade com precisão de três casas decimais)'''
def calcDensidade(matriz):
    densidade = 0
    qtdVertices = np.shape(matriz)[0] # numero de vertices
    qtdEdges = contaArestas(matriz)
    # print(qtdEdges)
    if tipoGrafo(matriz) == 1: #grafo direcionado
        densidade = qtdEdges / (qtdVertices * (qtdVertices - 1)) # formula para digrafo
    else:
        densidade = (2 * qtdEdges) / (qtdVertices * (qtdVertices - 1)) # formula para grafos nao direcionados
    t = 3
    d = int(densidade * 10**t)/10**t
    print('Densidade do grafo:', d, '\n')
    return densidade

'''Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.
Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta inserida.'''
def insereAresta(matriz, vi, vj):
    tipo = tipoGrafo(matriz)
    if tipo == 1: # se for digrafo
        matriz[vi-1][vj-1] = 1 #recebe 1 no lugar desejado

    elif tipo == 0:
        matriz[vi-1][vj-1] = 1
        matriz[vj-1][vi-1] = 1

    elif vi == vj:
        matriz[vi-1][vj-1] += 1 # ser for uma aresta de um so vertice nao precisa de simetria

    else: # se for qualquer grafo que nao seja direcionado
        matriz[vi-1][vj-1] += 1 # soma 1 aresta, podendo iniciar uma aresta ou transformar em multigrafo, adicionando mais uma aresta
        matriz[vj-1][vi-1] += 1 # mesma operacao, mas para deixar a matriz simetrica
    print('Aresta entre os pontos', vi, 'e', vj, 'criada com sucesso')    
    return matriz

'''Descrição: Remove uma aresta do grafo considerando o par de vértices vi e vj.
Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam os ids dos vértices)
Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta removida.'''
def removeAresta(matriz, vi, vj):
    tipo = tipoGrafo(matriz)
    if tipo == 1: # se for digrafo
        matriz[vi-1][vj-1] = 0 #recebe 1 no lugar desejado
    elif vi == vj and vi > 0 and vj > 0:
        matriz[vi-1][vj-1] -= 1 # se for uma aresta de um so vertice nao precisa ser simetrico
    elif vi > 0 and vj > 0: # se for qualquer grafo que nao seja direcionado
        matriz[vi-1][vj-1] -= 1 # subtrai 1 aresta, podendo retirar uma aresta de um multagrafo, ou apenas remover a aresta
        matriz[vj-1][vi-1] -= 1 # mesma operacao, mas para deixar a matriz simetrica
    print('Aresta entre os pontos', vi, 'e', vj, 'removida com sucesso')
    return matriz

'''Descrição: Insere um vértice no grafo.
Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice inserido.'''
def insereVertice(matriz, vi):
    if matriz[vi][vi] == NULL:
        print('Matriz ja possui esse id')
    else:
        for i in vi-1:
            matriz[vi-1][i] = 0
            matriz[i][vi-1] = 0
    return matriz

'''Descrição: Remove um vértice do grafo.
Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice removido.'''
def removeVertice(matriz, vi):

    return matriz
    
    







