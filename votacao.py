opção = 0
eleitores = int(input('Digite o número de eleitores: '))
candidatos = []
resposta = 's'
votoRosinha = 0
votoZezinho = 0
votoPaulodoPovo = 0


while opção != 5:
    print('------------------------------')
    print('MENU DE OPÇÕES')
    print('------------------------------')
    print('''[1] Lançar Candidato
[2] Votação           
[3] Resultado
[4] Sair''')
    print('------------------------------')
    opção = int(input('Por favor, escolha uma opção: '))

    if opção == 1:
        while resposta == 's':
            candidatos.append(input('Nome do candidato: '))
            resposta = input('Deseja continuar?')
            print(candidatos)
            print('Nome(s) adicionado(s) com sucesso!')

    elif opção == 2:
        print('------------------------------')
        print('MENU ELEITORAL')
        print('------------------------------')
        print('Vote [15] para Rosinha')
        print('Vote [20] para Zezinho')
        print('Vote [10] para Paulo do povo')
        print('------------------------------')
        for n in range(eleitores):
            voto = int(input("vote em 15, 20, ou 10: "))
            if voto == 15:
                votoRosinha = votoRosinha + 1
            elif voto == 20:
                votoZezinho = votoZezinho + 1
            elif voto == 10:
                votoPaulodoPovo = votoPaulodoPovo + 1
            else:
                print("voto inválido")

    elif opção == 3:
        print('Candidata Rosinha teve ', votoRosinha, 'voto(s)')
        print('Candidato Zezinho teve', votoZezinho, 'voto(s)')
        print('Candidato Paulo do Povo teve', votoPaulodoPovo, 'voto(s)')
        break

    elif opção == 4:
        print(' Obrigado(a), volte sempre!')
        break
    else:
        print('Opção inválida. Tente de novo! ;)')