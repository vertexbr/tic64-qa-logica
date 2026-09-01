# Guia de estudo · Aula 08

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso): este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a regra de negócio e a saída esperada.

**A tese da aula:** o `assert` não mudou. Ele é o mesmo da Aula 04, com a mesma sintaxe. O que mudou foi a casa dele: ele saiu do fim de um script solto e entrou numa função com nome, dentro de um arquivo com nome, e agora uma ferramenta encontra ele, roda ele e escreve um relatório do que passou e do que reprovou. Verificar deixou de ser uma linha no fim do arquivo e virou coisa que se guarda e se roda de novo.

**A regra do comando, e ela vale para os oito arquivos de teste desta pasta:** rode um por vez, **sempre nomeando o arquivo**. `pytest -s -v` sozinho aqui dentro coleta os oito de uma vez, dá 22 testes com 7 falhas, e o relatório vira um muro. Seis dos oito falham de propósito.

```bash
cd aulas/aula08
pytest test_aula08_regras.py -s -v
```

**A heurística para investigar:** `AssertionError` significa que a comparação chegou ao fim e obtido e esperado diferem. Volte à regra escrita e compare produto, entrada e expectativa. `TypeError`, `IndexError`, `KeyError`, `NameError` e `AttributeError` mostram que a execução quebrou antes da validação. Confira primeiro a entrada do teste e o contrato da função.

Os arquivos `.py` desta pasta terminam com um bloco de explicação linha a linha, marcado como gerado. A contagem de linhas abaixo inclui esse bloco, e ele não se edita à mão.

## `aula08_regras.py`

O produto: as duas regras que a loja precisa que funcionem. Não é teste, e o nome não começa com `test_` de propósito.

```python
def validar_idade_minima(idade):
    return idade >= 18


def tem_permissao(perfil):
    return perfil in ["admin", "gerente"]
```

Arquivo completo: `aulas/aula08/aula08_regras.py` (58 linhas). Para treinar, troque o `>=` por `>` e rode o `test_aula08_regras.py`. Os quatro continuam verdes, e essa é a lição: nenhum dos quatro usa 18 exato, então o de 20 passa dos dois jeitos e o de 16 reprova dos dois jeitos. Escreva o quinto teste que pega a troca, `assert validar_idade_minima(18) == True`, rode de novo, e desfaça o `>` depois. Suíte verde não quer dizer código certo; quer dizer que os casos escritos passaram.

## `test_aula08_regras.py`

O primeiro arquivo de teste do curso. Quatro testes, quatro verdes.

```python
from aula08_regras import validar_idade_minima, tem_permissao


def test_maior_de_idade_e_valido():
    # Preparação
    idade = 20
    # Ação
    resultado = validar_idade_minima(idade)
    # Validação
    assert resultado == True


def test_menor_de_idade_e_invalido():
    assert validar_idade_minima(16) == False
# ...
```

Arquivo completo: `aulas/aula08/test_aula08_regras.py` (103 linhas). Para treinar, tire o `test_` do nome de uma das funções e rode: o pytest não reclama, não dá erro, e diz que coletou um teste a menos. Silêncio, e não vermelho, é o que você ganha quando erra a convenção de nome. Depois acrescente um quinto teste para o perfil `"gerente"`, que a regra cita e nenhum dos quatro cobre.

## `test_aula08_escada.py`

Quatro degraus de asserção num teste só, e nenhum deles é conteúdo novo.

```python
from aula08_regras import validar_idade_minima


def test_escada_de_assercoes():
    # 1. igualdade, o degrau que resolve quase tudo
    assert validar_idade_minima(20) == True

    # 2. tipo, quando o formato do dado importa tanto quanto o valor
    assert isinstance(validar_idade_minima(20), bool)

    # 3. presença, o in da Aula 05
    assert "admin" in ["admin", "gerente"]

    # 4. ausência, o not in da mesma aula
    assert "visitante" not in ["admin", "gerente"]
```

Arquivo completo: `aulas/aula08/test_aula08_escada.py` (74 linhas). Para treinar, troque o segundo degrau por `assert isinstance(validar_idade_minima(16), bool)` e rode: continua verde, porque `False` também é `bool`. O degrau de tipo confere o formato e não o valor, e confundir os dois é o engano mais comum com `isinstance`.

## `test_aula08_atomico.py`

O teste que faz três coisas, e por que ele não serve. Ele reprova de propósito.

```python
from aula08_regras import validar_idade_minima, tem_permissao


def test_tres_validacoes_no_mesmo_teste():
    assert validar_idade_minima(20) == True
    assert tem_permissao("visitante") == True
    assert tem_permissao("admin") == False
```

Arquivo completo: `aulas/aula08/test_aula08_atomico.py` (58 linhas). Para treinar, conserte só o segundo `assert`, trocando o `True` por `False`, e rode de novo. O teste continua vermelho, agora no terceiro, e a sensação é de ter criado defeito novo. Você não criou: o terceiro já estava errado e o relatório nunca chegou nele. Depois quebre a função em três, uma por comportamento, e rode: agora o relatório diz **quais** falharam, em vez de dizer que um nome falhou.

