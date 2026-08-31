# Aula 08 - a escada de asserções, quatro degraus
#
# Nenhum degrau é conteúdo novo. A igualdade é da Aula 04, o isinstance é o
# type() de aulas/aula02/aula02_tipos_e_nomes.py com outro nome, e os dois
# últimos são o in e o not in de aulas/aula05/aula05_codigos_status.py, onde
# eles conferiam se um código HTTP estava na lista de sucesso.
#
# O acréscimo desta aula é a casa: os quatro moram dentro de uma função de
# teste, e uma ferramenta encontra e roda os quatro.
#
# A lista completa do que se pode asseverar é para CONSULTAR. Estes quatro são
# para guardar, e o primeiro resolve a maioria dos casos que vocês vão escrever.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos. Só admin e gerente têm permissão de
#   administração, e a resposta da validação de idade é sempre verdadeiro ou falso.
from aula08_regras import validar_idade_minima


def test_escada_de_assercoes():
    # 1. igualdade, o degrau que resolve quase tudo
    assert validar_idade_minima(20) == True

    # 2. tipo, quando o formato do dado importa tanto quanto o valor
    assert isinstance(validar_idade_minima(20), bool)

    # 3. presença, o in da Aula 05
    assert "admin" in ["admin", "gerente"]

    # 4. ausência, o not in da mesma aula
    assert "visitante" not in ["admin", "gerente"]

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-08.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 8 da apresentacao.
#
#      17  from aula08_regras import validar_idade_minima
#          Só uma função desta vez, porque só ela é chamada. Importar o que
#          não se usa não quebra nada e polui a leitura.
#
#      20  def test_escada_de_assercoes():
#          Um teste, quatro asserções.
#
#      21  # 1. igualdade, o degrau que resolve quase tudo
#
#      22  assert validar_idade_minima(20) == True
#          Compara valor com valor. É o degrau que resolve a maior parte do
#          que vocês vão escrever, e é o único que a Aula 04 já usava.
#
#      24  # 2. tipo, quando o formato do dado importa
#
#      25  assert isinstance(validar_idade_minima(20), bool)
#          isinstance responde é deste tipo? e devolve True ou False. É o
#          type() da Aula 02 numa forma que serve para asserção. Repare que
#          ele confere o tipo e não o valor: isinstance(False, bool) também é
#          True.
#
#      27  # 3. presença, o in da Aula 05
#
#      28  assert "admin" in ["admin", "gerente"]
#          O in de sempre. Aqui ele não chama função nenhuma: a asserção é
#          sobre a lista, e este degrau existe para nomear a forma.
#
#      30  # 4. ausência, o not in da mesma aula
#
#      31  assert "visitante" not in ["admin", "gerente"]
#          Cuidado com a ordem das palavras: é not in, junto, e não not
#          "visitante" in [...]. As duas funcionam e a segunda é ilegível.
#
# --- fim da explicacao linha a linha ---
