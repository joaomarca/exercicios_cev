al = int(input('Qual a altura da parede? '))
la = int(input('E a sua largura? '))
ar = al * la
ti = ar / 2
print('Para pintar essa parede que mede {} metros quadrados, seram necessários'.format(ar), end=' ')
print('{} litros de tinta.'.format(ti))
