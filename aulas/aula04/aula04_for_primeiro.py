# Aula 04 - o for só dá nome a um gesto antigo
#
# Quem já rodou uma suíte de regressão já fez isto à mão: "para cada caso de
# teste da lista, execute o caso". O for é isso escrito em Python. Não é
# conceito novo, é nome novo.
#
# Leia assim: para cada `caso` dentro de `casos_de_teste`, faça o que está
# recuado abaixo.
#
# A palavra `caso` é um nome inventado na hora: é a caixinha que recebe um
# item por volta, e podia ser `item` ou `cenario`. O que não muda são os
# dois-pontos no fim da linha e a indentação embaixo, que são as mesmas
# regras do if da Aula 03.

casos_de_teste = ["login válido", "login com senha errada", "login com usuário bloqueado"]

for caso in casos_de_teste:
    print(f"Executando: {caso}")

# Três voltas, porque a lista tem três itens. Quem decide o número de voltas
# é a lista, não este código: é por isso que, se chegarem quarenta casos, as
# duas linhas acima não mudam em nada.
assert len(casos_de_teste) == 3, f"esperado 3 casos, obtido {len(casos_de_teste)}"
print("Verificação passou: 3 casos percorridos")
