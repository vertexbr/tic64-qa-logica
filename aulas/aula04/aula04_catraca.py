# Aula 04 - o contador, que é a catraca do ônibus
#
# A catraca começa num número e soma um a cada pessoa que passa. Ela não
# guarda quem passou, guarda quantos passaram, e é a coisa mais parecida
# com um contador de testes aprovados que existe no mundo físico.
#
# Duas regras que este arquivo existe para mostrar:
#
#   1. O contador nasce ANTES do laço. Criado dentro, ele volta a zero em
#      cada volta e nunca acumula nada. A catraca do ônibus não é zerada a
#      cada passageiro.
#
#   2. A linha aprovados = aprovados + 1 se lê da direita para a esquerda:
#      pega o valor que está na caixinha, soma um, e guarda de volta na
#      mesma caixinha. O valor anterior é esquecido. Não é equação
#      matemática; se fosse, não faria sentido nenhum.
#
# Teste de mesa, volta por volta. Quando o seu número sair errado, é esta
# tabela que resolve, e ela cabe num papel:
#
#   volta   | resultado | aprovados no fim da volta
#   início  | -         | 0
#   1       | passou    | 1
#   2       | falhou    | 1
#   3       | passou    | 2

aprovados = 0
print(f"Antes da catraca: aprovados = {aprovados}")

resultados = ["passou", "falhou", "passou"]

for resultado in resultados:
    if resultado == "passou":
        aprovados = aprovados + 1
    print(f"Passou pela catraca '{resultado}': aprovados = {aprovados}")

assert aprovados == 2
print("Verificação passou: 2 aprovados em 3 execuções")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Fonte: curso-vertex/Aulas/Aula04-Uma-Massa-Varios-Cenarios/
#        explicacao-linha-a-linha/slide-16.md
# Para mudar o texto, edite o .md e rode
# curso-vertex/scripts/embutir_explicacao_no_codigo.py de novo.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 16 da apresentacao.
#
#      27  aprovados = 0
#          Antes do laço. É a catraca zerada antes do primeiro passageiro. Se
#          essa linha estivesse dentro do for, ela rodaria em toda volta e o
#          contador voltaria a zero sempre.
#
#      28  print(f"Antes da catraca: aprovados = {aprovados}")
#          Mostra o estado inicial. Existe para a turma ver o zero antes de
#          qualquer volta.
#
#      30  resultados = ["passou", "falhou", "passou"]
#          A massa: três execuções, duas delas aprovadas.
#
#      32  for resultado in resultados:
#          Três voltas.
#
#      33  if resultado == "passou":
#          A condição que decide se a catraca gira nesta volta.
#
#      34  aprovados = aprovados + 1
#          A linha do dia. Leia da direita para a esquerda: pega o valor que
#          está na caixinha, soma um, guarda de volta na mesma caixinha. O
#          valor anterior é esquecido.
#
#      35  print(f"Passou pela catraca '{resultado}': aprovados =
#          {aprovados}")
#          Recuado uma vez, então roda em toda volta, inclusive na que não
#          incrementou. É isso que deixa o teste de mesa visível na tela.
#
#      37  assert aprovados == 2
#          Depois do laço, quando o número já está fechado. A ordem importa:
#          prepara a massa, executa a lógica, valida no fim.
#
#      38  print("Verificação passou: 2 aprovados em 3 execuções")
#          Só executa porque a linha 37 passou.
#
# --- fim da explicacao linha a linha ---
