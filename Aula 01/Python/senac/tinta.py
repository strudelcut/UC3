largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

litros = area /3

latas = litros // 3.6

if litros % 3.6 != 0:
    latas += 1

custo = latas * 107

print(f'Quantidade de latas necessárias: {latas}, Custo total: {custo:.2f}')