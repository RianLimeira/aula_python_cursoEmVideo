"""t = []
d = []
m = []
mn = []
for c in range(0,3):
    d.append(input('nome: '))
    d.append(int(input('idade: ')))
    t.append(d[:])

print(t)
print(p)
print(f'foi inserida {len(d)}')
print(f'as mais velhas foi: {m[1]}')
print(f'as mais novas foi: {mn[1]}')"""
# ------------------------------------------
"""DESAFIO 84"""
# p = list()
# n = list()
# kg = list()
# opc = ''
# while True:
#     n.append(str(input('Digite seu nome: ')))
#     n.append(float(input('Digite eu peso: ')))
#     p.append(n[:])
#     kg.append(n[1])
#     n.clear()
#
#     opc = str(input('Deseja continuar S/N')).strip().lower()[0]
#     while opc != 's' and opc != 'n':
#         opc = str(input('Opção Errada. Deseja continuar S/N')).strip().lower()[0]
#     if opc == 'n':
#         break
# print(p)
# print(f'foi inserida {len(p)}')
# print(f'O maior peso foi de {max(kg):.2f}Kg. Peso de ', end='')
# for t in p:
#     if t[1] == max(kg):
#         print(f' {t[0]}. ', end='')
# print(f'\nO menor peso foi de {min(kg):.2f}Kg. Peso de ', end='')
# for t in p:
#     if t[1] == min(kg):
#         print(f' {t[0]} ', end='')

"""DESAFIO 85"""
"""
numeros = [[], []]
for c in range(0,7):
    nm = int(input(f'digite o {c+1}º numero'))
    if nm %2 ==0:
        numeros[0].append(nm)
    elif nm %2 == 1:
        numeros[1].append(nm)
print(sorted(numeros[0]))
print(sorted(numeros[1]))
"""
"""DESAFIO 86"""
"""
n = [[], [], []]
for c in range(3):
    for j in range(3):
        n[c].append(int(input(f'digite o valor[{c}] [{j}]')))
for c in range(3):
    for j in range(3):
        print(f'({n[c][j]:^5}) ', end="")
    print()
"""
"""DESAFIO 87"""
"""
n = [[], [], []]
np = []
for c in range(3):
    for j in range(3):
        num = int(input(f'Digite um numero [{c}, {j}]: '))
        n[c].append(num)
        if num %2 == 0:
            np.append(num)
print('=-' * 25)
for c in range(3):
    for j in range(3):
        print(f'({n[c][j]:^5}) ', end="")
    print()
print('=-' * 25)
print(f'a soma da terceira coluna é {(n[0][2] + n[1][2] + n[2][2])}')
print(f'maior da segunda linha {max(n[1])}')
print(f'soma dos pares {sum(np)}')
"""
"""DESAFIO 88"""
# l = []
# from random import randint
# import time
# n = int(input('digite a quantidade de jogos '))
# for i in range(n):
#     aleatorio = [randint(i + 1, 60) for i in range(6)]
#     if aleatorio not in l:
#         print(f'jogo {i+1}: {sorted(aleatorio)}')
#         time.sleep(1)

"""DESAFIO 89"""
# lista = []
# cont = 0
# while True:
#     lista.append([])
#     lista[cont].append(str(input('Digite o nome do aluno: ')))
#     lista[cont].append(float(input('Digite a primeira nota: ')))
#     lista[cont].append(float(input('Digite a segunda nota: ')))
#     # Vou colocar a media na 4 posição (3)
#     media = (lista[cont][1] + lista[cont][2]) / 2
#     lista[cont].append(media)
#     parar = str(input('Deseja continuar? [S/N] '))
#     if parar in 'Nn':
#         break
#     cont += 1
#
# print('x+'*30)
# print('Nº Nome          Média')
# print('-'*25)
# for pos, alun in enumerate(lista):
#     print(pos, f'{alun[0]:<15}', alun[3])
#
# while True:
#     print('-'*25)
#     aluno = int(input('Deseja ver a nota de qual aluno? (999 para parar) '))
#     if aluno == 999:
#         break
#     else:
#         print(f'As notas de {lista[aluno][0]} são {lista[aluno][1:3]}')
# print('Programa Finalizado\nVolte sempre! :D')

"""GUANABARA"""
ficha = []
while True:
    nome = input('nome: ')
    nota1 = float(input('n1: '))
    nota2 = float(input('n2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opc = str(input('deseja continuar? S/N')).strip().lower()[0]
    while opc not in 'sn':
        opc = str(input('deseja continuar? S/N')).strip().lower()[0]
    if opc == 'n':
        break
print(f'{"Nº:":<4}{"NOME:":<10}{"MEDIA:":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    nota = int(input('Qual aluno deseja ver? (999 para):'))
    if nota == 999:
        break
    if nota <= len(ficha) -1:
        print(f'Nota de {ficha[nota][0]} é {ficha[nota][1]}')
