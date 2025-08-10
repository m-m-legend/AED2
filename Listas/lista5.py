import math

def moeda(c, n, k):
    dp = [math.inf] * (k + 1)
    dp[0] = 0  

    for i in range(n):
        for j in range(c[i], k + 1):
            dp[j] = min(dp[j], dp[j - c[i]] + 1)

    return dp[k] if dp[k] != math.inf else -1

def mochila(n,peso,valor,capacidade):
    memo = [[0 for i in range(capacidade+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for x in range(1,capacidade+1):
            if x<peso[i-1]:
                memo[i][x] = memo[i-1][x]
            else:
                memo[i][x] = max(memo[i-1][x], valor[i-1] + memo[i-1][x-peso[i-1]])
                
    x = capacidade
    itens = []
    for i in range(n,0,-1):
        if memo[i][x] != memo[i-1][x]:
            itens.append(i-1)
            x -= peso[i-1]
    itens.reverse()
    return memo[n][capacidade], itens

c = [1,3,4]
print(moeda(c,len(c),7))

peso = [5,2,3,20,1]
valor = [4,1,11,3,2]
print(mochila(len(peso),peso,valor,28))

