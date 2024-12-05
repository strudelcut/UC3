# Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário.

# salario = float(input('Digite o salário: R$'))
# irpf = 0

# if salario <= 1903.98:
#     irpf = 0
# elif salario <= 2826.65:
#     irpf = (salario*12 - 1903.98) * 0.075 - 142.80
# elif salario <= 3751.05:
#     irpf = (salario*12 - 1903.98) * 0.15 - 354.80
# elif salario <= 4664.68:
#     irpf = (salario*12 - 1903.98) * 0.225 - 636.13
# else:
#     irpf = (salario*12 - 1903.98) * 0.275 - 869.36

# print(f'IRPF: R${irpf:.2f}')
# print(f'IPRF mensal: R${irpf/12:.2f}')


# Função para calcular o Imposto de Renda
def calcular_irpf(salario):
    if salario <= 1903.98:
        imposto = 0
    elif salario <= 2826.65:
        imposto = salario * 0.075
    elif salario <= 3751.05:
        imposto = salario * 0.15
    elif salario <= 4664.68:
        imposto = salario * 0.225
    else:
        imposto = salario * 0.275
    return imposto


# Leitura do salário
salario = float(input("Informe o salário do funcionário: R$ "))


# Calculando o IRPF
imposto = calcular_irpf(salario)


# Exibindo o resultado
print(f"O valor do IRPF a ser descontado é: R$ {imposto:.2f}")