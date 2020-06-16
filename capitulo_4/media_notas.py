# Arquivo: media_notas.py (UTF-8)
# Descrição: Programa para ler 4 notas e mostras a média. Exercício 4.5.3
# Autor: Pinheiro Jr.
# Data: 16/06/2020

nota_1 = int(input('\nInforme a 1ª nota: '))
nota_2 = int(input('Informe a 2ª nota: '))
nota_3 = int(input('Informe a 3ª nota: '))
nota_4 = int(input('Informe a 4ª nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print('\nNota 1: ', nota_1)
print('Nota 2: ', nota_2)
print('Nota 3: ', nota_3)
print('Nota 4: ', nota_4)

print('\nMédia: {:.2f}\n'.format(media))