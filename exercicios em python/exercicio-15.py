km_percorridos = float(input('Quantos kilometros você percorreu? '))
dias = int(input('Por quantos dias você alugou este carro? '))

km = 0.15
carro_por_dia = 60

preco = (km_percorridos * km) + (dias * carro_por_dia)

print('O preço a pagar é de {:.2f}.' .format(preco))