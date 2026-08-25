# Guia de estudo · Aula 04

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso) — este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

## `aula04_lista_status.py`

Primeira demonstração da Aula 04:

```python
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
# ...
```

Arquivo completo: `aulas/aula04/aula04_lista_status.py` (84 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_contagem_assert.py`

O arquivo-âncora da Aula 04:

```python
produtos = ["Camiseta", "Caneca", "Boné", "Mochila", "Adesivo", "Chaveiro"]

print(f"A listagem trouxe {len(produtos)} produtos")

# --- o confere? da Aula 03: a comparação sai na tela e alguém precisa ler ---
print(f"esperado: 6 | obtido: {len(produtos)} | confere? {len(produtos) == 6}")

# --- a mesma comparação, agora com poder de veto ---
assert len(produtos) == 6
print("Verificação passou: a listagem trouxe 6 produtos")

# --- e quando a conta não bate ---
# Trocar o 6 por 7 faz a verificação interromper o programa. O try/except
# está aqui só para o arquivo seguir até o fim.
try:
    assert len(produtos) == 7
# ...
```

Arquivo completo: `aulas/aula04/aula04_contagem_assert.py` (105 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_for_primeiro.py`

O `for` na forma mais curta possível, sobre uma lista de casos de teste.

```python
casos_de_teste = ["login válido", "login com senha errada", "login com usuário bloqueado"]

for caso in casos_de_teste:
    print(f"Executando: {caso}")

# Três voltas, porque a lista tem três itens. Quem decide o número de voltas
# é a lista, não este código: é por isso que, se chegarem quarenta casos, as
# duas linhas acima não mudam em nada.
assert len(casos_de_teste) == 3, f"esperado 3 casos, obtido {len(casos_de_teste)}"
print("Verificação passou: 3 casos percorridos")
```

Arquivo completo: `aulas/aula04/aula04_for_primeiro.py` (24 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_range.py`

O `range` e o off-by-one que mora nele:

```python
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
# ...
```

Arquivo completo: `aulas/aula04/aula04_range.py` (27 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_classificar_status.py`

A primeira demonstração guiada da aula:

```python
codigos_status = [200, 201, 404, 500, 302, 403]

# A massa é conferida antes de ser usada. Se a listagem chegar com um item
# a menos, o programa para aqui e não produz um relatório errado.
assert len(codigos_status) == 6
print("Massa conferida: 6 códigos para classificar")

for codigo in codigos_status:
    if codigo >= 200 and codigo < 300:
        categoria = "Sucesso"
    elif codigo >= 400 and codigo < 500:
        categoria = "Erro do cliente"
    elif codigo >= 500:
        categoria = "Erro do servidor"
    else:
        categoria = "Redirecionamento ou outro"
# ...
```

Arquivo completo: `aulas/aula04/aula04_classificar_status.py` (108 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_catraca.py`

O contador, que é a catraca do ônibus:

```python
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
# ...
```

Arquivo completo: `aulas/aula04/aula04_catraca.py` (85 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_catraca_sem_incremento.py`

O erro proposital da Aula 04, e o argumento de existência da automação:

```python
aprovados = 0
resultados = ["passou", "falhou", "passou"]

for resultado in resultados:
    if resultado == "passou":
        # aprovados = aprovados + 1
        print("achei um que passou")

print(f"aprovados = {aprovados}")

# A condição funcionou: o print de dentro do if apareceu duas vezes. O que
# faltou foi mudar a variável. A verificação é o que transforma um número
# errado, que ninguém notaria, em erro visível.
try:
    assert aprovados == 2, f"esperado 2, obtido {aprovados}"
    print("esta linha não chega a ser impressa")
# ...
```

Arquivo completo: `aulas/aula04/aula04_catraca_sem_incremento.py` (83 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_foguete.py`

O contador andando para trás.

```python
contagem = 5

for volta in range(5):
    print(f"{contagem}...")
    contagem = contagem - 1

print("Lançamento!")

assert contagem == 0, f"esperado 0, obtido {contagem}"
print("Verificação passou: a contagem chegou a zero")
```

Arquivo completo: `aulas/aula04/aula04_foguete.py` (26 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_freio_de_mao.py`

`break` e `continue` na mesma execução.

```python
usuarios = ["standard_user", "problem_user", "locked_out_user", "visual_user"]

# --- break: achei o que procurava, não preciso varrer o resto ---
for usuario in usuarios:
    print(f"Tentando login com {usuario}")
    if usuario == "locked_out_user":
        print("Usuário bloqueado encontrado. Freio de mão: parando a varredura.")
        break

print("Varredura encerrada")

# O visual_user estava na lista e não foi testado, porque o laço morreu
# antes de chegar nele. Isso é o comportamento esperado do break, e não um
# defeito: quem usa break aceita não visitar o resto.
assert usuarios[-1] == "visual_user"
print("Verificação passou: o último usuário da lista não chegou a ser visitado")
# ...
```

Arquivo completo: `aulas/aula04/aula04_freio_de_mao.py` (32 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_unicidade.py`

O acumulador e a unicidade.

```python
codigos = [200, 201, 404, 500, 302, 403]
falhas = []

for codigo in codigos:
    if codigo >= 400:
        falhas.append(codigo)

print(f"Códigos de falha encontrados: {falhas}")

assert len(falhas) == 3, f"esperado 3 falhas, obtido {len(falhas)}"
print("Verificação passou: 3 códigos de falha na execução")

print()

# --- unicidade: uma regra de negócio presente em quase todo sistema ---
# set joga fora as repetições. Se o tamanho da lista e o tamanho do
# ...
```

Arquivo completo: `aulas/aula04/aula04_unicidade.py` (53 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_laco_infinito.py`

A vacina contra o travamento que todo iniciante provoca em casa.

```python
contagem = 5

while contagem > 0:
    print(f"{contagem}...")
    contagem = contagem - 1

print("Lançamento!")

assert contagem == 0, f"esperado 0, obtido {contagem}"
print("Verificação passou: a contagem terminou em zero e o laço acabou")
```

Arquivo completo: `aulas/aula04/aula04_laco_infinito.py` (49 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_resumo_execucao.py`

A segunda demonstração guiada:

```python
resultados = ["passou", "falhou", "passou", "passou", "falhou"]
tempos = [1.20, 0.80, 3.45, 1.10, 2.90]

total = len(resultados)
aprovados = 0
falhas = 0

for resultado in resultados:
    if resultado == "passou":
        aprovados = aprovados + 1
    else:
        falhas = falhas + 1

percentual = (aprovados / total) * 100

mais_lento = tempos[0]
# ...
```

Arquivo completo: `aulas/aula04/aula04_resumo_execucao.py` (127 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula04_desafio_extra.py`

O desafio extra da aula:

```python
codigos = [200, 200, 404, 500, 200]
interrompida = False

for codigo in codigos:
    if codigo == 200:
        continue
    print(f"Código fora do esperado: {codigo}")
    if codigo >= 500:
        print("Erro de servidor. A suíte foi interrompida.")
        interrompida = True
        break

print(f"Suíte interrompida? {interrompida}")

# A variável já é booleana, então ela decide sozinha e não precisa de
# comparação. Escrever interrompida == True funciona e é redundante.
# ...
```

Arquivo completo: `aulas/aula04/aula04_desafio_extra.py` (28 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.
