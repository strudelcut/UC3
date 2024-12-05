# Escreva um programa que receba 10 números inteiros e conte quantos deles são pares.

cont = 0
for i in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        cont += 1
print(f'Quantidade de números pares: {cont}')