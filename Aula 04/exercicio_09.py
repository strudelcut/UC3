# Crie uma classe Funcionario com os atributos nome, horas_trabalhadas e valor_hora.
# Adicione os métodos:
# registrar_horas(horas) para registrar horas trabalhadas.
# calcular_pagamento() para calcular o pagamento baseado nas horas trabalhadas e no valor por hora.

class Funcionario:
    def __init__(self, nome, valor_hora):
        self.nome = nome
        self.horas = 0
        self.valor_hora = valor_hora
    def registrar_horas(self, horas):
        self.horas = horas

    def calcular_pagamento(self):
        return self.horas * self.valor_hora
    
funcionario = Funcionario('João', 10)
funcionario.registrar_horas(8)
print(f'R${funcionario.calcular_pagamento():.2f}')