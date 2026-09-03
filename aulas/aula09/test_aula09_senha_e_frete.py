# Aula 09 - a solução do segundo bloco, com dois parametrize no mesmo arquivo
#
# Duas regras, dois parametrize, sete testes no relatório. Um arquivo pode ter
# quantos parametrize precisar, e cada um governa só a função abaixo dele.
#
# A massa da senha mistura as duas naturezas de propósito, e é isso que o ids
# deixa legível. As duas primeiras linhas são valor-limite puro: 7 e 8
# caracteres, vizinho e fronteira. As duas últimas são partição de outra
# natureza, porque "sem maiúscula" e "sem número" são grupos de comportamento,
# não vizinhos de número.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Senha vale com 8 ou mais caracteres, ao menos um número e ao menos uma
#   maiúscula. Frete é grátis a partir de R$ 250,00, e 250,00 entra.
import pytest

from aula09_regras import senha_valida, tem_frete_gratis


@pytest.mark.parametrize("senha,esperado", [
    ("Abc1234", False),
    ("Abc12345", True),
    ("abcdefgh1", False),
    ("Abcdefghi", False),
], ids=[
    "sete_caracteres_recusa",
    "oito_caracteres_aceita",
    "sem_maiuscula_recusa",
    "sem_numero_recusa",
])
def test_politica_de_senha(senha, esperado):
    assert senha_valida(senha) == esperado


@pytest.mark.parametrize("total,esperado", [
    (249.99, False),
    (250.00, True),
    (300.00, True),
], ids=[
    "um_centavo_abaixo",
    "exatamente_no_limite",
    "bem_acima",
])
def test_frete_gratis(total, esperado):
    assert tem_frete_gratis(total) == esperado

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-21.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 21 da apresentacao.
#
#      15  import pytest
#
#      17  from aula09_regras import senha_valida, tem_frete_gratis
#          Duas funções do mesmo módulo, separadas por vírgula. É o mesmo from
#          ... import da Aula 06.
#
#      20  @pytest.mark.parametrize("senha,esperado", [
#          O primeiro decorador. Ele alcança a função da linha 31 e mais
#          nenhuma.
#
#      21  ("Abc1234", False),
#          Sete caracteres. Valor-limite: é o vizinho de baixo da fronteira de
#          8.
#
#      22  ("Abc12345", True),
#          Oito caracteres. A fronteira, e ela entra, porque a regra diz "8 ou
#          mais".
#
#      23  ("abcdefgh1", False),
#          Nove caracteres, tem número, e não tem maiúscula. Partição de outra
#          natureza: não é vizinho de número nenhum, é um grupo de
#          comportamento.
#
#      24  ("Abcdefghi", False),
#          Nove caracteres, tem maiúscula, e não tem número. O outro grupo.
#
#      25  ], ids=[
#
#      26  "sete_caracteres_recusa",
#          O nome diz o que a linha exercita, não o valor dela.
#
#      27  "oito_caracteres_aceita",
#
#      28  "sem_maiuscula_recusa",
#
#      29  "sem_numero_recusa",
#
#      30  ])
#
#      31  def test_politica_de_senha(senha, esperado):
#
#      32  assert senha_valida(senha) == esperado
#
# --- fim da explicacao linha a linha ---
