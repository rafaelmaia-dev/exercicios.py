#Código 01

numero = int(input('Digite um valor: '))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print('O dobro de {} vale {}' .format(numero, dobro, end = ' '))
print('O triplo de {} vale {}' .format(numero, triplo, end = ' '))
print('A raiz quadrada de {} é igual a {:.2f}' .format(numero, raiz_quadrada))


#Código 02

numero = int(input('Digite um valor: '))

print('O dobro de {} vale {}, o triplo vale {} e a raiz quadrada vale {:.2f}' .format(numero, (numero * 2), (numero * 3), (numero ** (1/2))))