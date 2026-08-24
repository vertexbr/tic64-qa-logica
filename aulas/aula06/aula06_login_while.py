# Aula 06 - o while das tentativas de login
#
# O requisito: "o sistema deve permitir até três tentativas de senha, e
# bloquear o usuário na terceira falha". Tem "até", tem condição de parada, e o
# acerto pode vir na primeira tentativa. É while.
#
# Leia a condição em voz alta: "enquanto o número de tentativas for menor que o
# total E ainda não tiver logado, repita". Duas condições ligadas por and,
# exatamente os operadores lógicos da Aula 03.
#
# Para ver o caminho do bloqueio, troque "JL1234!" por "errada3" na linha da
# massa e rode de novo. Mesma lógica, massa diferente, resultado diferente, e
# nenhuma linha de lógica alterada.

senha_correta = "JL1234!"
tentativas = ["errada1", "errada2", "JL1234!"]   # <- a massa

numero = 0
logou = False

while numero < len(tentativas) and not logou:
    senha = tentativas[numero]
    # Esta é a catraca do ônibus da Aula 04 de volta, com trabalho novo: ela é
    # o que garante que a condição um dia vira falsa. Ela vem ANTES de qualquer
    # if, então roda em toda volta. Apague esta linha e o terminal enche.
    # Esta linha é a catraca de aulas/aula04/aula04_catraca.py, igual letra por
    # letra. O acréscimo é o trabalho que ela faz aqui: lá ela contava, e aqui
    # ela é o que garante que a condição do while um dia vira falsa. Em
    # aulas/aula04/aula04_catraca_sem_incremento.py está o que acontece sem ela.
    numero = numero + 1
    if senha == senha_correta:
        print(f"Login OK na tentativa {numero}")
        logou = True
    else:
        print(f"Tentativa {numero} falhou")

if not logou:
    print("Usuário bloqueado")

print(f"Tentativas consumidas: {numero}")

# Repare como o esperado do primeiro assert foi escrito: ele não diz "True",
# ele diz a REGRA, que é "logou se a senha correta está entre as tentativas".
# Esperado vem da regra, obtido vem do programa. Escrito assim, o assert
# continua valendo quando eu trocar a massa ao vivo, e é isso que um teste
# bem escrito faz: ele descreve o requisito, não o resultado de uma execução.
assert logou == (senha_correta in tentativas)
assert numero == 3
print("As duas verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-19.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 19 da apresentacao.
#
#      15  senha_correta = "JL1234!"
#          O esperado, e ele vem do requisito.
#
#      16  tentativas = ["errada1", "errada2", "JL1234!"]   # <- a massa
#          A massa, e é só ela que muda para ver o outro caminho. Lista da
#          Aula 04, com três itens escolhidos: duas falhas e um acerto no
#          limite.
#
#      18  numero = 0
#          O contador começa em zero, porque nenhuma tentativa foi feita
#          ainda.
#
#      19  logou = False
#          A bandeira começa falsa, porque ninguém logou ainda. É o acumulador
#          booleano da Aula 04.
#
#      21  while numero < len(tentativas) and not logou:
#          Leia em voz alta: enquanto o número de tentativas for menor que o
#          total e ainda não tiver logado, repita. Duas condições ligadas por
#          and, que são os operadores lógicos da Aula 03 dentro de uma
#          estrutura nova.
#
#      22  senha = tentativas[numero]
#          Pega a tentativa da vez pelo número da posição. É LISTA USA NÚMERO
#          de volta, uma aula depois de o dicionário ter sido a estreia.
#
#      30  numero = numero + 1
#          A linha mais importante do arquivo. É a catraca da Aula 04, com
#          trabalho novo: ela é o que garante que a condição um dia vira
#          falsa. Ela está antes de qualquer if, então roda em toda volta.
#          Apague ela e o terminal enche.
#
#      31  if senha == senha_correta:
#          Dois iguais comparam, um igual guarda.
#
#      32  print(f"Login OK na tentativa {numero}")
#          O numero já foi incrementado, então ele diz a tentativa humana: a
#          terceira, não a segunda.
#
#      33  logou = True
#          Levanta a bandeira, e é ela que faz a segunda metade da condição
#          virar falsa na próxima volta.
#
#      34  else:
#          O caminho da falha.
#
#      35  print(f"Tentativa {numero} falhou")
#          Uma linha por tentativa gasta.
#
#      37  if not logou:
#          Fora do laço, e a indentação é o que diz isso. Se estivesse dentro,
#          imprimiria "bloqueado" a cada falha.
#
#      38  print("Usuário bloqueado")
#          Só aparece quando as três tentativas se esgotaram sem acerto.
#
#      40  print(f"Tentativas consumidas: {numero}")
#          Sai 3 nas duas massas, e é a evidência de que o laço parou por
#          motivo diferente em cada uma.
#
#      47  assert logou == (senha_correta in tentativas)
#          Ver a seção abaixo. Este assert é o mais importante do arquivo, e
#          não pela lógica dele.
#
#      48  assert numero == 3
#          Vale nas duas massas: com acerto na terceira, o contador chegou a
#          3; sem acerto, o laço rodou as três voltas.
#
#      49  print("As duas verificações passaram")
#          Fecha a execução, nas duas massas.
#
# --- fim da explicacao linha a linha ---
