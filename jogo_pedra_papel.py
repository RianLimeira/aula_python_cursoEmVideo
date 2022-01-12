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
