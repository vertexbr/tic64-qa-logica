# Aula 08 - a suíte da loja, e o defeito que só o teste do limite encontra
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO. Cinco passam e um falha, e o
# que falha achou um defeito de verdade no produto.
#
# Os seis testes saíram da REGRA escrita, não do código. É por isso que o
# test_frete_gratis_no_limite existe: a regra diz "frete grátis A PARTIR de
# 250,00", então 250,00 exato tem que ter frete grátis. O aula08_loja.py diz
# > 250.00, que exclui o próprio 250. O cliente que gasta exatamente duzentos e
# cinquenta reais paga frete e liga para o suporte.
#
# Aplique a heurística do dia no vermelho que sai daqui: o erro é
# AssertionError, então o código rodou até o fim e o resultado veio diferente do
# esperado. Suspeite do produto. E o produto está errado mesmo; a correção é
# trocar > por >=, e é uma tecla.
#
# O último teste fecha uma conta aberta na Aula 02: 99,90 com 10% de desconto dá
# 89,91 na sua cabeça e 89,91000000000001 em ponto flutuante. O pytest.approx
# compara com tolerância, e é a resposta que ficou prometida seis aulas atrás.
#
# Por que 250 e não 249 nem 251? A pergunta tem nome técnico e é a Aula 09.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O total é valor vezes quantidade, menos o desconto em reais. O frete é
#   grátis A PARTIR de 250,00, e 250,00 exato tem frete grátis.
import pytest

from aula08_loja import calcular_total, tem_frete_gratis, aplicar_desconto


def test_total_sem_desconto():
    assert calcular_total(100, 3) == 300


def test_total_com_desconto():
    assert calcular_total(100, 3, 50) == 250


def test_frete_gratis_acima_de_250():
    assert tem_frete_gratis(300) == True


def test_sem_frete_gratis_abaixo_de_250():
    assert tem_frete_gratis(100) == False


def test_frete_gratis_no_limite():
    total_no_limite = 250.00
    assert tem_frete_gratis(total_no_limite) == True


def test_desconto_aplicado_com_centavos():
    resultado = aplicar_desconto(99.90, 10)
    assert resultado == pytest.approx(89.91)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-21.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 21 da apresentacao.
#
#      26  import pytest
#          A primeira vez no curso que a turma importa o pytest dentro de um
#          teste. Nos arquivos anteriores ele só rodava o arquivo; aqui ele é
#          usado, na linha 54.
#
#      28  from aula08_loja import calcular_total, tem_frete_gratis,
#          aplicar_desconto
#          As três funções do slide 20.
#
#      31  def test_total_sem_desconto():
#
#      32  assert calcular_total(100, 3) == 300
#          Dois argumentos, e o terceiro vem do valor padrão. 100 * 3 - 0.0 dá
#          300.0, e 300.0 == 300 é True em Python: o tipo é diferente e o
#          valor é o mesmo.
#
#      35  def test_total_com_desconto():
#
#      36  assert calcular_total(100, 3, 50) == 250
#          Agora com o terceiro. Cinquenta reais, não cinquenta por cento.
#
#      39  def test_frete_gratis_acima_de_250():
#          O lado de cima da fronteira.
#
#      40  assert tem_frete_gratis(300) == True
#          Passa com > e passaria com >=. Este teste não distingue as duas
#          versões.
#
#      43  def test_sem_frete_gratis_abaixo_de_250():
#          O lado de baixo.
#
#      44  assert tem_frete_gratis(100) == False
#          Passa com as duas também.
#
#      47  def test_frete_gratis_no_limite():
#          O teste que ganha a aula. É o único dos três de frete que distingue
#          > de >=.
#
#      48  total_no_limite = 250.00
#          Variável nomeada, pela regra do slide 16.
#
#      49  assert tem_frete_gratis(total_no_limite) == True
#          250 > 250 é False, e o esperado é True. Reprova, e reprova com
#          razão.
#
#      52  def test_desconto_aplicado_com_centavos():
#
#      53  resultado = aplicar_desconto(99.90, 10)
#          99.90 - 9.99, que na sua cabeça dá 89.91.
#
#      54  assert resultado == pytest.approx(89.91)
#          Em ponto flutuante o resultado é 89.91000000000001. pytest.approx
#          compara com tolerância, e é a resposta que a Aula 02 deixou
#          prometida.
#
# --- fim da explicacao linha a linha ---
