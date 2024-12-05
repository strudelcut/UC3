# Considere que o preço da tarifa de energia é R$ 0,50 por kWh. Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. 
# Se o consumo for maior que 200 kWh, aplique um desconto de 10%.

# consumo = float(input('Digite o consumo de energia: '))
# if consumo > 200:
#     consumo = consumo * 0.9
# print(f'Valor a pagar: R${consumo * 0.50:.2f}')

consumo = float(input("Digite o consumo de energia em kWh: "))


valor = consumo * 0.50


if consumo > 200:
    valor -= valor * 0.10


print(f"O valor total da conta de energia é: R$ {valor:.2f}")