# Guia de estudo · Aula 07

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso): este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a regra de negócio e a saída esperada.

**A tese da aula, e ela vale mais que qualquer arquivo daqui:** confie nas mensagens do Python. Se você ler o erro, você já tem metade do que aconteceu. Quem está começando fecha o terminal no susto e vai perguntar antes de ler; o objetivo é inverter essa ordem.

**Como ler um traceback:** `LÊ A ÚLTIMA → SOBE → ACHA O SEU ARQUIVO`. A última linha diz **o que** aconteceu, o andar de baixo diz **onde**, e os andares acima dizem **quem chamou**. Isso vale para traceback, e traceback só existe quando o programa para. Erro de lógica não tem traceback nenhum, e é justamente por isso que ele é o caro.

## `aula07_relatorio.py`

O arquivo que abre a aula, com o terminal vermelho. Ele quebra de propósito.

```python
def taxa_de_aprovacao(passou, total):
    return passou / total * 100


def resumir_execucao(resultados):
    passou = resultados["passou"]
    total = resultados["total"]
    return f"Aprovação: {taxa_de_aprovacao(passou, total):.1f}%"


def imprimir_relatorio(execucoes):
    for execucao in execucoes:
        print(resumir_execucao(execucao))


execucoes = [
    {"passou": 12, "total": 15},
    {"passou": 0, "total": 0},   # <- este estoura
]
# ...
```

Arquivo completo: `aulas/aula07/aula07_relatorio.py` (39 linhas). Para treinar, rode o arquivo e leia o traceback em voz alta, de baixo para cima, apontando com o cursor: tipo, linha, função, quem chamou. Depois troque o `"total": 0` por `"total": 20` e rode de novo: o traceback desaparece e as duas linhas saem impressas.

## `aula07_erros_de_sintaxe.py`

Os três erros de sintaxe que toda turma comete, comentados com a mensagem exata de cada um e a versão certa rodando embaixo.

```python
# O ERRADO:
#     idade = 20
#     if idade >= 18
#         print("ok")
#
# O que o Python disse:
#       File "aula07_erros_de_sintaxe.py", line 2
#         if idade >= 18
#                       ^
#     SyntaxError: expected ':'

idade = 20
if idade >= 18:
    print("ok")
# ...
```

Arquivo completo: `aulas/aula07/aula07_erros_de_sintaxe.py` (81 linhas). Para treinar, descomente **uma** das versões erradas por vez, rode, leia a mensagem, e comente de novo antes de passar para a próxima. Duas descomentadas ao mesmo tempo só mostram a primeira, porque o Python para no primeiro erro de sintaxe.

## `aula07_nome_errado.py`

O bônus que mostra por que a mensagem inteira importa: capturada de um jeito ela traz a sugestão do Python, de outro jeito ela perde.

```python
total_pedido = 100

print("=== o que str(erro) entrega ===", flush=True)
try:
    print(total_pedid)
except NameError as erro:
    print(f"NameError: {erro}", flush=True)

print()
print("=== o que o Python entrega de verdade ===", flush=True)
try:
    print(total_pedid)
except NameError:
    traceback.print_exc()
# ...
```

Arquivo completo: `aulas/aula07/aula07_nome_errado.py` (38 linhas). Para treinar, compare as duas saídas lado a lado e repare no que a primeira perdeu. Depois corrija o nome nas duas linhas e rode: as duas seções ficam vazias, e é assim que tem que ser.

## `aula07_q1_indice.py`

Primeiro dos quatro quebrados. A lista tem três itens e o código pede a posição 3.

```python
casos = ["login válido", "login inválido", "senha em branco"]

try:
    print(f"Quarto caso: {casos[3]}")
except IndexError:
    traceback.print_exc()
# ...
```

Arquivo completo: `aulas/aula07/aula07_q1_indice.py` (28 linhas). Para treinar, antes de rodar escreva num papel o tipo do erro que você espera. Depois rode e confira. E responda a pergunta que fecha o assunto: numa lista de três itens, qual é a última posição válida?

## `aula07_q2_tipo.py`

Segundo dos quatro, e o mais interessante: a mensagem nunca diz a palavra "texto".

```python
quantidade = "3"
preco = 199.90

try:
    print(f"Total: {preco * quantidade + 10}")
except TypeError:
    traceback.print_exc()
# ...
```

Arquivo completo: `aulas/aula07/aula07_q2_tipo.py` (28 linhas). Para treinar, leia a mensagem sem consertar nada e escreva uma frase sua dizendo a causa. Depois envolva a `quantidade` com `int()` e rode: o total sai 609,70.

## `aula07_q3_atributo.py`

Terceiro dos quatro. O método é `strip()`, não `trim()`, e o Python sugere o certo.

```python
email = "  GAIA@Teste.com  "

try:
    print(email.trim().lower())
except AttributeError:
    traceback.print_exc()
# ...
```

