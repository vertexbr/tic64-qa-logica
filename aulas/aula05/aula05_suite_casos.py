# Aula 05 - a suíte de casos é uma lista de dicionários
#
# Guardem esta forma, porque ela é literalmente uma suíte de casos de teste: a
# lista dá a ordem, o dicionário dá os campos de cada caso.
#
# Toda resposta de listagem de API tem exatamente esta cara, e é por isso que
# ela volta nas Aulas 10 e 11. É também a massa da segunda demonstração de
# hoje.

suite = [
    {"caso": "login válido", "resultado": "passou"},
    {"caso": "senha errada", "resultado": "passou"},
    {"caso": "usuário bloqueado", "resultado": "falhou"},
]

for caso in suite:
    print(f"{caso['caso']}: {caso['resultado']}")

# O índice negativo da Aula 04 continua valendo na lista de fora, e agora ele
# entrega um dicionário, do qual se pega um campo por nome. Dois modos de
# acesso na mesma linha, um por andar.
print(f"Resultado mais recente: {suite[-1]['resultado']}")

assert len(suite) == 3
assert suite[-1]["resultado"] == "falhou"
print("Verificações passaram")
