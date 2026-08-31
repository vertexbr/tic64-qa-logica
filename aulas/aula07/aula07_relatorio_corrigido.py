# Aula 07 - os três defeitos do aula07_relatorio_bugado.py, corrigidos
#
# É o mesmo arquivo, com três caracteres de diferença e um except com tipo. Cada
# correção vem com o comentário do que estava errado e de como o defeito se
# manifestava, porque a lição é a investigação e não a linha certa.
#
# E o assert no fim de cada função é o que impede o defeito de voltar: ele
# escreve o resultado ESPERADO, que vem da regra, e compara com o OBTIDO, que
# vem do programa.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   As mesmas três do aula07_relatorio_bugado.py, agora com um assert por regra: é ele
#   que compara o esperado, que vem da regra, com o obtido, que vem do programa.


def calcular_media_aprovacao(resultados):
    aprovados = 0
    for r in resultados:
        if r == "passou":
            # DEFEITO 1, o principal da aula. Estava escrito "aprovados + 1",
            # sem o igual: a linha calculava um valor e jogava no lixo, porque
            # ninguém guardou o resultado. Para o Python isso é uma expressão
            # perfeitamente legal, então nenhuma mensagem avisa. É o processo
            # CRIA ANTES, PERCORRE, MUDA DENTRO, USA DEPOIS da Aula 04 com a
            # etapa MUDA DENTRO quebrada.
            aprovados = aprovados + 1
    return aprovados / len(resultados) * 100


def precisa_de_aprovacao_gerencial(valor_desconto):
    # DEFEITO 2, de fronteira. A regra escrita diz que precisa de aprovação
    # quando o desconto PASSA de 50%, e o código dizia ">= 50", que inclui o 50.
    # Um caractere de diferença, e ele só aparece se alguém testar exatamente
    # 50. Guardem a sensação: na Aula 09 ela ganha nome e vira técnica.
    if valor_desconto > 50:
        return True
    return False


def somar_valores(linhas):
    total = 0
    descartadas = []
    for linha in linhas:
        try:
            total = total + float(linha)
        # DEFEITO 3. Estava "except:" pelado com "pass" dentro, e o valor com
        # vírgula em vez de ponto foi descartado em silêncio: a soma dava 40 em
        # vez de 60. except genérico é o jeito mais rápido de transformar
        # defeito em silêncio.
        #
        # Repare no que a correção do except faz e no que ela não faz: ela não
        # conserta a soma, ela mostra o que consertar. O conserto é do dado.
        except ValueError as erro:
            descartadas.append(f"{linha} ({erro})")
    if descartadas:
        print(f"    ATENCAO: {len(descartadas)} valor(es) fora do formato: {descartadas}")
    return total


def normalizar(linhas):
    """Troca vírgula decimal por ponto, que é o que o float() do Python lê."""
    limpas = []
    for linha in linhas:
        limpas.append(linha.replace(",", "."))
    return limpas


notas = ["passou", "passou", "falhou"]

# Esperado vem da regra: duas de três aprovadas são 66,7%.
assert round(calcular_media_aprovacao(notas), 1) == 66.7
print(f"Aprovacao: {calcular_media_aprovacao(notas):.1f}%")

# Esperado vem da regra: 50 exato NÃO precisa de aprovação, 51 precisa.
assert precisa_de_aprovacao_gerencial(50) is False
assert precisa_de_aprovacao_gerencial(51) is True
print(f"Desconto de 50 por cento precisa de aprovacao? {precisa_de_aprovacao_gerencial(50)}")
print(f"Desconto de 51 por cento precisa de aprovacao? {precisa_de_aprovacao_gerencial(51)}")

# O except com tipo faz o valor recusado aparecer na tela. A soma continua 40,00,
# e é esse o ponto: agora eu sei por quê.
valores = ["10.00", "20,00", "30.00"]
print(f"Soma, com o aviso na tela: {somar_valores(valores):.2f}")

# Esperado vem da regra: os três valores somam 60,00. Com a vírgula normalizada,
# nada é descartado e o número fecha.
print(f"Soma, com a massa normalizada: {somar_valores(normalizar(valores)):.2f}")
assert somar_valores(normalizar(valores)) == 60.00

print()
print("As tres verificacoes passaram.")
