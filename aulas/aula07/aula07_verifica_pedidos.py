# Aula 07 - tempo 2: provar que ela recusou, sem ferramenta nova
#
# Nenhuma peça aqui é conteúdo novo de hoje além do try/except:
#   - a variável de estado é a mesma "logou" de aulas/aula06/aula06_login_while.py,
#     com trabalho novo: lá ela dizia se o login aconteceu, aqui ela diz se o
#     erro aconteceu;
#   - o assert é da Aula 04, com a mensagem depois da vírgula, que é o que faz
#     ele dizer o que deu errado em vez de reprovar calado;
#   - o "in" é da Aula 05, agora procurando um pedaço de texto dentro da
#     mensagem do erro em vez de uma chave dentro do dicionário.
#
# A frase que fixa o mecanismo: aqui o erro ACONTECENDO é aprovação, e o erro
# NÃO acontecendo é reprovação. É a inversão da lógica de sempre.
#
# São nove linhas para provar uma recusa. Na Aula 08 elas viram uma.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A função tem que recusar quantidade zero e nome em branco, cada um com a sua
#   mensagem. E o cálculo de frete não recusa nada: ele sempre devolve um valor.
import traceback

from aula07_pedidos import registrar_item, calcular_frete

# Caso 1: item válido. Isso a turma já faz desde a Aula 04.
assert registrar_item("Teclado", 2) == "2x Teclado"
print("OK - item valido registrado")

# Caso 2: quantidade zero DEVE ser recusada.
levantou = False
mensagem = ""
try:
    registrar_item("Teclado", 0)
except ValueError as erro:
    levantou = True
    mensagem = str(erro)

assert levantou, "a funcao NAO levantou ValueError: ela aceitou quantidade zero"
assert "quantidade" in mensagem, f"recusou por outro motivo: {mensagem}"
print(f"OK - recusou com a mensagem: {mensagem}")

# Caso 3: nome em branco também DEVE ser recusado, e por outro motivo.
# Três espaços é campo vazio para o usuário e campo preenchido para o código:
# é o nome.strip() de aulas/aula05/aula05_email_sujo.py pagando dividendo.
levantou = False
mensagem = ""
try:
    registrar_item("   ", 2)
except ValueError as erro:
    levantou = True
    mensagem = str(erro)

assert levantou, "a funcao NAO levantou ValueError: ela aceitou nome em branco"
assert "nome do item" in mensagem, f"recusou por outro motivo: {mensagem}"
print(f"OK - recusou com a mensagem: {mensagem}")

# ---------------------------------------------------------------------------
# A falha ao contrário, que é onde o conceito fecha.
#
# O calcular_frete não valida nada e nunca levanta erro: ele devolve zero ou
# vinte. Então "levantou" continua False, e o assert reprova.
#
# Esta é a única falha do curso em que o problema é a AUSÊNCIA de erro.
#
# Ela vai dentro de try/except AssertionError com print_exc() para o arquivo
# seguir até o fim e você ver a mensagem vermelha inteira. AVISO: numa
# verificação de verdade a falha INTERROMPE. Engolir asserção é o oposto de
# verificar, e é o antipadrão do aula07_except_pelado.py com outra roupa.
print()
print("=== a falha ao contrario ===", flush=True)

levantou = False
try:
    calcular_frete(100.00)
except ValueError:
    levantou = True

try:
    assert levantou, "a funcao NAO levantou ValueError"
except AssertionError:
    traceback.print_exc()

print()
print("Eu estava esperando um erro, ele nao veio, e isso reprovou a verificacao.")
print("E a frase que apareceu na tela fui eu que escrevi, depois da virgula.")
