produto = float(input('Qual é o preço do produto? R$'))

preço_com_desconto = produto - (produto * 0.05)
print('O produto que custava {:.2f}R$, na promoção com desconto de 5% vai custar {:.2f}R$' .format(produto, preço_com_desconto))