# Aula 06 - as três partes de uma função, e "definir não executa"
#
# Toda função tem três partes, e elas acontecem sempre nesta ordem:
# RECEBE, CALCULA, DEVOLVE. Guardem essa sequência, porque ela é o que fica na
# cabeça quando vocês olharem para uma função pela primeira vez. Ela está
# escrita no comentário de cada linha aqui embaixo.
#
# A fronteira dela: isto vale para função de um caminho só. Validação tem
# vários, e ela pode devolver antes de terminar de calcular. Isso tem nome, é
# retorno antecipado, e é assunto de outro arquivo desta mesma aula.
#
# A segunda metade do arquivo prova a coisa que confunde todo mundo uma vez:
# definir uma função NÃO executa ela. O def apenas guarda a receita com um
# nome; quem faz a receita virar bolo é a chamada, com os parênteses.

def calcular_frete(subtotal):    # RECEBE
    if subtotal >= 250:          # CALCULA
        return 0.0               # DEVOLVE
    return 20.0                  # DEVOLVE, pelo outro caminho


def nunca_chamada(valor):
    print(f"Se isto aparecer, a função executou: {valor}")
    return valor * 2


# Acima existem DUAS funções definidas. Só uma é chamada, e a linha abaixo é a
# chamada: nome, parênteses, e o argumento dentro dos parênteses. O 300 é o
# argumento; o subtotal lá em cima é o parâmetro. Parâmetro é o nome na
# definição, argumento é o valor na chamada, e é só isso que separa as duas
# palavras.
print(f"Frete de 300: R$ {calcular_frete(300.00):.2f}")

# A nunca_chamada foi definida e nunca chamada, então nada dela aparece na
# tela. Repare também que a linha abaixo NÃO chama nada: sem os parênteses,
# ela só menciona o nome da função, e o Python não reclama disso.
nunca_chamada
print("O arquivo terminou, e a nunca_chamada não imprimiu nada")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-06.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 6 da apresentacao.
#
#      16  def calcular_frete(subtotal):    # RECEBE
#          Nada executa. O Python cria um nome, calcular_frete, e amarra nele
#          o corpo indentado. O comentário da calha é para a turma ler, não
#          para o Python.
#
#      17  if subtotal >= 250:          # CALCULA
#          Não executa agora. Vai executar uma vez, quando a linha 32 chamar.
#
#      18  return 0.0               # DEVOLVE
#          Idem.
#
#      19  return 20.0                  # DEVOLVE, pelo outro caminho
#          Idem. Duas saídas, e é a mesma função do arquivo anterior.
#
#      22  def nunca_chamada(valor):
#          Segundo nome criado, segundo corpo guardado. Nada executa nesta
#          linha também.
#
#      23  print(f"Se isto aparecer, a função executou: {valor}")
#          Esta linha nunca roda em nenhuma execução deste arquivo, e o texto
#          dela existe para deixar isso óbvio se um dia rodar.
#
#      24  return valor * 2
#          Nunca roda.
#
#      32  print(f"Frete de 300: R$ {calcular_frete(300.00):.2f}")
#          A primeira coisa que executa no arquivo. A chamada acontece
#          primeiro, com subtotal valendo 300.00; ela devolve 0.0; o :.2f
#          formata para 0.00; o print escreve a linha.
#
#      37  nunca_chamada
#          Executa e não faz nada visível. O Python avalia o nome, encontra o
#          objeto função, descarta o resultado e segue. Sem os parênteses não
#          há chamada.
#
#      38  print("O arquivo terminou, e a nunca_chamada não imprimiu nada")
#          Segunda e última linha de saída.
#
# --- fim da explicacao linha a linha ---
