# Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa.

class Pessoa:
  def __init__(self, nome: str, idade: int):
      self.nome = nome
      self.idade = idade
  def exibir_informacoes(self):
     print(f'\nNome: {self.nome}\nIdade: {self.idade} anos\n')

nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))

pessoa = Pessoa(nome, idade)

pessoa.exibir_informacoes()