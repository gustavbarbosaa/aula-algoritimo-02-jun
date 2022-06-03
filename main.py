print("SISTEMA DE CADASTRO DE ALUNO")

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
turma = str(input('Digite sua turma: '))

aluno = {
    'nome': nome,
    'idade': idade,
    'turma': turma
}


print("Nome do aluno: ", aluno['nome'])
print("Idade do aluno: ", aluno['idade'])
print("Turma do aluno: ", aluno['turma'])

# Para adicionar valor usa .get(nome do chave)

# Para remover valor do dicionário .pop(nome do chave)
aluno.pop('idade')
print(aluno)


# Outra forma de remover é o del <nome do dicionario> [chave]
del aluno['nome']


# O metodo .popitem() remove sempre o último par de um dicionário (chave, valor)
aluno.popitem()
print(aluno)

# O método update é utilizado para atuallizar o diocionário


