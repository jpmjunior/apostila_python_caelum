# Arquivo: cadastro_de_usuarios.py (UTF-8)
# Descrição: Programa para cadastro de usuários usando dict_usuario. Exercício 4.5.4
# Autor: Pinheiro Jr.
# Data: 16/06/2020

dict_usuario = {}

dict_usuario['nome'] = input('Informe o nome: ')
dict_usuario['idade'] = input('Informe a idade: ')
dict_usuario['cidade'] = input('Informe a cidade: ')

for key in dict_usuario.keys():
    print(key + ': ' + dict_usuario[key])