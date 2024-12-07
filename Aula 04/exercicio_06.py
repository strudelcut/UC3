# Implemente uma classe Temperatura com os atributos celsius.
# Adicione métodos para:
# Converter para Fahrenheit (converter_para_fahrenheit).
# Converter para Kelvin (converter_para_kelvin).

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def converter_para_fahrenheit(self):
        return (self.celsius * 1.8) + 32

    def converter_para_kelvin(self):
        return self.celsius + 273.15

temp = Temperatura(25)
print(f'\nEm Fahrenheit: {temp.converter_para_fahrenheit():.2f}')
print(f'Em Kelvin: {temp.converter_para_kelvin():.2f}\n')