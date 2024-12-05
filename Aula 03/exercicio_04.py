# Calcule o preço médio dos produtos no arquivo.

with open('produtos.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    precos = [int(linha.split(',') [1]) for linha in conteudo]
    print(precos)    
    media = sum(precos) / len(precos)
    print(f'Média dos preços R${media:.2f}, fazueli!!!')