# Aula 05 - a contagem por chave, nas duas formas
#
# Na Aula 04, para contar aprovados e falhas, vocês criaram um contador para
# cada um. Agora imaginem que o relatório tem sete resultados possíveis:
# passou, falhou, ignorado, bloqueado, instável, não executado, erro de
# ambiente. Sete variáveis? Não.
#
# Aqui o dicionário vira o próprio contador: a chave é o resultado, o valor é
# a catraca daquele resultado. E o mnemônico da Aula 04 continua valendo, com
# dicionário no lugar do número:
#
#   CRIA ANTES -> PERCORRE -> MUDA DENTRO -> USA DEPOIS
#
# contagem = {} é o dicionário vazio, igual à lista vazia do acumulador. Ele
# nasce ANTES da primeira volta. Se ele nascer dentro do for, a contagem dá 1
# em tudo, e é a mesma armadilha do contador da aula passada.
#
# Guardem este arquivo com carinho: esta é a técnica que sustenta o desafio
# final da Aula 15.

resultados = ["passou", "falhou", "passou", "ignorado", "passou", "falhou"]

# --- forma longa: se a chave já existe soma um, se não existe começa em um ---
contagem = {}
for resultado in resultados:
    if resultado in contagem:
        contagem[resultado] = contagem[resultado] + 1
    else:
        contagem[resultado] = 1

print(contagem)

for chave in contagem:
    print(f"{chave}: {contagem[chave]}")

assert contagem["passou"] == 3
assert contagem["falhou"] == 2
assert contagem["ignorado"] == 1
print("Verificações da forma longa passaram")

# --- forma curta: o get ganhando o salário dele ---
# get(resultado, 0) diz "me dá o valor dessa chave, e se ela não existir me dá
# zero", e o zero é justamente o ponto de partida do contador. Uma linha faz o
# que quatro faziam. Aquele get da chave ausente não era detalhe, era isso.
contagem_curta = {}
for resultado in resultados:
    contagem_curta[resultado] = contagem_curta.get(resultado, 0) + 1

print(contagem_curta)
print("As duas formas deram o mesmo resultado")

assert contagem_curta == contagem
assert contagem_curta.get("erro", 0) == 0
print("Verificações da forma curta passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-19.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 19 da apresentacao.
#
#      21  resultados = ["passou", "falhou", "passou", "ignorado", "passou",
#          "falhou"]
#          A massa, e ela é a mesma forma da Aula 04: lista de itens que são
#          vários exemplos da mesma coisa. Três resultados diferentes em seis
#          execuções.
#
#      22  Linha em branco
#          Separa a massa da contagem.
#
#      24  contagem = {}
#          O dicionário vazio, igual à lista vazia do acumulador da Aula 04.
#          Ele nasce ANTES da primeira volta, e é aqui que o mnemônico da aula
#          passada é recuperado: cria antes, percorre, muda dentro, usa
#          depois.
#
#      25  for resultado in resultados:
#          Percorre a lista. A variável do laço é o texto do resultado, e é
#          ele que vira chave.
#
#      26  if resultado in contagem:
#          Pergunta se a chave já existe. É o mesmo in do slide 7, agora
#          decidindo um caminho em vez de imprimir um booleano.
#
#      27  contagem[resultado] = contagem[resultado] + 1
#          A chave já existia: soma um. Leia da direita para a esquerda, como
#          a catraca da Aula 04: pega o valor que estava lá, soma um, e guarda
#          de volta no mesmo lugar.
#
#      28  else:
#          A chave não existia.
#
#      29  contagem[resultado] = 1
#          Primeira aparição deste resultado: começa em um. Não em zero,
#          porque a volta em que a chave nasce já é uma ocorrência.
#
#      30  Linha em branco
#          Separa a contagem da leitura.
#
#      31  print(contagem)
#          Sai {'passou': 3, 'falhou': 2, 'ignorado': 1}. As chaves aparecem
#          na ordem em que apareceram na massa, não em ordem alfabética.
#
#      32  Linha em branco
#          Separa a impressão do dicionário inteiro da leitura item por item.
#
#      33  for chave in contagem:
#          Percorre o dicionário, e entrega as chaves, como no mapa de
#          ambientes do slide 10.
#
#      34  print(f"{chave}: {contagem[chave]}")
#          Sai uma linha por resultado. É o formato de relatório que um QA
#          entrega, e ele saiu de cinco linhas de código.
#
#      35  Linha em branco
#          Separa a leitura das verificações.
#
#      36  assert contagem["passou"] == 3
#          Prova a contagem do resultado mais frequente.
#
#      37  assert contagem["falhou"] == 2
#          Prova a do meio.
#
#      38  assert contagem["ignorado"] == 1
#          Prova a do resultado que apareceu uma vez só, que é o caso em que o
#          else da linha 28 foi o único caminho tomado.
#
#      39  print("Verificações da forma longa passaram")
#          Confirma que os três assert passaram.
#
# --- fim da explicacao linha a linha ---
