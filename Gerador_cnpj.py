from random import randint
from validador_cnpj.valida import regressao, regressao1, para_soma, soma, formula, imprimir

lista_aleatoria = [randint(0, 9) for i in range(8)]
cnpj = ''

for i in range(len(lista_aleatoria)):
    cnpj += str(lista_aleatoria[i])

cnpj += '0001'
soma_total1 = soma(para_soma(regressao1, cnpj))
digito1 = formula(soma_total1)

cnpj += '0' if digito1 > 9 else str(digito1)

soma_total2 = soma(para_soma(regressao, cnpj))
digito2 = formula(soma_total2)

cnpj += '0' if digito2 > 9 else str(digito2)
imprimir('CNPJ gerado', cnpj)
