regressao = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
regressao1 = regressao[1:5] + regressao[5:13]

def para_soma(lista1, lista2):
    lista_soma = []
    for i in range(len(lista1)):
        lista_soma.append(lista1[i] * int(lista2[i]))
    return lista_soma

def soma(funcao):
    return sum(funcao)

def formula(var):
    return 11 - (var % 11)

def imprimir(apresenta, string):
    print(f'{apresenta}: {string[:2]}.{string[2:5]}.{string[5:8]}/{string[8:12]}-{string[12:15]}')
