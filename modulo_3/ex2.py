'''
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio e imprima quanto cada um ganharia do prêmio com base no valor investido.
'''


premio = float(input('Insira o valor do Premio:\n'))

amg1 = float(input('Insira quanto o amigo 1 investiu:\n'))
amg2 = float(input('Insira quanto o amigo 2 investiu:\n'))
amg3 = float(input('Insira quanto o amigo 3 investiu:\n'))

total_investido = amg1 + amg2 + amg3

print('O prêmio do amigo 1 é R$ {:.2f}'.format((amg1/total_investido)*premio))
print('O prêmio do amigo 2 é R$ {:.2f}'.format((amg2/total_investido)*premio))
print('O prêmio do amigo 3 é R$ {:.2f}'.format((amg3/total_investido)*premio))