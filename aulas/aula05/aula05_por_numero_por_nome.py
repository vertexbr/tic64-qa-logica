# Aula 05 - o mesmo registro por número e por nome
#
# Na Aula 04 a massa era uma coluna de números, e o acesso era sempre pela
# posição: [0] era o primeiro, [-1] era o mais recente. Isso funciona enquanto
# os itens são vários exemplos da mesma coisa.
#
# Um usuário não é isso. Id, nome e e-mail são campos diferentes de uma coisa
# só, e campo tem nome. Guardar um registro numa lista obriga a contar no dedo,
# e quebra no dia em que alguém inclui um campo no meio.

# --- o jeito da Aula 04, e o problema dele ---
usuario_lista = [42, "Gaia Silva", "gaia@teste.com", "ativo", True]

print(usuario_lista[2])

# O dia em que o desenvolvedor inclui o telefone entre o nome e o e-mail:
usuario_com_telefone = [42, "Gaia Silva", "82999990000", "gaia@teste.com", "ativo", True]

print(usuario_com_telefone[2])

# A posição 2 continua respondendo, e agora responde a coisa errada. Nenhum
# erro e nenhum aviso: o teste passa a comparar telefone com e-mail e ninguém
# fica sabendo.

# --- o mesmo registro, agora com nome em cada campo ---
usuario = {"id": 42, "nome": "Gaia Silva", "email": "gaia@teste.com"}

print(usuario["nome"])
print(usuario["email"])

# --- alterar uma chave que existe, criar uma que não existe ---
usuario["nome"] = "Gaia Souza"
usuario["ativo"] = True

print(usuario)

assert usuario["nome"] == "Gaia Souza"
assert usuario["ativo"] == True
print("Verificações passaram: a alteração e a criação aconteceram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Fonte: curso-vertex/Aulas/Aula05-Lendo-JSON-com-Olhar-de-QA/
#        explicacao-linha-a-linha/slide-05.md
# Para mudar o texto, edite o .md e rode
# curso-vertex/scripts/embutir_explicacao_no_codigo.py de novo.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 5 da apresentacao.
#
#      26  usuario = {"id": 42, "nome": "Gaia Silva", "email":
#          "gaia@teste.com"}
#          Chaves em vez de colchetes na criação, e cada par é
#          "nome_do_campo": valor, separados por vírgula. É o mesmo dado da
#          lista de cima, agora com um rótulo do lado de cada valor.
#
#      27  Linha em branco
#          Separa a criação do registro das consultas nele.
#
#      28  print(usuario["nome"])
#          Sai Gaia Silva. Na leitura continua colchete, mas com o nome do
#          campo dentro dele em vez do número.
#
#      29  print(usuario["email"])
#          Sai gaia@teste.com. E aqui está a resposta do slide 3: se o
#          desenvolvedor incluir telefone no meio, esta linha continua
#          funcionando, porque nome não muda de lugar.
#
#      30  Linha em branco
#          Separa a leitura da escrita.
#
#      31  # --- alterar uma chave que existe, criar uma que não existe ---
#          Comentário de seção. O professor lê ele em voz alta antes de
#          revelar as duas linhas de baixo, porque o contraste entre as duas é
#          o conteúdo.
#
#      32  usuario["nome"] = "Gaia Souza"
#          Altera uma chave que já existia. O valor antigo é jogado fora.
#
#      33  usuario["ativo"] = True
#          Cria uma chave que não existia. Sintaxe idêntica à linha de cima,
#          efeito diferente, e o Python não avisa qual dos dois aconteceu.
#
#      34  Linha em branco
#          Separa a escrita da conferência.
#
#      35  print(usuario)
#          Sai o dicionário inteiro, com as chaves na ordem em que foram
#          criadas: o ativo aparece no fim porque foi o último a entrar. É
#          aqui que a turma vê que a linha 33 criou um campo novo.
#
#      36  Linha em branco
#          Separa a saída das verificações.
#
#      37  assert usuario["nome"] == "Gaia Souza"
#          Prova que a alteração pegou. Silêncio quando passa, como na Aula
#          04.
#
#      38  assert usuario["ativo"] == True
#          Prova que a criação pegou. Está escrito == True de propósito, pela
#          regra da Aula 03 de nunca escrever condição sem comparação
#          explícita.
#
#      39  print("Verificações passaram: a alteração e a criação aconteceram")
#          A linha que confirma que os dois assert de cima passaram. Sem ela,
#          silêncio é indistinguível de arquivo que não rodou.
#
# --- fim da explicacao linha a linha ---
