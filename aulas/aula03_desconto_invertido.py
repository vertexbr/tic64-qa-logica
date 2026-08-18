# Aula 03 - o erro proposital: a regra de desconto com os dois primeiros ramos trocados
#
# Nada quebra: não há erro de sintaxe nem exceção. O programa roda até o fim,
# imprime com formatação bonita, e o cliente VIP de 300 reais recebe 10% em
# vez de 20%. A primeira condição é mais genérica e engole todos os casos VIP,
# então o ramo específico nunca é avaliado. No depurador dá para ver: o
# destaque vai da linha do if direto para o desconto de 10, e a linha do ramo
# de 20% nunca acende, para nenhuma entrada possível.
#
# É o mesmo defeito da ordem trocada do aula01_classificar_defeito.py, agora
# flagrado pela evidência: o confere? sai False com o programa inteiro verde.

# --- massa de teste do caso ---
caso = "CT-01"
valor_compra = 300.00
cliente_vip = True
cupom_valido = False
produto_em_promocao = False
desconto_esperado = 20

# --- a decisão, na ordem errada de propósito ---
if cliente_vip:
    desconto = 10
elif cliente_vip and valor_compra > 200:
    desconto = 20
elif cupom_valido or produto_em_promocao:
    desconto = 5
else:
    desconto = 0

# --- evidência esperado x obtido ---
print(f"{caso} | esperado: {desconto_esperado}% | obtido: {desconto}% | confere? {desconto == desconto_esperado}")