Arquivo completo: `aulas/aula07/aula07_q3_atributo.py` (24 linhas). Para treinar, repare que a resposta já está na mensagem, depois do `Did you mean`. Troque para `strip()` e rode: sai `gaia@teste.com`, sem espaço e em minúscula.

## `aula07_q4_chave.py`

Quarto dos quatro, e é a Aula 05 cobrando o `.get()`.

```python
resultados = {"passou": 12, "falhou": 3}

try:
    print(f"Ignorados: {resultados['ignorado']}")
except KeyError:
    traceback.print_exc()
# ...
```

Arquivo completo: `aulas/aula07/aula07_q4_chave.py` (25 linhas). Para treinar, troque por `resultados.get("ignorado", 0)` e rode. Depois responda para você mesmo: neste caso, quebrar ou devolver zero é o certo? A resposta depende de o campo ser obrigatório ou opcional, e nenhuma das duas é sempre melhor.

## `aula07_try_except_massa.py`

O `try/except` de tipo específico, no uso de verdade: massa de teste com linha fora do formato.

```python
entradas = ["18", "cinquenta", "42", ""]

for bruta in entradas:
    try:
        idade = int(bruta)
        print(f"'{bruta}' virou {idade}")
    except ValueError as erro:
        print(f"'{bruta}' recusada. O Python disse: {erro}")
# ...
```

Arquivo completo: `aulas/aula07/aula07_try_except_massa.py` (57 linhas). Para treinar, acrescente `"0"` e `"-5"` na lista de entradas e rode: os dois passam, porque os dois são números válidos. Se a regra fosse "idade tem que ser positiva", o `try/except` não pegaria nenhum dos dois, e aí o trabalho é de um `if`, não de um `except`. Saber qual dos dois usar é metade da aula.

## `aula07_except_pelado.py`

O antipadrão proibido no curso, rodando, com as três versões lado a lado.

```python
def somar_pelado(linhas):
    total = 0
    for linha in linhas:
        try:
            total = total + float(linha)
        except:
            pass
    return total


def somar_com_tipo(linhas):
    total = 0
    for linha in linhas:
        try:
            total = total + float(linha)
        except ValueError as erro:
            print(f"    descartei '{linha}': {erro}")
    return total
# ...
```

Arquivo completo: `aulas/aula07/aula07_except_pelado.py` (69 linhas). Para treinar, troque um valor da massa por algo que dê **outro** tipo de erro, como `None`, e rode as duas funções. A pelada engole igual e continua devolvendo um número; a de tipo deixa o `TypeError` estourar, porque ela só se comprometeu com `ValueError`. Esse é o ponto inteiro: o `except` com tipo captura o que você previu e deixa passar o que você não previu, que é exatamente o que você quer saber.

## `aula07_pedidos.py`

A função que levanta o erro de propósito. Só de funções: não imprime nada quando rodado direto.

```python
def registrar_item(nome, quantidade):
    if nome.strip() == "":
        raise ValueError("nome do item é obrigatório")
    if quantidade <= 0:
        raise ValueError("quantidade precisa ser positiva")
    return f"{quantidade}x {nome.strip()}"


def calcular_frete(total):
    if total >= 250.00:
        return 0.0
    return 20.0
```

Arquivo completo: `aulas/aula07/aula07_pedidos.py` (37 linhas). Para treinar, apague a mensagem de um dos dois `raise`, deixando só `raise ValueError`, e rode o `aula07_usa_pedidos.py`. Funciona, e é pior: quem receber o erro não sabe qual regra violou. A mensagem é metade do valor do `raise`.

## `aula07_usa_pedidos.py`

Tempo 1 da prova de recusa: deixe estourar. Ele quebra de propósito.

```python
from aula07_pedidos import registrar_item

print(registrar_item("Teclado", 2))
print(registrar_item("Teclado", 0))
```

Arquivo completo: `aulas/aula07/aula07_usa_pedidos.py` (21 linhas). Para treinar, repare que este traceback atravessa **dois** arquivos, e responda: qual dos dois andares você consertaria? Depois inverta a ordem das duas linhas de `print` e rode: a linha válida deixa de aparecer, porque o programa morre antes de chegar nela.

## `aula07_verifica_pedidos.py`

Tempo 2, e o ponto em que o conceito da aula fecha. Aqui o erro acontecendo é aprovação, e o erro não acontecendo é reprovação.

```python
# Caso 2: quantidade zero DEVE ser recusada.
levantou = False
mensagem = ""
try:
    registrar_item("Teclado", 0)
except ValueError as erro:
    levantou = True
    mensagem = str(erro)

assert levantou, "a funcao NAO levantou ValueError: ela aceitou quantidade zero"
assert "quantidade" in mensagem, f"recusou por outro motivo: {mensagem}"
print(f"OK - recusou com a mensagem: {mensagem}")
# ...
```

Arquivo completo: `aulas/aula07/aula07_verifica_pedidos.py` (84 linhas). Três treinos, e vale fazer os três porque cada um mostra uma falha diferente.

