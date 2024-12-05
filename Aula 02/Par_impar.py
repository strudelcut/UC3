# Escreva um programa que receba um número inteiro e verifique se ele é par ou ímpar, exibindo o resultado.

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é impar')