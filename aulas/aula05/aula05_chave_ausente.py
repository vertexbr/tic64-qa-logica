# Aula 05 - as três ferramentas para a chave que talvez não exista
#
# O arquivo anterior quebrou com KeyError: 'telefone'. Este resolve, e resolve
# de três formas, porque as três servem para situações diferentes.
#
# O rótulo de prioridade, que é o que vale guardar: colchete quando o campo é
# obrigatório e a ausência dele é defeito que você QUER que estoure, get
# quando o campo é opcional. É o hábito que evita KeyError em suíte de
# madrugada.

usuario = {"id": 42, "nome": "Gaia Silva", "email": "gaia@teste.com"}

# --- in responde se a chave existe, e devolve booleano ---
print(f"Tem chave telefone? {'telefone' in usuario}")

# --- get devolve o valor, ou None se a chave não existe, sem quebrar ---
print(f"Com get: {usuario.get('telefone')}")

# --- get com segundo argumento devolve o padrão que você escolher ---
print(f"Com get e padrão: {usuario.get('telefone', 'não informado')}")

# --- e o colchete continua sendo o certo no campo obrigatório ---
print(f"O id, que é obrigatório: {usuario['id']}")

assert "email" in usuario
assert usuario.get("telefone") == None
assert usuario.get("telefone", "não informado") == "não informado"
print("As três verificações passaram")

# Nota de estilo, para quem já viu "is None" em algum lugar: aqui está escrito
# == None de propósito, pela regra da Aula 03 de nunca escrever condição sem
# comparação explícita. As duas formas funcionam, e o curso escolheu uma.

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Fonte: curso-vertex/Aulas/Aula05-Lendo-JSON-com-Olhar-de-QA/
#        explicacao-linha-a-linha/slide-07.md
# Para mudar o texto, edite o .md e rode
# curso-vertex/scripts/embutir_explicacao_no_codigo.py de novo.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 7 da apresentacao.
#
#      11  usuario = {"id": 42, "nome": "Gaia Silva", "email":
#          "gaia@teste.com"}
#          O mesmo registro do arquivo anterior, sem telefone. A ausência do
#          campo é o que faz o arquivo inteiro existir.
#
#      12  Linha em branco
#          Separa a massa das três ferramentas.
#
#      13  # --- in responde se a chave existe, e devolve booleano ---
#          Comentário de seção.
#
#      14  print(f"Tem chave telefone? {'telefone' in usuario}")
#          Sai False. O in responde presença e devolve booleano, igual ao in
#          de lista da Aula 04. Repare nas aspas simples na chave: a f-string
#          já está entre aspas duplas, e misturar as duas dá SyntaxError.
#
#      15  Linha em branco
#          Separa as ferramentas.
#
#      16  # --- get devolve o valor, ou None se a chave não existe, sem
#          quebrar ---
#          Comentário de seção.
#
#      17  print(f"Com get: {usuario.get('telefone')}")
#          Sai None. Onde o colchete levantou KeyError, o get devolve None e o
#          programa segue.
#
#      18  Linha em branco
#          Separa as ferramentas.
#
#      19  # --- get com segundo argumento devolve o padrão que você escolher
#          ---
#          Comentário de seção.
#
#      20  print(f"Com get e padrão: {usuario.get('telefone', 'não
#          informado')}")
#          Sai não informado. O segundo argumento é o valor de retorno quando
#          a chave não existe, e é ele que vira o zero do contador no slide
#          22.
#
#      21  Linha em branco
#          Separa as três ferramentas do contraexemplo.
#
#      22  # --- e o colchete continua sendo o certo no campo obrigatório ---
#          Comentário de seção, e o mais importante do arquivo.
#
#      23  print(f"O id, que é obrigatório: {usuario['id']}")
#          Sai 42. O colchete não é o jeito errado: é o jeito certo quando a
#          ausência do campo é defeito que você quer que estoure.
#
#      24  Linha em branco
#          Separa a leitura das verificações.
#
#      25  assert "email" in usuario
#          Prova que o campo obrigatório está presente. É o degrau da escada
#          de asserções que a Aula 08 recicla: presença de chave como
#          verificação deliberada, não como acidente.
#
#      26  assert usuario.get("telefone") == None
#          Prova que o get devolveu None sem quebrar.
#
#      27  assert usuario.get("telefone", "não informado") == "não informado"
#          Prova que o padrão foi devolvido. Três verificações, uma por
#          ferramenta.
#
#      28  print("As três verificações passaram")
#          Confirma que os três assert de cima passaram.
#
# --- fim da explicacao linha a linha ---
