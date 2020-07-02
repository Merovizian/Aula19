print(f"\033[;1m{'Desafio 090 - Nome e média em uma lista':*^70}\033[m")
# inicio o dicionario e a lista que vai conter os dicionarios
dicionario = dict()
lista = list()

while True:
    # cria a key e coloca o valor nome no dicionario e verifica se o usuario quer sair.
    nome = input(f"Qual o nome do aluno?: " if len(dicionario) == 0 else "Qual nome do aluno? ['N' - Sair]: ")
    if nome.lower()[0] == 'n':
        break
    dicionario['nome'] = nome
    # cria a key media e pede o valor para o usuario
    media = int(input(f"Qual a média do aluno {nome}: "))
    dicionario['media'] = media
    # Compara a media com o valor 6,o dicionario cria a key situação e coloca a string situação la
    if media < 6:
        situacao = '\033[1;31mReprovado\033[m'
    else:
        situacao = '\033[1;32mAprovado\033[m'
    dicionario['situacao'] = situacao

    lista.append(dicionario.copy())

# uma forma de printar listas de dicionarios
for p , a in enumerate(lista):
    print(f"O nome do {p+1} aluno é {a['nome']:<5} sua nota é {a['media']} e sua situação é {a['situacao']}.")