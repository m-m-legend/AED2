#1
def exp(base, nivel):
    if nivel == 1:
        return base
    elif nivel % 2 == 0:
        x = exp(base,nivel//2)
        return x*x
    else:
        x = exp(base,nivel//2)
        return x*x*base
    
def magia():
     while True:
        base = int(input("Poder base: "))
        nivel = int(input("Nivel: "))
        print(exp(base,nivel), "\n")
    
        


#2
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[0:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i=0; j=0; k=0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i=+1; k+=1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1; k+=1
            
def corrida():
    L = []
    qtd = int(input("Quantidade de pilotos: "))
    for i in range(qtd):
        x = int(input(f"Qual o tempo do piloto {i+1}? "))
        L.append(x)
    print(L)
    merge_sort(L)
    print(L)

#3
def buscaBin(arr,i,f,x):
    if i>f:
        return False
    else:
        mid = (i+f)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return buscaBin(arr,i,mid-1,x)
        else:
            return buscaBin(arr,mid+1,f,x)

def ilha():
    L = []
    qtd = int(input("Quantidade de posições: "))
    for i in range(qtd):
        x = int(input(f"Posição {i+1}: "))
        L.append(x)
    print(L)
    pos = int(input("Verificar Posição: "))
    result = buscaBin(L,0,qtd-1,pos)
    if result is not False:
        print("Tesouro encontrado!")
    else:
        print("Tesouro não encontrado.")

ilha()


   
