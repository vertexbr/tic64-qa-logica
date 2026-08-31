# Aula 07 - os três erros de sintaxe que toda turma comete
#
# Erro de sintaxe não deixa o arquivo nem começar: o Python recusa antes de
# rodar a primeira linha. Então os três exemplos NÃO podem morar aqui soltos,
# senão este arquivo não abriria. Eles ficam comentados, com a mensagem exata
# que o Python devolveu, e embaixo de cada um vem a versão certa rodando.
#
# Na aula o professor digita os três na frente da turma, um por vez, e roda.
# Este arquivo é para você repetir isso em casa: descomente uma linha por vez,
# rode, leia a mensagem, e comente de novo.
#
# SEM REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Este arquivo não implementa regra nenhuma: ele existe para mostrar três mensagens
#   do Python. O conteúdo é a mensagem, e o motivo está declarado para não ficar em
#   silêncio.

print("=== 1. dois-pontos esquecido ===")

# O ERRADO:
#     idade = 20
#     if idade >= 18
#         print("ok")
#
# O que o Python disse:
#       File "aula07_erros_de_sintaxe.py", line 2
#         if idade >= 18
#                       ^
#     SyntaxError: expected ':'
#
# Ele escreveu literalmente o que queria: expected ':', esperava dois-pontos.
# Vale para if, for, while e def. Todo bloco em Python abre com dois-pontos.

idade = 20
if idade >= 18:
    print("ok")


print()
print("=== 2. aspas não fechadas ===")

# O ERRADO:
#     nome = "Gaia
#     print(nome)
#
# O que o Python disse:
#       File "aula07_erros_de_sintaxe.py", line 1
#         nome = "Gaia
#                ^
#     SyntaxError: unterminated string literal (detected at line 1)
#
# unterminated string literal é "a string não terminou". Abriu aspas e nunca
# fechou. O editor ajuda aqui: da abertura até o fim do arquivo tudo fica
# colorido de string.

nome = "Gaia"
print(nome)


print()
print("=== 3. tabulação misturada com espaço ===")

# O ERRADO (a linha do return foi recuada com TAB e as outras com espaço):
#     def calcular(a, b):
#         total = a + b
#     <TAB>return total
#
# O que o Python disse:
#       File "aula07_erros_de_sintaxe.py", line 3
#         return total
#     TabError: inconsistent use of tabs and spaces in indentation
#
# Este é o mais confuso dos três, porque na tela o código parece perfeitamente
# alinhado. O olho não vê a diferença e o Python vê. A solução que resolve para
# sempre: configure o editor para converter tabulação em quatro espaços.

def calcular(a, b):
    total = a + b
    return total


print(f"calcular(2, 3) = {calcular(2, 3)}")
