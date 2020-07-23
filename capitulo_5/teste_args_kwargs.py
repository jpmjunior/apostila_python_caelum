# Arquivo: teste_args_kwargs.py (UTF-8)
# Descrição: Funções com número variável de parâmetros. Exercício 5.8.2
# Autor: Pinheiro Jr.
# Data: 23/07/2020

def teste_args_kwargs (arg1, arg2, arg3):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)

args = ('um', 2, 3)
teste_args_kwargs(*args)