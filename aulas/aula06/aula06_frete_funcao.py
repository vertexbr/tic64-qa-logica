# Aula 06 - o mesmo problema com função
#
# Compare com aula06_regra_repetida.py: aquele arquivo tem a regra escrita três
# vezes, este tem ela escrita uma. Se o negócio mudar 250 para 199, aqui você
# edita uma linha e os três clientes obedecem.
#
# Esse é o valor todo da função, e ele não é estético: é o número de lugares
# que você precisa editar quando a regra muda.

def calcular_frete(subtotal):
    if subtotal >= 250:
        return 0.0
    return 20.0


print(f"Frete da Ana:  R$ {calcular_frete(199.90 * 3):.2f}")
print(f"Frete do Beto: R$ {calcular_frete(49.90):.2f}")
print(f"Frete da Cris: R$ {calcular_frete(89.90 * 2):.2f}")

# Três cenários verificados sem copiar nenhuma linha de lógica, incluindo o
# 250 exato, que é a fronteira da regra. É a primeira vez no curso que isso
# acontece: até a Aula 05, verificar três cenários exigia três blocos.
assert calcular_frete(300.00) == 0.0
assert calcular_frete(100.00) == 20.0
assert calcular_frete(250.00) == 0.0
print("As três verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-05.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 5 da apresentacao.
#
#      10  def calcular_frete(subtotal):
#          def avisa que vem uma definição. Depois o nome, depois os
#          parênteses com o parâmetro, depois dois-pontos, e o corpo
#          indentado, como no if e no for. Nada roda nesta linha: a função
#          fica guardada esperando alguém chamar.
#
#      11  if subtotal >= 250:
#          A regra do negócio, e é a mesma linha que estava escrita três vezes
#          no arquivo anterior. O >= inclui o 250, e é isso que o terceiro
#          assert cobra.
#
#      12  return 0.0
#          Entrega 0.0 a quem chamou e encerra a função ali. As linhas abaixo
#          não rodam nesta passagem.
#
#      13  return 20.0
#          O outro caminho. Repare que não há else: se o if fosse verdadeiro,
#          o return de cima já teria encerrado a função. Escrever else aqui
#          funciona e não está errado; não escrever é o que o retorno
#          antecipado permite, e é assunto do slide 11.
#
#      14  Linha em branco
#          Separa a definição do uso.
#
#      15  Linha em branco
#          Duas linhas em branco entre uma função e o código que a segue é
#          convenção de Python, não capricho do editor.
#
#      16  print(f"Frete da Ana:  R$ {calcular_frete(199.90 * 3):.2f}")
#          Primeira chamada. O 199.90 * 3 é calculado antes de entrar na
#          função, então o que chega no parâmetro subtotal é 599.70. Sai R$
#          0.00.
#
#      17  print(f"Frete do Beto: R$ {calcular_frete(49.90):.2f}")
#          Segunda chamada, mesma função, argumento diferente. Sai R$ 20.00.
#
#      18  print(f"Frete da Cris: R$ {calcular_frete(89.90 * 2):.2f}")
#          Terceira chamada. 179.80 não alcança 250, então sai R$ 20.00. Três
#          clientes, uma regra.
#
#      19  Linha em branco
#          Separa os prints das verificações.
#
#      23  assert calcular_frete(300.00) == 0.0
#          Cenário acima da fronteira.
#
#      24  assert calcular_frete(100.00) == 20.0
#          Cenário abaixo da fronteira.
#
#      25  assert calcular_frete(250.00) == 0.0
#          A fronteira exata, e é o assert que vale mais que os outros dois.
#          Se alguém trocar o >= por > na linha 11, só este falha.
#
#      26  print("As três verificações passaram")
#          Se esta linha aparecer, os três assert passaram. Se um falhasse, o
#          programa pararia antes dela.
#
# --- fim da explicacao linha a linha ---
