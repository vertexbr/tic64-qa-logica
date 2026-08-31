# Aula 07 - a função que levanta o erro de propósito
#
# Vocabulário novo, e é o giro conceitual da aula: em programação se diz que a
# função "levanta" um erro. A palavra em inglês é raise, que é levantar. A
# função não sofre o erro, ela o levanta com a mão dela, para avisar quem
# chamou que aquilo não vai dar.
#
# E o reenquadramento que vem com ele: nem todo erro é problema. Quando a regra
# de negócio manda rejeitar, o erro é o comportamento ESPERADO, e quem verifica
# precisa provar que ele aconteceu. Se o sistema aceitar quantidade negativa em
# silêncio, aí sim você tem um defeito. O sistema recusar é o acerto.
#
# O calcular_frete vem de aulas/aula06/aula06_frete_funcao.py, com o mesmo corte
# de 250,00. O acréscimo desta aula é o contraste: ele NÃO valida nada e nunca
# levanta erro, e é justamente essa característica que o
# aula07_verifica_pedidos.py usa para produzir a falha ao contrário.
#
# Este arquivo é só de funções: ele não imprime nada quando rodado direto, e é
# de propósito. Quem usa é o aula07_usa_pedidos.py e o aula07_verifica_pedidos.py.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Item só é registrado com nome preenchido e quantidade positiva; cada recusa diz
#   qual das duas regras foi violada. O frete é grátis a partir de 250,00.


def registrar_item(nome, quantidade):
    if nome.strip() == "":
        raise ValueError("nome do item é obrigatório")
    if quantidade <= 0:
        raise ValueError("quantidade precisa ser positiva")
    return f"{quantidade}x {nome.strip()}"


def calcular_frete(total):
    if total >= 250.00:
        return 0.0
    return 20.0
