def dobro(numero):
    dobro = numero*2
    print(dobro)

def triplo(numero):
    triplo = numero*3
    print(triplo)

def maior(*numeros):
    cont = maior = 0
    for numero in numeros:
        if cont == 0:
            maior = numero
            cont += 1
        if numero > maior:
            maior = numero
    print(f'O maior valor informado foi {maior}.')