## `aula08_regras_quebradas.py`

O `aula08_regras.py` com um número trocado. O 18 virou 21, e nada mais mudou.

```python
def validar_idade_minima(idade):
    return idade >= 21


def tem_permissao(perfil):
    return perfil in ["admin", "gerente"]
```

Arquivo completo: `aulas/aula08/aula08_regras_quebradas.py` (27 linhas). Para treinar, abra os dois arquivos lado a lado e procure a diferença sem usar busca. Ela é um caractere, e essa é a lição: revisão por leitura não pega isso de forma confiável, e teste pega sempre.

## `test_aula08_regressao.py`

Os quatro testes do `test_aula08_regras.py`, apontados para o módulo estragado. A única diferença é a linha do `import`.

```python
from aula08_regras_quebradas import validar_idade_minima, tem_permissao


def test_maior_de_idade_e_valido():
    # Preparação
    idade = 20
    # Ação
    resultado = validar_idade_minima(idade)
    # Validação
    assert resultado == True
# ...
```

Arquivo completo: `aulas/aula08/test_aula08_regressao.py` (43 linhas). Para treinar, antes de rodar escreva num papel quantos dos quatro ficam vermelhos. A resposta não é quatro, e entender por que é metade do valor do exercício. Depois acrescente `assert validar_idade_minima(18) == True`, que cobra a fronteira da regra escrita, e rode: agora são dois vermelhos, e o segundo é o que pega a troca de forma direta.

## `aula08_desconto.py`

A regra de desconto da Aula 03, agora como função com `return`, testável de fora.

```python
def calcular_desconto(valor_compra, cliente_vip=False, tem_cupom=False):
    if cliente_vip and valor_compra > 200:
        return 20
# ...
```

Arquivo completo: `aulas/aula08/aula08_desconto.py` (24 linhas). Para treinar, chame a função com 200 exato e cliente VIP, e confira contra a regra escrita: ela diz **acima** de 200, então 200 cai no degrau de baixo. A função da atividade não é esta: ela tem quatro parâmetros e um deles é o produto em promoção, e a escada dela é você que escreve.

## `test_aula08_desconto.py`

O mesmo teste escrito de dois jeitos. Os dois reprovam pelo mesmo motivo, e só um explica por quê.

```python
from aula08_desconto import calcular_desconto


def test_desconto_de_cliente_vip():
    valor_compra = 300.00
    desconto_esperado = 25
    desconto_obtido = calcular_desconto(valor_compra, cliente_vip=True)
    assert desconto_obtido == desconto_esperado


def test_desconto_de_cliente_vip_sem_variaveis():
    assert calcular_desconto(300.00, True) == 25
```

Arquivo completo: `aulas/aula08/test_aula08_desconto.py` (75 linhas). Para treinar, rode com `-l` e leia as duas metades do relatório lado a lado. Depois corrija os dois esperados de 25 para 20 e rode de novo: os dois ficam verdes, e o relatório para de contar qualquer coisa. Variável nomeada só paga quando o teste reprova, e é justamente aí que você não está olhando para a tela.

## `aula08_loja.py`

As três funções da loja, com um defeito plantado no meio delas.

```python
def calcular_total(valor, quantidade, desconto=0.0):
    return valor * quantidade - desconto


def tem_frete_gratis(total):
    return total > 250.00


def aplicar_desconto(subtotal, percentual):
    return subtotal - (subtotal * percentual / 100)
```

Arquivo completo: `aulas/aula08/aula08_loja.py` (65 linhas). Para treinar, leia a regra escrita no cabeçalho antes de olhar o código, e responda o que `tem_frete_gratis(250.00)` deveria devolver. Depois rode a função e compare. A regra diz "a partir de 250,00" e o código diz `>`, e um caractere separa os dois.

## `test_aula08_loja.py`

A suíte da loja, seis testes escritos a partir da regra. Cinco passam, e o que falha achou defeito de verdade.

```python
import pytest

from aula08_loja import calcular_total, tem_frete_gratis, aplicar_desconto


def test_total_sem_desconto():
    assert calcular_total(100, 3) == 300


def test_total_com_desconto():
    assert calcular_total(100, 3, 50) == 250


def test_frete_gratis_acima_de_250():
    assert tem_frete_gratis(300) == True
# ...
```

Arquivo completo: `aulas/aula08/test_aula08_loja.py` (119 linhas). Para treinar, apague o `test_frete_gratis_no_limite` e rode: seis viram cinco, tudo fica verde, e o defeito continua lá. Depois devolva o teste, conserte o produto trocando `>` por `>=`, e rode de novo. Repare no que aconteceu: a suíte não consertou nada, ela avisou. E responda a pergunta que abre a Aula 09: por que o teste que encontrou o defeito foi justamente o de 250, e não o de 300 nem o de 100?

