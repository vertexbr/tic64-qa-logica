# Aula 04 - o laço infinito, e como sair dele
#
# ATENÇÃO: este arquivo roda e termina. A versão que trava está aqui em
# cima, comentada de propósito, para você poder provocar o travamento
# quando quiser, já sabendo como sair.
#
# O while não é conteúdo desta aula. Ele chega na Aula 06, com o contexto
# de tentativa de login com limite, que é o que justifica a existência
# dele. Aqui ele aparece por um motivo só: é o formato em que o laço
# infinito acontece com quem está começando.
#
# A VERSÃO QUE TRAVA:
#
#     contagem = 5
#
#     while contagem > 0:
#         print(f"{contagem}...")
#         # contagem = contagem - 1     <- a linha que falta
#
#     print("Lançamento!")
#
# Leia o while assim: "enquanto a contagem for maior que zero, imprima".
# A contagem vale cinco e nada dentro do laço muda ela, então a condição
# continua verdadeira para sempre e a tela enche sem parar. É a mesma
# lição da catraca e do foguete, agora na forma de castigo.
#
# PARA SAIR: Ctrl+C no terminal. Aparece isto:
#
#     Traceback (most recent call last):
#       File "aula04_laco_infinito.py", line 3, in <module>
#         print(f"{contagem}...")
#     KeyboardInterrupt
#
# KeyboardInterrupt é a mensagem mais assustadora e mais inofensiva do
# curso. Ela só diz "você mandou parar, eu parei". Não estragou nada, não
# perdeu arquivo, não travou máquina. Quando acontecer em casa às onze da
# noite, é Ctrl+C e segue a vida.

# --- a versão correta: a linha que faltava está de volta ---
contagem = 5

while contagem > 0:
    print(f"{contagem}...")
    contagem = contagem - 1

print("Lançamento!")

assert contagem == 0, f"esperado 0, obtido {contagem}"
print("Verificação passou: a contagem terminou em zero e o laço acabou")
