"""DESAFIO 78"""
"""n = []
for c in range(0,5):
    n.append(int(input(f'digite o {c+1}º numero ')))
print(f'o maior foi {max(n)} na posicao ', end='')
for i, v in enumerate(n):
    if v == max(n):
        print(f'{i} - ', end='')
print()
print(f'o menor foi {min(n)} na posicao ', end='')
for i, v in enumerate(n):
    if v == min(n):
        print(f'{i} - ', end='')
print()
"""
"""DESAFIO 79
v = []
valor = []
c=1
opc = ''
while True:
    n = int(input(f'digite o {c}º valor '))
    c+=1
    if n not in v:
        print('Valor Adicionado')
        valor.append(n)
    else:
        print('Valor Duplicado')
    v += [n]
    opc = str(input('Quer continuar? S/N ')).upper().strip()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if opc == 'N':
        break
print(f'os valores digitados foram {sorted(valor)}')
"""
"""DESAFIO 80
l = []
for c in range(0,5):
    n = int(input('digite um valor: '))
    if c == 0 or n > max(l):
        l.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        for nu, ct in enumerate(l):
            if n <=ct:
                l.insert(nu, n)
                print(f'Valor adicionado na posição {nu} da lista...')
                break
print(f' a order e: {l}')
"""
"""DESAFIO 81
l = []
while True:
    n = int(input('digite um numero'))
    l +=[n]
    opc = str(input('Deseja Continuar? S/N: ')).strip().lower()[0]
    while opc not in 'sn':
        opc = str(input('Quer continuar? S/N ')).lower().strip()[0]
    if opc == 'n':
        break
print(f'foi digitado {len(l)} numeros ')
l.sort(reverse=True)
print(l)
if l.count(5):
    print(f'o numero 5 foi digitado na posicao {l.index(5)}')
else:
    print('o numero 5 não foi digitado')
"""
"""DESAFIO 82
l = []
p = []
i = []
while True:
    n = int(input('digite um numero'))
    l +=[n]
    if n %2 ==0:
        p +=[n]
    elif n %2 ==1:
        i += [n]
    opc = str(input('Deseja Continuar? S/N: ')).strip().lower()[0]
    while opc not in 'sn':
        opc = str(input('Quer continuar? S/N ')).lower().strip()[0]
    if opc == 'n':
        break
print(l)
if p == []:
    print('não digitou numeros pares')
else:
    print(p)
if i == []:
    print('não digitou numeros pares')
else:
    print(i)
"""
"""DESAFIO 83"""
""" """
# l = []
# exp = str(input('digite a sua expressao: ')).strip()
# for sib in exp:
#     if sib == '(':
#         l.append('(')
#     elif sib == ')':
#         if len(l) > 0:
#             l.pop()
#         else:
#             l.append(')')
#             break
# if len(l) == 0:
#     print('valido')
# else:
#     print('invalido')
