def crescente(l): #lista.sort() or sorted(lista)
    lista = []
    cont = 0
    y = len(l)
    
    while cont < y:
        maior = 0
        for i in range(y):
            if (l[cont] > l[i]):
                maior = 1
        if (maior == 0):
            lista.append(l[cont])
            del l[cont]
            lista = lista + crescente(l)
            return lista
        cont += 1
    return lista


def remove_repetidos(x):
    cont = 0
    lista = []
    y = len(x)
    while cont < y:
        multiplo = 0
        for i in range(cont + 1, y):
            if (x[i] == x[cont]):
                multiplo = 1
        if (multiplo == 0):
            lista.append(x[cont])
        cont += 1
    return crescente(lista)

def soma_elementos(x):
    soma = 0
    for i in x:
        soma = soma + i
    return soma
lista = [1, 2, 3, 4, 5, 6]
            
