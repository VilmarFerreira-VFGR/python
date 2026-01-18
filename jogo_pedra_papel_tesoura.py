import random

opcoes = ['pedra', 'papel', 'tesoura']

while True:
    jogador = str(input('Digite: Pedra, Papel, Tesoura ou Sair: ')).lower()

    if jogador == 'sair' or jogador == 'Sair' or jogador == 'SAIR':
        print('\n===Obrigado por jogar!===\n')
        break
    if jogador not in opcoes:
        print('Opção inválida! Tente novamente')
        continue
        
    computador = random.choice(opcoes)
    print(f'O computador jogou {computador}')

    if jogador == computador:
        print('\n===Empate===\n')
    elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador =='papel'):
        print('\n===Você ganhou!===\n')
    else:
        print('\n===Você perdeu!===\n')