# Aula 08 - o teste que faz três coisas, e por que ele não serve
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO. A falha é o conteúdo, e não
# tem conserto: ela existe para mostrar duas coisas de uma vez.
#
# A primeira: o pytest PARA no primeiro assert que falha, e os seguintes daquela
# função não rodam. O terceiro assert aqui também está errado e não aparece em
# lugar nenhum do relatório. Em casa isso vira a sensação de ter criado defeito
# novo depois de consertar o primeiro: você não criou, só chegou no segundo.
#
# A segunda: teste que valida três coisas não diz qual delas quebrou. Você lê o
# relatório, vê um nome vermelho, e ainda precisa abrir o código para descobrir.
# A versão certa é uma função por comportamento, como no test_aula08_regras.py,
# onde o nome do teste já é o diagnóstico.
#
# PREPARA, AGE, VALIDA, ACABOU. Depois de validar, o teste acabou. Se você
# precisa agir de novo, é outro teste.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos. Só admin e gerente têm permissão de
#   administração; visitante não tem.
from aula08_regras import validar_idade_minima, tem_permissao


def test_tres_validacoes_no_mesmo_teste():
    assert validar_idade_minima(20) == True
    assert tem_permissao("visitante") == True
    assert tem_permissao("admin") == False

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-11.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 11 da apresentacao.
#
#      22  from aula08_regras import validar_idade_minima, tem_permissao
#          As mesmas duas funções do slide 4, sem alteração nenhuma. O produto
#          está certo; o problema é a forma do teste.
#
#      25  def test_tres_validacoes_no_mesmo_teste():
#          Um teste, três validações. O nome é honesto sobre o defeito, e no
#          relatório ele é a única coisa que aparece.
#
#      26  assert validar_idade_minima(20) == True
#          True == True. Passa, em silêncio, e a execução continua para a
#          linha seguinte.
#
#      27  assert tem_permissao("visitante") == True
#          False == True. Aqui o Python levanta AssertionError e a função
#          morre. Nada abaixo desta linha executa.
#
#      28  assert tem_permissao("admin") == False
#          True == False, que também está errado e nunca é avaliado. Esta
#          linha é a lição do slide.
#
# --- fim da explicacao linha a linha ---
