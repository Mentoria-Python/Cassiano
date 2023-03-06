unidade_sigla = 'UG'
unidade_codigo = '001'
unidade_classe_consumidora = 'A4-Verde-Comercial'
unidade_conexao = 'Bifásica'
unidade_condutor_tensao1 = 127
unidade_condutor_tensao2 = 220

# UR-3016707472-B1-Residencial-Trifásica 220/127

resultado = f'{unidade_sigla}-{unidade_codigo}-{unidade_classe_consumidora}-{unidade_conexao}-{unidade_condutor_tensao1}/{unidade_condutor_tensao2}V'
resultado2 = '{}-{}-{}-{}-{}V/{}V'.format(unidade_sigla, unidade_codigo, unidade_classe_consumidora, unidade_conexao, unidade_condutor_tensao1, unidade_condutor_tensao2)
resultado3 = unidade_sigla + '-' + unidade_codigo + '-' + str(unidade_condutor_tensao1)

tipo = type(unidade_condutor_tensao1)
unidade_condutor_tensao1 = str(unidade_condutor_tensao1)
tipo = type(unidade_condutor_tensao1)
print(tipo)