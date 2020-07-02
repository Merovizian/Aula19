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

    if escolha == 0:
        break

    if escolha == 2:
        print("-="*25)
        print(f"cod {'nome':<10} {'gols':<20} {'total':>10}")
        for p, v in enumerate(lista_jogadores):
            print(f"{p+1:<2} {v['nome']:<8} {v['gols']} {v['total']:>{int(30 - 3*len(v['gols']))}} ")
        print("-="*25)
        input("Pressione ENTER para continuar...")

    if escolha == 3:
        print('-'*40)
        menu3 = int(input("Mostrar levantamento de qual jogador? "))
        print(f"Levantmento do jogador {lista_jogadores[menu3-1]['nome']}")
        for p, v in enumerate(lista_jogadores[menu3-1]['gols']):
             print(f"No jogo {p+1} {lista_jogadores[menu3-1]['nome']} fez {v} gols.")
        input("Pressione ENTER para continuar...")




'''
# Mostra a lista completa com os dicionarios de cada jogador
print('-='*20)
for a in lista_jogadores:
    print(a)
print('-='*20)
# Mostra cada key e seu respectivo valor
for p, a in enumerate(lista_jogadores):
    print('*'*10,a['nome'],'*'*10)
    for p,v in a.items():
        print(f"O campo {p} tem valor: {v}")
print('-='*20)
# Mostra, para cada jogador, seus gols em cada partida.
for p, a in enumerate(lista_jogadores):
    print(f"O jogador {a['nome']} jogou {partidas[p]} partidas" )
    for k, v in enumerate(a['gols']):
        print(f"==> Na partida {k+1} fez {v} gols")
    print(f"Totalizando {a['total']} gols")

'''