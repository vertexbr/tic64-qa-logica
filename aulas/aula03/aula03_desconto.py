# Aula 03 - regra de desconto da loja virtual (critério de aceite CA-018)
#
# Regra de negócio, como chega no trabalho:
#   Cliente VIP com compra acima de R$ 200,00 recebe 20% de desconto.
#   Cliente VIP com compra de até R$ 200,00 recebe 10%.
#   Cupom válido ou produto em promoção, para cliente comum, recebe 5%.
#   Nenhuma das condições acima: sem desconto.
#
# Algoritmo em pseudocódigo, nas convenções da Aula 01:
#
#   ALGORITMO calcular_desconto
#   ENTRADA: valor_compra, cliente_vip, cupom_valido, produto_em_promocao
#
#   INÍCIO
#       SE cliente_vip é verdadeiro E valor_compra passa de 200 ENTÃO
#           desconto recebe 20
#       SENÃO SE cliente_vip é verdadeiro ENTÃO
#           desconto recebe 10
#       SENÃO SE cupom_valido é verdadeiro OU produto_em_promocao é verdadeiro ENTÃO
#           desconto recebe 5
#       SENÃO
#           desconto recebe 0
#       FIM SE
#
#       ESCREVER desconto
#       VALIDE: desconto obtido é igual ao desconto esperado do caso
#   FIM
#
# Planilha de casos de teste da aula. Para treinar, troque a massa abaixo
# pelo caso seguinte e rode de novo, um caso por execução:
#
#   caso   | valor_compra | cliente_vip | cupom_valido | produto_em_promocao | esperado
#   CT-01  | 300.00       | True        | False        | False               | 20
#   CT-02  | 150.00       | True        | False        | False               | 10
#   CT-03  | 200.00       | True        | False        | False               | 10   <- 200 exato não passa de 200
#   CT-04  | 180.00       | False       | True         | False               | 5
#   CT-05  | 180.00       | False       | False        | False               | 0

# --- massa de teste do caso ---
caso = "CT-01"
valor_compra = 300.00
cliente_vip = True
cupom_valido = False
produto_em_promocao = False
desconto_esperado = 20

# --- a decisão ---
# A escada é percorrida de cima para baixo, e só o primeiro ramo que der
# verdadeiro é executado. A condição mais específica vem primeiro.
if cliente_vip and valor_compra > 200:
    desconto = 20
elif cliente_vip:
    desconto = 10
elif cupom_valido or produto_em_promocao:
    desconto = 5
else:
    desconto = 0

valor_final = valor_compra - (valor_compra * desconto / 100)

# --- evidência esperado x obtido ---
print(f"{caso} | esperado: {desconto_esperado}% | obtido: {desconto}% | confere? {desconto == desconto_esperado}")
print(f"{caso} | valor final: R$ {valor_final:.2f}")
