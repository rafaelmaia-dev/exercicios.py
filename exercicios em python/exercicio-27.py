nome = str(input('Digite o seu nome completo: ')).strip()

dividido = nome.split()
print('Muito prazer em te conhecer {}!' .format(nome))
print('Seu primeiro nome é {}.' .format(dividido[0]))
print('Seu último nome é {}.' .format(dividido[-1]))