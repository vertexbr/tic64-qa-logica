# Aula 04 - o bug de lógica, o único dos três tipos que não grita
#
# Este arquivo é a catraca com a linha do incremento comentada. Repare no
# que acontece: não tem erro de sintaxe, não quebra, roda até o fim, e
# entrega o número errado.
#
# Os três tipos de erro, e por que este é o pior:
#   Erro de sintaxe   - o Python recusa o arquivo e mostra a linha.
#   Erro de execução  - o programa morre no meio e mostra o traceback.
#   Erro de lógica    - roda até o fim, sem reclamar, com o número errado.
#
# É o tipo de defeito que a automação existe para caçar. Sem a verificação
# do fim, este arquivo passaria batido e o relatório sairia com zero por
# cento de aprovação numa execução que teve dois testes aprovados.

aprovados = 0
resultados = ["passou", "falhou", "passou"]

for resultado in resultados:
    if resultado == "passou":
        # aprovados = aprovados + 1
        print("achei um que passou")

print(f"aprovados = {aprovados}")

# A condição funcionou: o print de dentro do if apareceu duas vezes. O que
# faltou foi mudar a variável. A verificação é o que transforma um número
# errado, que ninguém notaria, em erro visível.
try:
    assert aprovados == 2, f"esperado 2, obtido {aprovados}"
    print("esta linha não chega a ser impressa")
except AssertionError as erro:
    print(f"AssertionError: {erro}")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Fonte: curso-vertex/Aulas/Aula04-Uma-Massa-Varios-Cenarios/
#        explicacao-linha-a-linha/slide-17.md
# Para mudar o texto, edite o .md e rode
# curso-vertex/scripts/embutir_explicacao_no_codigo.py de novo.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 17 da apresentacao.
#
#      16  aprovados = 0
#          Igual ao arquivo anterior.
#
#      17  resultados = ["passou", "falhou", "passou"]
#          Mesma massa: duas execuções aprovadas.
#
#      19  for resultado in resultados:
#          Mesmas três voltas.
#
#      20  if resultado == "passou":
#          A condição funciona perfeitamente, e é isso que engana.
#
#      21  # aprovados = aprovados + 1
#          A linha comentada. O # a transforma em texto: o Python não a
#          executa e não reclama de nada.
#
#      22  print("achei um que passou")
#          Aparece duas vezes na saída, provando que o if está certo. É essa
#          prova que faz o defeito parecer impossível.
#
#      24  print(f"aprovados = {aprovados}")
#          Sai zero. O programa não tem opinião sobre isso estar certo ou
#          errado.
#
#      29  try:
#          Existe para o arquivo seguir até o fim depois da falha. Num arquivo
#          de verdade a verificação não vem embrulhada.
#
#      30  assert aprovados == 2, f"esperado 2, obtido {aprovados}"
#          A verificação com mensagem. É ela que transforma um número errado,
#          que ninguém notaria, em erro visível.
#
#      32  except AssertionError as erro:
#          Captura a falha.
#
#      33  print(f"AssertionError: {erro}")
#          Imprime a mensagem escrita na linha 30.
#
# --- fim da explicacao linha a linha ---
