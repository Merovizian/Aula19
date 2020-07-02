from idade import ano
print(f"\033[;1m{'Desafio 092 - Cadastro trabalhadores':*^70}\033[m")
# Inicia as listas e os dicionarios
dicionario = dict()
lista = list()
# Loop principal
while True:
    # Cria o nome no dicionario e pergunta ele ao usuario, caso digite 'n' o programa sai.
    dicionario['nome'] = input("Digite o nome: " if len(dicionario) == 0 else "Digite o nome ['N' para sair]: ")
    if dicionario['nome'].lower() == 'n':
        break
    # cria uma chave idade e usa o modulo que criei para determinar a idade pela data de nascimento.
    dicionario['idade'] = ano(input(f"Informe a data de nascimento de {dicionario['nome']}: "))
    # cria uma key de carteira de trabalho e coloca o valor pelo usuario.
    ctps = int(input("Qual CTPS? ['0' - se não possuir]: "))
    # caso o usuario não tenha uma CTPS serão criadas as keys com valores 0.
    if ctps == 0:
        dicionario['ctps'] = 0
        dicionario['contratação'] = 0
        dicionario['salario'] = 0
        dicionario['aposentadoria'] = dicionario['idade'] + 35
    # caso o usuario tenha a carteira, o programa pede ao usuario para colocar os valores nas keys
    else:
        dicionario['ctps'] = ctps
        dicionario['contratação'] = input(f"Informe o ano de contratação de {dicionario['nome']}: ")
        dicionario['salario'] = float(input(f"Informe o salário de {dicionario['nome']}: "))
        dicionario['aposentadoria'] = dicionario['idade'] + (35 - ano('01/01/' + str(dicionario['contratação'])))
    # coloca em uma lista o dicionario criado.
    lista.append(dicionario.copy())

# Printa na tela as keys e os valores de cada um dos itens da lista.
for a in lista:
    print(f"Trabalhador {a['nome']}:")
    for p , v in a.items():
        print(f"{p} tem valor {v}")
        
