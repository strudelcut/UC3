paes = int(input('Digite a quantidade de pães vendidos: ' ))
broa = int(input('Digite a quantidade de broas vendidas: '))

receita = (paes* 0.8) + (broa* 2.5)

lucro = receita * 0.57

poupa = lucro * 0.15

euro = (lucro - poupa) * 0.15

conv = euro / 4.6

print(f'Venda total de pães e broas: R${receita:.2f}')
print(f'O custo de fabricação: R${receita - lucro:.2f}')
print(f'Quanto irá guardar na poupança: R${poupa:.2f}')
print(f'Quantos euros irá comprar €{conv:.2f}')


