"""frase = 'Curso em Vídeo Python'
print(len(frase))
"""
"""Desafio 22 C
n = str(input('digite seu nome ')).strip()
print(n.upper())
print(n.lower())
print(len(n))
print(len(n.replace(" ", "")))
d = n.split()
print(len(d[0]))
"""
"""Desafio 23 X"""
"""Errado n = str(input('digite num '))
d = n.split()
print(d[0])"""

"""Modo Certo
num = int(input('digite num de 0 até 9999:\n '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Numero {num} possui: ')
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')
"""

"""DESAFIO 24 C
nome = str(input('digite o nome da cdd ')).strip()
q = nome.split()
if q[0].capitalize() == 'Santo':
    print('ele comeca')
else:
    print('não comeca')
"""
"""DESAFIO 25 C
nome = str(input('digite seu nome ')).strip()
divisao = nome.title().split()
if 'Silva' in divisao:
    print('voce tem Silva no seu nome')
else:
    print('voce nao tem SILVA no seu sobrenome')
"""
"""DESAFIO 26 C
l = str(input('digite uma frase ')).strip().lower()
cont = l.count('a')
print(cont)
print(l.find('a')+1)
print(l.rfind('a')+1)
"""
"""DESAFIO 27 C
nome = str(input('digite seu nome ')).strip()
d = nome.split()
print(f'primeiro nome {d[0]} e ultimo nome {d[-1]}')
"""
#find procura a posicao, in se é vdd ou falso se tem algo