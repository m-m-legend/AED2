import time

'''tempos = [
    [0, 6],
    [3, 5],
    [1, 4],
    [5, 9],
    [5, 7],
    [3, 9],
    [6, 10],
    [8, 11],
    [8, 12],
    [2, 14],
    [12, 16]
]
'''

def atividade(tempos):
    tempos.sort(key = lambda x:x[1])
    atividades = []
    atividades.append(tempos[0])
    for i in range(1,len(tempos)):
            if(tempos[i][0] > atividades[-1][1]):
                atividades.append(tempos[i])
    return atividades

tempos = []
qtd = int(input("Quantidade de elementos: "))
for i in range(0, qtd):
        elemento = []
        inicio = int(input(f"Horario de inicio {i+1}: "))
        fim = int(input(f"Horario de fim {i+1}: "))
        elemento.append(inicio)
        elemento.append(fim)
        tempos.append(elemento)

print(atividade(tempos))

        
        
        




                
    
    
    