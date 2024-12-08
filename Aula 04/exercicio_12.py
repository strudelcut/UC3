# Crie uma classe Produto com os atributos nome, codigo e preco.
# Adicione um método especial __str__ para exibir os detalhes do produto e um método para aplicar desconto (aplicar_desconto(percentual)).

class Produto:
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco

    def __str__(self):
        return f'Produto: {self.nome}, código: {self.codigo}, preço R${self.preco}'
    
    def aplicar_desconto(self, percentual):
        self.preco = self.preco - self.preco * (percentual/100)

produto = Produto('Arroz', 101010, 20.00)
print(produto)
produto.aplicar_desconto(10)
print(produto)