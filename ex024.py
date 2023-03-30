nome = input('Digite o nome completo da sua cidade: ').split()
nomePrimeiro = nome[0]
starts = nomePrimeiro.startswith('Santo')
if starts:
    print('O primeiro nome da sua cidade é Santo.')
else:
    print('O primeiro nome da sua cidade não é Santo.')
