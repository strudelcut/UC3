# Crie uma classe Estudante com atributos nome e notas (uma lista de notas). Adicione métodos para:
# Calcular a média das notas.
# Exibir uma mensagem dizendo se o estudante foi aprovado (média >= 6) ou reprovado.

class Estudante:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
   
    def calcular_media(self):
        return sum(self.notas)/len(self.notas)
   
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            print(f"{self.nome} aprovado com média {media:.2f}")
        else:
            print(f"{self.nome} reprovado com média {media:.2f}")
   
#Exemplo de uso
lista_nota = []
nome = input("Informe o nome: ")
for x in range(4):
    nota = int(input("Informe a nota: "))
    lista_nota.append(nota)


estudante = Estudante(nome,lista_nota)
estudante.verificar_aprovacao()  