# Arquivo: cadastro_de_usuarios.py (UTF-8)
# Descrição: Programa para cadastro de usuários usando dict_usuario. Exercício 4.5.5
# Autor: Pinheiro Jr.
# Data: 16/06/2020

dict_usuario = {}
lista_usuarios = []
resposta = 'S'

while resposta.upper() == 'S':
    dict_usuario['nome'] = input('\nInforme o nome: ')
    dict_usuario['idade'] = input('Informe a idade: ')
    dict_usuario['cidade'] = input('Informe a cidade: ')

    lista_usuarios.append(dict_usuario)

    resposta = input('\nDeseja cadastrar outro usuário? (s/n) ')

for dict_usuario in lista_usuarios:
    print()
    for key in dict_usuario.keys():
        print(key + ': ' + dict_usuario[key])

print()