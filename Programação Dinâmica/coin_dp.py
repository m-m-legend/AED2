import time

def imprime(matriz):
    for i in matriz:
        for  j in i:
            print(j, end=" ")
        print()
        
        
def moeda(moedas, valor):
    n = len(moedas)
    dp = [[0 if i == 0 else float('inf') for i in range(0, valor+1)] for j in range(0, n+1)]
    for j in range(1, n+1):
        for i in range(1, valor+1):
            if(i < moedas[j-1]):
                dp[j][i] = dp[j-1][i]
            else:
                dp[j][i] = min(dp[j-1][i],1 + dp[j][i-moedas[j-1]])
    return dp


moedas = [1,2,3,4]
valor = 7

imprime(moeda(moedas,valor))
