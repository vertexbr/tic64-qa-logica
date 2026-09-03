# Aula 09 - a tabela de decisão virando massa, sem perder nada
#
# Duas condições de sim ou não dão quatro combinações, e cada linha da tabela
# é um caso de teste. A terceira coluna da tabela é o resultado esperado, e é
# ela que vira o último parâmetro de cada linha da massa.
#
# É aqui que o erro grave fica visível: massa que mistura dado válido com dado
# inválido e aceita vermelho como normal destrói a suíte, porque no dia em que
# aparecer uma falha de verdade ninguém vai olhar. Com o esperado na linha,
# TODAS as quatro passam, e vermelho volta a significar defeito.
#
# Repare também que duas combinações diferentes têm o mesmo esperado, zero.
# Isso também é informação: a condição de valor só importa para quem é VIP.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cliente VIP com compra acima de R$ 200,00 recebe 20% de desconto. Cliente
#   VIP em compra de até R$ 200,00 recebe 10%. Cliente comum não recebe nada.
import pytest

from aula09_regras import desconto_vip


@pytest.mark.parametrize("cliente_vip,valor_compra,esperado", [
    (True, 300.00, 20),
    (True, 150.00, 10),
    (False, 300.00, 0),
    (False, 150.00, 0),
], ids=[
    "vip_acima_de_200",
    "vip_abaixo_de_200",
    "comum_acima_de_200",
    "comum_abaixo_de_200",
])
def test_tabela_de_decisao_do_desconto(cliente_vip, valor_compra, esperado):
    assert desconto_vip(valor_compra, cliente_vip) == esperado

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-18.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 18 da apresentacao.
#
#      18  import pytest
#          Necessário pelo decorador, como no slide 15.
#
#      20  from aula09_regras import desconto_vip
#          A função tem esse nome, e não calcular_desconto, de propósito:
#          calcular_desconto é o nome que a atividade da Aula 08 fixou, com
#          quatro parâmetros. Dois nomes iguais com assinaturas diferentes
#          numa semana de distância é armadilha.
#
#      23  @pytest.mark.parametrize("cliente_vip,valor_compra,esperado", [
#          Três nomes agora, não dois. Cada tupla abaixo precisa ter
#          exatamente três valores, e é aqui que a contagem tem de bater.
#
#      24  (True, 300.00, 20),
#          VIP e acima de 200. Primeira linha da tabela de decisão.
#
#      25  (True, 150.00, 10),
#          VIP e abaixo de 200.
#
#      26  (False, 300.00, 0),
#          Comum e acima de 200.
#
#      27  (False, 150.00, 0),
#          Comum e abaixo de 200. Mesmo esperado da linha anterior, e isso é
#          informação: a condição de valor só importa para quem é VIP.
#
#      28  ], ids=[
#          Fecha a massa e abre a lista de nomes. O ids é um argumento do
#          parametrize, e não um bloco separado.
#
#      29  "vip_acima_de_200",
#          O nome que vai aparecer entre colchetes no relatório, no lugar de
#          True-300.0-20.
#
#      30  "vip_abaixo_de_200",
#
#      31  "comum_acima_de_200",
#
#      32  "comum_abaixo_de_200",
#
#      33  ])
#          Fecha o ids e fecha a chamada do decorador. A lista de ids precisa
#          ter exatamente o mesmo tamanho da massa.
#
#      34  def test_tabela_de_decisao_do_desconto(cliente_vip, valor_compra,
#          esperado):
#          Os três nomes da linha 23, na mesma ordem.
#
#      35  assert desconto_vip(valor_compra, cliente_vip) == esperado
#          Repare que a ordem dos argumentos na chamada é a da função, e não a
#          da massa: a massa nomeia colunas, a função tem a assinatura dela.
#
# --- fim da explicacao linha a linha ---
