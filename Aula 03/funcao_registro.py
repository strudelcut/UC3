# Implemente funções que gerenciam um sistema de lista de alunos: Adicionar um aluno, Remover um aluno, Exibir todos os alunos.

def adicionar(nome):
    return lista.append(nome)

def remover(nome):
    return lista.remove(nome)

def exibir():
    for x in len(lista):
        print(lista[x])
        return
    
lista = []

while True:
    op = input('Operação: 1 - inserir / 2 - remover / 3 - listar / outro pra sair ')
    if '1' in op:
        adicionar(input('Informe o nome: '))
    elif '2' in op:
        remover(input('Informe o nome: '))
    elif '3' in op:
        exibir()
    else:
        break