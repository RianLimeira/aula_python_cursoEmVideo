"""
nome = str(input('Seu nome '))
if nome == 'Rian':
    print('Nome maravilhoso')
print(f'Bom dia, {nome}')
"""
"""DESAFIO 28
import random
num = random.randint(0, 5)
u = int(input('digite seu numero de 0 a 5 '))
if u == num:
    print(f'vc acertou, era o num {u}')
else:
    print(f'infelizmente errou, tente novamente\no numero era {num}')
"""
"""DESAFIO 29
num = int(input('digite os KM/h'))
if num <=80:
    print('vc esta dentro da norma')
else:
    print(f'a multa sera de {(num-80)*7}')
"""
"""DESAFIO 30
num = int(input('digite um numero '))
if num % 2 == 0:
    print('numero par')
else:
    print('numero impar')
"""
"""DESAFIO 31
num = int(input('digite qts KM/h'))
if num <=200:
    print(f'a viagem ficara R${num*0.50}')
else:
    print(f'a viagem ficara em R${num*0.45}')
"""
"""DESAFIO 32
from datetime import date
n = int(input('digite o ano OU 0 para verificar o ano atual'))
if n ==0:
    n = date.today().year
if n % 4 == 0 or n % 400 == 0 and n % 100 != 0:
    print(f'{n} é ano bissexto')
else:
    print(f'{n} nao é bissexto')
"""
"""DESAFIO 33
n1 = int(input('digite o prim num '))
n2 = int(input('digite o seg num '))
n3 = int(input('digite o ter num '))
c = [n1, n2, n3]
print(c)
if n1 < n2 and n1 < n3:
    print(f'o valor {n1} e o menor numero')
elif n2 < n1 and n2 < n3:
    print(f'o valor {n2} e o menor numero')
else:
    print(f'o valor {n3} e o menor numero')
#menores numeros acima, maiores abaixo
if n1 > n2 and n1 > n3:
    print(f'o valor {n1} e o maior numero')
elif n2 > n1 and n2 > n3:
    print(f'o valor {n2} e o maior numero')
else:
    print(f'o valor {n3} e o maior numero')
"""
"""DESAFIO 34
s = float(input('digite seu salario '))
if s > 1250:
    print(f'o novo salario com 10% e de {s + (s * 10/100)}')
else:
    print(f'o novo salario com 15% e de {s + (s * 15/100)}')
"""
"""DESAFIO 35
n1 = int(input('digite o prim num '))
n2 = int(input('digite o seg num '))
n3 = int(input('digite o ter num '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('e possivel formar um triangulo')
else:
    print('nao é possivel formar um triangulo')
"""
