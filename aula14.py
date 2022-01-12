""" DESAFIO 57
c = 's'
while c == 's':
    sexo = str(input('qual o seu sexo [M/F] ')).strip().lower()
    if sexo == 'm' or sexo == 'f':
        c = str(input('deseja continuar ? [S/N] ')).lower()
    elif sexo != 'm' or sexo != 'f':
        print(f'opção errada! {sexo}')
        print('digite novamente')
print('ACABOU')
"""
"""DESAFIO 58 
import random
from time import sleep
num = random.randint(0, 10)
jg = 0
opcao = 's'
while opcao == 's':
    print('-'*20)
    u = int(input('digite seu numero de 0 a 10 '))
    print('ANALIZANDO')
    sleep(1)
    if u == num:
        print(f'vc acertou, era o num {u}')
        opcao = 'n'
    else:
        if u < num:
            print(f'infelizmente errou, tente novamente')
            print('DICA: o numero é maior')
            jg += 1
            opcao = str(input('vc deseja continuar tentando [s/n] ')).strip().lower()
        elif u > num:
            print(f'infelizmente errou, tente novamente')
            print('DICA: o numero é menor')
            jg += 1
            opcao = str(input('vc deseja continuar tentando [s/n] ')).strip().lower()
print(f'vc tentou {jg} vezes para acertar')
"""
"""DESAFIO 59 
n = 0
n1 = int(input('digite o primeiro numero '))
n2 = int(input('digite o segundo numero '))
while n != 5:
    opc = int(input("[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair\n"))
    if opc == 1:
        s = n1 + n2
        print(f'a soma é {s}')
    elif opc == 2:
        s = n1 * n2
        print(f'a multiplicacao é {s}')
    elif opc == 3:
        if n1 > n2:
            print(f'o maior é {n1}')
        else:
            print(f'o maior é {n2}')
    elif opc == 4:
        print('digite os novos numeros:')
        n1 = int(input('digite o primeiro numero '))
        n2 = int(input('digite o segundo numero '))
    elif opc == 5:
        n=5
        print('FIM')
    else:
        print('OPÇÃO ERRADA, DIGITE NOVAMENTE\n')
"""
"""DESAFIO 60
n = int(input('digite um numero '))
nu = 0
f = 1
print(f'{n}! = ', end='')
while n > 1:
    print(f'{n}', end='')
    print(' x ' if n >2 else ' = ', end='')
    if n == 0:
        f = 1
    elif n == 1:
        f = 1
    else:
        f = f * n
        n -= 1
print(f'o fatorial é {f}')
"""
"""DESAFIO 61 com FOR
a1 = int(input('digite o primeiro termo '))
r = int(input('digite o numero da razao '))
decimo = a1 + (10) * r
for n in range(a1, decimo, r):
    print(n, end=" → ")
print('FIM')
"""
"""DESAFIO 61 com WHILE
a1 = int(input('digite o primeiro termo '))
r = int(input('digite o numero da razao '))
cont = 1
while cont <= 10:
    print(f'{a1}')
    a1+= r
    cont +=1
print('FIM')
"""
"""DESAFIO 62
from time import sleep
a1 = int(input('digite o primeiro termo '))
r = int(input('digite o numero da razao '))
cont = 1
termos = 0
c = int(input('digite a quantidade de termos para ver de inicio '))
while c != 0:
    termos += c
    while cont <= termos:
        print(f'{a1}')
        a1+= r
        cont +=1
    print('PAUSA')
    c = int(input('quantos termos quer ver a mais, OU 0 para parar'))
print(f'FIM com {termos} termos informados ')
"""
"""DESAFIO 63"""
"""COM LISTA
n= int(input("numero"))
lista=[1,1]
for i in range(n-2):
      lista.append(lista[-1]+lista[-2])
print(lista)
"""
"""Guanabara while
a1 = int(input('digite qts numero '))
t1 =0
t2 = 1
cont = 3
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= a1:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont+=1
print(' → FIM')
"""
"""DESAFIO 64
n = c = s = 0
while n != 999:
    n = int(input('digite um valor'))
    if n != 999:
        s += n
        c += 1
print(f'a soma de {c} numeros foi: {s}')
"""
"""DESAFIO 65
s = c = 0
maior = menor = 0
opcao = 's'
lst = []  # listalista vazia
while opcao == 's':
    n = float(input('Digite um numero'))
    opcao = str(input('vc deseja continuar [s/n] ')).strip().lower()
    lst += [n] #adiciona na lista os numeros
    s += n #faz a soma dos numeros
    c += 1 #contador

print(f'foi digitado {c} numeros e a media foi {s / c:.2f}')
print('O Maior numero foi:', max(lst))  # maximo valor da lista
print('O Menor numero foi:', min(lst))  # minimo valor da lista
"""