# Aula 08 - o primeiro arquivo de teste do curso
#
# Duas convenções, e são as duas únicas coisas que o pytest exige para achar um
# teste: o ARQUIVO começa com test_ e a FUNÇÃO começa com test_. Fora delas o
# pytest não reclama, não dá erro, e diz "collected 0 items".
#
# O assert é o de aulas/aula04/aula04_contagem_assert.py, sem uma vírgula de
# diferença. O acréscimo desta aula é a casa dele: ele saiu do fim de um script
# solto e entrou numa função com nome, que uma ferramenta encontra e roda.
#
# Nenhum teste aqui imprime nada. Teste que passa é silencioso, e quem fala é o
# relatório do pytest.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos, e 18 entra. Só admin e gerente
#   têm permissão de administração; qualquer outro perfil não tem.
from aula08_regras import validar_idade_minima, tem_permissao


def test_maior_de_idade_e_valido():
    # Preparação
    idade = 20
    # Ação
    resultado = validar_idade_minima(idade)
    # Validação
    assert resultado == True


def test_menor_de_idade_e_invalido():
    assert validar_idade_minima(16) == False


def test_admin_tem_permissao():
    assert tem_permissao("admin") == True


def test_visitante_nao_tem_permissao():
    assert tem_permissao("visitante") == False

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-05.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 5 da apresentacao.
#
#      17  from aula08_regras import validar_idade_minima, tem_permissao
#          O Python procura um arquivo aula08_regras.py na mesma pasta e traz
#          as duas funções pelo nome. Se o arquivo não estiver ao lado, aqui é
#          onde sai ModuleNotFoundError, e a execução morre antes de qualquer
#          teste rodar.
#
#  18, 19  Linhas em branco
#
#      20  def test_maior_de_idade_e_valido():
#          O pytest encontra esta função pelo prefixo test_ e a executa. Sem
#          argumento nenhum: o pytest chama funções de teste sem parâmetro.
#
#      21  # Preparação
#          Comentário. Não executa e não muda nada. Está aqui só nesta
#          primeira função, para nomear o padrão.
#
#      22  idade = 20
#          O dado de entrada, com nome. Poderia estar embutido na chamada da
#          linha 24, e o slide 16 mostra o que se perde quando ele está.
#
#      23  # Ação
#
#      24  resultado = validar_idade_minima(idade)
#          A chamada acontece aqui, e o retorno fica guardado. Depois desta
#          linha o produto já fez todo o trabalho dele.
#
#      25  # Validação
#
#      26  assert resultado == True
#          A única linha que pode reprovar. Se resultado == True der
#          verdadeiro, o Python segue calado e a função termina; se der falso,
#          ele levanta AssertionError e o pytest marca o teste como FAILED.
#
#      29  def test_menor_de_idade_e_invalido():
#          Segundo teste. Nome diferente, e é ele que vai aparecer no
#          relatório.
#
#      30  assert validar_idade_minima(16) == False
#          O padrão inteiro em uma linha: prepara, age e valida ao mesmo
#          tempo. Cabe porque o teste é pequeno, e é assim que a maioria fica
#          no dia a dia.
#
#      33  def test_admin_tem_permissao():
#
#      34  assert tem_permissao("admin") == True
#
#      37  def test_visitante_nao_tem_permissao():
#          Este é um teste de cenário negativo, e ele guarda a inversão em que
#          todo iniciante tropeça uma vez.
#
#      38  assert tem_permissao("visitante") == False
#          Ele passa quando o sistema recusa corretamente. Verde aqui
#          significa "o visitante não tem permissão, como eu previ", e não "o
#          visitante entrou".
#
# --- fim da explicacao linha a linha ---
