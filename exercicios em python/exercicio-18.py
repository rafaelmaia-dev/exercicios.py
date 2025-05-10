#Código 01

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

seno = co / hipotenusa
cosseno = ca / hipotenusa
tangente = co / ca

print('O SENO do ângulo é {:.2f}.'.format(seno))
print('O COSSENO do ângulo é {:.2f}.'.format(cosseno))
print('A TANGENTE do ângulo é {:.2f}.'.format(tangente))


#Código 02

import math

angulo = float(input('Digite o valor do ângulo: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O ângulo de {:.2f} tem o SENO de {:.2f}.' .format(angulo, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}.' .format(angulo, cosseno))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}.' .format(angulo, tangente))









