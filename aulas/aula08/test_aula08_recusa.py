# Aula 08 - as nove linhas da Aula 07 viram uma
#
# Na aula passada, provar que registrar_item recusou quantidade zero custou
# nove linhas em aulas/aula07/aula07_verifica_pedidos.py: uma variável de
# estado começando em False, um try, a chamada, um except que muda a variável
# para True, a mensagem guardada, e dois assert no fim.
#
# Aquelas nove linhas continuam certas e continuam valendo. Elas são o
# mecanismo, e é por isso que a Aula 07 escreveu elas primeiro: quem entendeu o
# mecanismo lê a linha de hoje e sabe exatamente o que ela faz por baixo.
#
# O with pytest.raises(ValueError) diz: eu ESPERO um ValueError aqui dentro. Se
# vier, o teste passa. Se não vier nada, o pytest reprova o teste sozinho, e
# essa é a metade que a gente escreveu na mão semana passada com o
# assert levantou.
#
# O terceiro teste é a falha ao contrário da Aula 07, agora numa linha: a
# quantidade é válida, a função devolve o texto e não levanta erro nenhum, então
# o pytest reprova porque o erro que era esperado NÃO aconteceu.
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO: dois passam e o terceiro falha,
# e é o terceiro que ensina.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Item só é registrado com nome preenchido e quantidade positiva; cada recusa
#   diz qual das duas regras foi violada.
import pytest

from aula08_pedidos import registrar_item


def test_recusa_quantidade_zero():
    with pytest.raises(ValueError):
        registrar_item("Teclado", 0)


def test_recusa_diz_o_motivo():
    with pytest.raises(ValueError) as erro:
        registrar_item("   ", 2)
    assert "nome do item" in str(erro.value)


def test_quantidade_valida_nao_deveria_ser_recusada():
    with pytest.raises(ValueError):
        registrar_item("Teclado", 2)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-22.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 22 da apresentacao.
#
#      27  import pytest
#          Necessário, porque o raises é do pytest e não do Python.
#
#      29  from aula08_pedidos import registrar_item
#          A mesma função da Aula 07, copiada sem uma linha de diferença. O
#          produto não mudou; quem verifica é que mudou.
#
#      32  def test_recusa_quantidade_zero():
#
#      33  with pytest.raises(ValueError):
#          Lê-se: eu espero um ValueError aqui dentro. O with é a mesma
#          palavra que abre arquivo, e o que ela faz é ligar um comportamento
#          na entrada e outro na saída do bloco.
#
#      34  registrar_item("Teclado", 0)
#          A função levanta ValueError. O raises captura, confere que é do
#          tipo pedido, e o teste passa. Sem o with, esse mesmo erro faria o
#          teste falhar.
#
#      37  def test_recusa_diz_o_motivo():
#          Não basta recusar; tem que recusar pelo motivo certo.
#
#      38  with pytest.raises(ValueError) as erro:
#          O as erro guarda o objeto do erro numa variável, para você conferir
#          o conteúdo dele depois do bloco.
#
#      39  registrar_item("   ", 2)
#          Três espaços. Para o usuário é campo vazio; para o código é campo
#          preenchido, e é o nome.strip() da Aula 05 que resolve isso lá
#          dentro.
#
#      40  assert "nome do item" in str(erro.value)
#          Fora do with, e tem que ser: dentro do bloco, a linha depois da que
#          estourou nunca executa. erro.value é o erro em si, str() tira a
#          mensagem dele, e o in da Aula 05 procura o pedaço.
#
#      43  def test_quantidade_valida_nao_deveria_ser_recusada():
#          A falha ao contrário, e é o slide 18 da Aula 07 em uma linha.
#
#      44  with pytest.raises(ValueError):
#          O raises espera um erro.
#
#      45  registrar_item("Teclado", 2)
#          Quantidade válida, nome preenchido. A função devolve "2x Teclado" e
#          não levanta nada. O raises reprova o teste por ausência.
#
# --- fim da explicacao linha a linha ---
