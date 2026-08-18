# Aula 03 - operadores: matemáticos, de comparação e lógicos

# --- matemáticos ---
# A barra simples sempre devolve float, mesmo em divisão exata.
# A barra dupla é divisão inteira, e o % é o resto da divisão.
print(10 + 5)
print(10 / 5)
print(7 // 2)
print(7 % 2)

# --- comparação ---
# Todo operador de comparação devolve um bool: True ou False, nunca outra coisa.
# Um sinal de igual guarda, dois sinais comparam.
status_code = 200

print(status_code == 200)
print(status_code != 200)
print(status_code < 300)
print(status_code >= 200)

# --- lógicos ---
# and exige as duas verdadeiras, or exige pelo menos uma, not inverte.
bug_corrigido = True
regressao_encontrada = False

print(bug_corrigido and not regressao_encontrada)
print(bug_corrigido or regressao_encontrada)
print(not bug_corrigido)
