# Implemente uma classe chamada Produto com:
# Atributos: nome, preco e estoque.
# Um método chamado vender que reduz o estoque ao vender o produto, se houver unidades disponíveis.
# Um método chamado repor que aumenta o estoque ao receber novas unidades.

# class Produto:
#     def __init__(self, nome: str, preco: int, estoque: int = 0):
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque
    
#     def vender(self, unidades: int):
#         if self.estoque != 0:
#             self.estoque -= unidades
#             print(f'\nVendidos: {unidades} unidades\nEm estoque: {self.estoque} unidades.\n')
#         else:
#             print(f'\nEstoque esgotado!\n')
        
#     def repor(self, unidades):
#         self.estoque += unidades
#         print(f'\nEm estoque: {self.estoque}\n')


 
# prod = input('Nome do produto: ')
# preco = int(input('Preço do Produto: '))
# estoque = int(input('Unidades do produto: '))

# produto = Produto(prod, preco, estoque)

# opcao = int(input('Vender 1, Repor 2: '))

# if 1 == opcao:
#     unidades = int(input('Quantidade vendidas: '))
#     produto.vender(unidades)

# elif 2 == opcao:
#     unidades =  int(input('Quantidade adicionadas: '))
#     produto.repor(unidades)

# else:
#     pass

class Produto:
    def __init__(self,nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


    def vender(self, quantidade: int):
        if(quantidade <= self.estoque):
            self.estoque -= quantidade
            print(f"Vendido {quantidade} unidade(s)")
        else:
            print("Estoque insuficiente")
   
    def repor(self, quantidade: int):
        self.estoque += quantidade
        print(f"Adicionado {quantidade} unidade(s)")


#Exemplo de uso
produto = Produto("Caneta", 2.50, 100)
produto.vender(10)
produto.repor(20)
print(f"Estoque atual: {produto.estoque}")




