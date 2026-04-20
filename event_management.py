def cadastro_eventos(eventos):
    evento = input('\nNome do evento: ')
    eventos[evento] = set()

def adicionar_participante(eventos):
    evento = input('\nInforme o evento para adicionar participante: ')
    if evento in eventos:
        participante = input('\nNome do participante: ')
        eventos[evento].add(participante)
    else:
        print('Evento nao encontrado!')

def listagem_eventos(eventos):
    for i, evento in enumerate(eventos, start=1):
        print(f'\n{i} - {evento}')

def listagem_participantes(eventos):
    evento = input('\nInforme o evento que deseja consultar: ')
    if evento in eventos:
        print(f'\nPARTICIPANTES DO {evento}')
        for i, parti in enumerate(eventos[evento], start=1):
            print(f'\n{i} - {parti}')
    else:
        print('Evento nao encontrado!')

def comparar_eventos(eventos):
    evento1 = input('Digite o nome do primeiro evento: ') 
    evento2 = input('Digite o nome do segundo evento: ')
    if evento1 in eventos and evento2 in eventos:
        print('\nParticipantes em comum:')
        print(eventos[evento1] & eventos[evento2])

    else:
        print('Evento nao encontrado')

def todos_participantes(eventos):
    todos = set()

    for participantes in eventos.values():
        todos |= participantes

    if todos:
        print(todos)
    else:
        print('Nenhum participante cadastrado.')


eventos = {}

while True:
    print('\n[1] Cadastrar eventos\n[2] Adicionar participante\n[3] Listar eventos\n[4] Ver participantes\n[5] Comparar eventos\n[6] Todos participantes\n[7] Sair')
    try:
        opcao = int(input('Escolha uma opcao: '))
    except ValueError:
        print('Digite apenas numeros!')
        continue

    if opcao == 1:
        cadastro_eventos(eventos)

    elif opcao == 2:
        adicionar_participante(eventos)
    
    elif opcao == 3:
        listagem_eventos(eventos)
    
    elif opcao == 4:
        listagem_participantes(eventos)
    
    elif opcao == 5:
        comparar_eventos(eventos)
    
    elif opcao == 6:
        todos_participantes(eventos)
    
    elif opcao == 7:
        break
    
    else:
        print('Opcao invalida!')


print('Programa encerrado!')


