"""DESAFIO 96"""
# def area(a, b):
#     s = a * b
#     print(f'A area de um terreno {a}X{b} é {s}m²')
#
#
# a = float(input('digite a largura (m)'))
# b = float(input('digite o comprimento (m)'))
# area(a,b)


"""DESAFIO 97"""
# def escreve(a):
#     print('~' * len(a))
#     print(a)
#     print('~' * len(a))
#
# escreve('Ola, Mundo!')

"""DESAFIO 98"""
# from time import sleep
#
#
# def contador(i, f, p):
#     if i < f:
#         if p > 0:
#             for n in range(f):
#                 sleep(.2)
#                 print(i, end=" ")
#                 i += p
#                 if i > f:
#                     break
#             print('FIM')
#         if p == 0:
#             if i == 0 or i > 0 or i < 0:
#                 p = 1
#                 for n in range(f + f + 1):
#                     sleep(0.2)
#                     print(i, end=" ")
#                     i += p
#                     if i > f:
#                         break
#                 print('FIM')
#         elif p < 0:
#             if i == 0 or i > 0:
#                 for n in range(f + 1):
#                     sleep(0.3)
#                     print(i, end=" ")
#                     i += p
#                     if i > f:
#                         break
#                 print()
#             print('FIM')
#     elif i > f:
#         if p > 0:
#             for n in range(i):
#                 sleep(0.2)
#                 print(i, end=" ")
#                 i -= p
#                 if i < f:
#                     break
#             print('FIM')
#         if p == 0:
#             if f == 0 or f > 0 or f < 0:
#                 p = 1
#                 for n in range(i + i + 1):
#                     sleep(0.2)
#                     print(i, end=" ")
#                     i -= p
#                     if i < f:
#                         break
#                 print('FIM')
#         elif p < 0:
#             if f == 0 or f > 0:
#                 p *= -1
#                 for n in range(i + 1):
#                     sleep(0.2)
#                     print(i, end=" ")
#                     i -= p
#                     if i < f:
#                         break
#                 print('FIM')
#
#
# contador(1, 10, 1)
# print()
# contador(10, 0, 2)
# print()
# i = int(input('inicio: '))
# f = int(input('fim: '))
# p = int(input('passo: '))
# print()
# contador(i, f, p)

"""DESAFIO 99"""
# from time import sleep
#
# def maior(*num):
#     mx = 0
#     if num:
#         print(f'foi digitado {num} com {len(num)} numeros')
#         print(f'{max(num)} foi o maior')
#     else:
#         print(f'não foi digitado nenhum numero. Maior é 0')
#
#
# maior(1, 2, 5, 6)
# maior(1, 2, 0)
# maior()

"""DESAFIO 100"""
# from random import randint
# from time import sleep
#
# def sorteia():
#     for i in range(5):
#         n = randint(0, 9)
#         num.append(n)
#         print(n, end=" ")
#         sleep(0.5)
#
# def somaPar(a):
#     soma = 0
#     for i in range(len(num)):
#         if num[i] % 2 == 0:
#             soma += num[i]
#     print(soma)
#
#
# num = []
# sorteia()
# print()
# somaPar(num)