Primeiro, troque `registrar_item("Teclado", 0)` por `registrar_item("Teclado", 2)`, que é um dado **válido**. O `except` nunca roda, `levantou` continua `False`, e o primeiro `assert` reprova dizendo que a função não levantou erro. É a falha ao contrário, provocada por você.

Segundo, troque o trecho conferido de `"quantidade"` para `"nome do item"`. O erro vem, o tipo está certo, mas veio por outro motivo, e o segundo `assert` pega. Repare que a mensagem imprime o que foi **obtido**, porque a f-string coloca a variável ali dentro.

Terceiro, tire o `levantou = False` de antes do `try` e rode. Dá `NameError`, porque a variável só passaria a existir dentro do `except`. Cria antes, muda dentro: é o mesmo processo do contador da Aula 04.

## `aula07_relatorio_bugado.py`

Três defeitos plantados, e nenhum deles quebra o programa. Ele roda, não avisa, e os três números estão errados.

```python
def calcular_media_aprovacao(resultados):
    aprovados = 0
    for r in resultados:
        if r == "passou":
            aprovados + 1
    return aprovados / len(resultados) * 100


def precisa_de_aprovacao_gerencial(valor_desconto):
    # Regra escrita: precisa de aprovação quando o desconto PASSA de 50%.
    if valor_desconto >= 50:
        return True
    return False
# ...
```

Arquivo completo: `aulas/aula07/aula07_relatorio_bugado.py` (51 linhas). Para treinar, **não abra o arquivo corrigido**. Faça assim: calcule os três números de cabeça a partir das regras escritas, rode, e compare. Onde o número diferir, coloque um `print` dentro do laço ou do `if` e rode de novo. O `print` é a evidência, e é ele que transforma "acho que é aqui" em "é aqui".

Dica sobre o primeiro defeito, que é o principal: o Python aceita `aprovados + 1` sem reclamar nada, porque isso é uma expressão perfeitamente legal. Ele calcula o valor e joga fora, porque ninguém guardou.

## `aula07_relatorio_corrigido.py`

Os três defeitos corrigidos, com o comentário de cada um colado na linha dele.

```python
def normalizar(linhas):
    """Troca vírgula decimal por ponto, que é o que o float() do Python lê."""
    limpas = []
    for linha in linhas:
        limpas.append(linha.replace(",", "."))
    return limpas


notas = ["passou", "passou", "falhou"]

# Esperado vem da regra: duas de três aprovadas são 66,7%.
assert round(calcular_media_aprovacao(notas), 1) == 66.7
# ...
```

Arquivo completo: `aulas/aula07/aula07_relatorio_corrigido.py` (91 linhas). Para treinar, desfaça **uma** correção por vez e rode: o `assert` daquela regra reprova e diz qual é. Isso é o valor inteiro de escrever o esperado por extenso: o defeito que levou dez minutos para ser achado passa a ser achado em um segundo, para sempre.

Repare no que a correção do `except` faz e no que ela não faz: ela não conserta a soma, ela mostra o que consertar. O conserto era do dado.

## `aula07_defeitos_pos_aula.py`

A atividade pós-aula. **Prazo: 08/09/2026, às 23h59.**

Cinco defeitos: **dois de execução** e **três de lógica**. As quatro regras de negócio estão escritas por extenso no cabeçalho do arquivo, e é de lá que sai o resultado esperado de cada número.

```python
CASOS = [
    {"nome": "login valido", "status": "passou", "duracao": "1.20"},
    {"nome": "login invalido", "status": "passou", "duracao": "0,95"},
    {"nome": "senha em branco", "status": "falhou", "duracao": "2.10"},
    {"nome": "senha curta", "status": "passou", "duracao": "2.00"},
    {"nome": "logout", "status": "passou", "duracao": "0.80"},
]


def contar_aprovados(casos):
    aprovados = 0
    for caso in casos:
        if caso["status"] == "passou":
            aprovados + 1
    return aprovados
# ...
```

Arquivo completo: `aulas/aula07/aula07_defeitos_pos_aula.py` (80 linhas).

Como fazer, e a ordem importa mais que a velocidade:

1. **Leia as quatro regras do cabeçalho e calcule os quatro números no papel.** Taxa de sucesso, tempo total, casos lentos, e o que o detalhe de cada caso deve imprimir. Se você pular esta etapa, os três de lógica ficam invisíveis.
2. **Rode.** Os dois de execução aparecem, um por vez, e o Python diz o arquivo e a linha de cada um.
3. **Conserte os dois e rode de novo.** Agora o programa vai até o fim e imprime quatro números.
4. **Compare os quatro números com os do papel.** Onde diferir, tem defeito de lógica. Use `print` para conseguir evidência antes de mexer em qualquer linha.

Para cada um dos cinco, registre **sintoma** (o que você viu), **causa** (a linha e o motivo) e **correção** (o que você escreveu no lugar). Entregue o arquivo corrigido e o registro dos cinco, mesmo que você não tenha achado todos: vale mais registrar quatro bem que listar cinco no chute.
