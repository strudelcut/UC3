# Crie um programa que calcule o valor total de uma compra feita em várias parcelas. Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. 
# Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.

# parcela = float(input('Digite a quantidade de parcelas: '))
# valor = float(input('Digite o valor da parcela: R$'))

# total = parcela * valor

# if total > 1000:
#     total += total * 0.05

# print(f'Valor total: R${total:.2f}')

parcelas = int(input("Quantas parcelas? "))
valor_parcela = float(input("Valor da parcela: R$ "))


total = parcelas * valor_parcela


if total > 1000:
    total += total * 0.05


print(f"Valor total a pagar: R$ {total:.2f}")