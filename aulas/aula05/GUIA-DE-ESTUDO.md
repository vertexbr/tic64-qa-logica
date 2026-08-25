# Guia de estudo · Aula 05

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso) — este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

## `aula05_por_numero_por_nome.py`

Primeira demonstração da Aula 05:

```python
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

# ...
```

Arquivo completo: `aulas/aula05/aula05_por_numero_por_nome.py` (106 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_chave_ausente_erro.py`

Os dois `KeyError` da aula, na ordem que importa:

```python
usuario = {"id": 42, "nome": "Gaia Silva", "email": "gaia@teste.com"}

# --- erro 1: o dedo procurando a posição zero, que é o hábito da Aula 04 ---
try:
    print(usuario[0])
except KeyError as erro:
    print(f"KeyError: {erro}")

# Cuidado com a leitura errada, que é a mais comum: isso NÃO quer dizer que
# dicionário recusa número. Aceita, e {0: "ok"} é dicionário válido. O que
# aconteceu foi uma busca pela chave 0, que este dicionário não tem. A regra
# do dia é sobre nome contra posição, não sobre texto contra número.
print(f"Dicionário aceita chave numérica? {0 in {0: 'ok'}}")

# --- erro 2: a chave que não existe neste registro ---
try:
# ...
```

Arquivo completo: `aulas/aula05/aula05_chave_ausente_erro.py` (40 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_chave_ausente.py`

A resposta ao arquivo anterior, em três ferramentas:

```python
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
# ...
```

Arquivo completo: `aulas/aula05/aula05_chave_ausente.py` (110 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_aninhado.py`

A estrutura mais importante do curso:

```python
usuario = {
    "id": 42,
    "nome": "Gaia Silva",
    "email": "  GAIA@Teste.COM  ",
    "situacao": "ativo",
    "perfis": ["admin", "editor"],
    "endereco": {"cidade": "Fortaleza", "uf": "CE"}
}

print(f"Cidade: {usuario['endereco']['cidade']}")
print(f"Primeiro perfil: {usuario['perfis'][0]}")
print(f"Quantidade de perfis: {len(usuario['perfis'])}")
print(f"É admin? {'admin' in usuario['perfis']}")

assert usuario["endereco"]["uf"] == "CE"
assert len(usuario["perfis"]) == 2
# ...
```

Arquivo completo: `aulas/aula05/aula05_aninhado.py` (127 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_suite_casos.py`

Lista de dicionários, que é literalmente uma suíte de casos de teste:

```python
suite = [
    {"caso": "login válido", "resultado": "passou"},
    {"caso": "senha errada", "resultado": "passou"},
    {"caso": "usuário bloqueado", "resultado": "falhou"},
]

for caso in suite:
    print(f"{caso['caso']}: {caso['resultado']}")

# O índice negativo da Aula 04 continua valendo na lista de fora, e agora ele
# entrega um dicionário, do qual se pega um campo por nome. Dois modos de
# acesso na mesma linha, um por andar.
print(f"Resultado mais recente: {suite[-1]['resultado']}")

assert len(suite) == 3
assert suite[-1]["resultado"] == "falhou"
# ...
```

Arquivo completo: `aulas/aula05/aula05_suite_casos.py` (26 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_mapa_ambientes.py`

O dicionário que quem testa usa mais do que qualquer outro, e ele não é dicionário de pessoa:

```python
ambientes = {
    "teste": "https://teste.loja.com",
    "homologacao": "https://homologacao.loja.com",
    "producao": "https://loja.com",
}

# Percorrer um dicionário com for entrega as CHAVES, não os valores, e é por
# isso que ambientes[nome] aparece dentro do laço para ver o endereço.
for nome in ambientes:
    print(f"{nome}: {ambientes[nome]}")

ambiente_atual = "teste"
url_base = ambientes[ambiente_atual]

print(f"Rodando a suíte contra: {url_base}")
print(f"Endereço de login: {url_base}/login")
# ...
```

Arquivo completo: `aulas/aula05/aula05_mapa_ambientes.py` (97 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_json_minusculo_erro.py`

JSON e dicionário Python são visualmente quase idênticos, e a diferença são três palavras:

```python
resposta = {"nome": "Gaia", "ativo": True, "telefone": None}

print(resposta)
print(f"Ativo? {resposta['ativo']}")
print(f"Telefone: {resposta['telefone']}")

# None não é a mesma coisa que texto vazio nem que zero, e essa distinção
# aparece em resposta de API todo dia: campo que veio nulo contra campo que
# veio em branco são dois defeitos diferentes.
print(f"O telefone é None? {resposta['telefone'] == None}")
print(f"O telefone é texto vazio? {resposta['telefone'] == ''}")

assert resposta["ativo"] == True
assert resposta["telefone"] == None
print("Verificações passaram: o resto é igual ao dicionário de sempre")
```

Arquivo completo: `aulas/aula05/aula05_json_minusculo_erro.py` (44 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_resposta_listagem.py`

A resposta de listagem copiada da aba de rede do navegador e transcrita para dicionário Python.

```python
resposta = {
    "quantidade": 3,
    "produtos": [
        {"nome": "Api de teste", "preco": 1000, "quantidade": 1, "_id": "4Y9sHbAT4YGPVdnD"},
        {"nome": "TV SONY", "preco": 5000, "quantidade": 10, "_id": "K6leHdftCeOJj8BJ"},
        {"nome": "Mouse Gamer", "preco": 100, "quantidade": 50, "_id": "9OVBpvPYbjaXqBTG"},
    ]
}

print(f"A API disse que trouxe {resposta['quantidade']} produtos")
print(f"A lista tem de verdade {len(resposta['produtos'])} produtos")

assert resposta["quantidade"] == len(resposta["produtos"])
print("Verificação passou: o campo quantidade bate com o tamanho da lista")

# Dois degraus a mais, e os dois são vocabulário que a Aula 08 recicla dentro
# ...
```

Arquivo completo: `aulas/aula05/aula05_resposta_listagem.py` (38 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_usuario_beto.py`

Primeira demonstração guiada da Aula 05, e o arquivo para refazer em casa:

```python
usuario = {
    "id": 7,
    "nome": "Beto Nunes",
    "email": "  BETO@Loja.COM  ",
    "situacao": "ativo",
    "perfis": ["editor"],
    "endereco": {"cidade": "Maceió", "uf": "AL"}
}

print(f"Nome: {usuario['nome']}")
print(f"Cidade: {usuario['endereco']['cidade']}")
print(f"UF: {usuario['endereco']['uf']}")
print(f"Primeiro perfil: {usuario['perfis'][0]}")
print(f"Tem telefone? {'telefone' in usuario}")
print(f"Telefone: {usuario.get('telefone', 'não informado')}")

# ...
```

Arquivo completo: `aulas/aula05/aula05_usuario_beto.py` (44 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_email_sujo.py`

O antídoto de uma família inteira de testes instáveis.

```python
email_bruto = "  GAIA@Teste.COM  "

print(f"Original: '{email_bruto}'")
print(f"Tamanho original: {len(email_bruto)}")
print(f"Só com strip: '{email_bruto.strip()}'")
print(f"Só com lower: '{email_bruto.lower()}'")

# strip tira espaço das duas pontas, lower põe tudo em minúscula, e as duas
# juntas na mesma linha são o que se chama normalizar. Funciona porque cada
# método devolve uma string nova, e o método seguinte age sobre esse resultado.
email_limpo = email_bruto.strip().lower()

print(f"Normalizado: '{email_limpo}'")

# String em Python é IMUTÁVEL: método de texto nunca muda o original, ele
# devolve um texto novo. Se você escrever email.strip() sozinho numa linha e
# ...
```

Arquivo completo: `aulas/aula05/aula05_email_sujo.py` (140 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_codigos_status.py`

Pertinência com lista de códigos, que é o jeito legível de validar status.

```python
codigos_de_sucesso = [200, 201, 204]
codigos_de_erro_servidor = [500, 502, 503]

codigo = 201

print(f"Status recebido: {codigo}")
print(f"Está entre os de sucesso? {codigo in codigos_de_sucesso}")
print(f"Está entre os erros de servidor? {codigo in codigos_de_erro_servidor}")

assert codigo in codigos_de_sucesso
assert codigo not in codigos_de_erro_servidor
print("Verificações passaram")
```

Arquivo completo: `aulas/aula05/aula05_codigos_status.py` (25 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_contagem_por_chave.py`

Contagem por chave nas duas formas, e é a técnica que sustenta o desafio final da Aula 15.

```python
resultados = ["passou", "falhou", "passou", "ignorado", "passou", "falhou"]

# --- forma longa: se a chave já existe soma um, se não existe começa em um ---
contagem = {}
for resultado in resultados:
    if resultado in contagem:
        contagem[resultado] = contagem[resultado] + 1
    else:
        contagem[resultado] = 1

print(contagem)

for chave in contagem:
    print(f"{chave}: {contagem[chave]}")

assert contagem["passou"] == 3
# ...
```

Arquivo completo: `aulas/aula05/aula05_contagem_por_chave.py` (133 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_data_em_partes.py`

Trabalho de QA todo dia:

```python
data_texto = "2026-08-06"
partes = data_texto.split("-")

ano = partes[0]
mes = partes[1]
dia = partes[2]

print(f"Dia: {dia}, mês: {mes}, ano: {ano}")

# Para tirar o zero de "08" eu converti para número e voltei para texto. O int
# joga o zero fora porque zero à esquerda não significa nada em número.
mes_sem_zero = str(int(mes))
data_brasileira = f"{dia}/{mes}/{ano}"
rotulo = f"{dia}/{mes_sem_zero}/{ano}"

print(f"Mês sem o zero à esquerda: {mes_sem_zero}")
# ...
```

Arquivo completo: `aulas/aula05/aula05_data_em_partes.py` (46 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula05_validar_usuarios.py`

Segunda demonstração guiada da Aula 05, e o arquivo que junta as três estruturas do curso até aqui:

```python
usuarios = [
    {"id": 1, "nome": "Ana",  "email": "  ANA@Loja.COM  ", "situacao": "ativo",   "perfis": ["admin"]},
    {"id": 2, "nome": "",     "email": "beto@loja.com",    "situacao": "ativo",   "perfis": ["editor"]},
    {"id": 3, "nome": "Cris", "email": "cris.loja.com",    "situacao": "inativo", "perfis": []},
    {"id": 4, "nome": "Dani", "email": "dani@loja.com",    "situacao": "ativo",   "perfis": ["admin"]},
]

contagem = {}

for usuario in usuarios:
    problemas = []

    if usuario["nome"] == "":
        problemas.append("sem nome")
    if usuario["situacao"] == "inativo":
        problemas.append("inativo")
# ...
```

Arquivo completo: `aulas/aula05/aula05_validar_usuarios.py` (73 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.
