# dados = [
#     {'dia': 12, 'mes': 2, 'ano': 1999, 'temp': 30.5},
#     {'dia': 23, 'mes': 12, 'ano': 2000, 'temp': 32.5},
#     {'dia': 14, 'mes': 7, 'ano': 2001, 'temp': 35.5}
# ]
#
# for i in range(len(dados)):
#     print(f'A temperatura do dia: {dados[i].get("dia")}/{dados[i].get("mes")}/'
#           f'{dados[i].get("ano")} é {dados[i].get("temp")}°C')
#
# pessoas = ['Gustavo', 'Jose']
# contatos = ['9114-8935', '4002-8922']
#
# contatos = dict(zip(pessoas, contatos))
# print(contatos)

pessoas = {}
n = int(input('Quantas pessoas você quer cadastrar? '))
for i in range(n):
    nome = input('Digite seu nome: ')
    idade = int(input('DIgite sua idade: '))
    sexo = input('Digite seu sexo: ')
    pessoas[nome] = {'idade': idade, 'sexo': sexo}
print(pessoas)

