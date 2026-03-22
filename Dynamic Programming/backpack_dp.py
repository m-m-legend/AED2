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