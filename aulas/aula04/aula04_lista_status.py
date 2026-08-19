# Aula 04 - a massa de teste inteira numa variável só
#
# Antes desta aula, seis códigos de status seriam seis variáveis:
#
#   codigo_1 = 200
#   codigo_2 = 201
#   codigo_3 = 404
#   ...
#
# Isso não escala. Quarenta status novos na resposta da API seriam quarenta
# variáveis novas, e a regra de classificação teria que ser escrita quarenta
# vezes.
#
# Lista é uma planilha de uma coluna: um valor por linha, e você chega em
# qualquer linha pelo número dela.

# --- a massa, agora numa variável só ---
codigos_status = [200, 201, 404, 500, 302, 403]

print(codigos_status)
print(codigos_status[0])
print(codigos_status[2])
print(codigos_status[-1])
print(len(codigos_status))
print(404 in codigos_status)
print(999 in codigos_status)

# --- o erro de índice, provocado de propósito ---
# Seis itens, índices de zero a cinco: o último índice é sempre o tamanho
# menos um. Pedir o seis levanta IndexError. O try/except existe para o
# arquivo não morrer aqui e a saída de baixo continuar aparecendo.
try:
    print(codigos_status[6])
except IndexError as erro:
    print(f"IndexError: {erro}")

# --- o índice certo, para ver o verde depois do vermelho ---
print(codigos_status[5])

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Fonte: curso-vertex/Aulas/Aula04-Uma-Massa-Varios-Cenarios/
#        explicacao-linha-a-linha/slide-05.md
# Para mudar o texto, edite o .md e rode
# curso-vertex/scripts/embutir_explicacao_no_codigo.py de novo.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 5 da apresentacao.
#
#      18  codigos_status = [200, 201, 404, 500, 302, 403]
#          Uma variável, seis valores, na ordem em que foram escritos. Os
#          colchetes são o que faz disso uma lista.
#
#      19  Linha em branco
#          Separa a massa das consultas.
#
#      20  print(codigos_status)
#          Imprime a lista inteira, com colchetes e vírgulas: é assim que o
#          Python mostra uma lista.
#
#      21  print(codigos_status[0])
#          Sai 200. Zero é a primeira posição, e essa é a convenção que a
#          turma vai carregar para sempre.
#
#      22  print(codigos_status[2])
#          Sai 404. Conte no dedo com a turma: 0 é 200, 1 é 201, 2 é 404.
#
#      23  print(codigos_status[-1])
#          Sai 403. Menos um conta de trás para frente e devolve o último, sem
#          precisar saber o tamanho.
#
#      24  print(len(codigos_status))
#          Sai 6. len conta itens, e esse número é o que vira asserção no
#          slide 7.
#
#      25  print(404 in codigos_status)
#          Sai True. O in responde presença e devolve booleano, o mesmo tipo
#          da Aula 02.
#
#      26  print(999 in codigos_status)
#          Sai False. Ausência responde igual, e é a versão de lista da
#          verificação "esse status não pode aparecer".
#
# --- fim da explicacao linha a linha ---
