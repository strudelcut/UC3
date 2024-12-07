# Crie uma classe Livro com atributos titulo e autor. Sobrescreva o método especial __str__ para que, ao usar print em um objeto da classe, ele exiba o título e o autor do livro no 
# formato: "Título: <titulo>, Autor: <autor>"

class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self) -> str:
        return f'\nTítulo: {self.titulo}, Autor: {self.autor}\n'
    
livro = Livro('Dom Casmurro', 'Machado de Assim')

print(livro)