# Arquivo: programa.py (UTF-8)
# Descrição: Jogo da adivinhação
# Autor: Pinheiro Jr.
# Data: 14/06/2020

print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42

chute = int(input('Digite o seu número: '))
print('Você digitou: ', chute)

if(numero_secreto == chute):
    print('Você acertou!')
elif(chute > numero_secreto):
    print('Você errou! O seu chute foi maior que o número secreto')
elif(chute < numero_secreto):
    print('Você errou! O seu chute foi menor que o número secreto')