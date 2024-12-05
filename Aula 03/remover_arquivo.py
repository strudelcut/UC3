# Exclusão de um arquivo

import os

if os.path.exists('produtos.txt'):
    os.remove('produtos.txt')
    print('Arquivo removido com sucesso!')
else:
    print('Arquivo não encontrado!')