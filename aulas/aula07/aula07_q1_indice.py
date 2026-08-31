# Aula 07 - quebrado 1 de 4: posição que não existe na lista
#
# Rode, leia a ÚLTIMA linha primeiro, e responda três coisas:
#   1. o tipo do erro
#   2. a linha onde estourou
#   3. uma frase sua dizendo a causa
#
# Não conserte. Hoje o exercício é ler.
#
# O erro vai dentro de try/except com traceback.print_exc() para o arquivo
# seguir até o fim e você ver o traceback igual ao que o Python imprime sozinho.
# AVISO: numa verificação de verdade a falha INTERROMPE. Aqui é recurso de
# demonstração, não padrão para copiar.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A suíte tem três casos de teste cadastrados, e o relatório imprime um deles pela
#   posição na lista.
import traceback

casos = ["login válido", "login inválido", "senha em branco"]

try:
    print(f"Quarto caso: {casos[3]}")
except IndexError:
    traceback.print_exc()

print()
print("A lista tem três itens, nas posições 0, 1 e 2.")
