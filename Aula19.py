# dicionarios, iniciando e exemplos
pessoas = {'nome': 'Eric Giobini', 'idade': 22, 'sexo':'Masculino'}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f"O aluno {pessoas['nome']} tem {pessoas['idade']} anos de idade.")

# Printando valore e chaves
print(pessoas.keys(),pessoas.values())
print(pessoas.items())

# Usando for
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k in pessoas.items():
    print(k)

# Usando for com .itens()
for p, v in pessoas.items():
    print(f"{p} = {v}")

# Deletando itens
del pessoas['sexo']
print(pessoas.items())

# Alterando itens
pessoas['nome'] = 'Aline Gotardo'
print(pessoas.items())

# Adicionando itens
pessoas['peso'] = 56.4
print(pessoas.items())

# Usando listas para criar dicionarios
brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['sigla'])
print(brasil[1]['uf'])

# For para criar listas de dicionarios e COPIA de Dicionarios
estado = dict()
brasil = list()

for c in range(0,2):

    estado['uf'] = input("Informe a UNIDADE FEDERATIVA: ")
    estado['sigla'] = input(f"Informe a SIGLA de {estado['uf']}: ")
    brasil.append(estado.copy())


print(brasil)
for c in brasil:
    print(f"{c['uf']} tem como sigla {c['sigla']}.")

for c in brasil:
    for k in c.values():
        print(k, end=' ')
    print()

