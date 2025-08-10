import math

def moeda(moedas, n, valor):
    result = [math.inf] * (valor + 1)
    result[0] = 0  

    for i in range(n):
        for j in range(moedas[i], valor + 1):
            result[j] = min(result[j], result[j - moedas[i]] + 1)

    return result[valor] if result[valor] != math.inf else -1

def mochila(pesos, valores, capacidade,n):
    dp = [[0 for i in range(n+1) ] for j in range(capacidade+1)]
    for k in range(0,capacidade+1):
        dp[k][0] = 0
    for i in range(1,capacidade+1):
        for j in range(1,n+1):
            if(pesos[j-1]<=i):
                dp[i][j] = max(dp[i][j-1], valores[j-1] + dp[i-pesos[j-1]][j-1])
            else:
                dp[i][j] = dp[i][j-1]
    return dp

def escrever(matriz):
    for i in matriz:
        for j in i:
            print(j, end= " ")
        print()
    

pesos = [5,4,3,6]
valores = [10,7,4,12]
capacidade = 10
n = 4
print(escrever(mochila(pesos,valores,capacidade,n)))



            