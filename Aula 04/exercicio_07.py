# Crie uma classe Tarefa com os atributos descricao e status (inicialmente "pendente").
# Adicione métodos para:
# Alterar o status para "concluída" (marcar_como_concluida).
# Exibir os detalhes da tarefa (exibir_tarefa).

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.status = 'Pendente'

    def marcar_concluida(self):
        self.status = 'Concluída'

    def exibir_tarefa(self):
        print(f'\nTarefa: {self.descricao}, Status: {self.status}\n')

tarefa = Tarefa('Estudar Python')
tarefa.exibir_tarefa()
tarefa.marcar_concluida()
tarefa.exibir_tarefa()