# Lê os dados da loteria
premio = float(input('Quanto foi o prêmio da loteria?\n'))
ganhadores = int(input('Quantos jogadores ganhadores tiveram na loteria?\n'))

# Lista de ganhadores
list_ganhadores = []

# Lê os valores investidos por ganhador
for i in range(0, ganhadores):
    nome = input('Qual o nome do jogador {}?\n'.format(i+1))
    valor_investido = float(input('Quanto investiu o ganhador {}?\n'.format(nome)))
    list_ganhadores.append(
        {
            'nome': nome,
            'valor_investido': valor_investido,
        }
    )

# Calcula o total de investimento dos ganhadores
total = 0
for g in list_ganhadores:
    total += g['valor_investido']

# Imprime na tela o valor recebido por ganhador
for g in list_ganhadores:
    print('Valor recebido pelo ganhador {} foi de R$ {:.2f}'.format(g['nome'], (g['valor_investido'] / total) * premio))
