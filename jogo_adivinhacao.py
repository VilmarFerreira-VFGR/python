import random

numero_secreto = random.randint(1, 10)

tentativas = 0

while tentativas < 5:
    palpite = int(input('Digite um número entre 1 e 10: '))
    tentativas += 1

    if palpite == numero_secreto:
        break
    elif palpite < numero_secreto:
        print('O número é maior')
    elif palpite > numero_secreto:
        print('O número é menor')

if palpite == numero_secreto:
    print(f'Parabéns! Você acertou na {tentativas}ª tentativa')
else:
    print('Você perdeu!')
    print('Máximo de 5 tentativas alcançadas')