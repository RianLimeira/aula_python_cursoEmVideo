# pessoas = {'nome': 'Rian', 'sexo': 'M', 'idade': 20}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# # itens é tudo, keys é os atributos e values é os valores
"""DESAFIO 90"""
# aluno = {}
# aluno['n'] = str(input('digite o nome '))
# aluno['m'] = float(input('digite a media'))
# if aluno['m'] >=7:
#     aluno['situacao'] = 'aprovado'
#     print('aprovado')
# else:
#     aluno['situacao'] = 'reprovado'
#     print('reprovado')
# print(aluno)

import operator
"""DESAFIO 91"""
# from random import randint
# import time
# l = []
# jg = {}
# dado = []
# for j in range(0, 4):
#     n = randint(1, 6)
#     print(f'O jogador{j}: {n}')
#     time.sleep(0)
#     l.append(n)
#     jg['jg'] = l
#
# print(f'{sorted(l)}')
# print('/*-' * 10)
# print(jg)
"""----EX91----"""
# from random import randint
# import time
# import operator
# dado = []
# l = []
# jg = {'jogador1': randint(1, 6),
#       'jogador2': randint(1, 6),
#       'jogador3': randint(1, 6),
#       'jogador4': randint(1, 6),}
# rank = sorted(jg.items(), key=operator.itemgetter(1), reverse=True)
# for k, v in jg.items():
#     print(f'{k} = {v}')
# print('-*'*30)
# for i in range(4):
#     print(f'{i+1} lugar: {rank[i]}')
#     time.sleep(1)

"""DESAFIO 92"""
# import datetime
# d = {}
# d['nome'] = str(input('digite seu nome '))
# d['nascimento'] = int(input('digite ano-nascimento '))
# d['ctps'] = int(input('digite o numero da sua carteira (0 se não tiver) '))
# while d['ctps'] <0:
#     print('digite um valor acima de 0')
#     d['ctps'] = int(input('digite o numero da sua carteira (0 se não tiver) '))
# if d['ctps'] == 0:
#     print(d)
#     print('-*-' * 30)
#     print(f'Seu nome {d["nome"]}')
#     ano = datetime.date.today()
#     print(f'idade {ano.year - d["nascimento"]} anos')
#     print(f'ctps {d["ctps"]}')
# else:
#     d['contrato'] = int(input('ano-contratado '))
#     d['salario'] = float(input('salario '))
#     print(d)
#     print('-*-' * 30)
#     print(f'Seu nome {d["nome"]}')
#     ano = datetime.date.today()
#     print(f'idade {ano.year - d["nascimento"]} anos')
#     print(f'ctps {d["ctps"]}')
#     print(f'contatado em {d["contrato"]}')
#     print(f'salario: {d["salario"]:.1f}')
#     aposentadoria = datetime.date.today()
#     if ((aposentadoria.year) - (d["contrato"] + 35)) * -1 <=0:
#         print('ja pode se aposentar, vc fez 35 anos de contribuição ')
#     else:
#         print(f'falta {((aposentadoria.year) - (d["contrato"] + 35)) * -1} - para 35 anos')
#         print(f'sua idade {(((aposentadoria.year) - (d["contrato"] + 35)) * -1) + (ano.year - d["nascimento"])} aposentado')

"""DESAFIO 93"""
# jogador = {}
# gols = []
# soma = 0
# jogador['nome'] = str(input('digite o nome do jogador '))
# partidas = int(input('quantas partidas foram? '))
# for i in range(partidas):
#     g = int(input(f'numeros de gols na partida{i} '))
#     gols += [g]
#     soma = sum(gols)
# jogador['gols'] = gols
# jogador['total'] = soma
# print(jogador)
# print('*-'*30)
# print(f'O campo nome é {jogador["nome"]}')
# print(f'O campo gols é {jogador["gols"]}')
# print(f'O campo total é {jogador["total"]}')
# print('*-'*30)
# print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
# for j in range(partidas):
#     print(f'{" ":^5}=> Na partida {j}, fez {jogador["gols"][j]}')
# print(f'foi um total de {jogador["total"]}')

"""DESAFIO 94"""
# d = {}
# l = []
# mulher = []
# sidade = []
# amedia = []
# ctd = 0
# while True:
#     d['nome'] = str(input('digite seu nome '))
#     d['sexo'] = str(input('sexo M/F? ')).upper().strip()[0]
#     while d['sexo'] not in 'MmFf':
#         d['sexo'] = str(input('sexo M/F? '))
#     idade = int(input('digite sua idade '))
#     sidade +=[idade]
#     soma = sum(sidade)
#     d['idade'] = idade
#     ctd += 1
#     if d['sexo'] == 'F':
#         mulher += [d['nome']]
#     l.append(d.copy())
#
#     opc = str(input('deseja continuar? S/N ')).upper().strip()[0]
#     while opc not in 'SN':
#         opc = str(input('deseja continuar? S/N ')).upper().strip()[0]
#     if opc == 'N':
#         break
# media = soma / ctd
# print(l)
# print(f'foi cadastradas {ctd} pessoas')
# print(f'a media foi {media}')
# print(f'as mulheres foram: {mulher}')
# print('Lista acima da media: ')
# print()
# for i in range(ctd):
#     if l[i]['idade'] > media:
#         amedia += [l[i]]
#         print(f'nome = {l[i]["nome"]}; sexo = {l[i]["sexo"]}; idade = {l[i]["idade"]}; ') #poderia trocar pelo amedia tbm
#         print()
# print('ENCERRANDO')

"""DESAFIO 95"""
# lista = []
# gols = []
# soma = ctd = 0
# while True:
#     nome = str(input('digite o nome do jogador '))
#     partidas = int(input('quantas partidas foram? '))
#     for i in range(partidas):
#         g = int(input(f'numeros de gols na partida{i} '))
#         gols.append(g)
#     info = {'nome': nome, 'quantidade': partidas, 'gols': gols[:], 'soma': sum(gols)}
#     ctd += 1
#     lista.append(info.copy())
#     info.clear()
#     gols.clear()
#     opc = str(input('deseja continuar? SN ')).strip().upper()[0]
#     print('-' * 30)
#     while opc not in 'SN':
#         opc = str(input('deseja continuar? SN ')).strip().upper()[0]
#     if opc in 'N':
#         break
# print('-' * 30)
# print(lista)
# print(f'{"cod":<4}{"nome":<11}{"gols":<15} total')
# for n, i in enumerate(lista):
#     print(f'{n:<4}{i["nome"]:<11} {str(i["gols"]):<18}{i["soma"]}')
# while True:
#     nota = int(input('Qual jogador deseja ver? (999 para):'))
#     if nota == 999:
#         break
#     if nota <= len(lista) - 1:
#         c = 0
#         print(f'-- Levantamento do jogador {lista[nota]["nome"]}:')
#         for cp in lista[nota]["gols"]:
#             print(f' {"No":>5} jogo {c} fez {cp} gols')
#             c += 1
#         print(f'No total {lista[nota]["soma"]} gols')
#     else:
#         print(f'Não existe jogador com o número {nota} por favor digite novamente:')
# print('<<< VOLTE SEMPRE >>>')
