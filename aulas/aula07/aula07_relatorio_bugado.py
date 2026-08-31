# Aula 07 - três defeitos plantados, e nenhum deles quebra o programa
#
# Ele roda. Não tem traceback, não tem vermelho, não tem aviso. E os três
# números impressos estão errados.
#
# Sua tarefa é achar os três e, para cada um, escrever três coisas:
#   HIPÓTESE     o que você acha antes de testar
#   EVIDÊNCIA    o que você fez para confirmar
#   CAUSA RAIZ   a linha e o motivo
#
# Comece pelo primeiro número impresso e pergunte se ele faz sentido. Duas notas
# de "passou" em três deveriam dar 66,7%.
#
# A correção dos três está no aula07_relatorio_corrigido.py. Não abra antes de
# tentar: o exercício é a investigação, não a resposta.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Três regras escritas: a média de aprovação é a proporção de casos que passaram; o
#   desconto precisa de aprovação gerencial quando passa de 50%; e a soma dos valores
#   inclui todos os valores da massa.


def calcular_media_aprovacao(resultados):
    aprovados = 0
    for r in resultados:
        if r == "passou":
            aprovados + 1
    return aprovados / len(resultados) * 100


def precisa_de_aprovacao_gerencial(valor_desconto):
    # Regra escrita: precisa de aprovação quando o desconto PASSA de 50%.
    if valor_desconto >= 50:
        return True
    return False


def somar_valores(linhas):
    total = 0
    for linha in linhas:
        try:
            total = total + float(linha)
        except:
            pass
    return total


notas = ["passou", "passou", "falhou"]
print(f"Aprovacao: {calcular_media_aprovacao(notas)}%")
print(f"Desconto de 50 por cento precisa de aprovacao? {precisa_de_aprovacao_gerencial(50)}")
print(f"Soma: {somar_valores(['10.00', '20,00', '30.00'])}")
