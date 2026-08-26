# Aula 06 - escopo, ou o que atravessa a parede da função
#
# Um quadrado dentro de outro: o de fora é o programa, o de dentro é a função.
# Quem está dentro consegue ver o que está fora; quem está fora não consegue
# ver o que está dentro. Variável criada dentro da função nasce quando a função
# é chamada e morre quando ela termina.
#
# A única coisa que atravessa a parede é o que o return entrega.
#
# AVISO: os try/except deste arquivo existem para ele seguir até o fim e
# mostrar os dois casos na mesma execução. Numa suíte de verdade a falha
# interrompe, e engolir exceção é o oposto de verificar.

def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    return subtotal


total = calcular_total(10.00, 3)
print(f"Total: {total}")

# O subtotal existiu, fez o trabalho e foi embora. Não é bug: é o escopo
# funcionando. A mensagem do Python diz exatamente isso.
try:
    print(subtotal)
except NameError as erro:
    print(f"NameError: {erro}")


# Agora a parte que confunde de verdade: duas variáveis com o MESMO nome, em
# quadrados diferentes, são coisas diferentes.
def dobrar(valor):
    valor = valor * 2
    return valor


valor = 10
resultado = dobrar(valor)

print(f"Dentro da função o valor virou 20, e devolveu {resultado}")
print(f"Fora da função, valor continua {valor}")

# A regra prática que decide onde a variável mora, e é ela que responde noventa
# por cento das dúvidas de "onde eu declaro isso": dado usado em mais de um
# lugar sobe para parâmetro ou para retorno, e dado usado num lugar só fica
# dentro da função.
assert valor == 10
assert resultado == 20
print("As duas verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-12.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 12 da apresentacao.
#
#      14  def calcular_total(preco, quantidade):
#          Nada executa. Dois parâmetros guardados com o corpo.
#
#      15  subtotal = preco * quantidade
#          Quando chamada, subtotal nasce dentro da função, valendo 30.0. Este
#          nome existe só enquanto a chamada durar.
#
#      16  return subtotal
#          Entrega o valor 30.0. Repare que ele entrega o valor, não a
#          variável: o nome fica para trás, o número vai.
#
#      19  total = calcular_total(10.00, 3)
#          A função roda inteira e termina. subtotal morre neste instante.
#          total fica valendo 30.0, na margem.
#
#      20  print(f"Total: {total}")
#          Sai Total: 30.0. Primeira linha.
#
#      24  try:
#          Recurso didático, e precisa ser dito: sem ele o arquivo pararia
#          aqui e as três últimas linhas nunca apareceriam.
#
#      25  print(subtotal)
#          O Python procura o nome subtotal na margem e não encontra, porque
#          ele nunca existiu aqui. Levanta NameError antes de o print receber
#          nada.
#
# 26 e 27  except NameError as erro: e o print
#          Sai NameError: name 'subtotal' is not defined. Segunda linha, e a
#          mensagem descreve o escopo com precisão.
#
#      32  def dobrar(valor):
#          Terceiro nome de função. Nada executa.
#
#      33  valor = valor * 2
#          Quando chamada, o valor de dentro passa a valer 20. Esta linha
#          reatribui o parâmetro, e o parâmetro é uma variável local como
#          qualquer outra.
#
#      34  return valor
#          Entrega 20.
#
#      37  valor = 10
#          Nasce um valor na margem, valendo 10. Mesmo nome do parâmetro da
#          linha 33, e são duas gavetas diferentes.
#
#      38  resultado = dobrar(valor)
#          O argumento enviado é 10. Dentro, a linha 33 mexe na cópia local.
#          resultado fica 20.
#
#      40  print(f"Dentro da função o valor virou 20, e devolveu {resultado}")
#          Sai 20. Terceira linha.
#
#      41  print(f"Fora da função, valor continua {valor}")
#          Sai 10. Quarta linha, e é a que prova. A função não estragou o
#          valor de fora.
#
#      47  assert valor == 10
#          Passa. Se as duas variáveis fossem a mesma coisa, este falharia.
#
#      48  assert resultado == 20
#          Passa. O que voltou mudou.
#
#      49  print("As duas verificações passaram")
#          Quinta linha.
#
# --- fim da explicacao linha a linha ---
