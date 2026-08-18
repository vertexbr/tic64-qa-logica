# Aula 03 - evidência esperado x obtido no caso de teste de login da Aula 02
#
# A massa é a mesma do aulas/aula02/aula02_login.py. O que muda é a evidência: em vez
# de só mostrar os valores, cada linha agora compara o esperado com o obtido e
# imprime o resultado da comparação. Quem julga a igualdade é o Python; quem
# ainda lê o True no fim da linha é você.

# --- massa de teste (a mesma da Aula 02) ---
caso = "CT-01"
usuario_informado = "Nadinha"
senha_informada = "JL1234!"
usuario_esperado = "Nadinha"
senha_esperada = "JL1234!"
valor_produto = 199.90
quantidade = 3

# --- processamento ---
total = valor_produto * quantidade

# --- evidência esperado x obtido ---
print(f"{caso} | usuário | esperado: {usuario_esperado} | obtido: {usuario_informado} | confere? {usuario_informado == usuario_esperado}")
print(f"{caso} | senha   | esperado: {senha_esperada} | obtido: {senha_informada} | confere? {senha_informada == senha_esperada}")
print(f"{caso} | total   | esperado: 599.70 | obtido: {total} | confere? {total == 599.70}")

# --- o defeito invisível da aula: espaço no fim do texto esperado ---
# Na tela os dois valores parecem idênticos e o confere? sai False. O !r na
# f-string mostra o valor com as aspas, e é ele que revela o espaço.
usuario_esperado_com_defeito = "Nadinha "

print(f"{caso} | usuário | esperado: {usuario_esperado_com_defeito} | obtido: {usuario_informado} | confere? {usuario_informado == usuario_esperado_com_defeito}")
print(f"{caso} | usuário | esperado: {usuario_esperado_com_defeito!r} | obtido: {usuario_informado!r} | confere? {usuario_informado == usuario_esperado_com_defeito}")
