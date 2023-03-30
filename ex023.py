numero = input('Digite um número entre 0 e 9999: ')
numeroSplit = ' '.join(numero).split(' ')
numeroM = numeroSplit[0]
numeroC = numeroSplit[1]
numeroD = numeroSplit[2]
numeroU = numeroSplit[3]
print('Unidade = {}\nDezena = {}'.format(numeroU, numeroD))
print('Centena = {}\nMilhar = {}'.format(numeroC, numeroM))
