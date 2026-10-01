# Criar um protocolo no formato ANO-NÚMERO-INICIAIS e testar textos com acentos, maiúsculas e espaços extras. (2026-0042-JDS)
continuar = 's'
while continuar == 's':
    print('-'*50)
    ano = (input("Digite o ano da reclamação: "))
    numero_protocolo = (input("Digite o número de protocolo: "))
    nome = input("Digite seu nome: ")
    print('-'*50)

    numero_protocolo = numero_protocolo.zfill(4)
    nome = nome.upper().split()
    iniciais = ''.join([palavra[0] for palavra in nome])

    protocolo = '-'.join([ano, numero_protocolo, iniciais])
    print (protocolo)
    print('-'*50)

    continuar = input("Deseja continuar? [S/N] ").lower()
    print('-'*50)

print("Programa Finalizado!")
print('-'*50)

# RESUMO
# importar bibliotecas:
# import (nome da biblioteca)
# from (nome da biblioteca) import (função da biblioteca)
# ctrl + espaço para mostrar as funções da biblioteca
# site python.org tem a documentação de todas as bibliotecas

# frase = "Curso em Vídeo Python"
# print(frase) # O Python diferencia maiúsculas de minúsculas
# print(frase[9]) # Pega a letra na posição 9, começando do 0
# print(frase[9:14]) # Pega a letra na posição 9 até a 13 - Vídeo
# print(frase[9:21:2]) # Pega a letra na posição 9 até a 20 pulando 2 em 2 - Vdo Pto
# print(frase[:5]) # Pega a letra da posição 0 ate 4 - Curso
# print(frase[15:]) # Pega a letra da posição 15 ao fim - Python
# print(frase[9::3]) # Pega a letra 9 até o fim pulando 3 em 3 - VdoPh

# len(frase) # conta quantos caracteres, incluindo espaços
# frase.count('o') # conta quantos o tem na frase
# frase.count('o', 0, 13) # conta quantos o tem na frase de 0 a 12
# frase.find('deo') # posição onde começa deo
# frase.find('android') # retorna -1 pois não tem android na frase
# frase.replace('Python', "Android") # substitui Python por Android
# frase.upper() # tudo vira maiúsculo
# frase.lower() # tudo vira minúsculo
# frase.capitalize() # deixa primeira letra maiúscula
# frase.title() # deixa todas palavras com primeira letra maiúscula
# frase.strip() # tira espaços no começo e final
# frase.rstrip() # tira espaços no final
# frase.lstrip() # tira espaços no começo
# frase.split() # separa as palavras em uma lista
# ''.join(frase) # junta as palavas com o que estiver entre aspas

# print('Curso' in frase) # retorna True ou False se tiver em frase
# print('''lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.''') 

# print(frase.upper().count('O')) # mistura de funções, deixa td maiúsculo e conta quantos O tem
# frase = frase.replace('Python', 'Android') # substitui Python por Android e atribui a frase dnv
# print (frase.lower().find('python')) #mistura funções, deixa td minúsculo e procura python

# dividido = frase.split()
# print(dividido[0][3]) # pega a palavra 0 da lista e a letra 3 dessa palavra
