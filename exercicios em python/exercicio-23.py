# Código 01

numero = str(input('Digite uma número: '))

print('unidade: {}, dezena: {}, centena: {}, milhar: {}' .format(numero[-1], numero[-2], numero[-3], numero[-4]))


# Código 02 

num = int(input('Informe um número: '))
n = str(num)

n.split()
print('unidade: {}, dezena: {}, centena: {}, milhar: {}' .format(n[-1], n[-2], n[-3], n[-4]))



# Código 03

num = int(input('Digite um valor: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}, dezena: {}, centena: {}, milhar: {}' .format(u, d, c, m))
