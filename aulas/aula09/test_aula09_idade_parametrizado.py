# Aula 09 - as mesmas cinco linhas, numa função só
#
# Compare com test_aula09_idade_na_mao.py, ao lado: os casos são exatamente os
# mesmos, e o relatório continua mostrando cinco testes. O arquivo tem o mesmo
# número de linhas de código, mas a chamada e o assert aparecem uma vez.
#
# Três coisas novas, e são só três:
#   1. a string "idade,esperado" dá nome às colunas da planilha;
#   2. a lista de tuplas é a massa, uma linha por caso;
#   3. a função de teste recebe esses dois nomes como parâmetros, que é o
#      parâmetro de função da Aula 06 chegando no teste.
#
# O comentário ao lado de cada linha registra por que aquele valor foi usado.
# Escreva a lista antes do código para revisar a escolha sem ruído de sintaxe.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A idade já cadastrada é inteiro não negativo. A partir de 18, libera.
import pytest

from aula09_regras import validar_idade_minima


@pytest.mark.parametrize("idade,esperado", [
    (17, False),    # vizinho de baixo da fronteira
    (18, True),     # a fronteira, e ela entra
    (19, True),     # vizinho de cima
    (0, False),     # representante distante; redundante para cobertura
    (120, True),    # representante distante; redundante para cobertura
])
def test_idade_minima(idade, esperado):
    assert validar_idade_minima(idade) == esperado

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-15.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 15 da apresentacao.
#
#      18  import pytest
#          Agora o arquivo precisa do pytest importado, e não só instalado. O
#          assert é do Python, mas o decorador é do pytest. Esquecer esta
#          linha dá NameError: name 'pytest' is not defined.
#
#      20  from aula09_regras import validar_idade_minima
#          O mesmo import do slide 11, sem mudança.
#
#      23  @pytest.mark.parametrize("idade,esperado", [
#          O decorador. Ele envolve a função abaixo e manda o pytest chamá-la
#          uma vez por linha da massa. A string dá nome às colunas, e esses
#          nomes precisam bater com os parâmetros da linha 30.
#
#      24  (17, False),    # vizinho de baixo da fronteira
#          Primeira linha da massa. Na execução desta linha, idade vale 17 e
#          esperado vale False.
#
#      25  (18, True),     # a fronteira, e ela entra
#
#      26  (19, True),     # vizinho de cima
#
#      27  (0, False),     # representante distante; redundante para cobertura
#          Caso adicional da demonstração, não exigido pela técnica.
#
#      28  (120, True),    # representante distante; redundante para cobertura
#          Mesmo papel na partição aceita.
#
#      29  ])
#          Fecha a lista e fecha a chamada do decorador. O colchete fecha a
#          massa, o parêntese fecha o parametrize.
#
#      30  def test_idade_minima(idade, esperado):
#          Ao contrário das outras funções de teste, esta recebe argumentos.
#          Eles não vêm de fixture: vêm da massa, pelo nome. É o parâmetro de
#          função da Aula 06 chegando no teste.
#
#      31  assert validar_idade_minima(idade) == esperado
#          Uma linha, cinco execuções. Nada aqui sabe qual caso está rodando,
#          e é isso que faz a função caber em uma linha.
#
# --- fim da explicacao linha a linha ---
