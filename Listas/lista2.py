import numpy as np, random as rd

#1 [*]
def torreHanoi(n, orig, dest, aux):
    if n == 1:  
        disco = orig.pop()  
        dest.append(disco)  
    else:
        
        torreHanoi(n-1, orig, aux, dest)

        disco = orig.pop()
        dest.append(disco)
        
        torreHanoi(n-1, aux, dest, orig)
        
#2 [*]
def count_inversions(arr):
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort_count(arr[:mid])
        right, inv_right = merge_sort_count(arr[mid:])

        merged = []
        i = j = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i  #contando as inversões
                j += 1

        merged += left[i:]
        merged += right[j:]

        return merged, inv_left + inv_right + inv_count

    _, total_inversions = merge_sort_count(arr)
    return total_inversions


#3 [*] 
def invasor(arr, i, j):
    if i > j:
        return False
    if arr[i] == 1:
        return True
    return invasor(arr, i + 1, j)


def perguntaPos(arr):
    while True:
        i = int(input("Qual o limite mínimo que quer procurar? "))
        j = int(input("Qual o limite máximo que quer procurar? "))

        print(f"\n→ Procurando entre as posições {i} e {j}...")

        if i == j and arr[i] == 1:
            print(f"Você achou a posição exata do invasor! Posição: {i}\n")
            break

        resultado = invasor(arr, i, j)

        if resultado:
            print("Sim, o invasor está no intervalo.\n")
        else:
            print("Não, o invasor não está no intervalo.\n")
            
#4 [*]
def strassen(A, B):
    n = A.shape[0]

    # caso base: 1x1 matriz
    if n == 1:
        return A * B

    #n^log(n) fica a complexidade
    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    #peguei fórmula da GeeksforGeeks
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))


    
arr = [0,0,0,1]
rd.shuffle(arr)
#perguntaPos(arr)

arr2 = [2,4,1,3,5]
print(count_inversions(arr2))

mat1 = [[1,2],
        [3,4]]
mat2 = [[5,6],
        [7,8]]

mat1 = np.array(mat1)
mat2 = np.array(mat2)

print(strassen(mat1,mat2))

