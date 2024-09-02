
#mostra matriz
def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return
#cria matriz
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

matriz = cria_matriz(10,10)

#diagonal ruim
def diagonal_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = 1
    return

#diagonal bom
def diagonal_bom(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return

matriz = cria_matriz(10,10)

def contra_diagonal_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + j == len(matriz) - 1:
                matriz[i][j] = 1
    return

#contra diagonal
def contra_diagonal_bom(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return

def trigonal_inferior_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i > j:
                matriz[i][j] = 1
    return

#trigonal inferior
def trigonal_inferior_bom(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return

def trigonal_superior_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i < j:
                matriz[i][j] = 1
    return

#trigonal superior
def trigonal_superior_bom(matriz):
    for j in range(len(matriz)):
        for i in range(j):
            matriz[i][j] = 1
    return

#matriz transposta
def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

#xadrez
def tabuleiro_xadrez(xadrez):
    for i in range(len(xadrez())):
        for j in range(len(xadrez[i])):
            if i%2 == j%2:
                xadrez()[i][j] = 1
            else:
                xadrez[i][j] = 0
    return

