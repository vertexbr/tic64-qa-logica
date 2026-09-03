# Guia de estudo · Aula 09

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso): este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a regra de negócio e a saída esperada.

**A tese da aula:** existe um número infinito de dados e você não vai testar todos, então a pergunta não é quantos testes, é **quais**. Três técnicas respondem isso, e nenhuma delas é sintaxe: particionamento agrupa dados que se comportam igual, valor-limite ataca a fronteira, e tabela de decisão cobre as combinações. Depois de escolher os casos, o `@pytest.mark.parametrize` colapsa os testes quase idênticos numa função só, com o resultado esperado em cada linha da massa.

**A regra do comando, e aqui ela é mais dura que na Aula 08:** rode um arquivo por vez, **sempre nomeando o arquivo**. Nesta pasta dois arquivos erram na **coleta** de propósito, e erro de coleta interrompe a execução inteira: um `pytest` sem caminho aqui dentro produz uma tela vermelha em que nenhum teste rodou.

```bash
cd aulas/aula09
pytest test_aula09_idade_na_mao.py -s -v
```

**A regra que separa este curso de vários tutoriais:** o resultado esperado é o último parâmetro de cada linha da massa, e assim **todas as linhas passam**. Massa que mistura dado válido com inválido e aceita vermelho como normal destrói a suíte, porque no dia em que aparecer uma falha de verdade ninguém vai olhar.

## `aula09_regras.py`

O produto. Quatro regras que já existem no curso, e uma quinta reduzida a duas condições para caber numa tabela de decisão.

```python
def validar_idade_minima(idade):
    return idade >= 18


def tem_frete_gratis(total):
    return total >= 250.00
```

**Treino:** olhe a `classificar_nota`, no fim do arquivo, e conte quantos números estão escritos nela. Cada número é uma fronteira, e cada fronteira pede dois valores. Escreva a lista dos seis antes de olhar o próximo arquivo.

## `test_aula09_idade_na_mao.py`

Os cinco casos, um por função. É a forma que você escreveria sozinho depois da Aula 08, e ela está correta.

```python
def test_idade_17_e_rejeitada():
    assert validar_idade_minima(17) == False


def test_idade_18_e_aceita():
    assert validar_idade_minima(18) == True
```

**Treino:** conte quantas vezes o `def`, a chamada e o `assert` aparecem. São cinco de cada, para carregar dez valores. Guarde o número: o arquivo parametrizado da próxima seção tem o mesmo tamanho, e o que muda é isto.

## `test_aula09_idade_parametrizado.py`

Os mesmos cinco casos, numa função só. Três coisas novas, e só três.

```python
@pytest.mark.parametrize("idade,esperado", [
    (17, False),    # vizinho de baixo da fronteira
    (18, True),     # a fronteira, e ela entra
    (19, True),     # vizinho de cima
])
def test_idade_minima(idade, esperado):
    assert validar_idade_minima(idade) == esperado
```

**Treino:** apague uma linha da massa e rode. O `collected` cai junto, e é assim que se confirma que cada linha é um teste independente.

## `test_aula09_tabela_decisao.py`

A tabela de decisão de duas condições, com `ids`. Quatro combinações, quatro linhas, quatro testes.

```python
@pytest.mark.parametrize("cliente_vip,valor_compra,esperado", [
    (True, 300.00, 20),
    (True, 150.00, 10),
], ids=[
    "vip_acima_de_200",
    "vip_abaixo_de_200",
])
```

**Treino:** acrescente uma quinta linha na massa e **não** acrescente o quinto `ids`. Rode e leia a mensagem: ela aparece na coleta, e nada roda.

## `test_aula09_senha_e_frete.py`

Dois `parametrize` no mesmo arquivo, e cada um governa só a função abaixo dele.

```python
@pytest.mark.parametrize("senha,esperado", [
    ("Abc1234", False),
    ("Abc12345", True),
], ids=[
    "sete_caracteres_recusa",
    "oito_caracteres_aceita",
])
def test_politica_de_senha(senha, esperado):
    assert senha_valida(senha) == esperado
```

**Treino:** a regra da senha tem três condições. Confira se a massa tem um negativo para cada uma, e repare que `"abc"` sozinha não serviria: ela é curta, sem número e sem maiúscula ao mesmo tempo, então prova só a primeira.

## `test_aula09_frete_quebrado.py`

A mesma massa do frete, apontada para o arquivo estragado. Sai com exit code 1 de propósito.

```python
from aula09_regras_frete_quebrado import tem_frete_gratis
```

**Treino:** rode e leia o nome entre colchetes na linha vermelha. Depois apague a lista de `ids` inteira, rode de novo, e compare o que o relatório passa a dizer.

## `test_aula09_nome_errado.py` e `test_aula09_massa_desalinhada.py`

As duas armadilhas, e as duas erram na coleta.

```python
@pytest.mark.parameterize("idade,esperado", [   # sem "e" no meio: parametrize
```

**Treino:** corrija o nome do decorador no primeiro arquivo e rode. Depois desfaça. Ver a mensagem uma vez economiza dez minutos na próxima vez que ela aparecer.

## `test_aula09_do_csv.py` e `aula09_massa_frete.csv`

O desafio extra: a massa sai de um arquivo, e passa a ser editável por quem não escreve Python.

```python
massa.append((float(linha["total"]), linha["esperado"] == "True"))
```

**Treino:** apague a conversão `== "True"` e deixe só `linha["esperado"]`. Rode e veja o que acontece: toda string não vazia é verdadeira, então `"False"` passa a valer verdadeiro e uma linha da massa muda de significado sem nenhum erro aparecer.

## `test_exemplo_playwright.py`

O teste que prova que o Playwright ficou instalado. Não é aula de Playwright.

```python
def test_abre_pagina_de_treino(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()
```

**Treino:** nenhum. Rode, veja o `1 passed`, e pare por aí. De onde vem a `page`, o que é `get_by_role` e por que `expect` em vez de `assert` são a Aula 12.

## A atividade

A entrega não é código: é massa de teste, em `entregas/massa_aula09.csv`. A regra é a `classificar_nota`, e o modelo de formato é o `aula09_massa_notas.csv` desta pasta.

```bash
pytest tests/test_massa_aula09.py -v
```
