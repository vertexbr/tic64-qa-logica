# Aula 08 - o mesmo teste escrito de dois jeitos, e o relatório de cada um
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO. Os dois testes falham, e
# falham pelo MESMO motivo: eles esperam 25 e a função devolve 20. A diferença
# está inteira no que o relatório consegue contar sobre a falha.
#
# Rode com a opção que lista as variáveis locais e compare as duas metades:
#
#   pytest test_aula08_desconto.py -l
#
# No primeiro, o pytest imprime o conteúdo de cada variável com o nome que você
# deu, e você lê o relatório sabendo qual era a entrada, qual era a expectativa
# e o que veio. No segundo, sai "assert 20 == 25" e nada mais, porque não existe
# variável nenhuma para listar.
#
# Os dois dizem QUE falhou. Só o primeiro diz POR QUE. Custa três linhas.
#
# A regra prática: dê nome ao dado de entrada, ao esperado e ao obtido. Quem vai
# ler isso na esteira de integração às onze da noite não vai abrir o seu código.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cliente VIP acima de 200 tem 20% de desconto. Estes dois testes cobram 25,
#   e é essa diferença que produz o vermelho.
from aula08_desconto import calcular_desconto


def test_desconto_de_cliente_vip():
    valor_compra = 300.00
    desconto_esperado = 25
    desconto_obtido = calcular_desconto(valor_compra, cliente_vip=True)
    assert desconto_obtido == desconto_esperado


def test_desconto_de_cliente_vip_sem_variaveis():
    assert calcular_desconto(300.00, True) == 25

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-16.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 16 da apresentacao.
#
#      24  from aula08_desconto import calcular_desconto
#          A regra CA-018 da Aula 03, embalada em função. Ela devolve 20 para
#          VIP acima de 200, que é o que a regra do curso sempre disse.
#
#      27  def test_desconto_de_cliente_vip():
#          A versão com variáveis nomeadas. Três linhas a mais que a outra.
#
#      28  valor_compra = 300.00
#          O dado de entrada, com nome.
#
#      29  desconto_esperado = 25
#          O esperado, com nome. E ele está errado de propósito: a regra diz
#          20.
#
#      30  desconto_obtido = calcular_desconto(valor_compra, cliente_vip=True)
#          O obtido, com nome. cliente_vip=True é parâmetro por nome, o que
#          deixa a chamada legível sem precisar lembrar a ordem.
#
#      31  assert desconto_obtido == desconto_esperado
#          20 == 25. Reprova. E as três variáveis das linhas 28, 29 e 30 ainda
#          existem quando ele reprova, que é o ponto do slide.
#
#      34  def test_desconto_de_cliente_vip_sem_variaveis():
#          A mesma pergunta, em uma linha.
#
#      35  assert calcular_desconto(300.00, True) == 25
#          20 == 25. Reprova igual. Mas aqui não existe variável nenhuma para
#          o relatório listar: os valores nascem e morrem dentro da própria
#          linha.
#
# --- fim da explicacao linha a linha ---
