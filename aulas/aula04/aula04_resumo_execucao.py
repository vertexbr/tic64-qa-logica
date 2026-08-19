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
# Por que mais_lento começa valendo tempos[0] e não zero: zero funciona
# por acidente enquanto todos os tempos são positivos, e falha feio no dia
# em que a lista tem valor negativo. Começar pelo primeiro item da própria
# lista é o jeito honesto.
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
