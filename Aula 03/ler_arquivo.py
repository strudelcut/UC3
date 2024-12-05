# Lendo o counteúdo do arquivo.

with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print('Conteúdo do arquivo')
    print(conteudo)