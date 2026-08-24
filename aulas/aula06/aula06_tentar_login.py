# Aula 06 - o while virando função-pergunta
#
# O bloco solto de aula06_login_while.py não era testável: para verificar o
# caminho do bloqueio era preciso editar o arquivo e rodar de novo. Aqui ele
# está embalado, e os dois cenários viram duas linhas.
#
# Olhem o que o retorno antecipado fez: a variável logou desapareceu, porque o
# return sai do laço E da função de uma vez. A função devolve o número da
# tentativa em que logou, e zero quando não logou nenhuma.

def tentar_login(senha_correta, tentativas):
    numero = 0
    while numero < len(tentativas):
        senha = tentativas[numero]
        numero = numero + 1
        if senha == senha_correta:
            return numero
    return 0


acertou = tentar_login("JL1234!", ["errada1", "errada2", "JL1234!"])
bloqueou = tentar_login("JL1234!", ["errada1", "errada2", "errada3"])

print(f"Logou na tentativa: {acertou}")
print(f"Bloqueado, devolveu: {bloqueou}")

# Dois cenários em duas linhas, incluindo o caminho de bloqueio, e sem editar
# nada entre as duas execuções. É isso que a função entrega ao teste.
assert tentar_login("JL1234!", ["errada1", "errada2", "JL1234!"]) == 3
assert tentar_login("JL1234!", ["errada1", "errada2", "errada3"]) == 0
assert tentar_login("JL1234!", ["JL1234!"]) == 1
print("As três verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-20.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 20 da apresentacao.
#
#      11  def tentar_login(senha_correta, tentativas):
#          Os dois dados que estavam soltos na margem viraram parâmetros. Foi
#          a regra prática do escopo decidindo: dado usado em mais de um lugar
#          sobe para parâmetro.
#
#      12  numero = 0
#          O contador nasce dentro da função, e morre quando ela termina. Cada
#          chamada tem o seu. É o que permite chamar a função duas vezes sem
#          uma interferir na outra.
#
#      13  while numero < len(tentativas):
#          A condição perdeu metade. Não há mais and not logou, e a comparação
#          com o slide 19 é o ponto todo deste slide.
#
#      14  senha = tentativas[numero]
#          Igual ao slide 19.
#
#      15  numero = numero + 1
#          A catraca, no mesmo lugar e pelo mesmo motivo.
#
#      16  if senha == senha_correta:
#          Igual ao slide 19.
#
#      17  return numero
#          Aqui está o slide. O return sai do if, sai do while e sai da
#          função, os três de uma vez. É por isso que a variável logou
#          desapareceu: ela existia só para dizer ao while que podia parar, e
#          o return já faz isso.
#
#      18  return 0
#          Só é alcançado quando o laço terminou sem acerto. Zero é a resposta
#          para "não logou em nenhuma tentativa", e é honesto porque tentativa
#          nenhuma se chama zero.
#
#      21  acertou = tentar_login("JL1234!", ["errada1", "errada2",
#          "JL1234!"])
#          Primeiro cenário. Devolve 3.
#
#      22  bloqueou = tentar_login("JL1234!", ["errada1", "errada2",
#          "errada3"])
#          Segundo cenário, na linha seguinte, sem editar nada. Devolve 0.
#
#      24  print(f"Logou na tentativa: {acertou}")
#          Sai 3.
#
#      25  print(f"Bloqueado, devolveu: {bloqueou}")
#          Sai 0.
#
#      29  assert tentar_login("JL1234!", ["errada1", "errada2", "JL1234!"])
#          == 3
#          O caminho do acerto.
#
#      30  assert tentar_login("JL1234!", ["errada1", "errada2", "errada3"])
#          == 0
#          O caminho do bloqueio, que no slide 19 exigia editar o arquivo.
#          Esta linha é o valor inteiro de ter embalado.
#
#      31  assert tentar_login("JL1234!", ["JL1234!"]) == 1
#          Acerto na primeira, que é o cenário que o requisito permite e
#          ninguém testa. Custou uma linha.
#
#      32  print("As três verificações passaram")
#          Fecha a execução.
#
# --- fim da explicacao linha a linha ---
