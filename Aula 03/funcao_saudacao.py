# Crie uma função cumprimentar que receba o nome e a hora do dia, e retorne uma mensagem personalizada. Bom dia, Boa tarde ou Boa noite.

def cumprimentar(nome, hora):
    if hora < 12:
        return f'Bom dia, {nome}!'
    elif hora < 18:
        return f'Boa tarde, {nome}!'
    else:
        return f'Boa noite, {nome}!'
    
name = input('Digite um nome: ')
time = int(input('Digite a hora: '))
saudacao = cumprimentar(name, time)

print(saudacao)