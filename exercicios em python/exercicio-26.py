frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra A aparece {} vezes na frase.' .format(frase.count('a')))
print('A primeira letra A apareceu na posição {}.' .format(frase.find('a')))
print('A última letra A apareceu na posição {}.' .format(frase.rfind('a')))
