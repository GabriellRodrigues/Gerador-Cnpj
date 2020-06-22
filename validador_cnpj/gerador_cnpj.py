from random import randint
from valida_cnpj import regressao, regressao1, para_soma, soma, formula, imprimir

lista_aleatoria = [randint(0, 9) for i in range(8)]
cnpj_gerado = ''

for i in range(len(lista_aleatoria)):
    cnpj_gerado += str(lista_aleatoria[i])

cnpj_gerado += '0001'
soma_total1 = soma(para_soma(regressao1, cnpj_gerado))
digito1 = formula(soma_total1)

cnpj_gerado += '0' if digito1 > 9 else str(digito1)

soma_total2 = soma(para_soma(regressao, cnpj_gerado))
digito2 = formula(soma_total2)

cnpj_gerado += '0' if digito2 > 9 else str(digito2)

