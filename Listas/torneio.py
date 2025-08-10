import numpy as np, random as rd

def Torneio(T,tam):
    if tam == 1:
        T[0][0] = 1
    else:
        p = tam//2
        Torneio(T,p)
        for i in range(p):
            for j in range(p):
                T[i+p][j] = T[i][j] + p
                T[i][j+p] = T[i+p][j]
                T[i+p][j+p] = T[i][j]

def matrizQuad(n):
    matriz = [[int(input(f"Elemento [{i}] [{j}]: ")) for j in range(n)] for i in range(n)]
    return matriz

def escrever(matriz):
    for i in matriz:
        for j in i:
            print(j, end=' ')
        print()
    print()
    
matriz_zeros = np.zeros((8, 8), dtype=int)
Torneio(matriz_zeros,8)
escrever(matriz_zeros)

mat1 = matrizQuad(2)
escrever(mat1)
Torneio(mat1,2)
escrever(mat1)

mat2 = matrizQuad(4)
escrever(mat2)
Torneio(mat2,4)
escrever(mat2)





            
    
    