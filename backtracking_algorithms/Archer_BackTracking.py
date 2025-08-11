def somar(L):
    soma = 0
    for i in L:
        soma += i
    return soma

def minimoDeAcertos(alvos, total):
    alvosAcertados = []
    
    def backtrack(alvosAcertados):
        for i in alvos[::-1]:
            alvosAcertados.append(i)
            if somar(alvosAcertados) < total:
                backtrack(alvosAcertados)
            if somar(alvosAcertados) == total:
                return alvosAcertados
            alvosAcertados.pop()

    alvosAcertados = backtrack(alvosAcertados)
    return alvosAcertados

def imprimir(L):
    for i in L:
        print(f"{i}", end=" ")
    print("")
    
def main():
    casos = int(input("{número de casos} "))
    for i in range(casos):
        entrada = input("{numero de alvos} {total} ").split(" ")
        n, total = int(entrada[0]), int(entrada[1])
        alvos = [int(i) for i in input("{alvos} ").split(" ")]
        if len(alvos) != n:
            return 1

        alvosAcertados = minimoDeAcertos(alvos, total)
        print(f"Foram necessários {len(alvosAcertados)} flechadas para alcançar {total} pontos. Alvos acertados: ")
        imprimir(alvosAcertados)

if __name__ == "__main__":
    main()
