import time, random as rd

def imprimirMatriz(M, m, n):   
    for i in range(0, m+1):
        for j in range(0, n+1):
            print(f" {M[i][j]}  ", end="")
        print()
    print()

def F(M, linha, coluna, A, B, Sol):
    for i in range(1, linha + 1):
        for j in range(1, coluna + 1):
            if A[i - 1] == B[j - 1]:
                M[i][j] = M[i - 1][j - 1] + 1   
                                                
            elif M[i - 1][j] >= M[i][j - 1]:   
                M[i][j] = M[i - 1][j]
            else:                             
                M[i][j] = M[i][j - 1]
    
    i = linha
    j = coluna
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            Sol.append(A[i-1])
            i -= 1
            j -= 1
        elif M[i - 1][j] > M[i][j-1]:
            i -= 1
        else:
            j -= 1
    Sol.reverse()
              


def SCML(A, m, B, n):
    M = [[0 for j in range(n+1)] for i in range(m+1)]
    Sol = []
    

    inicio = time.time()
    
    F(M, m, n, A, B, Sol)
    
    fim = time.time()
    
    tempo_total = fim - inicio
    
    print("Tempo final do algoritmo (aproximadamente): {:.6f}".format(tempo_total))
    
    #imprimirMatriz(M,m,n)
    print(Sol)
    print(f"tamanho: {M[m][n]}")
    
    
    print("\n")


#TESTES MANUAIS
    
A = [1, 3, 5, 3]
B = [1, 2, 4, 5, 7]


SCML(A, len(A), B, len(B))

A = [7, 1, 3, 9, 2, 5, 4]
B = [1, 9, 2, 5, 8, 4]

SCML(A,len(A), B, len(B))

A = "CDABG" 
B = "DG"

SCML(A, len(A), B, len(B))

A = [1,2,5,5,4,7]
B = [0,3,5,4,5,8]

SCML(A, len(A), B, len(B))

#TESTES AUTOMATICOS

C = []
D = []

for i in range(1000):
    C.append(rd.randint(-100,100))
for j in range(1000):
    D.append(rd.randint(-100,100))
    
SCML(C,len(C),D,len(D))




