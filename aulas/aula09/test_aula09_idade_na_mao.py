# Aula 09 - os cinco casos escritos na mão, um por função
#
# Este arquivo é a DOR, e a dor é o conteúdo. Ele existe para ficar na tela em
# silêncio por quinze segundos antes de o parametrize aparecer.
#
# Os três primeiros casos cobrem a fronteira: 17, 18 e 19. Os casos 0 e 120
# repetem partições já cobertas e entram apenas para tornar a duplicação visível
# antes da refatoração. Eles não são exigidos pela técnica.
#
# Repare no que muda de uma função para a outra: um número e um True ou False.
# Todo o resto é copiado. Cinco funções para carregar dez valores.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A idade já cadastrada é inteiro não negativo. A partir de 18, libera.
from aula09_regras import validar_idade_minima


def test_idade_17_e_rejeitada():
    assert validar_idade_minima(17) == False


def test_idade_18_e_aceita():
    assert validar_idade_minima(18) == True


def test_idade_19_e_aceita():
    assert validar_idade_minima(19) == True


def test_idade_0_e_rejeitada():
    assert validar_idade_minima(0) == False


def test_idade_120_e_aceita():
    assert validar_idade_minima(120) == True

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-11.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 11 da apresentacao.
#
#      15  from aula09_regras import validar_idade_minima
#          O Python procura aula09_regras.py na mesma pasta e traz a função
#          pelo nome. Se o arquivo não estiver ao lado, sai
#          ModuleNotFoundError aqui, e nenhum dos cinco testes chega a rodar.
#
#      18  def test_idade_17_e_rejeitada():
#          O pytest encontra a função pelo prefixo test_. O nome é o
#          diagnóstico: ele vai aparecer inteiro no relatório.
#
#      19  assert validar_idade_minima(17) == False
#          Prepara, age e valida na mesma linha. validar_idade_minima(17)
#          devolve False, e False == False é verdadeiro, então o Python segue
#          calado.
#
#      22  def test_idade_18_e_aceita():
#          A fronteira. Este é o teste que reprova se alguém trocar o >= por >
#          no produto.
#
#      23  assert validar_idade_minima(18) == True
#
#      26  def test_idade_19_e_aceita():
#          O vizinho de cima. Ele confirma que a partição de aceitação começou
#          de verdade e não parou no 18.
#
#      27  assert validar_idade_minima(19) == True
#
#      30  def test_idade_0_e_rejeitada():
#          Representante distante da fronteira. Repete uma partição já coberta
#          e entra para deixar a duplicação visível.
#
#      31  assert validar_idade_minima(0) == False
#
#      34  def test_idade_120_e_aceita():
#          Outro representante distante. Também é redundante para cobertura.
#
#      35  assert validar_idade_minima(120) == True
#
# --- fim da explicacao linha a linha ---
