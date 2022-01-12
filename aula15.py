"""n = s = 0
while True:
    n = int(input('num '))
    if n == 999:
        break
    s+=n
print(f'soma {s}')
"""
"""DESAFIO 66
n = c = s = 0
while True:
    n = int(input('digite um valor'))
    if n == 999:
        break
    s += n
    c += 1
print(f'a soma de {c} numeros foi: {s}')
"""
"""DESAFIO 67
while True:
    n = int(input('digite um numero'))
    if n <0:
        break
    for i in range(11):
        cal = i * n
        print(f'{i} x {n} = {cal}')
print('FIM')
"""
"""Versão propria desafio 68"""
"""import random

pc = random.randint(1, 2)
g = e = p = 0
print('''[1]Par
[2]Impar''')

while True:
    jg = int(input('Digite uma opção'))
    if jg == 1 and pc == 1:
        print('os dois colocou par')
        e += 1
    elif jg == 2 and pc == 2:
        print('os dois colocou impar')
        e += 1
    elif (jg == 2 and pc == 1) or (jg == 1 and pc == 2):
        print('voce perdeu')
        p +=1
        break
    elif jg > 2 or jg < 1:
        print('Opção Incorreta')
print(f'voce empatou: {e}')"""
"""DESAFIO 68"""
"""import random
g  = 0
pc = random.randint(0, 10)
while True:
    n = int(input('digite um numero '))
    soma = n + pc
    compa = str(input('Digite Par ou Impar ')).strip().lower()[0]
    if compa == 'p' and soma % 2 == 0:
        print('voce ganhou')
        g += 1
    elif compa == 'i' and soma % 2 == 1:
        print('voce ganhou')
        g += 1
    elif compa != 'i' and compa != 'p':
        print('opcao errada')
    else:
        print('voce perdeu')
        break
print(f'voce ganhou {g} vezes')
"""
"""DESAFIO 69"""
"""
h = m = t = 0
while True:
    print('-' * 25)
    print('  CADASTRE UMA PESSOA ')
    print('-' * 25)
    i = int(input('idade: '))
    s = str(input('[M/F] ')).strip().lower()[0]
    while s != 'm' and s != 'f':
        s = str(input('[M/F] ')).strip().lower()[0]
    if s == 'f' and i < 20:
        m += 1
    if i > 18:
        t += 1
    if s == 'm':
        h += 1
    c = str(input('Deseja continuar ? [S/N] ')).strip().lower()[0]
    while c != 's' and c != 'n':
        c = str(input('Deseja continuar ? [S/N] ')).strip().lower()[0]
    if c == 'n':
        break
print('FIM DO PROGRAMA')
print(f'total com +18: {t}')
print(f'total homens: {h}')
print(f'total mulher <20: {m}')
"""
"""DESAFIO 70"""
""" 
l1 = []
nomebarato = ''
g = p = m = ctd = 0
while True:
    pr = str(input('digite o nome do produto: ')).strip().lower()
    v = float(input('digite o valor: '))
    ctd += 1
    l1 += [v]
    if ctd == 1 or v < m:
        m = v
        nomebarato = pr
    c = str(input('Deseja continuar ? [S/N] ')).strip().lower()[0]

    while c != 's' and c != 'n':
        c = str(input('Deseja continuar ? [S/N] ')).strip().lower()[0]
    if v > 0:
        g += v
    if v > 1000:
        p += 1
    if c == 'n':
        break
print(f'total gasto: {g}')
print(f'{p} produtos custam mais de R$1000,00')
print(f'{min(l1)} é {nomebarato} com valor mais barato')
"""
"""DESAFIO 71"""
"""
nota100 = nota20 = nota50 = nota10 = nota5 = nota2 = resto = 0
sq = int(input('digite o valor a sacar R$'))
total = sq
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 5
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        else:
            print('valor impossivel de sacar')
            break
        totced = 0
        if total == 0:
            break"""
"""
while True:
    valor = int(input('Digite o valor do saque: '))
    if valor == 0:  # Para quando o valor é igual a 0
        break

    cem = int(valor // 100)  # Calcula notas de 100
    valor -= cem * 100

    cinquenta = int(valor // 50)  # Calcula notas de 50
    valor -= cinquenta * 50

    vinte = valor // 20  # Calcula notas de 20
    valor -= vinte * 20

    dez = valor // 10  # Calcula notas de 10
    valor -= dez * 10

    cinco = valor // 5  # Calcula notas de 5
    valor -= cinco * 5

    dois = int(valor // 2)  # Calcula notas de 2
    break
print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 20,00 = ', vinte)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  2,00 = ', dois)"""
"""print('Notas R$  1,00 = ', um)"""
"""total = int(input('digite um valor inteiro: '))
for i in (100, 50, 20, 10, 5, 2, 1):
    tced = 0
    while total >= i:
        total -= i
        tced += 1
    if tced != 0:
        print(f'Total de cédulas de R$ {i}: {tced}')"""