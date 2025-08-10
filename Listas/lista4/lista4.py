import time

def quick_sort(arr, left, right):
    if left < right:
        pos = partition(arr, left, right)
        quick_sort(arr,left,pos-1)
        quick_sort(arr,pos+1, right)
    
def partition(arr,left,right):
    i = left; j = right-1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i+=1
        while j > left and arr[j] >= pivot:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]
    return i

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i=0;j=0;k=0
        
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
            i+=1;k+=1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1;k+=1

arquivos = ["100.txt", "500.txt", "1000.txt", "1000000.txt", "10000000.txt"]
for nome in arquivos:
    with open(nome, "r") as arquivo:
        dados = arquivo.read().strip().split(",")
        L1 = []
        for i in dados:
            L1.append(i)
        L2 = L1.copy()
        

    print(f"\n=== Testando com arquivo: {nome} ({len(L1)} elementos) ===\n")
            
    antes1 = time.time()
    merge_sort(L1)
    exec1 = time.time() - antes1
    print(L1, f"Tempo de execução Merge Sort {len(L1)} elementos: {exec1} segundos \n\n")

    antes2 = time.time()
    quick_sort(L2,0,len(L2)-1)
    exec2 = time.time() - antes2
    print(L2, f"Tempo de execução Quick Sort {len(L2)} elementos: {exec2} segundos \n\n")
    






            
        
        