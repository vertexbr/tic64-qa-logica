# Guia de estudo · Aula 02

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso) — este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

## `aula02.py`

Demonstração da Aula 02, o cenário de compra.

```python
valor_produto = 199.90
quantidade = 3
cliente_ativo = True
valor_minimo_frete_gratis = 250.00

total = valor_produto * quantidade

print(f"Produto: R$ {valor_produto:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total da compra: R$ {total:.2f}")
print(f"Cliente ativo? {cliente_ativo}")
print(f"Frete grátis a partir de R$ {valor_minimo_frete_gratis:.2f}")

print(type(valor_produto))
print(type(quantidade))
print(type(cliente_ativo))
```

Arquivo completo: `aulas/aula02/aula02.py` (19 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula02_login.py`

Segunda demonstração da Aula 02, o caso de teste de login.

```python
usuario_informado = "Nadinha"
senha_informada = "JL1234!"
usuario_esperado = "Nadinha"
senha_esperada = "JL1234!"
tentativas = 0
token = None

print(f"Usuário informado: {usuario_informado}")
print(f"Usuário esperado: {usuario_esperado}")
print(f"Usuários iguais? {usuario_informado == usuario_esperado}")
print(f"Senhas iguais? {senha_informada == senha_esperada}")
print(f"Tentativas: {tentativas} | Token: {token}")
```

Arquivo completo: `aulas/aula02/aula02_login.py` (14 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula02_tipos_e_nomes.py`

Demonstrações do primeiro ciclo da Aula 02:

```python
valor_produto = 199.90      # certo: o nome descreve o conteúdo

# x = 199.90                  # proibido neste curso: não diz o que guarda
# dado1 = True                 # proibido neste curso: não diz o que guarda

# Os cinco tipos que este curso usa, com um exemplo do vocabulário do curso
# para cada um:

endpoint = "/api/login"     # str, texto, sempre entre aspas
status_code = 200           # int, número inteiro, sem aspas
tempo_resposta = 1.42       # float, decimal, com PONTO
cliente_ativo = True        # bool, True ou False, com maiúscula
token = None                 # None, ausência de valor

print(f"endpoint: {endpoint} | tipo: {type(endpoint)}")
# ...
```

Arquivo completo: `aulas/aula02/aula02_tipos_e_nomes.py` (76 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula02_conversao_e_armadilhas.py`

Demonstrações do segundo ciclo da Aula 02:

```python
qtd_da_tela = "10"      # veio da tela, então é texto
qtd_do_estoque = "5"    # veio de um arquivo, então é texto

print(f"Sem converter: {qtd_da_tela + qtd_do_estoque}")
print(f"Convertido: {int(qtd_da_tela) + int(qtd_do_estoque)}")

# --- O par 200 e "200" ---------------------------------------------------
#
# Na tela os dois valores parecem a mesma informação. Para o Python são
# tipos diferentes, e por isso o primeiro == abaixo dá falso.

codigo = 200
codigo_texto = "200"

print(f"codigo == codigo_texto? {codigo == codigo_texto}")
# ...
```

Arquivo completo: `aulas/aula02/aula02_conversao_e_armadilhas.py` (99 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.
