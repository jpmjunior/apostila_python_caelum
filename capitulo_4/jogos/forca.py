# Arquivo: forca.py (UTF-8)
# Descrição: Jogo da forca
# Autor: Pinheiro Jr.
# Data: 15/06/2020

print('\n*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = 'banana'
letras_acertadas = ['_','_','_','_','_','_']

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while not acertou and not enforcou:
    chute = input('Qual letra? ')

    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
        acertou = '_' not in letras_acertadas
    else:
        erros += 1
        enforcou = erros >= 6
    
    print('Letras acertadas: ', letras_acertadas)