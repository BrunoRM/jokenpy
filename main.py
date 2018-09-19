import time
import random

def validar_empate(placar):
    print('EMPATE!! :)')

def validar_vitoria_jogador(placar):
    print('PARABÉNS, VOCÊ VENCEU!! :D')
    placar['jogador'] += 1

def validar_vitoria_maquina(placar):
    print('O COMPUTADOR VENCEU :(')
    placar['computador'] += 1

def exibir_placar(placar):
    print('------ PLACAR ------')
    print('  Jogador: ' + str(placar['jogador']))
    print('  Computador: ' + str(placar['computador']))
    print('--------------------')
    
opcoes = {'0': 'PEDRA', '1': 'PAPEL', '2': 'TESOURA'}
placar = {'jogador': 0, 'computador': 0}

while True:
        
    exibir_placar(placar)
    
    print('------ ESCOLHA UMA DAS OPÇÕES ABAIXO ------')
    for key in opcoes:
        print(f'[ {key} ] - {opcoes[key]}')
    print('-------------------------------------------')

    escolha_usuario = input('Sua escolha é: ')

    if escolha_usuario not in opcoes:
        print('Escolha inválida')
        continue

    escolha_usuario = opcoes[escolha_usuario]
    escolha_maquina = opcoes[str(random.randrange(len(opcoes)))]

    print('\nJO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!!!!\n')

    print(f'Sua escolha foi: {escolha_usuario}')
    print(f'A escolha do computador foi: {escolha_maquina}\n')
        
    if escolha_usuario == escolha_maquina:
        validar_empate(placar)        
    elif escolha_usuario == 'PEDRA' and escolha_maquina == 'PAPEL':
        validar_vitoria_maquina(placar)        
    elif escolha_usuario == 'PEDRA' and escolha_maquina == 'TESOURA':
        validar_vitoria_jogador(placar)        
    elif escolha_usuario == 'PAPEL' and escolha_maquina == 'PEDRA':
        validar_vitoria_jogador(placar)        
    elif escolha_usuario == 'PAPEL' and escolha_maquina == 'TESOURA':
        validar_vitoria_maquina(placar)        
    elif escolha_usuario == 'TESOURA' and escolha_maquina == 'PEDRA':
        validar_vitoria_maquina(placar)        
    elif escolha_usuario == 'TESOURA' and escolha_maquina == 'PAPEL':
        validar_vitoria_jogador(placar)
    
    resposta_jogar_novamente = (input('\nDeseja jogar novamente? [s/n]: ')).lower()

    if resposta_jogar_novamente not in ['s', 'n']:
        print('Escolha inválida. O jogo será finalizado...')        
        break

    if resposta_jogar_novamente.lower() == 'n':
        break

print('\nObrigado por jogar!!\n')
exibir_placar(placar)
