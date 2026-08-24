# Aula 06 - a bateria de funções da loja
#
# GUARDEM ESTE ARQUIVO. Ele é o material de trabalho da Aula 08, quando a
# ferramenta que organiza verificações entrar para cuidar destes assert.
#
# Nada aqui é conteúdo novo, e é isso que faz o arquivo valer: a classificação
# de severidade vocês escreveram em português na Aula 01, virou if na Aula 03 e
# acabou de virar função com nome próprio. A classificação de status era o for
# da Aula 04. A geração de e-mail é o strip e o lower da Aula 05, agora com
# replace trocando espaço por ponto. Nada de novo além da embalagem, e a
# embalagem é a função.

def tem_frete_gratis(total):
    return total >= 250.00


def classificar_severidade(impede_producao, tem_workaround):
    if impede_producao and not tem_workaround:
        return "CRÍTICA"
    if impede_producao and tem_workaround:
        return "ALTA"
    return "MÉDIA"


def classificar_status_code(codigo):
    if 200 <= codigo < 300:
        return "sucesso"
    if 400 <= codigo < 500:
        return "erro do cliente"
    if codigo >= 500:
        return "erro do servidor"
    return "outro"


def gerar_email_teste(nome):
    limpo = nome.strip().lower().replace(" ", ".")
    return f"{limpo}@qatest.com"


print(f"250 tem frete grátis? {tem_frete_gratis(250.00)}")
print(f"Severidade:  {classificar_severidade(True, False)}")
print(f"Código 302:  {classificar_status_code(302)}")
print(f"E-mail sujo: {gerar_email_teste('  Gaia Silva  ')}")

assert tem_frete_gratis(250.00) == True
assert classificar_severidade(True, True) == "ALTA"
assert classificar_status_code(302) == "outro"
assert gerar_email_teste("  Gaia Silva  ") == "gaia.silva@qatest.com"
print("Todas as verificações passaram")

# E agora a descoberta que é de graça, e ela não foi plantada aqui: rode com um
# nome acentuado e olhe o til.
#
# lower põe em minúscula e não tira acento nenhum, então esta função gera
# e-mail com acento, e e-mail com acento é recusado por boa parte dos sistemas.
# Consertar não é assunto de hoje. O que é assunto de hoje é que o dado que
# você escolhe para testar decide o que você encontra.
print(f"Com acento:  {gerar_email_teste('João Silva')}")
