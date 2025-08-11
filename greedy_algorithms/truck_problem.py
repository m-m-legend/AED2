import time


def caminhao(C, itens):
    itens.sort(reverse = True)
    caminhoes = []; 
    while(len(itens)>0):
        caminhao = []
        i = 0
        soma = 0
        while(soma < C and i < len(itens)):
            if(C - soma >= itens[i]):
                caminhao.append(itens[i])
                soma += itens[i]
                itens.pop(i)
            else:
                i += 1
        caminhoes.append(caminhao)
    return caminhoes

itens = []

qtd = int(input("Quantos elementos quer adicionar na lista? "))
for i in range(0, qtd):
    elemento = int(input(f"Elemento {i+1}: "))
    itens.append(elemento)
    
capacidade = int(input("Qual a capacidade dos caminhoes? "))
print(caminhao(capacidade, itens))







            
                
            
    
    