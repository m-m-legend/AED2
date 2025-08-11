import time

moedas = [1,5,10,25]
quantidade = [0] * len(moedas)


def moeda(moedas, valor, quantidade):
    moedas.sort(reverse = True)
    #[25,10,5,1]
    soma = 0; i = 0; cont = 0
    while(soma < valor):
        if(valor - soma >= moedas[i]):
            soma += moedas[i]
            quantidade[len(quantidade)-1-i] += 1
            cont += 1
            continue
        else:
            i += 1
    return cont, quantidade

print(moedas)
print(quantidade)

print(moeda(moedas, 15, quantidade))

        
        
    
    