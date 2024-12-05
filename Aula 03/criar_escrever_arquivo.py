# Criando, ou abrindo um arquivo para escrita.

with open('dados.txt', 'w') as arquivo:
    arquivo.write('Curso: Programação em Python\n')
    arquivo.write('Aluno: Maria\n')
    arquivo.write('Progresso: 85%\n')