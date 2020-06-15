# Arquivo: programa.py (UTF-8)
# Descrição: Jogo da adivinhação
# Autor: Pinheiro Jr.
# Data: 14/06/2020

print('\n******************************')
print('*    Jogo da adivinhação     *')
print('******************************\n')

numero_secreto = 42
pontuacao = 1000
rodada = 1
nivel = input('Escolha um nível (1 = fácil, 2 = médio, 3 = difícil): ')

if nivel == '1':
    total_de_tentativas = 20
elif nivel == '2':
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print('\nTentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    
    if(acertou):
        print('Você acertou!')
        print('Pontuação: ', pontuacao)
        break
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto')
        pontuacao = pontuacao - abs(chute - numero_secreto)
    elif(menor):
        print('Você errou! O seu chute foi menor que o número secreto')
        pontuacao = pontuacao - abs(chute - numero_secreto)
    
print('\nFim do jogo\n')