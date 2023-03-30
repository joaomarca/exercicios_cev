frase = input('Digite uma frase: ')
fraseA = frase.count('a')
fraseAP = frase.find('a') + 1
fraseARP = frase.rfind('a') + 1
print("""Sua frase contém a letra 'a' {} vezes, aparecendo pela primeira vez na {}ª posição.""".format(fraseA, fraseAP))
print('E aparecendo pela última vez na {}ª posição.'.format(fraseARP))
