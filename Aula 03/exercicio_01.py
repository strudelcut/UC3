# Exercício 1: Escreva um arquivo chamado produtos.txt com os seguintes dados:
# Arroz,20
# Feijão,15
# Açúcar,10


with open('produtos.txt', 'w') as arquivo:
    arquivo.write('Arroz, 20\n')
    arquivo.write('Feijão, 15\n')
    arquivo.write('Açúcar, 10\n')