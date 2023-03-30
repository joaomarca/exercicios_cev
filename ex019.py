from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Agora do segundo: ')
a3 = input('Agora do terceiro: ')
a4 = input('E, por fim, do quarto: ')
lista = [a1, a2, a3, a4]

aluno = choice(lista)
print(aluno)