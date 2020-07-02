print(f"\033[;1m{'Desafio 094 - Classificação de pessoas':*^70}\033[m")
# inicia as variaveis
pessoas_dict = dict()
pessoas_list = list()
media = contador = 0
# loop para criação de listas e dicionarios
while True:
    # cria a key nome e pede ao usuario seu valor, case seja 'n' ou 'N' sai do loop
    pessoas_dict['nome'] = input("Infome o nome da pessoa: " if len(pessoas_dict) == 0 else "Informe o nome da pessoa[N - Sair]: ")
    if pessoas_dict['nome'].lower() == 'n':
        break
    # Cria a key 'sexo' e coloca o valor, logo apos resume o valor em um caracter upper ('M' ou 'F').
    while True:
        pessoas_dict['sexo'] = input(f"Informe o sexo de {pessoas_dict['nome']}: ").upper()[0]
        if pessoas_dict['sexo']  in 'FM':
            break
        print("Informe um valor correto")

    # cria a key 'idade' e pergunta ao usuario seu valor
    pessoas_dict['idade'] = int(input(f"Informe a idade de {pessoas_dict['nome']}: "))
    # adiciona na lista o dicionario criado
    pessoas_list.append(pessoas_dict.copy())

# loop para percorrer na lista pessoas e procurar pela idade, adicionando este valor na media
for a in pessoas_list:
    media += a['idade']
# depois de pegar todos os valores de idade a variavel é dividida pela quantidade de pessoas da lista
media = media / (len(pessoas_list))



# printa a quantidade de pessoas e a media de idade
print('-='*20)
print(f"Foram cadastradas {len(pessoas_list)} pessoas.")
print(f"A media de idade das {len(pessoas_list)} pessoas é de {media:.2f} anos")
# printa as mulheres que estao nos dicionarios
print(f"As mulheres cadastradas foram: ", end='')
for a in pessoas_list:
  if a['sexo'] == 'F':
     print(f"{a['nome']}", end=' ')
     contador += 1
if contador == 0:
    print("Não Foram cadastradas mulheres!")

# loop que percorre os dicionarios das listas para retornar as pessoas que tem idade acima da media
print(f"\nLista de pessoas que possuem mais de {media:.2f} anos:")
for a in pessoas_list:
    if a['idade'] > media:
        print(f"{a.values()}")


