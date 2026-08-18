# Aula 01 - algoritmo de classificação de severidade de defeito
#
# Regra de negócio, dita em aula antes de qualquer linha de pseudocódigo:
#   Defeito que impede o uso do sistema é severidade CRÍTICA.
#   Se não impede o uso, mas afeta uma funcionalidade, é severidade ALTA.
#   Qualquer outra coisa é severidade BAIXA.
#
# Algoritmo em pseudocódigo, exatamente como escrito em aula:
#
#   ALGORITMO classificar_defeito
#   ENTRADA: impede_uso (sim/não), afeta_funcionalidade (sim/não)
#
#   INÍCIO
#       SE impede_uso é verdadeiro ENTÃO
#           severidade recebe "CRÍTICA"
#       SENÃO SE afeta_funcionalidade é verdadeiro ENTÃO
#           severidade recebe "ALTA"
#       SENÃO
#           severidade recebe "BAIXA"
#       FIM SE
#
#       ESCREVER severidade
#       VALIDE: severidade é uma entre CRÍTICA, ALTA, BAIXA
#   FIM
#
# A "escada" de SE / SENÃO SE / SENÃO é percorrida de cima para baixo, e só o
# primeiro ramo que der verdadeiro é executado. impede_uso precisa vir
# primeiro porque é a condição mais grave: se afeta_funcionalidade fosse
# verificada antes, um defeito que impede o uso e também afeta uma
# funcionalidade (as duas verdadeiras ao mesmo tempo) seria classificado como
# ALTA em vez de CRÍTICA.

def classificar_defeito(impede_uso: bool, afeta_funcionalidade: bool) -> str:
    if impede_uso:
        severidade = "CRÍTICA"
    elif afeta_funcionalidade:
        severidade = "ALTA"
    else:
        severidade = "BAIXA"

    return severidade


# Teste de mesa feito em aula: impede_uso = sim, afeta_funcionalidade = sim.
severidade_correta = classificar_defeito(impede_uso=True, afeta_funcionalidade=True)
print(f"Severidade: {severidade_correta}")
# VALIDE: severidade é uma entre CRÍTICA, ALTA, BAIXA -> CRÍTICA está na lista, teste de mesa OK


# O erro proposital da aula: a mesma regra, com as duas condições invertidas.
#
#   SE afeta_funcionalidade é verdadeiro ENTÃO
#       severidade recebe "ALTA"
#   SENÃO SE impede_uso é verdadeiro ENTÃO
#       severidade recebe "CRÍTICA"
#
# Nada quebra: não há erro de sintaxe nem exceção, e a linha VALIDE ainda
# passa, porque "ALTA" está entre as três severidades permitidas. O problema
# não é de execução, é de lógica: o mesmo defeito que derruba o sistema passa
# a ser classificado como ALTA em vez de CRÍTICA.

def classificar_defeito_com_erro_de_logica(impede_uso: bool, afeta_funcionalidade: bool) -> str:
    if afeta_funcionalidade:
        severidade = "ALTA"
    elif impede_uso:
        severidade = "CRÍTICA"
    else:
        severidade = "BAIXA"

    return severidade


severidade_com_erro = classificar_defeito_com_erro_de_logica(impede_uso=True, afeta_funcionalidade=True)
print(f"Severidade com a ordem trocada: {severidade_com_erro}")
# Mesmo defeito do teste de mesa acima (impede_uso=True, afeta_funcionalidade=True),
# e o resultado muda de CRÍTICA para ALTA só por causa da ordem das condições.