Troque também o `pytest.approx(89.91)` por `89.91` cru no último teste e rode: ele reprova com `assert 89.91000000000001 == 89.91`, que é a conta da Aula 02 cobrando o troco seis aulas depois.

## `test_aula08_tipo_do_erro.py`

Uma linha só, e ela reprova pelo motivo errado. O defeito aqui é do teste.

```python
from aula08_loja import calcular_total


def test_total_com_quantidade_em_texto():
    assert calcular_total(100, "3") == 300
```

Arquivo completo: `aulas/aula08/test_aula08_tipo_do_erro.py` (29 linhas). Para treinar, leia a última linha do relatório e repare que ela fala de `-` e não de `*`: a multiplicação não reclamou, porque `100 * "3"` em Python repete o texto e devolve `"333"`. Quem estourou foi a subtração. Depois troque `"3"` por `3` e rode: verde. O tipo do erro mostra onde a execução parou. A regra escrita mostra se o ajuste pertence ao produto ou ao teste.

## `aula08_pedidos.py`

O `registrar_item` da Aula 07, sem uma linha de diferença. O que mudou foi quem verifica.

```python
def registrar_item(nome, quantidade):
    if nome.strip() == "":
        raise ValueError("nome do item é obrigatório")
    if quantidade <= 0:
        raise ValueError("quantidade precisa ser positiva")
    return f"{quantidade}x {nome.strip()}"
```

Arquivo completo: `aulas/aula08/aula08_pedidos.py` (26 linhas). Para treinar, chame a função com três espaços no nome e responda por que ela recusa: o `strip()` da Aula 05 tira os espaços das pontas antes da comparação, então campo com espaço é campo vazio. Depois apague o `.strip()` da primeira linha e rode o `test_aula08_recusa.py`: o teste da mensagem fica vermelho, porque a função passou a aceitar o que devia recusar.

## `test_aula08_recusa.py`

As nove linhas da Aula 07 viram uma, com `pytest.raises`. O terceiro teste reprova de propósito.

```python
import pytest

from aula08_pedidos import registrar_item


def test_recusa_quantidade_zero():
    with pytest.raises(ValueError):
        registrar_item("Teclado", 0)


def test_recusa_diz_o_motivo():
    with pytest.raises(ValueError) as erro:
        registrar_item("   ", 2)
    assert "nome do item" in str(erro.value)
# ...
```

Arquivo completo: `aulas/aula08/test_aula08_recusa.py` (101 linhas). Três treinos, e cada um mostra uma coisa diferente.

Primeiro, mova o `assert "nome do item" in str(erro.value)` para dentro do `with`, uma linha abaixo da chamada, e rode. Ele fica verde sem ter verificado nada, porque a linha depois da que estourou nunca executa. É um falso-verde nascendo na sua frente.

Segundo, troque o trecho conferido de `"nome do item"` para `"quantidade"` e rode. O erro vem, o tipo está certo, e mesmo assim reprova, porque veio pelo outro motivo. Recusar não basta: tem que recusar pelo motivo certo.

Terceiro, olhe o `test_quantidade_valida_nao_deveria_ser_recusada` e escreva com as suas palavras por que ele reprova. Nada quebrou, nada estourou, e é exatamente essa a falha: o erro que era esperado não aconteceu.

## `colisao-de-nome/random.py`

O arquivo que se importa sozinho. Ele quebra de propósito, e mora numa pasta só dele para não contaminar as outras.

```python
import random

sorteado = random.choice(["admin", "gerente", "visitante"])
print(f"Perfil sorteado: {sorteado}")
```

Arquivo completo: `aulas/aula08/colisao-de-nome/random.py` (34 linhas). Para treinar, leia o traceback e repare que ele aponta duas vezes para o mesmo arquivo, linhas 31 e 33: o arquivo importou a si próprio.

Depois faça o teste que mostra o tamanho do estrago. Copie essas quatro linhas para um arquivo novo chamado `sorteio.py`, na mesma pasta, e rode ele. O `sorteio.py` não tem defeito nenhum, o nome dele está certo, e mesmo assim ele quebra: o `import random` dele encontra o `random.py` do lado antes da biblioteca padrão. Repare que o traceback acusa um arquivo que você nem chamou. Um arquivo mal nomeado contamina a pasta inteira, e é por isso que este mora sozinho.

Não renomeie o `random.py`, porque renomear apaga a demonstração. Apague o `sorteio.py` quando terminar.

## A atividade pós-aula

A entrega não fica nesta pasta. Você escreve `calcular_desconto` em `entregas/regras_desconto.py`, na raiz do repositório, e confere sozinho:

```bash
pytest tests/test_desconto_aula08.py -v
```

**Prazo: 08/09/2026, às 23h59.** `6 passed` significa que a sua função obedece a regra em todos os casos que a atividade cobra. O passo a passo e a regra cobrada estão no [README.md](../../README.md) da raiz e no cabeçalho do próprio `tests/test_desconto_aula08.py`.
