'''notas = [7.5, 8.0, 6.5, 9.0, 5.5] 
Faça um programa que:
Mostre todas as notas.
Mostre a primeira nota.
Mostre a última nota.
Adicione uma nova nota 8.5.
Altere a nota 5.5 para 6.0.
Remova a nota 7.5.
Mostre quantas notas existem agora.
Mostre a lista final.'''

notas = [7.5, 8.0, 6.5, 9.0, 5.5]
print (notas)
for nota in notas:
    print(nota, end =" ")
print ('\nA primeira nota da lista é',notas[0])
print ('A última nota da lista é',notas[-1])
notas.append(8.5) 
notas [-2] = 6.0
del notas [0] # deleta na posição indicada
# nota.pop(1) elimina pela posição, geralmente final 
# nota.remove(7.5) elimina pelo conteúdo
print('A quantidade de notas é',len(notas))
print(notas)