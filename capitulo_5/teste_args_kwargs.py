# Arquivo: teste_args_kwargs.py (UTF-8)
# Descrição: Funções com número variável de parâmetros. Exercício 5.8.3
# Autor: Pinheiro Jr.
# Data: 23/07/2020

def teste_args_kwargs (arg1, arg2, arg3):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)

kwargs = {'arg1': 'um', 'arg3': 3, 'arg2': 'dois'}
teste_args_kwargs(**kwargs)