"""DESAFIO 101"""
# from datetime import date
#
#
# def voto():
#     global v
#     dt = date.today().year - v
#     print(f'com {dt} anos: ', end="")
#     if dt <16:
#         print('NÃO VOTA')
#     elif dt >=18 and dt <65:
#         print('VOTO OBRIGATORIO')
#     else:
#         print('VOTO OPCIONAL')
#
#
# v = int(input('digite o ano que nasceu'))
# voto()

"""DESAFIO 102"""

# def fatorial(n, show=False):
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(f'{c}', end=" ")
#             if c - 1 > 0:
#                 print('-', end=" ")
#             if c - 1 == 0:
#                 print('=', end=" ")
#         f *= c
#     print(f)
#     #     f *= c
#     # print(f)
#     return f
#
#
# fatorial(5, True)

"""DESAFIO 103"""

# def ficha(nome='', gols=0):
#     global nomes, gol
#     if nomes != '':
#         nome = nomes
#     if nomes == '':
#         nomes = "<DESCONHECIDO>"
#     if gols =='':
#         gol=0
#     return nome
#
#
# nomes = str(input('digite o Jogador:'))
# gol = (input('num de Gols: '))
# ficha(nome=nomes, gols=gol)
# print(f'O jogador {nomes} fez {gol} gols')

"""DESAFIO 104"""
## ERROO ###
# def leiaInt(a):
#     while True:
#         if a.isdecimal():
#             print('e numero')
#             break
#         else:
#                 print('não é um numero. Digite outra vez')
#                 n = input('digite um numero: ')
#                 if n.isdecimal():
#                     print('e numero')
#                     break
#
#
# n = input('digite um numero: ')
# leiaInt(n)

### CERTO ###
# def leiaInt(a):
#     n = input(a)
#     if n.isnumeric() == False:
#         while n.isnumeric() == False:
#             print('não é numero, digite outra vez ')
#             n = input(a)
#     if n.isnumeric():
#         print(f'é o numero {n}')
#     return n
#
#
# num = leiaInt('digite um valor')

"""DESAFIO 105"""
#
#
# def notas(*num, sit=False):
#     """
#
#     :param num: são todas as notas
#     :param sit: para mostrar a situação das médias
#     :return: retorna o dicionario com as informação
#     """
#     d = {}
#
#     d['total'] = len(num)
#     d['maior'] = max(num)
#     d['menor'] = min(num)
#     m = sum(num) / len(num)
#     d['media'] = m
#     if sit:
#         if m >= 7:
#             d['situacao'] = 'BOA'
#         else:
#             d['situacao'] = 'RUIM'
#     return d
#
#
# resp = notas(5.5, 9.5, 10, 6.5, sit=False)
# print(resp)


"""DESAFIO 106"""
# from termcolor import colored
#
#
# def ajuda(cm):
#     help(cm)
#
#
# def tl(msg, cor=0):
#     tm = len(msg) + 4
#     print('~' * tm)
#     print(msg)
#     print('~' * tm)
#
#
# cmd = ''
# while True:
#     tl(colored('  SISTEMA DE AJUDA', 'yellow'))
#     cmd = input('Função/Biblioteca ')
#     if cmd.lower() == 'fim':
#         break
#     else:
#         ajuda(colored(cmd, 'green'))
# tl(colored('  ATÉ LOGO', 'red'))
