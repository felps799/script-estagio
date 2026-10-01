'''Crie uma função chamada `mostrar_personagem` que receba um dicionário contendo informações de um personagem.
Utilize:
```python
personagem = {
    "nome": "Cococi",
    "classe": "Mago",
    "nivel": 10,
    "vida": 100
}
```
A função deverá receber o dicionário e mostrar as informações no seguinte formato:
```text
=== PERSONAGEM ===

Nome: Cococi
Classe: Mago
Nível: 10
Vida: 100
```
Depois, crie uma segunda função chamada `aumentar_nivel`.
Ela deverá receber o personagem e aumentar seu nível em `1`.
No final:
Nível antes: 10
Nível depois: 11'''

personagem = {
    "nome": "Cococi",
    "classe": "Mago",
    "nivel": 10,
    "vida": 100}
nivel = 0

def mostrar_personagem():
    print('=== PERSONAGEM ===')
    print(f'Nome: {personagem["nome"]}')
    print(f'Classe: {personagem["classe"]}')
    print(f'Nível: {personagem["nivel"]}')
    print(f'Vida: {personagem["vida"]}')

mostrar_personagem()

def aumentar_nivel():
    print(f'Nível antes: {personagem["nivel"]}')
    print(f'Nível depois: {(personagem["nivel"]+1)}')
    personagem["nivel"] = personagem["nivel"]+1

aumentar_nivel()
mostrar_personagem()
