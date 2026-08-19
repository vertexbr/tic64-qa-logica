# Aula 04 - contar item de lista é asserção de QA, não curiosidade
#
# Este arquivo é a ponte entre a Aula 03 e a de hoje.
#
# Na Aula 03 a evidência saía impressa e alguém precisava ler a tela:
#
#   print(f"esperado: 6 | obtido: {len(produtos)} | confere? {len(produtos) == 6}")
#
# Hoje a mesma comparação sai do print e é entregue ao Python:
#
#   assert len(produtos) == 6
#
# É a mesma comparação, len(produtos) == 6. A diferença está no que
# acontece quando ela dá errado: o print depende de alguém ler a tela, e o
# assert interrompe o programa na hora.
#
# No trabalho manual isso é a conferência que você já faz: abrir a tela de
# listagem e contar os produtos com o olho. O assert é a mesma conferência
# sem depender de ninguém estar olhando.

produtos = ["Camiseta", "Caneca", "Boné", "Mochila", "Adesivo", "Chaveiro"]

print(f"A listagem trouxe {len(produtos)} produtos")

# --- o confere? da Aula 03: a comparação sai na tela e alguém precisa ler ---
print(f"esperado: 6 | obtido: {len(produtos)} | confere? {len(produtos) == 6}")

# --- a mesma comparação, agora com poder de veto ---
assert len(produtos) == 6
print("Verificação passou: a listagem trouxe 6 produtos")

# --- e quando a conta não bate ---
# Trocar o 6 por 7 faz a verificação interromper o programa. O try/except
# está aqui só para o arquivo seguir até o fim.
try:
    assert len(produtos) == 7
    print("esta linha não chega a ser impressa")
except AssertionError as erro:
    print(f"AssertionError sem mensagem: {erro!r}")

# --- o que se perde, e como recuperar ---
# Repare na linha acima: o AssertionError chegou vazio. Ele avisa que a
# conferência falhou e não diz nem o que era esperado nem o que veio. A
# evidência da Aula 03 dizia as duas coisas.
#
# A vírgula depois da comparação devolve isso: o que vem depois dela é a
# mensagem que aparece quando a verificação falha.
try:
    assert len(produtos) == 7, f"esperado 7, obtido {len(produtos)}"
    print("esta linha não chega a ser impressa")
except AssertionError as erro:
    print(f"AssertionError com mensagem: {erro}")

# --- índice negativo: o resultado mais recente da suíte ---
# Menos um é o último, menos dois é o penúltimo. Quando a lista é o
# histórico de execução, execucoes[-1] é o resultado mais recente, e é
# justamente ele que interessa saber se quebrou.
execucoes = ["passou", "passou", "falhou", "passou", "falhou"]

print(f"Resultado mais recente da suíte: {execucoes[-1]}")
print(f"Execução anterior a ela: {execucoes[-2]}")

assert execucoes[-1] == "falhou", f"esperado falhou, obtido {execucoes[-1]}"
print("Verificação passou: a última execução falhou")
