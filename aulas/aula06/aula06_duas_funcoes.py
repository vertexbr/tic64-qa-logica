# Aula 06 - o arquivo da demonstração guiada 1
#
# Duas funções, escritas do zero na frente da turma. Refazer este arquivo em
# casa, sem olhar, é o melhor uso de dez minutos que vocês têm esta semana.
#
# Os dois tropeços mais prováveis ao refazer: print no lugar de return dentro
# da função, que faz ela parecer funcionar e devolver None, e a chamada escrita
# sem os parênteses, que não executa nada e não reclama de nada.

def tem_frete_gratis(total):
    return total >= 250.00


def gerar_email_teste(nome):
    limpo = nome.strip().lower().replace(" ", ".")
    return f"{limpo}@qatest.com"


print(f"300 tem frete grátis? {tem_frete_gratis(300.00)}")
print(f"100 tem frete grátis? {tem_frete_gratis(100.00)}")
print(f"250 tem frete grátis? {tem_frete_gratis(250.00)}")
print(f"E-mail gerado: {gerar_email_teste('  Gaia Silva  ')}")

# O terceiro assert é o que vale mais: 250 é a fronteira da regra, e é lá que
# o >= se separa do >. Valor-limite se escolhe, não se sorteia.
assert tem_frete_gratis(300.00) == True
assert tem_frete_gratis(100.00) == False
assert tem_frete_gratis(250.00) == True
assert gerar_email_teste("  Gaia Silva  ") == "gaia.silva@qatest.com"
print("As quatro verificações passaram")
