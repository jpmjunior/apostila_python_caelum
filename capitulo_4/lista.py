# Arquivo: lista.py (UTF-8)
# Descrição: Programa usando lista. Exercício 4.5.1
# Autor: Pinheiro Jr.
# Data: 16/06/2020

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print('Maior elemento: ', max(lista))
print('Menor elemento: ', min(lista))

print('Números pares: ', end='')
for numero in lista:
    if numero % 2 == 0:
        print('{}; '.format(numero), end='')

elemento_1 = lista[0]
print('\nOcorrências do 1º elemento: ', lista.count(elemento_1))