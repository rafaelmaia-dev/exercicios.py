largura = float(input('Qual é a largura da sua parede em metros? '))
altura = float(input('Qual é a altura da sua parede em metros? '))

area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m'. format(largura, altura, area))

tinta = area / 2

print('Para pintar essa parede, você precisará de {} litros de tinta.' .format(tinta))

