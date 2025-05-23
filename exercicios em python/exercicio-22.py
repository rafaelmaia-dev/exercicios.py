nome = str(input('Digite o seu nome completo: ')).strip()
print(nome)
print(nome.lower())
print(nome.upper())

# .format(len(nome) - nome.count(' '))) 
# O nome.count(' '))) vai subtrair os espaços existentes

print('Seu nome ao todo tem {} letras.' .format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras.' .format(nome.find(' ')))

dividido = nome.split()
print('Seu nome {} tem {} letras.' .format(dividido[0], len(dividido[0])))



