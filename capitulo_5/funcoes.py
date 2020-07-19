# Arquivo: funcoes.py (UTF-8)
# Descrição: Prática de funções. Exercício 5.5.11
# Autor: Pinheiro Jr.
# Data: 18/07/2020

# Função: velocidade_media()
#   distancia: metros
#   tempo: segundos
def velocidade_media(distancia, tempo):
    return divisao(distancia,tempo)

def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def divisao(num1,num2):
    return num1/num2

def calculadora(num1, num2):
    return soma(num1,num2), subtracao(num1,num2), num1*num2, num1/num2

print(velocidade_media(100,20))
print(velocidade_media(-20,10))
print(velocidade_media(150,0))
