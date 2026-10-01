# Criar um pequeno sistema de decisão em Python que receba informações de uma situação e, de acordo com regras de negócio, classifique sua prioridade e determine se o caso deve ser automatizado, enviado para revisão humana ou bloqueado. Depois, registrar pelo menos seis casos de teste, incluindo casos comuns, valores de fronteira e situações envolvendo dados sensíveis, indicando o resultado esperado de cada caso. (= ex036.py)

# CONDIÇÕES ANINHADAS:
# if (condição):
# elif (condição):
# else:

from time import sleep
print('--=--' *20)
nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
cpf = str(input('Digite seu CPF: '))
renda = float(input('Digite sua renda: '))
valor_casa = float(input('Digite o valor da casa: R$'))
anos = int(input('Digite em quantos anos pretende pagar: '))
print('--=--' *20)

print('PROCESSANDO...')
sleep (2)

if idade < 18 or (valor_casa / (anos*12)) > 0.3*renda:
    print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não se enquadra nos critérios desse empréstimo.')

else:
    prestacao_mensal = valor_casa / (anos*12)
    if renda < 1500:
        print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não tem base financeira para solicitar esse empréstimo.')

    elif renda > 50000 and prestacao_mensal <= 0.3*renda:
        print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não necessita solicitar esse empréstimo.')
        
    elif renda > 20000 and renda <= 50000 and prestacao_mensal <= 0.3*renda:
        print('\033[41;1;32m Parabéns, empréstimo aprovado! \033[m Te encaminharemos para a revisão humana.')

    elif renda >= 1500 and renda <= 20000 and prestacao_mensal <= 0.3*renda:
        print('\033[41;1;32m Parabéns, empréstimo aprovado! \033[m Te encaminharemos para o setor automatizado.')
        
    else:
        print('Seu empréstimo foi \033[41;1;30m bloqueado \033[m! Você não se enquadra nos critérios desse empréstimo.')

print('--=--' *20)