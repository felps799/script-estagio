'''Crie um arquivo chamado:
```text
utilidades.py
```
Dentro dele, crie três funções:
```python
def dobro(numero):
    ...

def triplo(numero):
    ...

def maior(numero1, numero2):
    ...
```

Depois, crie outro arquivo chamado:
```text
main.py
```
Importe as funções do módulo `utilidades` e utilize-as.
O programa deverá apresentar:
```text
Dobro de 5: 10
Triplo de 5: 15
Maior entre 8 e 12: 12
```
Coloque as funções dentro de `calculos.py` e faça a importação no `main.py`.'''

import utilidades
utilidades.dobro(5)
utilidades.triplo(5)
utilidades.maior(12,8)