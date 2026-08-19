# Aula 04 - a mesma regra em cada item da massa (demonstração guiada 1)
#
# Regra de classificação, como ela chega no trabalho:
#   2xx é sucesso.
#   4xx é erro do cliente.
#   5xx é erro do servidor.
#   O resto, aqui o 302, é redirecionamento ou outro.
#
# Algoritmo em pseudocódigo, nas convenções da Aula 01:
#
#   ALGORITMO classificar_status
#   ENTRADA: codigos_status (lista de números)
#
#   INÍCIO
#       VALIDE que a lista tem 6 itens
#       PARA CADA codigo EM codigos_status FAÇA
#           SE codigo está entre 200 e 299 ENTÃO
#               categoria recebe "Sucesso"
#           SENÃO SE codigo está entre 400 e 499 ENTÃO
#               categoria recebe "Erro do cliente"
#           SENÃO SE codigo é 500 ou mais ENTÃO
#               categoria recebe "Erro do servidor"
#           SENÃO
#               categoria recebe "Redirecionamento ou outro"
#           FIM SE
#           ESCREVER codigo e categoria
#       FIM PARA
#   FIM
#
# Quem decide o número de voltas é a lista, não este código. É por isso que
# quarenta status novos não mudariam nada aqui embaixo.

codigos_status = [200, 201, 404, 500, 302, 403]

# A massa é conferida antes de ser usada. Se a listagem chegar com um item
# a menos, o programa para aqui e não produz um relatório errado.
assert len(codigos_status) == 6
print("Massa conferida: 6 códigos para classificar")

for codigo in codigos_status:
    if codigo >= 200 and codigo < 300:
        categoria = "Sucesso"
    elif codigo >= 400 and codigo < 500:
        categoria = "Erro do cliente"
    elif codigo >= 500:
        categoria = "Erro do servidor"
    else:
        categoria = "Redirecionamento ou outro"

    # Este print está alinhado com o if, e não dentro dele: por isso ele
    # roda em toda volta, e não só quando alguma condição é verdadeira.
    print(f"Status {codigo}: {categoria}")
