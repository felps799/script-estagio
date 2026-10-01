'''personagem = ("Cococi", "Mago", 15, 100, 80)
A tupla representa:
(nome, classe, nível, vida, mana)
Faça um programa que:
Mostre o nome.
Mostre a classe.
Mostre o nível.
Mostre a vida.
Mostre a mana.
Mostre quantas informações existem na tupla.
Mostre todas as informações usando for.'''

personagem = ("Cococi", "Mago", 15, 100, 80)
for informacao in personagem:
    nome = personagem[0]
    classe = personagem[1]
    nivel = personagem[2]
    vida = personagem[3]
    mana = personagem[4]
    numero_info = len(personagem)
    print(f'O nome do personagem é {nome}, da classe {classe}, de nível {nivel}, com {vida} de vida e {mana} de mana. Essa lista contém {numero_info} informações desse personagem.')
    break