import time
import random

def validar_empate(placar):
    print('EMPATE!! :)')

def validar_vitoria_jogador(placar):
    print('PARABÉNS, VOCÊ VENCEU!! :D')
    placar['jogador'] += 1

def validar_vitoria_cpu(placar):
    print('A CPU VENCEU :(')
    placar['cpu'] += 1

def exibir_placar(placar):
    print('------ PLACAR ------')
    print('  Jogador: ' + str(placar['jogador']))
    print('  CPU: ' + str(placar['cpu']))
    print('--------------------')
    
opcoes = {'0': 'PEDRA', '1': 'PAPEL', '2': 'TESOURA'}
placar = {'jogador': 0, 'cpu': 0}
continuar_jogando = True

exibir_placar(placar)

while continuar_jogando:
        
    print('------ ESCOLHA UMA DAS OPÇÕES ABAIXO ------')
    for key in opcoes:
        print(f'[ {key} ] - {opcoes[key]}')
    print('-------------------------------------------')

    escolha_usuario = input('Sua escolha é: ')

    if escolha_usuario not in opcoes:
        print('Escolha inválida')
        continue

    escolha_usuario = opcoes[escolha_usuario]
    escolha_cpu = opcoes[str(random.randrange(len(opcoes)))]

    print('\nJO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!!!!\n')

    print(f'Sua escolha foi: {escolha_usuario}')
    print(f'A escolha da CPU foi: {escolha_cpu}\n')
        
    if escolha_usuario == escolha_cpu:
        validar_empate(placar)        
    elif escolha_usuario == 'PEDRA' and escolha_cpu == 'PAPEL':
        validar_vitoria_cpu(placar)        
    elif escolha_usuario == 'PEDRA' and escolha_cpu == 'TESOURA':
        validar_vitoria_jogador(placar)        
    elif escolha_usuario == 'PAPEL' and escolha_cpu == 'PEDRA':
        validar_vitoria_jogador(placar)        
    elif escolha_usuario == 'PAPEL' and escolha_cpu == 'TESOURA':
        validar_vitoria_cpu(placar)        
    elif escolha_usuario == 'TESOURA' and escolha_cpu == 'PEDRA':
        validar_vitoria_cpu(placar)        
    elif escolha_usuario == 'TESOURA' and escolha_cpu == 'PAPEL':
        validar_vitoria_jogador(placar)
    
    jogar_novamente = (input('\nDeseja jogar novamente? [s/n]: ')).lower()

    if jogar_novamente not in ['s', 'n']:
        print('Escolha inválida. O jogo será finalizado...')        
        continuar_jogando = False

    if jogar_novamente.lower() == 'n':
        continuar_jogando = False

print('\nObrigado por jogar!!\n')
exibir_placar(placar)
