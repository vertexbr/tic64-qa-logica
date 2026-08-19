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
