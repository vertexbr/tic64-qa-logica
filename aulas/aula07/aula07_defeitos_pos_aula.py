# Aula 07 - ATIVIDADE PÓS-AULA: cinco defeitos plantados
#
# São cinco, e eles não são do mesmo tipo:
#   DOIS DE EXECUÇÃO   o programa para no meio, e o Python te diz onde
#   TRÊS DE LÓGICA     o programa roda até o fim e imprime número errado
#
# Os dois de execução você acha rodando. Os três de lógica só aparecem se você
# declarar o resultado esperado ANTES de rodar. Esse é o exercício de verdade.
#
# Para cada um dos cinco, registre três linhas:
#   SINTOMA     o que você viu
#   CAUSA       a linha e o motivo
#   CORREÇÃO    o que você escreveu no lugar
#
# Entregue o arquivo corrigido e o registro dos cinco, mesmo que você não tenha
# achado todos. Vale mais registrar quatro bem que listar cinco no chute.
#
# ---------------------------------------------------------------------------
# AS REGRAS ESCRITAS, que é de onde sai o resultado esperado. Leia as quatro
# antes de rodar, e calcule cada número de cabeça primeiro.
#
#   1. A taxa de sucesso é a quantidade de casos que passaram dividida pela
#      quantidade TOTAL de casos da massa, em porcentagem.
#   2. O tempo total é a soma das durações de todos os casos, em segundos.
#   3. Um caso é considerado lento quando a duração PASSA de 2 segundos.
#   4. O relatório imprime, para cada caso, o nome, o status e a duração.
# ---------------------------------------------------------------------------
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   As quatro regras estão escritas por extenso no bloco abaixo, e é de lá que sai o
#   resultado esperado de cada número. Leia as quatro antes de rodar.

CASOS = [
    {"nome": "login valido", "status": "passou", "duracao": "1.20"},
    {"nome": "login invalido", "status": "passou", "duracao": "0,95"},
    {"nome": "senha em branco", "status": "falhou", "duracao": "2.10"},
    {"nome": "senha curta", "status": "passou", "duracao": "2.00"},
    {"nome": "logout", "status": "passou", "duracao": "0.80"},
]


def contar_aprovados(casos):
    aprovados = 0
    for caso in casos:
        if caso["status"] == "passou":
            aprovados + 1
    return aprovados


def taxa_de_sucesso(casos):
    return contar_aprovados(casos) / 4 * 100


def tempo_total(casos):
    total = 0.0
    for caso in casos:
        total = total + float(caso["duracao"])
    return total


def contar_lentos(casos):
    lentos = 0
    for caso in casos:
        if float(caso["duracao"]) >= 2.0:
            lentos = lentos + 1
    return lentos


def imprimir_detalhe(casos):
    for caso in casos:
        print(f"  {caso['nome']}: {caso['status']}, {caso['tempo']}s")


print("=== Relatorio de execucao ===")
imprimir_detalhe(CASOS)
print()
print(f"Casos aprovados: {contar_aprovados(CASOS)}")
print(f"Taxa de sucesso: {taxa_de_sucesso(CASOS):.1f}%")
print(f"Tempo total: {tempo_total(CASOS):.2f}s")
print(f"Casos lentos: {contar_lentos(CASOS)}")
