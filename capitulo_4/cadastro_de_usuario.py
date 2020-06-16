# Arquivo: cadastro_de_usuario.py (UTF-8)
# Descrição: Programa Cadastro de Usuário. Exercício 4.5.2
# Autor: Pinheiro Jr.
# Data: 16/06/2020

lista = []

nome = input('\nInforme o nome: ')
sobrenome = input('Informe o sobrenome: ')
idade = input('Informe a idade: ')

lista.append(nome)
lista.append(sobrenome)
lista.append(idade)

print('\nDados cadastrados: {}\n'.format(lista))
