#1
from random import randint
def soma(arr):
	total = 0
	if len(arr) == 0:
		return 0
	else:
		for i in arr:
			total += i
		return total
	
	
lista = []
y = int(input("Insira o salário: "))

while y != 0:
    lista.append(y)
    y = int(input("Insira o salário: "))
	
	
print(soma(lista))
#2
def somaRec(arr, f):
    if len(arr) == 0:
        return 0
    elif f == 0:
        return 0
    else:
        return somaRec(arr, f - 1) + arr[f]

#3
def soma2(arr, i, f):
    if i>f:
        return 0
    elif i==f:
        return arr[f]
    else:
        return soma2(arr, i+1, f-1) + arr[i] + arr[f]
        
#4
def muro(arr,pos):
    passo = 0
    pos = randint(0, len(arr)-1)
    while True:
        if pos + passo < len(arr) and muro[pos+passo] == 0:
            print("Ta no muro")
            break
        elif pos - passo >= 0 and muro[pos - passo] == 0:
            print("Ta no muro")
            break
        elif passo >= len(arr):
            print("Nao ta no muro")
            break
        else:
            passo += 1
        
	
	

		
