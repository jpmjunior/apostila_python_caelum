# Arquivo: funcoes.py (UTF-8)
# Descrição: Prática de funções. Exercício 5.5.10
# Autor: Pinheiro Jr.
# Data: 18/07/2020

# Função: velocidade_media()
#   distancia: metros
#   tempo: segundos
def velocidade_media(distancia, tempo):
    return distancia/tempo

def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def calculadora(num1, num2):
    return soma(num1,num2), subtracao(num1,num2), num1*num2, num1/num2

print(calculadora(10,3))
print(calculadora(2,6))
print(calculadora(3,4.2))