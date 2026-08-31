# Aula 07 - o relatório que imprime a primeira linha e morre na segunda
#
# ESTE ARQUIVO QUEBRA DE PROPÓSITO, e é o único da aula que sai com exit code 1
# junto com o aula07_usa_pedidos.py. Não é descuido: o traceback é o conteúdo do
# dia, ele é a última coisa que aparece, e não existe saída depois dele para
# alguém perder. Rode e leia a mensagem.
#
# As três funções vêm de aulas/aula06/aula06_duas_funcoes.py, com a mesma
# embalagem de função-pergunta que recebe, calcula e devolve. O acréscimo desta
# aula é a massa: o segundo item da lista tem total zero, e é ele que estoura.
#
# Leia o traceback de baixo para cima: a última linha diz O QUE, o andar de
# baixo diz ONDE, e os andares acima dizem QUEM CHAMOU.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A taxa de aprovação é a quantidade de casos que passaram dividida pelo total de
#   casos, em porcentagem. A regra escrita não diz o que fazer quando o total é zero.

def taxa_de_aprovacao(passou, total):
    return passou / total * 100


def resumir_execucao(resultados):
    passou = resultados["passou"]
    total = resultados["total"]
    return f"Aprovação: {taxa_de_aprovacao(passou, total):.1f}%"


def imprimir_relatorio(execucoes):
    for execucao in execucoes:
        print(resumir_execucao(execucao))


execucoes = [
    {"passou": 12, "total": 15},
    {"passou": 0, "total": 0},   # <- este estoura
]

imprimir_relatorio(execucoes)
