salario = float(input('Digite o seu salário: R$'))

novo_salario = salario + (salario * 0.15)

print('Seu salário era R$ {:.2f}. Com um aumento de 15%, ele passou a ser R$ {:.2f}.' .format(salario, novo_salario))