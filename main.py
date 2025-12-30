from random import randint
from time import sleep
import pygame
pygame.init()
opcao = 0
audio_menu_tocado = False 
audio_jokenpo_tocado = False
audio_adivinhacao_tocado = False
while opcao != 4:
    print('--' * 15)
    print('{:=^30}'.format(' JOGOS '))
    print('--' * 15)
    print('''Escolha uma dessas opções abaixo:
[ 1 ] ADIVINHAÇÃO
[ 2 ] JOKENPÔ
[ 3 ] PAR OU ÍMPAR
[ 4 ] SAIR DO PROGRAMA''')
    sleep(2.5)
    if not audio_menu_tocado:
        pygame.mixer.music.load('audio_menu_jogos.mp3')
        pygame.mixer.music.play()
        sleep(7) 
        audio_menu_tocado = True
    opcao = int(input('>>>> Qual é sua opção? '))
    if opcao == 1:
        numero_secreto = randint(0, 10)
        tentativas = 0
        limite_tentativas = 5
        acerto = False
        print('--' * 15)
        print('{:=^30}'.format(' ADIVINHAÇÃO '))
        print('--' * 15)
        if not audio_adivinhacao_tocado:
            pygame.mixer.music.load('audio_adivinhacao_menu.mp3')
            pygame.mixer.music.play()
            audio_adivinhacao_tocado = True
        
        while not acerto and tentativas < limite_tentativas:
            chute_usuario = int(input(f'Tentativas ({tentativas + 1}/{limite_tentativas}) - Adivinhe um número entre (0 e 10): '))
            tentativas += 1
            
            if chute_usuario == numero_secreto:
                print('--' * 15)
                print('{:^30}'.format(' VOCÊ ACERTOU! '))
                print(f'Você acertou em {tentativas} tentativa(s)')
                print('--' * 15)
                acerto = True
                pygame.mixer.music.load('audio_de_acerto.mp3')
                pygame.mixer.music.play()
            elif chute_usuario > numero_secreto:
                print('Menos... Tente novamente.')
                pygame.mixer.music.load('audio_adivinhacao(1).mp3')
                pygame.mixer.music.play()
                sleep(1)
            else:
                print('Mais... Tente novamente.')
                pygame.mixer.music.load('audio_adivinhacao(2).mp3')
                pygame.mixer.music.play()
                sleep(1)
        if not acerto:
            print('--' * 30)
            print('{:^30}'.format(f' VOCÊ ESGOTOU AS TENTATIVAS. O número era ({numero_secreto}) '))
            print('--' * 30)
            pygame.mixer.music.load('audio_de_erro.mp3')
            pygame.mixer.music.play()

    elif opcao == 2:
        itens = ['Pedra', 'Papel', 'Tesoura']
        computador = randint(0, 2)
        while True:
            print('--' * 15)
            print('{:=^30}'.format(' JOKENPÔ '))
            print('--' * 15)
            print('''Escolha sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
            if not audio_jokenpo_tocado:
                pygame.mixer.music.load('audio_jokenpo_menu.mp3')
                pygame.mixer.music.play()
                sleep(4) 
                audio_jokenpo_tocado = True

            jogador = int(input('Qual é sua opção? '))
            if jogador in [0, 1, 2]:
                break
            else:
                print('--' * 17)
                print('Opção inválida. Tente novamente.')
                print('--' * 17)
                pygame.mixer.music.load('audio_opcao_invalida.mp3')
                pygame.mixer.music.play()
                sleep(3)

        print('--' * 15)
        print('JO...')
        pygame.mixer.music.load('audio_JO.mp3')
        pygame.mixer.music.play()
        sleep(1)
        print('KEN...')
        pygame.mixer.music.load('audio_KEN.mp3')
        pygame.mixer.music.play()
        sleep(1)
        print('PÔ!!!')
        pygame.mixer.music.load('audio_PO.mp3')
        pygame.mixer.music.play()
        sleep(0.5)
        print('--' * 15)
        print(f'COMPUTADOR: ({itens[computador]})')
        print(f'VOCÊ: ({itens[jogador]})')
        print('--' * 15)    
        if computador == 0:
            if jogador == 0:
                print('{:^30}'.format(' EMPATE '))
                pygame.mixer.music.load('audio_de_empate.mp3')
                pygame.mixer.music.play()
            elif jogador == 1:
                print('{:^30}'.format(' VOCÊ VENCEU! '))
                pygame.mixer.music.load('audio_de_acerto.mp3')
                pygame.mixer.music.play()
            elif jogador == 2:
                print('{:^30}'.format(' COMPUTADOR VENCEU! '))
                pygame.mixer.music.load('audio_de_erro.mp3')
                pygame.mixer.music.play()
        elif computador == 1:
            if jogador == 0:
                print('{:^30}'.format(' COMPUTADOR VENCEU! '))
                pygame.mixer.music.load('audio_de_erro.mp3')
                pygame.mixer.music.play()
            elif jogador == 1:
                print('{:^30}'.format(' EMPATE! '))
                pygame.mixer.music.load('audio_de_empate.mp3')
                pygame.mixer.music.play()
            elif jogador == 2:
                print('{:^30}'.format(' VOCÊ VENCEU! '))
                pygame.mixer.music.load('audio_de_acerto.mp3')
                pygame.mixer.music.play()
        elif computador == 2:
            if jogador == 0:
                print('{:^30}'.format(' VOCÊ VENCEU! '))
                pygame.mixer.music.load('audio_de_acerto.mp3')
                pygame.mixer.music.play()
            elif jogador == 1:
                print('{:^30}'.format(' COMPUTADOR VENCEU! '))
                pygame.mixer.music.load('audio_de_erro.mp3')
                pygame.mixer.music.play()
            elif jogador == 2:
                print('{:^30}'.format(' EMPATE! '))
                pygame.mixer.music.load('audio_de_empate.mp3')
                pygame.mixer.music.play()
        
        pygame.mixer.music.play()
        print('--' * 15)

    elif opcao == 3:
        print('--' * 15)
        print('{:=^30}'.format(' PAR OU ÍMPAR '))
        print('--' * 15)
        pygame.mixer.music.load('audio_digite_valor.mp3')
        pygame.mixer.music.play()
        jogador = int(input('Digite um valor: '))
        computador = randint(0, 10)
        total = (jogador + computador)
        pygame.mixer.music.load('audio_par_ou_impar.mp3')
        pygame.mixer.music.play()

        tipo = ' '
        while tipo not in 'PI':
            tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        print('--' * 25)
        print(f'Você jogou ({jogador}) e o computador ({computador}). Total de ({total})')
        if total % 2 == 0:
            print('(DEU PAR)')
        else:
            print('(DEU ÍMPAR)')
        print('--' * 15)

        if tipo == 'P':
            if total % 2 == 0:
                print('{:^30}'.format(' VOCÊ ACERTOU! '))
                pygame.mixer.music.load('audio_de_acerto.mp3')
                pygame.mixer.music.play()
            else:
                print('{:^30}'.format(' COMPUTADOR VENCEU! '))
                pygame.mixer.music.load('audio_de_erro.mp3')
                pygame.mixer.music.play()

        elif tipo == 'I':
            if total % 2 == 1:
                print('{:^30}'.format(' VOCÊ ACERTOU! '))
                pygame.mixer.music.load('audio_de_acerto.mp3')
                pygame.mixer.music.play()
            else:
                print('{:^30}'.format(' COMPUTADOR VENCEU! '))
                pygame.mixer.music.load('audio_de_erro.mp3')
                pygame.mixer.music.play()
        print('--' * 15)

    elif opcao == 4:
        print('--' * 15)
        print('{:^30}'.format(' FINALIZANDO...'))
        print('--' * 15)
        pygame.mixer.music.load('audio_finalizando_programa.mp3')
        pygame.mixer.music.play()
        sleep(2)
    else:
        print('--' * 17)
        print('Opção inválida. Tente novamente.')
        print('--' * 17)
        pygame.mixer.music.load('audio_opcao_invalida.mp3')
        pygame.mixer.music.play()
        sleep(3)
