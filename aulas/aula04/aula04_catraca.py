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
