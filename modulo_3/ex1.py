'''
Faça um programa que calcule a % de geração de um sistema de energia solar, o programa deve ler dois valores números:

1 - Consumo anual de uma Unidade
2 - Geração

Depois faça o programa retornar a porcentagem de geração sobre o consumo anual.
'''

consumo_anual = float(input('Insira o Consumo Anual:\n'))
geracao = float(input('Insira a Geração:\n'))

resultado = (geracao / consumo_anual) * 100

print('A % de geração é {:.2f}%'.format(resultado))