# Aula 06 - função-comando e função-pergunta
#
# Duas famílias de função, e nomear a diferença resolve a confusão de vez.
#
# Função-comando faz algo e não devolve nada: registrar evidência, imprimir
# relatório, clicar num botão. Você chama e segue.
#
# Função-pergunta devolve uma resposta: a senha é válida? o total é quanto? o
# frete é grátis? Você chama e guarda o resultado.
#
# O teste só conversa com função-pergunta, porque precisa de algo para
# comparar. Função que valida e não devolve nada não é feia: é intestável.

def registrar_evidencia(caso, resultado):
    print(f"[EVIDÊNCIA] {caso}: {resultado}")


def senha_tem_tamanho_minimo(senha):
    return len(senha) >= 8


# A de cima é comando: chamou, apareceu na tela, e nada volta.
registrar_evidencia("login válido", "passou")

# A de baixo é pergunta: chamou, guardou, e agora dá para comparar.
tamanho_ok = senha_tem_tamanho_minimo("JL12345!")
tamanho_curto = senha_tem_tamanho_minimo("JL1234!")

print(f"JL12345! tem 8 ou mais? {tamanho_ok}")
print(f"JL1234! tem 8 ou mais?  {tamanho_curto}")

# E a prova de que a função-comando não serve para o teste: o que ela devolve.
# A linha da evidência aparece na tela, e o que volta é None.
devolvido = registrar_evidencia("senha errada", "passou")
print(f"O que registrar_evidencia devolve: {devolvido}")

# Escrevemos == True e == False de propósito, pela regra de comparação
# explícita da Aula 03: o curso escreve a comparação inteira, sempre.
assert tamanho_ok == True
assert tamanho_curto == False
assert devolvido == None
print("As três verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-10.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 10 da apresentacao.
#
#      14  def registrar_evidencia(caso, resultado):
#          Dois parâmetros, e o nome é verbo. Esta é a família comando: ela
#          faz algo.
#
#      15  print(f"[EVIDÊNCIA] {caso}: {resultado}")
#          Escreve na tela e acabou. Não há return nenhum nesta função, e isso
#          é decisão, não esquecimento: o destino do texto é o olho humano.
#
#      18  def senha_tem_tamanho_minimo(senha):
#          Um parâmetro, e o nome é uma pergunta disfarçada de afirmação. Esta
#          é a família pergunta.
#
#      19  return len(senha) >= 8
#          A comparação >= 8 já produz True ou False, e o return entrega esse
#          valor. Não precisa de if: quem escreve if len(senha) >= 8: return
#          True / else: return False está escrevendo quatro linhas para o que
#          a comparação já faz numa.
#
#      23  registrar_evidencia("login válido", "passou")
#          Chamada de comando. Aparece a linha na tela, e nada é guardado,
#          porque não há nada para guardar.
#
#      26  tamanho_ok = senha_tem_tamanho_minimo("JL12345!")
#          Chamada de pergunta, e o resultado é guardado. Oito caracteres,
#          então tamanho_ok fica True.
#
#      27  tamanho_curto = senha_tem_tamanho_minimo("JL1234!")
#          Sete caracteres. tamanho_curto fica False. É a senha que atravessou
#          o curso inteiro falhando na fronteira.
#
#      29  print(f"JL12345! tem 8 ou mais? {tamanho_ok}")
#          Sai True. Repare que o print está fora da função: a função
#          devolveu, e quem chamou decidiu o que fazer com o valor.
#
#      30  print(f"JL1234! tem 8 ou mais?  {tamanho_curto}")
#          Sai False.
#
#      34  devolvido = registrar_evidencia("senha errada", "passou")
#          Aqui está a prova. A linha da evidência aparece na tela, porque a
#          função rodou, e ao mesmo tempo devolvido recebe o que ela entregou.
#
#      35  print(f"O que registrar_evidencia devolve: {devolvido}")
#          Sai None. Não é bug e não é falha: função sem return devolve None,
#          e é isso que faz dela intestável.
#
#      39  assert tamanho_ok == True
#          Compara a variável, não a chamada.
#
#      40  assert tamanho_curto == False
#          O cenário negativo.
#
#      41  assert devolvido == None
#          O assert mais interessante do arquivo: ele verifica que a função-
#          comando não devolve nada. É a única forma de escrever um teste
#          contra ela, e testar que algo é nada não verifica comportamento
#          nenhum.
#
#      42  print("As três verificações passaram")
#          Fecha a execução.
#
# --- fim da explicacao linha a linha ---
