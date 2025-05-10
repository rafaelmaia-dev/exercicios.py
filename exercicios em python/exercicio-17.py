#Código 01

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (a ** 2 + b ** 2) ** (1/2)

print('O comprimento da hipotenusa é de {:.2f}.' .format(hipotenusa))


#Cógido 02

from math import hypot

hipotenusa = hypot(a, b)

print('A hipotenusa vai medir: {:.2f}.' .format(hipotenusa))



