# Escreva um programa que receba números inteiros até que o usuário digite 0. Calcule e exiba a média dos números positivos digitados.

soma = 0
cont = 0

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    if num > 0:
        soma += num
        cont += 1

if num == 0:
    print('Nenhum número positivo digitado.')
else:
    print(f'Média dos números positivos: {soma / cont}')