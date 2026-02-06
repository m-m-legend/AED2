itens = [[10, 60],[20,100],[30,120],[10,30]]
C = 50

def fracionaria(itens, C):
    for i in range(0, len(itens)):
        itens[i].append(itens[i][1]/itens[i][0])
    itens.sort(key = lambda x:x[2], reverse = True)
    #[[10,60,6], [20,100,5], [30,120,4], [10,30,3]]
    soma = 0; peso = 0; mochila = []; j = 0
    while(peso <= C and j < len(itens)):
        if C - peso >= itens[j][0]:
            peso += itens[j][0]
            soma += itens[j][1]
            mochila.append(itens[j])
            itens.pop(j)
        else:
            soma += ((C-peso)/itens[j][0])*itens[j][1]
            mochila.append(itens[j])
            break
    return mochila, soma

print(fracionaria(itens, C))

            
            
        
    