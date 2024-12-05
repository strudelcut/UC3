# Leia o conteúdo do arquivo produtos.txt e exiba no console.

with open('produtos.txt', 'r') as arquivo:
    leia = arquivo.read()
    print(leia)