# Aula 03 - classificação de defeitos: o pseudocódigo da Aula 01 virando código
#
# A regra da Aula 01 foi atualizada para a forma que aparece em triagem de
# defeito de verdade:
#   Impede produção e não tem workaround: CRÍTICA.
#   Impede produção e tem workaround: ALTA.
#   Qualquer outro caso: MÉDIA.
#
# Algoritmo em pseudocódigo, nas convenções da Aula 01:
#
#   ALGORITMO classificar_defeito
#   ENTRADA: impede_producao (sim/não), tem_workaround (sim/não)
#
#   INÍCIO
#       SE impede_producao é verdadeiro E não tem_workaround ENTÃO
#           severidade recebe "CRÍTICA"
#       SENÃO SE impede_producao é verdadeiro E tem_workaround ENTÃO
#           severidade recebe "ALTA"
#       SENÃO
#           severidade recebe "MÉDIA"
#       FIM SE
#
#       ESCREVER severidade
#       VALIDE: severidade obtida é igual à severidade esperada do caso
#   FIM
#
# Dois booleanos dão 4 combinações, sempre. Planilha de casos da aula, para
# treinar trocando a massa, um caso por execução:
#
#   caso   | impede_producao | tem_workaround | severidade esperada
#   CT-01  | True            | False          | CRÍTICA
#   CT-02  | True            | True           | ALTA
#   CT-03  | False           | False          | MÉDIA
#   CT-04  | False           | True           | MÉDIA   <- o caso que quase ninguém testa

# --- massa de teste do caso ---
caso = "CT-01"
impede_producao = True
tem_workaround = False
severidade_esperada = "CRÍTICA"

# --- a decisão ---
if impede_producao and not tem_workaround:
    severidade = "CRÍTICA"
elif impede_producao and tem_workaround:
    severidade = "ALTA"
else:
    severidade = "MÉDIA"

# --- evidência esperado x obtido ---
print(f"{caso} | esperado: {severidade_esperada} | obtido: {severidade} | confere? {severidade == severidade_esperada}")
