"""DESAFIO 72"""
""" 
numE = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opc = ''
while True:
    c = int(input('digite um numero de 0 a 20 '))
    while c < 0 or c > 20:
        print('erro')
        c = int(input('digite um numero de 0 a 20 '))
    print(numE[c])
    opc = str(input('Quer continuar? S/N ')).upper().strip()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if opc == 'N':
        break
"""
"""DESAFIO 73"""
"""
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians', 'Fortaleza', 'Internacional', 'Fluminense',
         'América-MG', 'Ceará', 'Santos', 'Cuiabá', 'Athletico-PR', 'São Paulo', 'Juventude', 'Atlético-GO', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print(f'lista de Times: {times}')
print('-=' * 25)
print(f'5 primeiros: {times[:5]}')
print('-=' * 25)
print(f'4 últimos: {times[-4:]} ')
print('-=' * 25)
print(f'Times Ordem Alfabetica: {sorted(times)}')
print('-=' * 25)
c = times.index('Chapecoense')
print(f'Chapecoense está na {c+1} posição')
"""
"""DESAFIO 74"""
"""from random import randint
t = tuple(randint(i + 0, 9) for i in range(4))
print(t)
print(f'o menor foi {min(t)}')
print(f'o maior foi {max(t)}')
"""
"""DESAFIO 75"""
"""t = tuple()
p = []
n = nv = ctd = 0
while ctd <4:
    n = (int((input('digite um valor'))))
    if n %2 ==0:
        p += [n]
        nv +=1
    t = list(t)
    t.insert(ctd, n)
    ctd +=1
print(f'Vc digitou os valores {tuple(t)}')
print(f'o valor 9 apareceu {t.count(9)} vezes')
if t.count(3):
    print(f'O valor 3 apareceu na {t.index(3)+1}ª posição')
else:
    print('O valor 3, nao está em nenhuma posição')
print(f'Os valores pares digitados foram {nv} numeros: {p}')
"""
"""DESAFIO 76
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<20}", f" R$ {produtos[c+1]:>2.2f}")
"""
"""DESAFIO 77"""

"""palavras = (
    'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
    'progrmador', 'futuro')
for i in palavras:
    print(f'\na palavra {i.upper()} tem as vogais: ',end='')
    for v in i:
        if v.lower() in 'aeiou':
            print(v, end=' ')
"""