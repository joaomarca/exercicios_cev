nome = input('Digite seu nome completo:')
nomeSplit = nome.split()
nomePrimeiro = nomeSplit[0]
nomeUltimo = nomeSplit[-1]
print('Seu primeiro nome é {} e seu último nome é {}.'.format(nomePrimeiro, nomeUltimo))
