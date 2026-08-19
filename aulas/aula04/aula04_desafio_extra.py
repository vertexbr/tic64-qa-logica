# Aula 04 - desafio extra: os dois comandos no mesmo laço
#
# continue pula os 200 e break mata a varredura no primeiro 500. O último
# 200 da lista nunca chega a ser visitado.
#
# A variável interrompida é o que permite verificar isso com uma linha de
# verificação em vez de ler a tela: sem ela, a única prova de que a
# varredura parou seria a ausência de uma linha impressa, e ausência de
# linha não se compara com nada.

codigos = [200, 200, 404, 500, 200]
interrompida = False

for codigo in codigos:
    if codigo == 200:
        continue
    print(f"Código fora do esperado: {codigo}")
    if codigo >= 500:
        print("Erro de servidor. A suíte foi interrompida.")
        interrompida = True
        break

print(f"Suíte interrompida? {interrompida}")

# A variável já é booleana, então ela decide sozinha e não precisa de
# comparação. Escrever interrompida == True funciona e é redundante.
assert interrompida
print("Verificação passou: a varredura parou no primeiro erro de servidor")
