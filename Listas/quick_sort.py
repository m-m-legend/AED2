def quick_sort(arr,left,right):
    if left<right:
        pos = partition(arr,left,right)
        quick_sort(arr,left,pos-1)
        quick_sort(arr,pos+1,right)
        
def partition(arr,left,right):
    i = left; j = right-1
    pivot = arr[right]
    
    while i<j:
        while i<right and arr[i] <= pivot:
            i+=1
        while j>left and arr[j] > pivot:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]
    return i

L = [2,4,1,5,3]
quick_sort(L,0,len(L)-1)
print(L)