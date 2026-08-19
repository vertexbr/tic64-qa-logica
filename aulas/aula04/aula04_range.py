# Aula 04 - range, e o off-by-one que mora nele
#
# range(3) gera zero, um e dois: três números, começando em zero e
# terminando em dois. Guarde a frase: range de N vai de zero até N menos um.
#
# É o erro de contagem mais comum de quem está começando, e ele tem nome em
# inglês, off-by-one, porque erra sempre por exatamente um.

for i in range(3):
    print(f"Volta número {i}")

print()

# --- a versão com a posição, que é para consultar, não para guardar ---
# Use esta só quando o número da posição fizer parte do que você quer, tipo
# imprimir "caso 3 de 10". Se você usou range(len(...)) só para depois
# escrever lista[i], escolheu o caminho longo.
casos_de_teste = ["login válido", "login com senha errada", "login com usuário bloqueado"]

for posicao in range(len(casos_de_teste)):
    print(f"Caso {posicao + 1} de {len(casos_de_teste)}: {casos_de_teste[posicao]}")

# O mais um vai no número que você imprime, nunca no limite do range. Escrever
# range(len(lista) + 1) para "começar do 1" estoura na última volta com
# IndexError, e é o erro que essa linha existe para não deixar acontecer.
assert len(casos_de_teste) == 3
print("Verificação passou: as duas formas deram o mesmo número de voltas")
