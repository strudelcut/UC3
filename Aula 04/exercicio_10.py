# Crie uma classe Filme com os atributos titulo, genero e duracao (em minutos).
# Implemente um método especial para exibir os detalhes do filme de forma legível.

class Filme:
    def __init__(self, titulo, genero, duracao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao

    def __str__(self):
        return f'Título: {self.titulo}\nGenero: {self.genero}\nDuração: {self.duracao} minutos.'
    

filme = Filme('O Senhor dos Anéis: O Retorno do Rei.', 'Ação, Fantasia.', 201)
print(filme)