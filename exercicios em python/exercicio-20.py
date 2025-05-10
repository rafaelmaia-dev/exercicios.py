#Código 01

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

sorteado = ([n1, n2, n3, n4])
random.shuffle(sorteado)

print('A ordem de apresentação será: {}, {}, {}, {}.' .format(*sorteado))



#Código 02

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

sorteado = ([n1, n2, n3, n4])
shuffle(sorteado)

print('A ordem de apresentação será: {}, {}, {}, {}.' .format(*sorteado))



