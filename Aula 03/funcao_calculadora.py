# Implemente uma função que receba dois números e uma operação (+, -, *, /) e devolva o resultado.

# def calc(num1: int, num2: int, op: str):
#     if op == '+':
#         return num1 + num2
#     elif op == '-':
#         return num1 - num2
#     elif '*' in op: 
#         return num1 * num2
#     elif '/' in op:
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return 'Somente Deus divide por 0.'
#     else:
#         return 'Operação inválida.'


# primeiro = int(input('Digite um número: '))
# segundo = int(input('Digite um número: '))
# opera = input('Qual operação? ')

# print(calc(primeiro, segundo, opera))

def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:  # Evita divisão por zero
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"


# Exemplos de uso:
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
op = input('Informe a operação(+,-,*,/): ')
print(calculadora(n1, n2, op))