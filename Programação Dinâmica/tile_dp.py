def azulejo(n):
    dp = [None for i in range(0, n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

def imprime(matriz):
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

n = 5

print(azulejo(n))
