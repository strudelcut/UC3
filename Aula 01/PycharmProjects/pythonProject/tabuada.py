# Escreva um programa que exiba a tabuada de multiplicação de um número digitado pelo usuário, de 1 a 10.

num = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')