from random import randint
import time
print(f"\033[;1m{'Desafio 091 - Jogando com numeros aleatorios eu um dicionario':*^70}\033[m")
# cria um dicionario e uma lista
dicionario = dict()
lista = list()

# cria as keys e coloca os valores delas no dicionario e o dicionario dentro da lista.
for a in range (0,4):
    dicionario['nome'] = input(f"Informe o nome o {a+1}o jogador: ")
    # a key 'dado' é preenchida com um valor random que vai de 1 a 6 - usando o ranint
    dicionario['dado'] = randint(1,6)
    lista.append(dicionario.copy())

# printa na tela os nomes e os valores tirados nos dados
print("Valores Sorteados:")
for a in lista:
    time.sleep(1)
    print(f"O jogador {a['nome']} tirou {a['dado']}")

time.sleep(1)
# ordena a lista usando a função sorted com argumentos.
lista = sorted(lista , key= lambda k:k['dado'], reverse=True)

# printa na tela os valores já ordenados.
print("Ranking dos Jogadores:")
for a, v in enumerate(lista):
    print(f"{a+1}o lugar {v['nome']} com {v['dado']} ")