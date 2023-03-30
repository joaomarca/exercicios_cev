dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados com o carro nesse período? '))
kmc = km * 0.15
dic = dias * 60
pc = dic + kmc
print('O preço a ser pago pelo aluguel do carro é de {} reais.'.format(pc))
