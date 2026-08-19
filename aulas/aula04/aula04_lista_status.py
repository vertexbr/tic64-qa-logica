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
