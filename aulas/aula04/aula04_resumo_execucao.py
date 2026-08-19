# Aula 04 - o resumo de uma execução de suíte (demonstração guiada 2)
#
# Cinco casos de teste. A primeira lista diz o resultado de cada um, a
# segunda diz quantos segundos cada um levou, na mesma ordem.
#
# Três coisas que este arquivo tem e a catraca não tinha:
#   1. Dois contadores em vez de um, aprovados e falhas.
#   2. Um percentual calculado a partir deles.
#   3. Um acumulador que guarda o maior valor visto, em vez de somar.
#
# Por que mais_lento começa valendo tempos[0] e não zero: zero só funciona
# se você souber de antemão que nenhum valor da lista é negativo. Aqui você
# sabe, porque duração não é negativa, e é justamente por isso que o exemplo
# engana: o hábito passa para o próximo detector, onde o dado pode ser saldo
# ou variação, e aí o zero vence a comparação e o detector devolve um valor
# que não está na lista. Começar pelo primeiro item não supõe nada sobre o
# dado, e o campeão inicial é sempre um candidato real.
#
# Este é o formato dos números que aparecem no relatório de execução que
# você lê no trabalho: total, aprovados, falhas, percentual e o mais lento.

resultados = ["passou", "falhou", "passou", "passou", "falhou"]
tempos = [1.20, 0.80, 3.45, 1.10, 2.90]

total = len(resultados)
aprovados = 0
falhas = 0

for resultado in resultados:
    if resultado == "passou":
        aprovados = aprovados + 1
    else:
        falhas = falhas + 1

percentual = (aprovados / total) * 100

mais_lento = tempos[0]
for tempo in tempos:
    if tempo > mais_lento:
        mais_lento = tempo

print(f"Total de testes: {total}")
print(f"Aprovados: {aprovados}")
print(f"Falhas: {falhas}")
print(f"Percentual de aprovação: {percentual:.1f}%")
print(f"Tempo do teste mais lento: {mais_lento:.2f}s")

assert aprovados + falhas == total, f"esperado {total}, obtido {aprovados + falhas}"
assert percentual == 60.0, f"esperado 60.0, obtido {percentual}"
assert mais_lento == 3.45, f"esperado 3.45, obtido {mais_lento}"
print("Todas as verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Fonte: curso-vertex/Aulas/Aula04-Uma-Massa-Varios-Cenarios/
#        explicacao-linha-a-linha/slide-24.md
# Para mudar o texto, edite o .md e rode
# curso-vertex/scripts/embutir_explicacao_no_codigo.py de novo.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 24 da apresentacao.
#
#      22  resultados = [...]
#          Cinco casos de teste, três aprovados.
#
#      23  tempos = [1.20, 0.80, 3.45, 1.10, 2.90]
#          Os tempos, na mesma ordem dos resultados. Duas listas paralelas, e
#          a ordem é o que amarra uma na outra.
#
#      25  total = len(resultados)
#          Cinco. Vem da massa, não de contar na mão.
#
#      26  aprovados = 0
#          Contador criado antes do laço.
#
#      27  falhas = 0
#          Segundo contador, e é o que muda em relação à catraca.
#
#      29  for resultado in resultados:
#          Cinco voltas.
#
#      30  if resultado == "passou":
#
#      31  aprovados = aprovados + 1
#          Sobe numa volta.
#
#      32  else:
#
#      33  falhas = falhas + 1
#          Sobe na outra. Como todo caso cai num dos dois, a soma dos dois
#          fecha o total, e é isso que a linha 48 confere.
#
#      35  percentual = (aprovados / total) * 100
#          Depois do laço, com os números já fechados. Três dividido por cinco
#          dá 0.6, vezes 100 dá 60.0.
#
#      37  mais_lento = tempos[0]
#          O acumulador começa valendo o primeiro item da própria lista, não
#          zero.
#
#      38  for tempo in tempos:
#          Segundo laço, sobre a outra lista.
#
#      39  if tempo > mais_lento:
#          Compara com o campeão atual.
#
#      40  mais_lento = tempo
#          Troca o campeão. Aqui não se soma nada: guarda-se o maior visto até
#          agora.
#
# 42 a 46  os cinco print
#          O relatório na tela, com :.1f no percentual e :.2f no tempo, que é
#          a formatação da Aula 02.
#
#      48  assert aprovados + falhas == total, ...
#          Coerência: nenhum caso ficou de fora da contagem.
#
#      49  assert percentual == 60.0, ...
#          O número que vai para o relatório.
#
#      50  assert mais_lento == 3.45, ...
#          O detector achou o valor certo.
#
#      51  print("Todas as verificações passaram")
#          Só chega aqui se as três passarem.
#
# --- fim da explicacao linha a linha ---
