"""DESAFIO 36
v = float(input('digite o valor da casa '))
s = float(input('digite o salario '))
a = float(input('digite a qts parcela-ano '))
p = v / (a * 12)
c = (s * 30 / 100)
if p > c:
    print(f'Voce não pode ter o emprestimo, parcela de R${p:.2f} é superior a 30% do salario atual R${c:.2f}')
else:
    print(f'emprestimo de ate {c:.2f} aprovado')
    print(f'emprestimo para a simulacao da casa, o parcelamento sera R${p:.2f} e seu salario fica R${s-p:.2f} por mes')
"""
"""DESAFIO 37
#existe tbm a função bin(), oct() e hex()
n = str(input('digite um numero '))
print('=-=' * 15)
sel = int(input('selecione a base numerica:\n1 para binario\n2 para octal\n3 para hexadecimal\n'))
if sel == 1:
    print(int(n, 2))
elif sel == 2:
    print(int(n, 8))
else:
    print(int(n, 16))
"""
"""DESAFIO 38
n1 = int(input('digite o prim num '))
n2 = int(input('digite o seg num '))
c = [n1, n2]
print(c)
if n1 > n2:
    print(f'o primeiro valor: {n1} e o maior numero')
elif n2 > n1:
    print(f'o segundo valor: {n2} e o maior numero')
else:
    print('os numeros sao iguais')
"""
"""DESAFIO 39
from datetime import date
ano = int(input('digite o ano que nasceu '))
al = date.today().year
print(al)
calc = al - ano
if calc <18:
    print(f'ainda não deu o tempo, falta {(calc - 18)*(-1)}anos')
elif calc == 18:
    print('está na hora de se alistar')
else:
    print(f'ja passou do tempo, esta atrasado {calc - 18} anos')
"""
"""DESAFIO 40
n1 = float(input('digite o prim num '))
n2 = float(input('digite o seg num '))
media = (n1+n2) / 2
if media <5:
    print(f'reprovado')
elif media >= 5 and media <7:
    print(f'recuperacao')
else:
    print('aprovado')
"""
"""DESAFIO 41
from datetime import date
ano = int(input('digite o ano que nasceu '))
al = date.today().year
print(al)
calc = al - ano
if calc <=9:
    print('mirim')
elif calc <= 14 and calc > 9:
    print('infantil')
elif calc <= 19 and calc > 14:
    print('junior')
elif calc <= 20 and calc > 19:
    print('senior')
else:
    print('master')
"""
"""DESAFIO 42
n1 = int(input('digite o prim num '))
n2 = int(input('digite o seg num '))
n3 = int(input('digite o ter num '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('e possivel formar um triangulo')
    if n1 == n2 == n3:
        print('triangulo equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('triangulo isosceles')
    elif n1 != n2 != n3 != n1:
        print('triangulo escaleno')
else:
    print('nao é possivel formar um triangulo')
"""
"""DESAFIO 43
a = float(input('digite sua altura '))
kg = float(input('digite seu peso '))
imc = kg / (a * a)
print(f'o imc e de {imc}')
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')
"""
"""DESAFIO 44
v = float(input('digite o valor '))
cond = int(input('digite a forma de pagamento\n1- dinheiro/cheque/pix\n2- avista cart\n3- 2x cart\n4- 3x+ cart\n'))
if cond == 1:
    print(f'valor 10%: {v - (v * 10 / 100):.2f}')
elif cond == 2:
    print(f'valor 5%: {v - (v * 5 / 100):.2f}')
elif cond == 3:
    print(f'valor: {v:.2f}')
else:
    print(f'valor com taxa: {v + (v * 20 / 100):.2f}')
"""
"""DESAFIO 45
import random
t = 1
while t != 0:

    jg = ['pedra', 'papel', 'tesoura']
    p = str(input('digite sua jogada ')).strip().lower()
    pc = random.choice(jg)
    if (p == 'pedra' and pc == 'pedra') or (p == 'tesoura' and pc == 'tesoura') or (p == 'papel' and pc == 'papel'):
        print(f'\033[4:33:40mempate!!!\033[m ele colocou {pc} e vc {p}')
    elif (p == 'pedra' and pc == 'papel') or (p == 'tesoura' and pc == 'pedra') or (
            p == 'papel' and pc == 'tesoura'):
        print(f'\033[4:31:40mComputador ganhou!\033[m\n ele colocou {pc} e vc {p}')
    else:
        print(f'\033[4:32:40mvoce ganhou!!\033[m \n o computador colocou {pc}')
    print('\033[4:36mContinue Jogando!!\033[m')
"""