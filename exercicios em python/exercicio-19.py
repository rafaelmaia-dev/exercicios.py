#Código 01

import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

sorteado = random.choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno que foi sorteado para apagar a lousa foi: {}!' .format(sorteado))



#Código 02

from random import choice 

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

sorteado = choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno sorteado para apagar a lousa foi o {}!' .format(sorteado))