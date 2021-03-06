# Arquivo: lista.py (UTF-8)
# Descrição: Programa usando lista. Exercício 4.5.1
# Autor: Pinheiro Jr.
# Data: 16/06/2020

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# Imprime maior e menor elemento
print('Maior elemento: ', max(lista))
print('Menor elemento: ', min(lista))

# Imprime números pares
print('Números pares: ', end='')
for numero in lista:
    if numero % 2 == 0:
        print('{}; '.format(numero), end='')

# Imprime o número de ocorrências do 1º elemento da lista
elemento_1 = lista[0]
print('\nOcorrências do 1º elemento: ', lista.count(elemento_1))

# Imprime a média dos elementos
media = sum(lista) / len(lista)
print('Média dos elementos: {:.2f}'.format(media))

# Imprime a soma dos valores negativos
soma_negativos = 0.0
for numero in lista:
    if numero < 0:
        soma_negativos += numero
print('Soma de elementos negativos: {:.2f}'.format(soma_negativos))