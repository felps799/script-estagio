'''RSOR DE NÚMEROS
Crie um programa que peça ao usuário dois números e realize uma divisão.

Exemplo:
Digite o primeiro número: 10
Digite o segundo número: 2
Resultado: 5.0
Porém, o programa precisa tratar situações em que o usuário digite algo inválido.
Utilize try e except para tratar:
1. Entrada que não seja número
Exemplo:
Digite o primeiro número: abc
O programa deverá informar:
Erro: digite apenas números.
2. Divisão por zero
Exemplo:
Digite o primeiro número: 10
Digite o segundo número: 0
O programa deverá informar:
Erro: não é possível dividir por zero.'''

try:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    resultado = numero1 / numero2
except ValueError:
    print('Erro: digite apenas números.')
except ZeroDivisionError:
    print('Erro: não é possível dividir por zero.')
else:
    print(f'Resultado: {resultado}')