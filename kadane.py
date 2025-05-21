import time, random

def max3(A, B, C):
    if (A >= B and A >= C):
        return A
    elif (B >= A and B >= C):
        return B
    else:
        return C

def max2(A,B):
    if A >= B:
        return A
    else:
        return B
		
def min2(A, B):
    if A <= B:
        return A
    else: 
        return B
	
		

def somaAoMeio(vetor, inicio, meio, fim, d):
    temp_ini = time.time()
    soma_esquerda = float('-inf') #Pegando um número bem pequeno
    soma_direita = float('-inf')  #Pegando um número bem pequeno
    
    
    inicio_esquerda=meio; s = 0
    for i in range(meio, inicio - 1, -1):
        s += vetor[i]
        if soma_esquerda < s:
            soma_esquerda = s
            inicio_esquerda=i
    final_esquerda=meio

	
    inicio_direita = meio+1
    final_direita = meio+1
    s = 0
    for i in range(meio + 1, fim + 1):
        s += vetor[i]
        if soma_direita < s:
            soma_direita = s
            final_direita=i
	
    temp_fim = time.time()
    d["somaAoMeio"] = d.get("somaAoMeio", 0) + (temp_fim - temp_ini)
    
    return soma_esquerda + soma_direita, inicio_esquerda,final_direita


def subArray(vetor, i, j, d):
    if i > j:
        return float('-inf'),None,None
    elif i == j:
        return vetor[i],i,i
    else:
        meio = (i + j)//2
		
        A,ia,fa = subArray(vetor, i, meio, d)
        B,ib,fb = subArray(vetor, meio + 1, j, d)
        C,ic,fc = somaAoMeio(vetor, i, meio, j, d)
	
    maior = max3(A,B,C)
    if maior==A:	
        return A,ia,fa
    elif maior==B:
        return B,ib,fb
    else:
        return C,ic,fc		

def maximoSubArray(vetor, d):
    inicio = time.time()
    resultado = subArray(vetor, 0, len(vetor) - 1, d)
    fim = time.time()
    d["tempoTotal"] = fim - inicio
    return resultado
 
array_teste=[23,687,-21,-1,43,-56,190,-943]
Array_1 = []	
Array_2 = []
Array_3 = []
Array_4 = []
Array_5 = []

for i in range(100):
    Array_1.append(random.randint(-100, 100))
	
for i in range(1000):
    Array_2.append(random.randint(-100, 100))

for i in range(10000):
    Array_3.append(random.randint(-100, 100))

for i in range(100000):
    Array_4.append(random.randint(-100, 100))

for i in range(1000000):
    Array_5.append(random.randint(-100, 100))

registros = {}
a,b,c=maximoSubArray(Array_1, registros)

print(f"Maior soma do array 1: {a} Começo: {b} Fim: {c}")     

print("Tempo (subArray): {:.6f}".format(registros.get("tempoTotal")))
print("Tempo (somaAoMeio): {:.6f}".format(registros.get("somaAoMeio")))
print("")

registros = {}
a,b,c=maximoSubArray(Array_2, registros)

print(f"Maior soma do array 2: {a} Começo: {b} Fim: {c}")

print("Tempo (subArray): {:.6f}".format(registros.get("tempoTotal")))
print("Tempo (somaAoMeio): {:.6f}".format(registros.get("somaAoMeio")))
print("")

registros = {}
a,b,c=maximoSubArray(Array_3, registros)

print(f"Maior soma do array 3: {a} Começo: {b} Fim: {c}")

print("Tempo (subArray): {:.6f}".format(registros.get("tempoTotal")))
print("Tempo (somaAoMeio): {:.6f}".format(registros.get("somaAoMeio")))
print("")

registros = {}
a,b,c=maximoSubArray(Array_4, registros)
          
print(f"Maior soma do array 4: {a} Começo: {b} Fim: {c}")  

print("Tempo (subArray): {:.6f}".format(registros.get("tempoTotal")))
print("Tempo (somaAoMeio): {:.6f}".format(registros.get("somaAoMeio")))
print("")

registros = {}
a,b,c=maximoSubArray(Array_5, registros)

print(f"Maior soma do array 5: {a} Começo: {b} Fim: {c}")

print("Tempo (subArray): {:.6f}".format(registros.get("tempoTotal")))
print("Tempo (somaAoMeio): {:.6f}".format(registros.get("somaAoMeio")))
print("")

registros = {}
a,b,c=maximoSubArray(array_teste, registros)

print(f"Maior soma do array teste: {a} Começo: {b} Fim: {c}")

print("Tempo (subArray): {:.6f}".format(registros.get("tempoTotal")))
print("Tempo (somaAoMeio): {:.6f}".format(registros.get("somaAoMeio")))
