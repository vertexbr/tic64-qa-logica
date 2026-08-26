# Aula 06 - print contra return, o momento mais importante da aula
#
# As duas funções somam dois mais dois, e as duas parecem funcionar. Rode antes
# de ler o resto deste comentário e olhe as três linhas da saída.
#
# print fala em voz alta; return entrega um documento. Quem estava ouvindo
# escutou o 4, mas ninguém tem papel na mão para levar embora. A consequência
# de QA é o ponto todo: teste precisa de valor para comparar, e teste contra
# None é teste contra o nada.

def soma_com_print(a, b):
    print(a + b)


def soma_com_return(a, b):
    return a + b


resultado_print = soma_com_print(2, 2)
resultado_return = soma_com_return(2, 2)

print(f"Com print, resultado_print vale: {resultado_print}")
print(f"Com return, resultado_return vale: {resultado_return}")

# Agora o erro que fecha o assunto. Usar numa conta o retorno de uma função que
# não retorna produz um nome de erro que vocês vão ver muito: NoneType.
#
# AVISO: este try/except existe para o arquivo seguir até o fim e mostrar o
# erro na mesma execução. Numa suíte de verdade a falha interrompe, e engolir
# exceção é o oposto de verificar.
try:
    print(resultado_print * 10)
except TypeError as erro:
    print(f"TypeError: {erro}")

# O return é o que faz a conta ser possível.
print(f"E com return a mesma conta funciona: {resultado_return * 10}")

assert resultado_print == None
assert resultado_return == 4
print("As duas verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-07.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 7 da apresentacao.
#
#      11  def soma_com_print(a, b):
#          Dois parâmetros. Nada executa: o corpo fica guardado.
#
#      12  print(a + b)
#          Quando chamada, soma, escreve o resultado na tela, e termina sem
#          return. Função que termina sem return devolve None, sempre, e isso
#          é regra da linguagem e não acidente deste arquivo.
#
# 15 e 16  def soma_com_return(a, b): e return a + b
#          Mesma soma, e o valor é entregue a quem chamou em vez de escrito.
#
#      19  resultado_print = soma_com_print(2, 2)
#          Duas coisas na mesma linha: a função escreve 4 na tela, e
#          resultado_print recebe o que ela devolveu, que é None. A linha de
#          saída aparece antes de a variável existir.
#
#      20  resultado_return = soma_com_return(2, 2)
#          Nada aparece na tela, e resultado_return fica valendo 4.
#
#      22  print(f"Com print, resultado_print vale: {resultado_print}")
#          Sai None. O f de f-string converte para texto o que encontrar,
#          inclusive a ausência de valor.
#
#      23  print(f"Com return, resultado_return vale: {resultado_return}")
#          Sai 4.
#
#      31  try:
#          Recurso didático, e ele precisa ser dito em voz alta: existe para o
#          erro e a correção caberem na mesma execução. Numa suíte de verdade
#          a falha interrompe.
#
#      32  print(resultado_print * 10)
#          None * 10 não existe em Python. A multiplicação levanta TypeError
#          antes de o print receber qualquer coisa, então esta linha não
#          escreve nada.
#
#      33  except TypeError as erro:
#          Captura o erro e amarra ele ao nome erro.
#
#      34  print(f"TypeError: {erro}")
#          Escreve a mensagem do erro. O texto dela nomeia o tipo do valor que
#          faltou: NoneType.
#
#      37  print(f"E com return a mesma conta funciona: {resultado_return *
#          10}")
#          4 * 10 dá 40. Mesma conta, outro valor de entrada, e é a prova do
#          outro lado.
#
#      39  assert resultado_print == None
#          Passa. É a única verificação possível contra a função que só
#          imprime, e ela não verifica comportamento nenhum.
#
#      40  assert resultado_return == 4
#          Passa, e este compara um valor com o esperado.
#
#      41  print("As duas verificações passaram")
#          Sexta e última linha de saída.
#
# --- fim da explicacao linha a linha ---
