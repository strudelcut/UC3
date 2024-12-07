# Crie uma classe ItemEstoque com os seguintes atributos: nome, quantidade e preco_unitario.
# Adicione os métodos:
# adicionar_estoque(quantidade) para aumentar o estoque.
# remover_estoque(quantidade) para reduzir o estoque, verificando a quantidade disponível.
# calcular_valor_total() que retorna o valor total do estoque.

class ItemEstoque:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f'{quantidade} unidades de {self.nome} adicionadas ao estoque.')

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f'{quantidade} unidades de {self.nome} removidas ao estoque.')
        else:
            print(f'Estoque Esgotado')
        
    def calcular_valor_total(self):
        return self.quantidade * self.preco_unitario
    

item = ItemEstoque("Lápis", 50, 1.50)
item.adicionar_estoque(20)
item.remover_estoque(30)
print(f"Valor total do estoque: R${item.calcular_valor_total():.2f}")