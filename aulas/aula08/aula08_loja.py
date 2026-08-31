# Aula 08 - as três funções da loja, como elas chegaram para testar
#
# ATENÇÃO AO tem_frete_gratis DA LINHA 27. Ele NÃO é a versão que vocês
# escreveram: em aulas/aula06/aula06_funcoes_da_loja.py a comparação é
# >= 250.00, e está certa lá. Aqui ela é > 250.00.
#
# Esta é a versão que chegou do outro lado, e é o defeito plantado da
# demonstração 2. Ele não se anuncia: o arquivo roda, não dá erro nenhum, e a
# função devolve False para exatamente 250,00. Quem escrever o teste a partir da
# REGRA escrita encontra o defeito; quem escrever o teste olhando o código
# escreve um teste que concorda com o erro.
#
# O calcular_total é o total de aulas/aula02/aula02.py com desconto opcional, e
# o aplicar_desconto é a conta de percentual de aulas/aula03/aula03_desconto.py.
# O acréscimo dos dois é a embalagem em função, que é a Aula 06.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O total é valor vezes quantidade, menos o desconto em reais. O frete é
#   grátis A PARTIR de 250,00, e 250,00 exato tem frete grátis.


def calcular_total(valor, quantidade, desconto=0.0):
    return valor * quantidade - desconto


def tem_frete_gratis(total):
    return total > 250.00


def aplicar_desconto(subtotal, percentual):
    return subtotal - (subtotal * percentual / 100)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-20.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 20 da apresentacao.
#
#      22  def calcular_total(valor, quantidade, desconto=0.0):
#          Três parâmetros, e o terceiro tem valor padrão: quem chamar com
#          dois argumentos recebe desconto = 0.0 de graça. É a Aula 06.
#
#      23  return valor * quantidade - desconto
#          Multiplicação primeiro, subtração depois, pela precedência de
#          sempre. Esta linha não valida nada: ela confia que os dois
#          primeiros são número, e é ela que estoura no slide 17.
#
#      26  def tem_frete_gratis(total):
#          Função-pergunta, devolve booleano.
#
#      27  return total > 250.00
#          O defeito. A regra escrita diz "grátis A PARTIR de 250,00", e >
#          exclui o próprio 250. O arquivo roda, não dá erro nenhum, e a
#          função devolve False para exatamente 250,00.
#
#      30  def aplicar_desconto(subtotal, percentual):
#
#      31  return subtotal - (subtotal * percentual / 100)
#          Os parênteses não são decoração: sem eles, subtotal - subtotal *
#          percentual seria calculado antes da divisão e o resultado mudaria.
#          A conta é a mesma de aulas/aula03/aula03_desconto.py.
#
# --- fim da explicacao linha a linha ---
