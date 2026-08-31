# Aula 07 - o bônus de trinta segundos que economiza minutos
#
# As versões recentes do Python sugerem a correção quando você erra um nome.
# Quem lê a mensagem inteira resolve em cinco segundos; quem lê só a primeira
# metade abre o navegador e gasta cinco minutos.
#
# O erro vai dentro de try/except só para o arquivo seguir até o fim e mostrar
# as duas metades da lição na mesma execução. AVISO, e ele é importante: numa
# verificação de verdade a falha INTERROMPE. Engolir erro é o oposto de
# verificar, e é exatamente o antipadrão do aula07_except_pelado.py.
#
# Detalhe que decide qual função usar aqui: traceback.print_exc() imprime a
# sugestão "Did you mean" inteira, igual ao Python quando ninguém captura.
# str(erro) e traceback.format_exception_only() PERDEM a sugestão, e a
# sugestão é justamente o que este arquivo existe para mostrar.
#
# SEM REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Mesmo caso do aula07_erros_de_sintaxe.py: o conteúdo é a mensagem do Python, e não
#   uma regra de negócio.
import traceback

total_pedido = 100

print("=== o que str(erro) entrega ===", flush=True)
try:
    print(total_pedid)
except NameError as erro:
    print(f"NameError: {erro}", flush=True)

print()
print("=== o que o Python entrega de verdade ===", flush=True)
try:
    print(total_pedid)
except NameError:
    traceback.print_exc()

print()
print("Ele perguntou se você quis dizer total_pedido. E quis.")
