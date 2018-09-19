import time
import random

def validar_empate(placar):
    print('EMPATE!! :)')

def validar_vitoria_jogador(placar):
    print('PARABÉNS, VOCÊ VENCEU!! :D')
    placar[0] = placar[0] + 1

def validar_vitoria_maquina(placar):
    print('O COMPUTADOR VENCEU :(')
    placar[1] = placar[1] + 1

def exibir_placar(placar):
    print('------ PLACAR ------')
    print('  Jogador: ' + str(placar[0]))
    print('  Computador: ' + str(placar[1]))
    print('--------------------')

def tratar_escolha(escolha):
    if escolha == '0': return 'PEDRA'
    elif escolha == '1': return 'PAPEL'
    else: return 'TESOURA'
    
opcoes = ['0', '1', '2']

jogar_novamente = True

# placar[0] = pontuação do jogador
# placar[1] = pontuação do computador
placar = [0, 0]

while jogar_novamente:
        
    exibir_placar(placar)
    
    print('------ ESCOLHA UMA DAS OPÇÕES ABAIXO ------')
    print('[ 0 ] - PEDRA')
    print('[ 1 ] - PAPEL')
    print('[ 2 ] - TESOURA')

    escolha_usuario = input('Sua escolha é: ')

    if escolha_usuario not in opcoes:
        print('Escolha inválida')
        continue

    escolha_maquina = opcoes[random.randrange(len(opcoes))]

    print('JO')
    time.sleep(0.6)
    print('KEN')
    time.sleep(0.6)
    print('PO!!!!')

    print('')
    print('Sua escolha foi: ' + tratar_escolha(str(escolha_usuario)))
    print('A escolha da máquina foi: ' + tratar_escolha(str(escolha_maquina)))
    print('')
        
    if escolha_usuario == '0' and escolha_maquina == '0':
        validar_empate(placar)
    elif escolha_usuario == '0' and escolha_maquina == '1':
        validar_vitoria_maquina(placar)
    elif escolha_usuario == '0' and escolha_maquina == '2':
        validar_vitoria_jogador(placar)
    elif escolha_usuario == '1' and escolha_maquina == '1':
        validar_empate(placar)
    elif escolha_usuario == '1' and escolha_maquina == '0':
        validar_vitoria_jogador(placar)
    elif escolha_usuario == '1' and escolha_maquina == '2':
        validar_vitoria_maquina(placar)
    elif escolha_usuario == '2' and escolha_maquina == '2':
        validar_empate(placar)
    elif escolha_usuario == '2' and escolha_maquina == '0':
        validar_vitoria_maquina(placar)
    elif escolha_usuario == '2' and escolha_maquina == '1':
        validar_vitoria_jogador(placar)

    print('')
    resposta_jogar_novamente = (input('Deseja jogar novamente? [s/n]: ')).lower()

    if resposta_jogar_novamente not in ['s', 'n']:
        print('Escolha inválida. O jogo será finalizado...')
        jogar_novamente = False

    if resposta_jogar_novamente.lower() == 'n':
        jogar_novamente = False

print('Obrigado por jogar!!')
print(' ')
print('O placar final foi: ')
exibir_placar(placar)
print('')
