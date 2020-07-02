import somalista
print(f"\033[;1m{'Desafio 094 - Jogador gols Aprimorado':*^70}\033[m")
# Inicia o dicionario e as listas auxiliares
jogador = dict()
gols = list()
partidas = list()
lista_jogadores = list()
contador = 0

# loop infinito para criação dos dicionarios e das listas
while True:
    print(f"\n"*30)
    print("-="*15,"MENU JOGADOR","-="*15)
    print(f'''1 - Adicionar Jogador.
2 - Exibir Jogadores.
3 - Detalhes de jogador.
0 - Sair''')
    escolha = int(input(f"Escolha uma das opções acima: "))
    # Retorna erro caso o usuario digite uma opçao errada
    if escolha not in range (0,4):
        print("\033[1;31mOpção Errada!\033[m")
        input("Pressione ENTER para continuar!")

    if escolha == 1:
        # Cria a key nome e coloca nela o valor digitado pelo usuario
        jogador['nome'] = input("Digite o nome do jogador: ")
        # Adiciona um valor na lista 'partidas'
        partidas.append(int(input(f"Informe quantas partidas {jogador['nome']} jogou: ")))
        # Usa o valor da lista de partidas para criar um loop para adicionar na lista gols quantos gols tem cada partida
        for a in range (0,partidas[contador]):
            gols.append(int(input(f"quantos gols {jogador['nome']} fez na partida {a+1}? ")))
        # a lista de gols é adicionado na key criada no dicionario
        jogador['gols'] = gols[:]
        # criei um modulo para fazer a soma de valores de uma lista e usei para somar os gols da lista gols e colocar no dicionario
        jogador['total'] = somalista.soma(gols)
        # Adiciona o dicionario na lista.
        lista_jogadores.append(jogador.copy())
        contador += 1
        gols.clear()
        print(f"\033[1;34mO jogador {jogador['nome']} foi adicionado com sucesso!\033[m")
        input("Pressione ENTER para continuar...")
    # Sai do menu
    if escolha == 0:
        break
    # Menu 2
    if escolha == 2:
        print("-="*25)
        print("cod ",end='')
        # For para listar as keys dos jogadores
        for i in jogador.keys():
            print(f"{(i):<15}",end='')
        print()
        # For para mostrar os valores das keys metodo 1
        for p, v in enumerate(lista_jogadores):
            print(f" {p+1:<2} {v['nome']:<10} {str(v['gols']):<20} {v['total']:>2} ")
        print("-"*50)
        # For para mostrar os valores das keys metodo 2
        for p, v in enumerate(lista_jogadores):
            print(f" {p+1:<2}",end=' ')
            for k in v.values():
                print(f"{str(k):<15}",end='')
            print()
        print("-=" * 25)

        input("Pressione ENTER para continuar...")
    # menu 3
    if escolha == 3:
        print('-'*40)
        # pede ao usuario qual cod de jogador ele quer
        menu3 = int(input("Mostrar levantamento de qual jogador? "))
        # compara o codigo dado com o tamanho da lista de jogadores
        if menu3 > len(lista_jogadores):
            print(f"Não existe jogador com o codigo informado!")
        else:
             # For para mostrar o jogador selecionado.
             print(f"Levantmento do jogador {lista_jogadores[menu3-1]['nome']}")
             for p, v in enumerate(lista_jogadores[menu3-1]['gols']):
                print(f"No jogo {p+1} {lista_jogadores[menu3-1]['nome']} fez {v} gols.")
        input("Pressione ENTER para continuar...")
