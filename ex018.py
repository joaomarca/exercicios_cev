import math
angd = float(input('Digite o valor do ângulo: '))
angr = math.radians(angd)
sen = math.sin(angr)
cos = math.cos(angr)
tan = math.tan(angr)
print('O valor do seno do angulo {} é de {}, do cosseno é {} e da tangente é de {}.'.format(angd, sen, cos, tan))
