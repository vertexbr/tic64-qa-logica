# Aula 05 - os dois KeyError, provocados de propósito
#
# Os dois erros que a aula precisa mostrar, na ordem que importa: primeiro o
# hábito de lista da Aula 04 batendo num dicionário, depois o campo opcional
# que não veio.
#
# Os dois estão dentro de try/except para o arquivo rodar até o fim e mostrar
# os dois na mesma execução. Sem isso o Python pararia no primeiro e a saída
# de baixo não apareceria.
#
# AVISO, e ele é a parte que se leva para o trabalho: numa suíte de verdade
# você NÃO faz isso. Falha tem que interromper. Engolir exceção é o oposto de
# verificar, e except largo é a forma mais comum de um teste ficar verde sem
# ter testado nada. Aqui o try/except é recurso didático, para os dois erros
# caberem num arquivo só.

usuario = {"id": 42, "nome": "Gaia Silva", "email": "gaia@teste.com"}

# --- erro 1: o dedo procurando a posição zero, que é o hábito da Aula 04 ---
try:
    print(usuario[0])
except KeyError as erro:
    print(f"KeyError: {erro}")

# Cuidado com a leitura errada, que é a mais comum: isso NÃO quer dizer que
# dicionário recusa número. Aceita, e {0: "ok"} é dicionário válido. O que
# aconteceu foi uma busca pela chave 0, que este dicionário não tem. A regra
# do dia é sobre nome contra posição, não sobre texto contra número.
print(f"Dicionário aceita chave numérica? {0 in {0: 'ok'}}")

# --- erro 2: a chave que não existe neste registro ---
try:
    print(usuario["telefone"])
except KeyError as erro:
    print(f"KeyError: {erro}")

# Este é o erro que paga o arquivo seguinte. Resposta de API tem campo
# opcional, e usuário sem telefone existe. Colchete num campo opcional quebra
# o teste por ausência de dado, não por defeito no produto.
print("As duas mensagens dizem exatamente qual chave o Python não achou")
