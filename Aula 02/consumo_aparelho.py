# Crie um programa que calcule o consumo total de energia de vários aparelhos em uma casa. Pergunte o consumo de cada aparelho em kWh e a quantidade de horas que o aparelho 
# fica ligado por dia. O programa deve somar o consumo diário de todos os aparelhos e calcular o custo total de energia no mês.

total_consumo = 0
numero_aparelhos = int(input("Quantos aparelhos? "))


for i in range(numero_aparelhos):
    consumo = float(input(f"Consumo do aparelho {i+1} (kWh): "))
    horas = float(input(f"Quantas horas por dia o aparelho {i+1} fica ligado? "))
    consumo_diario = consumo * horas
    total_consumo += consumo_diario


custo_mensal = total_consumo * 30 * 0.50  # Preço de R$ 0,50 por kWh
print(f"O custo mensal de energia será: R$ {custo_mensal:.2f}")