# Aula 09 - o módulo do produto, que é o que a massa de teste vai exercitar
#
# Este arquivo NÃO é um teste. Ele é o produto: as quatro regras que a loja
# precisa que funcionem. Quem testa são os arquivos test_aula09_*.py ao lado.
#
# As quatro já existem no curso. Elas vêm para cá porque a Aula 09 não é sobre
# escrever regra nova: é sobre escolher QUAIS dados usar para testar regra que
# já existe, e depois colapsar os casos escolhidos num parametrize.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos, e 18 entra. Frete é grátis a
#   partir de R$ 250,00, e 250,00 entra. Senha vale com 8 ou mais caracteres,
#   ao menos um número e ao menos uma maiúscula. Nota de 90 para cima é
#   excelente, de 80 a 89 é bom, de 70 a 79 é suficiente, abaixo disso é
#   insuficiente.


# Mesma regra de aulas/aula08/aula08_regras.py, sem uma vírgula de diferença.
# O acréscimo desta aula não está no código: está na escolha de quais idades
# testar. A fronteira é 18, então os valores obrigatórios são 17, 18 e 19.
def validar_idade_minima(idade):
    return idade >= 18


# Mesma regra de aulas/aula06/aula06_funcoes_da_loja.py, com o >= correto.
# O acréscimo desta aula é a massa: 249.99, 250.00 e 300.00, que é vizinho de
# baixo, fronteira e representante da partição de cima.
def tem_frete_gratis(total):
    return total >= 250.00


# Mesma função de aulas/aula06/aula06_senha_valida.py, que era o extra de casa
# da Aula 06. Ela vem pronta porque boa parte da turma não escreveu, e sem ela
# o segundo bloco desta aula viraria aula de string em vez de aula de massa.
# O acréscimo desta aula é a massa de quatro linhas, que mistura valor-limite
# (7 e 8 caracteres) com partição de outra natureza (sem maiúscula, sem número).
def senha_valida(senha):
    if len(senha) < 8:
        return False
    tem_numero = False
    tem_maiuscula = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isupper():
            tem_maiuscula = True
    return tem_numero and tem_maiuscula


# A escada de faixas da Aula 03, no formato de retorno antecipado que a Aula 06
# ensinou. O acréscimo desta aula é enxergar que ela tem TRÊS fronteiras, 70,
# 80 e 90, e que cada uma pede o próprio par de valores.
def classificar_nota(nota):
    if nota >= 90:
        return "excelente"
    if nota >= 80:
        return "bom"
    if nota >= 70:
        return "suficiente"
    return "insuficiente"


# A regra de desconto da Aula 03 reduzida às DUAS condições que cabem numa
# tabela de decisão projetável. O nome é desconto_vip, e não calcular_desconto,
# de propósito: calcular_desconto é o nome que a atividade da Aula 08 fixou,
# com quatro parâmetros, e reaproveitar o nome com outra assinatura uma aula
# depois faria a turma importar a função errada.
def desconto_vip(valor_compra, cliente_vip):
    if cliente_vip and valor_compra > 200.00:
        return 20
    if cliente_vip:
        return 10
    return 0

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-07.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 7 da apresentacao.
#
#      53  def classificar_nota(nota):
#          Nada executa. Um parâmetro fica guardado com o corpo, esperando
#          alguém chamar.
#
#      54  if nota >= 90:
#          Primeiro degrau. Repare no >=: com > a nota 90 exata cairia no
#          degrau de baixo, e ninguém perceberia até um aluno com 90 receber
#          "bom".
#
#      55  return "excelente"
#          O return encerra a função inteira, não só o if. É por isso que os
#          degraus abaixo não precisam de elif.
#
#      56  if nota >= 80:
#          Este if só é alcançado quando a linha 54 deu falso, ou seja, quando
#          a nota já é menor que 90. Por isso ele não precisa escrever nota <
#          90 and nota >= 80.
#
#      57  return "bom"
#
#      58  if nota >= 70:
#          Mesmo raciocínio: aqui a nota já é comprovadamente menor que 80.
#
#      59  return "suficiente"
#
#      60  return "insuficiente"
#          O caso que sobra. Não tem else porque não precisa: se a execução
#          chegou nesta linha, os três degraus falharam.
#
# --- fim da explicacao linha a linha ---
