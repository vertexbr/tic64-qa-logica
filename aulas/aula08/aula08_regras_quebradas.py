# Aula 08 - a mesma regra, com um número trocado
#
# Este é o aula08_regras.py com UMA diferença: o 18 virou 21 na linha da idade.
# O resto é igual palavra por palavra.
#
# A troca não foi sabotagem. Alguém achou que estava melhorando a regra, salvou,
# e não rodou nada. É assim que regressão entra em produção, e é exatamente esse
# o argumento de existir teste: ele é o ponto de controle que avisa que o
# contrato mudou, mesmo quando ninguém teve má intenção.
#
# Em aula o professor faz essa troca AO VIVO no aula08_regras.py e desfaz com
# Ctrl+Z. Este arquivo existe para você repetir a demonstração em casa sem
# precisar estragar o original.
#
# Rode o test_aula08_regressao.py contra ele e conte os vermelhos antes.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A regra escrita continua a mesma: cadastro liberado a partir de 18 anos. O
#   código é que passou a dizer 21, e nenhuma mensagem de erro avisa isso.


def validar_idade_minima(idade):
    return idade >= 21


def tem_permissao(perfil):
    return perfil in ["admin", "gerente"]
