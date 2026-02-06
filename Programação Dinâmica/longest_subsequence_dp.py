A = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(A)

table = [[0]*n for _ in range(n)]

for i in range(n):
    dp = [1]*n  
    for j in range(i+1):  
        best = 1
        for k in range(j):
            if A[k] < A[j]:
                best = max(best, dp[k] + 1)
        dp[j] = best
        table[i][j] = dp[j]

print("A =", A)
print("Tabela (linha i = usando A[0..i], col j = LIS terminando em j; j>i => 0)\n")
for i,row in enumerate(table):
    print(f"i={i:>1} ({A[i]:>3}):", row)
print("\nComprimento do LIS final =", max(table[-1]))

print("\nTabela formatada (com '-' para j>i):")
for i,row in enumerate(table):
    fmt = [str(x) if idx<=i else '-' for idx,x in enumerate(row)]
    print(f"i={i:>1} ({A[i]:>3}):", fmt)
