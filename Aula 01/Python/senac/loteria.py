bruto = float(input('Digite o valor do prêmio: '))
liquido = bruto * 0.93

print(f'Prêmio bruto: R${bruto:.2f}, prêmio liquido: R${liquido:.2f}\nPrêmio do primeiro ganhador: R${liquido * 0.46:.2f}\nPrêmio do segundo ganhador: R${liquido * 0.32:.2f}\nPrêmio do terceiro ganhador R${liquido * 0.22:.2f}')