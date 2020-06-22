import re
from random import randint
import os
from valida_cnpj import soma, para_soma, regressao1, regressao, formula, imprimir

if __name__ == "__main__":

    while True: 
        escolha = int(input('Escolha uma opção: \n1 - Gerar CNPJ \n2 - Validar CNPJ \n3 - Sair\n'))
        if escolha == 1:
            os.system('cls')
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
            print()
            imprimir('Cnpj gerado', cnpj_gerado)
            print()
        elif escolha == 2:
            os.system('cls')
            op_validar = int(input('1 - Validar cnpj gerado \n2 - Validar cnpj externo\n'))
            if op_validar == 1:
                contador = 0
                cn = re.sub(r'[^0-9]', '', cnpj_gerado)
                novo_cnpj = cn[:12]

                soma_total1 = soma(para_soma(regressao1, novo_cnpj))
                digito1 = formula(soma_total1)

                novo_cnpj = novo_cnpj + '0' if digito1 > 9 else novo_cnpj+str(digito1)

                soma_total2 = soma(para_soma(regressao, novo_cnpj))
                digito2 = formula(soma_total2)

                novo_cnpj = novo_cnpj + '0' if digito2 > 9 else novo_cnpj+str(digito2)

                imprimir('Original', cnpj_gerado)
                imprimir('Validação', novo_cnpj)
                print('CNPJ válido\n' if novo_cnpj == cn else 'CNPJ inválido\n')
                
            elif op_validar == 2:
                cnpj = str(input('Digite um cnpj: '))
                contador = 0

                cn = re.sub(r'[^0-9]', '', cnpj_gerado)
                novo_cnpj = cn[:12]

                soma_total1 = soma(para_soma(regressao1, novo_cnpj))
                digito1 = formula(soma_total1)

                novo_cnpj = novo_cnpj + '0' if digito1 > 9 else novo_cnpj+str(digito1)

                soma_total2 = soma(para_soma(regressao, novo_cnpj))
                digito2 = formula(soma_total2)

                novo_cnpj = novo_cnpj + '0' if digito2 > 9 else novo_cnpj+str(digito2)

                imprimir('Original', cnpj)
                imprimir('Validação', novo_cnpj)
                print('CNPJ válido\n' if novo_cnpj == cn else 'CNPJ inválido\n')
            else:
                print('Opção inválida\n')
        elif escolha == 3:
            break
        else:
            pass

