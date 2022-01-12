"""DESAFIO 46
from time import sleep
n = int(input('digite o numero para contagem regressiva '))
for n in range(n, 0, -1):
    c = n-1
    print(n)
    sleep(1)
print('FIM')
"""
"""DESAFIO 47
p = 1
print(f'os numeros pares entre 1 e 50 são: ')
for p in range(1, 51):
    if p % 2 == 0:
        print(p)
print('FIM')
"""
"""DESAFIO 48
s = 0
n = 0
cont = 0
print('somatoria entre os numeros impares 1 a 500:')
for n in range(1, 501,2):
   # print(n, end=" ")
    if n % 3 == 0:
        cont = cont + 1
        s += n
        print(n)
print(f'somatoria de {cont} numeros impares foi {s}')
"""
"""DESAFIO 49
num = int(input("Qual o seu numero "))
for i in range(11):
    calc = i * num
    print(num, "*", i, ": ", calc)
"""
"""DESAFIO 50
s= 0
for n in range(1, 7):
    n= int(input('digite o numero '))
    if n % 2 == 0:
        s += n
print(f'somatoria pares foi {s}')
"""
"""DESAFIO 51"""
"""Usuario
a1 = int(input('digite o primeiro termo '))
r = int(input('digite o numero da razao '))
s = a1 + r
a2 = 0
print(f'{a1}+{r}={s}')
for n in range(0, 10):
    a2 = s
    s += r
    print(s)
"""
"""Guanabara
a1 = int(input('digite o primeiro termo '))
r = int(input('digite o numero da razao '))
decimo = a1 + (10) * r
for n in range(a1, decimo, r):
    print(n, end=" → ")
print('FIM')
"""
"""DESAFIO 52
n = int(input('verificador de num primos '))
if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
    print('é primo')
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n == 1:
    print('numero não é primo')
else:
    print('e primo')
"""
"""DESAFIO 53
n = str(input('digite sua frase: ')).strip().lower().replace(" ", "")
l = [n]
if n == n[::-1]:
    print('e um palindromo')
else:
    print('nao e um palindromo')
"""
"""DESAFIO 54
from datetime import date
s=0
for n in range(0, 7):
    p = int(input('digite o ano de nascimento '))
    c = date.today().year - p
    if c >= 21:
        print('já é de maioridade')
        s = n
    else:
        print(f'ainda não é de maior, falta {(c - 21) * -1} ano(s)')
print(f'somatoria foi {s+1}')
"""
"""DESAFIO 55 SOLUÇÃO COM ERRO
for n in range(0, 5):
    p = (input('digite o peso '))
    l = [p]
    max_number = max(l)
    min_number = min(l)
print(f'o numero maior e {max_number}')
print(f'o numero menor e {min_number}')"""
"""CERTO
lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input(f'Peso da {c}ª pessoa: '))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista
"""
"""DESAFIO 56"""
media = 0
cont = 0
teste = 0
lista = []
velho = 0
nomevelho = ''
for i in range(1, 5):
    nome = str(input('digite seu nome '))
    idade = int(input('digite sua idade '))
    sexo = str(input('digite M ou F para o sexo ')).strip().lower()
    media = ((idade * i) / 4)
    lista += nome
    if sexo == 'f' and idade <20:
        cont += 1
        print(cont)
    if i == 1 and sexo == 'm':
        velho = idade
        nomevelho = nome
    if sexo == 'm' and idade > velho:
        velho = idade
        nomevelho = nome
print(f'media de idade e {media}')
print(f'o homem mais velho é: {nomevelho} com {velho} anos')
print(f'existe {cont} mulher abaixo de 20 anos ')
