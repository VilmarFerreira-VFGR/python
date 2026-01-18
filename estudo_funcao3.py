def cadastro():
    usuarios =[]
    while True:
        nome = str(input('Digite o nome de usuário: '))
        idade = int(input('Digite a idade do usuário: '))
        peso = float(input('Digite o peso do usuário: '))
        altura = int(input('Digite a altura em cm do usuário: '))
        opcao = int(input('Digite:\n(1) - Continuar\n(2) - Sair\n... '))

        usuario = {'nome': nome, 'idade': idade, 'peso': peso, 'altura': altura}
        usuarios.append(usuario)
        if opcao == 1:
            continue
            usuario += 1
        elif opcao == 2:
            break
        else:
            print('Erro! Tente novamente')
            continue
    print('\n===Resultados cadastrais===\n')
    for u in usuarios:
        print(f'Usuário {u['nome'].upper()} cadastrado com sucesso!')
        print(f'Idade: {u['idade']} anos')
        print(f'Peso: {u['peso']}Kg')
        print(f'Altura: {u['altura']/100}m')
        peso_ideal = altura-100
        perder_peso = peso - peso_ideal
        print(f'{u['nome'].upper()}, seu peso ideal é {peso_ideal}Kg')
        print(f'Você precisa perder {perder_peso}Kg para chegar ao peso ideal\n')    

cadastro()
