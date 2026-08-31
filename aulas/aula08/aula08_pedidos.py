# Aula 08 - o mesmo registrar_item da aula passada, sem uma linha de diferença
#
# É o código de aulas/aula07/aula07_pedidos.py, copiado sem alteração nenhuma.
# O acréscimo desta aula não está no arquivo: está em quem verifica. Lá foram
# nove linhas de try, except, variável de estado e dois assert para provar que
# a função recusou. Aqui as nove viram uma, no test_aula08_recusa.py.
#
# Vale relembrar o reenquadramento da Aula 07, porque ele é o que faz a
# verificação de hoje ter sentido: quando a regra de negócio manda rejeitar, o
# erro é o comportamento ESPERADO. O sistema recusar é o acerto, e quem verifica
# precisa provar que a recusa aconteceu.
#
# Este arquivo é só de funções e não imprime nada quando rodado direto, também
# como o original. Quem usa é o test_aula08_recusa.py.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Item só é registrado com nome preenchido e quantidade positiva; cada recusa
#   diz qual das duas regras foi violada.


def registrar_item(nome, quantidade):
    if nome.strip() == "":
        raise ValueError("nome do item é obrigatório")
    if quantidade <= 0:
        raise ValueError("quantidade precisa ser positiva")
    return f"{quantidade}x {nome.strip()}"
