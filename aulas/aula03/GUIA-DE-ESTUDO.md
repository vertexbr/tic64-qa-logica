# Guia de estudo · Aula 03

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso) — este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

## `aula03_operadores.py`

Primeira demonstração da Aula 03:

```python
print(10 + 5)
print(10 / 5)
print(7 // 2)
print(7 % 2)

# --- comparação ---
# Todo operador de comparação devolve um bool: True ou False, nunca outra coisa.
# Um sinal de igual guarda, dois sinais comparam.
status_code = 200

print(status_code == 200)
print(status_code != 200)
print(status_code < 300)
print(status_code >= 200)

# --- lógicos ---
# ...
```

Arquivo completo: `aulas/aula03/aula03_operadores.py` (28 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula03_login_evidencia.py`

A evidência esperado x obtido no caso de teste de login da Aula 02, com a mesma massa do `aulas/aula02/aula02_login.py`.

```python
caso = "CT-01"
usuario_informado = "Nadinha"
senha_informada = "JL1234!"
usuario_esperado = "Nadinha"
senha_esperada = "JL1234!"
valor_produto = 199.90
quantidade = 3

# --- processamento ---
total = valor_produto * quantidade

# --- evidência esperado x obtido ---
print(f"{caso} | usuário | esperado: {usuario_esperado} | obtido: {usuario_informado} | confere? {usuario_informado == usuario_esperado}")
print(f"{caso} | senha   | esperado: {senha_esperada} | obtido: {senha_informada} | confere? {senha_informada == senha_esperada}")
print(f"{caso} | total   | esperado: 599.70 | obtido: {total} | confere? {total == 599.70}")

# ...
```

Arquivo completo: `aulas/aula03/aula03_login_evidencia.py` (31 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula03_desconto.py`

O arquivo-âncora da Aula 03:

```python
caso = "CT-01"
valor_compra = 300.00
cliente_vip = True
cupom_valido = False
produto_em_promocao = False
desconto_esperado = 20

# --- a decisão ---
# A escada é percorrida de cima para baixo, e só o primeiro ramo que der
# verdadeiro é executado. A condição mais específica vem primeiro.
if cliente_vip and valor_compra > 200:
    desconto = 20
elif cliente_vip:
    desconto = 10
elif cupom_valido or produto_em_promocao:
    desconto = 5
# ...
```

Arquivo completo: `aulas/aula03/aula03_desconto.py` (63 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula03_desconto_invertido.py`

O erro proposital da Aula 03:

```python
caso = "CT-01"
valor_compra = 300.00
cliente_vip = True
cupom_valido = False
produto_em_promocao = False
desconto_esperado = 20

# --- a decisão, na ordem errada de propósito ---
if cliente_vip:
    desconto = 10
elif cliente_vip and valor_compra > 200:
    desconto = 20
elif cupom_valido or produto_em_promocao:
    desconto = 5
else:
    desconto = 0
# ...
```

Arquivo completo: `aulas/aula03/aula03_desconto_invertido.py` (32 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula03_gate_release.py`

A escada de faixas da Aula 03, no contexto que a turma vai viver a carreira inteira:

```python
taxa_aprovacao = 85
decisao_esperada = "libera com ressalva"

# --- a decisão ---
if taxa_aprovacao >= 90:
    decisao = "libera"
elif taxa_aprovacao >= 80:
    decisao = "libera com ressalva"
elif taxa_aprovacao >= 70:
    decisao = "segura para revisão"
else:
    decisao = "bloqueia"

# --- evidência esperado x obtido ---
print(f"Taxa {taxa_aprovacao}% | esperado: {decisao_esperada} | obtido: {decisao} | confere? {decisao == decisao_esperada}")
```

Arquivo completo: `aulas/aula03/aula03_gate_release.py` (53 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula03_defeitos.py`

A classificação de defeitos da Aula 01 virando Python, com a regra numa forma que evoluiu desde lá:

```python
caso = "CT-01"
impede_producao = True
tem_workaround = False
severidade_esperada = "CRÍTICA"

# --- a decisão ---
if impede_producao and not tem_workaround:
    severidade = "CRÍTICA"
elif impede_producao and tem_workaround:
    severidade = "ALTA"
else:
    severidade = "MÉDIA"

# --- evidência esperado x obtido ---
print(f"{caso} | esperado: {severidade_esperada} | obtido: {severidade} | confere? {severidade == severidade_esperada}")
```

Arquivo completo: `aulas/aula03/aula03_defeitos.py` (51 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `quadro_erro4.py`

O quarto erro do quadro da Aula 03, o pior do curso:

```python
idade_texto = "18"
# idade = int(idade_texto)

if idade_texto == 18:
    print("maior de idade")
else:
    print("menor de idade")

# print(type(idade_texto))
# print(type(18))
# print(idade_texto == 18)
```

Arquivo completo: `aulas/aula03/quadro_erro4.py` (11 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.
