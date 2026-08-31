# Aula 07 - tempo 1: deixe estourar
#
# ESTE ARQUIVO QUEBRA DE PROPÓSITO, e é o segundo e último da aula que sai com
# exit code 1, junto com o aula07_relatorio.py. Aqui a parada é o conteúdo: o
# programa está certo, ele recusou o que devia recusar, e o problema é que ele
# PAROU. Um programa que morre no meio não diz se o comportamento foi o
# esperado, e nem deixa o resto rodar. Embrulhar isso em try/except apagaria a
# única coisa que este arquivo existe para mostrar.
#
# Leia o traceback de baixo para cima, como no aula07_relatorio.py: o tipo, a
# mensagem, a linha do raise dentro do aula07_pedidos.py, e a linha que chamou.
#
# O tempo 2 está no aula07_verifica_pedidos.py.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A mesma do aula07_pedidos.py: item só é registrado com nome preenchido e quantidade
#   positiva. Aqui ela é chamada com quantidade zero de propósito.
from aula07_pedidos import registrar_item

print(registrar_item("Teclado", 2))
print(registrar_item("Teclado", 0))
