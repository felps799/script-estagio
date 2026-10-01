# COMANDO: Ler nome, idade, altura, área e experiência prévia; exibir valores e tipos de forma organizada.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
area = input("Digite sua área de atuação: ")
exp = input("Digite sua experiência prévia: ")
print(f"Olá, {nome}, você tem {idade} anos, mede {altura} metros, atua na área de {area} e tem experiência prévia em {exp}.")
print(f"Tipo de dado do nome: {type(nome)}")
print(f"Tipo de dado da idade: {type(idade)}")
print(f"Tipo de dado da altura: {type(altura)}")
print(f"Tipo de dado da área: {type(area)}")
print(f"Tipo de dado da experiência: {type(exp)}")
input("Pressione ENTER para encerrar o programa.")

# RESUMO:
# adição +                            ordem de precedência: (); **; * ou / ou // ou %; + ou -
# subtração -                         na ordem em que aparecem da esquerda para a direita
# multiplicação *                     concatenar = juntar strings/variáveis
# divisão /
# potenciação ** ou pow(base, expoente)
# "raidiciação" ** (1/numero) ou pow(base, 1/numero)
# resto da divisão %                   
# comentário shift + 3                 
# divisão inteira //
# igual ==

# organizar informações 
# nome = input("Qual é o seu nome? ")
# print(f"Prazer em te conhecer {nome:=^20}!") # centralizado
# print(f"Prazer em te conhecer {nome:->20}!") # alinhado a direita
# print(f"Prazer em te conhecer {nome:-<20}!") # alinhado a esquerda
# print(f"Prazer em te conhecer {nome:-^20}!") # centralizado com traços
# print(f"Prazer em te conhecer {nome: <20}!") # espaço vazio

# operadores aritméticos
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))
# a = n1 + n2 
# s = n1 - n2
# m = n1 * n2
# d = n1/n2
# di = n1//n2
# p = n1**n2
# mo = n1%n2
# print(f"A soma é {a}, \n a subtração é {s}, \n a multiplicação é {m}, \n a divisão é {d:.3f}, \n a divisão inteira é {di}, \n a potência é {p} \n e o resto da divisão é {mo}.")
# no final da videoaula, ele passa os exercícios do número 5 ao 15, os quais estou fazendo e salvando em uma pasta separada, chamada "Lista de Exercícios - Py3". A pasta "Tarefas Estágio" contém apenas os exercícios que o HERISSON HYAN passou para serem feitos como tarefa, e não os exercícios do curso :).