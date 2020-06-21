import re
from validador_cnpj.valida import soma, para_soma, regressao1, regressao, formula, imprimir

cnpj = str(input('Digite um cnpj: '))
contador = 0

cn = re.sub(r'[^0-9]', '', cnpj)
novo_cnpj = cn[:12]

soma_total1 = soma(para_soma(regressao1, novo_cnpj))
digito1 = formula(soma_total1)

novo_cnpj = novo_cnpj + '0' if digito1 > 9 else novo_cnpj+str(digito1)

soma_total2 = soma(para_soma(regressao, novo_cnpj))
digito2 = formula(soma_total2)

novo_cnpj = novo_cnpj + '0' if digito2 > 9 else novo_cnpj+str(digito2)

print(f'Original: {cnpj}')
imprimir('Validação', novo_cnpj)
print('CNPJ válido' if novo_cnpj == cn else 'CNPJ inválido')
