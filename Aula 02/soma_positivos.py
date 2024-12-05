# Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. Exiba a soma de todos os números positivos digitados.

soma = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    soma += num
print(f'Soma: {soma}')