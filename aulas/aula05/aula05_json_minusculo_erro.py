# Aula 05 - JSON e Python: três palavras de diferença
#
# JSON é o formato em que as APIs falam, e ele é visualmente quase idêntico ao
# dicionário do Python. Quase. As diferenças são três palavras:
#
#   JSON     Python
#   true     True
#   false    False
#   null     None
#
# Quando você copiar um JSON de resposta e colar no editor para virar massa de
# teste, é exatamente aqui que vai quebrar.
#
# PARA VER O ERRO: descomente a linha 26 e rode. O Python para nela, e a
# mensagem vem com a correção sugerida:
#
#   NameError: name 'true' is not defined. Did you mean: 'True'?
#
# Ler a sugestão economiza minutos, e ela só aparece assim, num erro que
# interrompe de verdade. Por isso a linha fica comentada em vez de embrulhada
# num try/except: try/except esconde justamente a parte que ensina.
#
# Depois de ver o erro, comente a linha de novo e rode: o resto do arquivo
# mostra que, com as três palavras trocadas, tudo funciona igual.

# --- a versão que quebra, com o JSON colado cru ---
# resposta = {"nome": "Gaia", "ativo": true, "telefone": null}

# --- a versão corrigida, com as três palavras trocadas ---
resposta = {"nome": "Gaia", "ativo": True, "telefone": None}

print(resposta)
print(f"Ativo? {resposta['ativo']}")
print(f"Telefone: {resposta['telefone']}")

# None não é a mesma coisa que texto vazio nem que zero, e essa distinção
# aparece em resposta de API todo dia: campo que veio nulo contra campo que
# veio em branco são dois defeitos diferentes.
print(f"O telefone é None? {resposta['telefone'] == None}")
print(f"O telefone é texto vazio? {resposta['telefone'] == ''}")

assert resposta["ativo"] == True
assert resposta["telefone"] == None
print("Verificações passaram: o resto é igual ao dicionário de sempre")
