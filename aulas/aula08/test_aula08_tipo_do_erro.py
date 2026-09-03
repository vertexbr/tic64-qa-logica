# Aula 08 - o outro lado do vermelho: quando o defeito é do seu teste
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO, e o vermelho dele NÃO é defeito
# do produto. É defeito do teste, e saber separar os dois é o trabalho.
#
# O tipo do erro mostra por onde começar:
#
#   AssertionError                        a comparação rodou, mas esperado e
#                                         obtido são diferentes. Volte à REGRA.
#
#   TypeError, IndexError, KeyError,      a execução parou ANTES da validação.
#   NameError, AttributeError             Confira a linha, os dados e o contrato.
#
# Aqui a quantidade foi passada como "3", entre aspas, e a função nunca chegou
# no assert: 100 * "3" repete o texto e devolve "333", e quem estourou foi a
# SUBTRAÇÃO do desconto. Abrir relatório de bug com isso é devolução na certa.
#
# São os tipos de erro da Aula 07 aplicados ao relatório do pytest. O tipo mostra
# onde a execução parou. A regra e os dados mostram o que precisa de
# correção.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O total é valor vezes quantidade, menos o desconto em reais. A função espera
#   número nos dois primeiros parâmetros, e não converte texto sozinha.
from aula08_loja import calcular_total


def test_total_com_quantidade_em_texto():
    assert calcular_total(100, "3") == 300
