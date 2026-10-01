'''Crie um dicionário representando um jogador:
```python
jogador = {
    "nome": "Cococi",
    "pontos": 80,
    "nivel": 3,
    "vidas": 2
}
```
Crie uma função chamada `mostrar_jogador()` que receba o dicionário e mostre:
```text
=== JOGADOR ===

Nome: Cococi
Pontos: 80
Nível: 3
Vidas: 2
```
Depois, crie uma função chamada `adicionar_pontos()`.
A função deverá:
* receber o jogador e uma quantidade de pontos;
* adicionar esses pontos ao jogador;
* retornar o jogador atualizado.
Exemplo:

```python
jogador = adicionar_pontos(jogador, 50)
```
Resultado esperado:
```text
Pontos: 130
```
Crie uma função chamada `verificar_nivel()`.

Ela deverá verificar os pontos do jogador:

* 100 pontos ou mais → nível 4
* 200 pontos ou mais → nível 5
* abaixo de 100 → permanece no nível atual

Depois, mostre o jogador novamente.'''

jogador = {
    "nome": "Cococi",
    "pontos": 80,
    "nivel": 3,
    "vidas": 2
}


def mostrar_jogador(who):
    print('=== JOGADOR ===')
    print()
    print(f'Nome: {who["nome"]}')
    print(f'Pontos: {who["pontos"]}')
    print(f'Nível: {who["nivel"]}')
    print(f'Vidas: {who["vidas"]}')


def adicionar_pontos(who, quantidade):
    who["pontos"] += quantidade
    return who


def verificar_nivel(who):
    if who["pontos"] >= 200:
        who["nivel"] = 5
    elif who["pontos"] >= 100:
        who["nivel"] = 4
    else:
        print(f'Permanece no nível {who["nivel"]}')


mostrar_jogador(jogador)
jogador = adicionar_pontos(jogador, 50)
print(f'Pontos: {jogador["pontos"]}')
verificar_nivel(jogador)
mostrar_jogador(jogador)