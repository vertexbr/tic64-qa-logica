# Aula 08 - o módulo do produto, que é o que vai ser testado
#
# Este arquivo NÃO é um teste. Ele é o produto: as duas regras que a loja
# precisa que funcionem. Quem testa é o test_aula08_regras.py, ao lado.
#
# A separação é a primeira coisa da aula: um arquivo com a regra, outro com a
# verificação da regra. Até hoje as duas moravam juntas, e o assert ficava
# colado no fim do mesmo arquivo, como em aulas/aula06/aula06_funcoes_da_loja.py.
#
# O nome não tem test_ na frente de propósito. Se tivesse, o pytest tentaria
# rodar as funções daqui como se fossem casos de teste.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos, e 18 entra. Só admin e gerente
#   têm permissão de administração; qualquer outro perfil não tem.


def validar_idade_minima(idade):
    return idade >= 18


def tem_permissao(perfil):
    return perfil in ["admin", "gerente"]

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-04.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 4 da apresentacao.
#
#      18  def validar_idade_minima(idade):
#          Nada executa. Um parâmetro fica guardado com o corpo, esperando
#          alguém chamar. É a Aula 06 inteira em uma linha.
#
#      19  return idade >= 18
#          Devolve um booleano, nunca um número. idade >= 18 já é True ou
#          False antes de o return tocar nele: a comparação acontece primeiro,
#          o return só entrega o resultado. Quem escreve if idade >= 18:
#          return True está fazendo a mesma coisa em três linhas.
#
#      20  Linha em branco
#
#      21  Linha em branco
#          Duas linhas entre funções é a convenção do Python, e o PyCharm
#          reclama com um aviso amarelo se você deixar uma só.
#
#      22  def tem_permissao(perfil):
#          Também função-pergunta, e também devolve booleano.
#
#      23  return perfil in ["admin", "gerente"]
#          O in da Aula 05, que lá procurava chave em dicionário e código de
#          status em lista. Aqui ele procura texto numa lista de dois itens e
#          devolve True ou False. A lista é criada e jogada fora a cada
#          chamada, e para dois itens isso não custa nada.
#
# --- fim da explicacao linha a linha ---
