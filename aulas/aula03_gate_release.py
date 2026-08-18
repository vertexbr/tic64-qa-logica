# Aula 03 - o gate de release: liberar ou não, pela taxa de aprovação da suíte
#
# Regra: taxa de aprovação de 90% ou mais libera a release; 80% ou mais libera
# com ressalva; 70% ou mais segura para revisão; abaixo disso bloqueia.
# Quatro faixas, três fronteiras.
#
# Algoritmo em pseudocódigo, nas convenções da Aula 01:
#
#   ALGORITMO decidir_gate_de_release
#   ENTRADA: taxa_aprovacao
#
#   INÍCIO
#       SE taxa_aprovacao é maior ou igual a 90 ENTÃO
#           decisao recebe "libera"
#       SENÃO SE taxa_aprovacao é maior ou igual a 80 ENTÃO
#           decisao recebe "libera com ressalva"
#       SENÃO SE taxa_aprovacao é maior ou igual a 70 ENTÃO
#           decisao recebe "segura para revisão"
#       SENÃO
#           decisao recebe "bloqueia"
#       FIM SE
#
#       ESCREVER decisao
#       VALIDE: decisão obtida é igual à decisão esperada do caso
#   FIM
#
# Massa de fronteira da aula. Para treinar, troque a taxa e a decisão esperada
# e rode de novo, um caso por execução:
#
#   taxa | decisão esperada    | por que vale testar
#   90   | libera              | a fronteira exata, >= inclui
#   89   | libera com ressalva | um abaixo da fronteira
#   80   | libera com ressalva | fronteira de baixo da faixa
#   79   | segura para revisão | um abaixo
#   70   | segura para revisão | fronteira do último ramo
#   69   | bloqueia            | cai no else

# --- massa de teste do caso ---
taxa_aprovacao = 85
decisao_esperada = "libera com ressalva"

# --- a decisão ---
if taxa_aprovacao >= 90:
    decisao = "libera"
elif taxa_aprovacao >= 80:
    decisao = "libera com ressalva"
elif taxa_aprovacao >= 70:
    decisao = "segura para revisão"
else:
    decisao = "bloqueia"

# --- evidência esperado x obtido ---
print(f"Taxa {taxa_aprovacao}% | esperado: {decisao_esperada} | obtido: {decisao} | confere? {decisao == decisao_esperada}")
