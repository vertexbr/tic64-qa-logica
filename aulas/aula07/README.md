# Aula 07 - Encontrando defeitos no próprio código

Demonstrações de código da Aula 07, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

Esta é a única pasta do repositório em que **três arquivos saem com exit code diferente de zero, de propósito**. Nas outras aulas a regra é que todo arquivo roda do início ao fim, e erro proposital vai dentro de `try/except`. Aqui a regra abre exceção em três casos, porque neles a parada é o conteúdo da aula e não há saída nenhuma depois dela para alguém perder:

| Arquivo | Exit code | Por quê |
|---|--:|---|
| `aula07_relatorio.py` | 1 | o traceback é a última coisa da tela, e é a aula inteira |
| `aula07_usa_pedidos.py` | 1 | o ponto é que o programa **parou**; embrulhar em `try/except` apagaria isso |
| `aula07_defeitos_pos_aula.py` | 1 | é a atividade, e ela chega quebrada na sua mão de propósito |

Os outros doze saem 0. Para rodar a bateria inteira, do PowerShell, na raiz do repositório:

```powershell
Get-ChildItem aulas\aula07\*.py | ForEach-Object { python -X utf8 $_.FullName }
```

## Arquivos

- `aula07_relatorio.py`
- `aula07_erros_de_sintaxe.py`
- `aula07_nome_errado.py`
- `aula07_q1_indice.py`
- `aula07_q2_tipo.py`
- `aula07_q3_atributo.py`
- `aula07_q4_chave.py`
- `aula07_try_except_massa.py`
- `aula07_except_pelado.py`
- `aula07_pedidos.py`
- `aula07_usa_pedidos.py`
- `aula07_verifica_pedidos.py`
- `aula07_relatorio_bugado.py`
- `aula07_relatorio_corrigido.py`
- `aula07_defeitos_pos_aula.py`

## Os três tipos de erro, que é o mapa da aula

A pasta está organizada nesta ordem, e vale ler ela nela:

**Sintaxe** não deixa o arquivo nem começar. O Python recusa antes de rodar a primeira linha, e quem avisa é ele, na hora. É o `aula07_erros_de_sintaxe.py`.

**Execução** para no meio. O Python avisa quando chega ali, com o traceback. São o `aula07_relatorio.py`, os quatro quebrados e o `aula07_usa_pedidos.py`.

**Lógica** nunca aparece. O programa roda até o fim, imprime número errado, e ninguém avisa: só o teste. É o `aula07_relatorio_bugado.py`, e é para pegar esse que a automação de teste existe.

Os dois primeiros o Python entrega de graça, e por isso são os baratos. O terceiro chega em produção, três semanas depois, pela boca do cliente.

## `aula07_relatorio.py`

O arquivo que abre a aula, com o terminal vermelho. As três funções vêm de `aulas/aula06/aula06_duas_funcoes.py`, com a mesma embalagem de função-pergunta que recebe, calcula e devolve; o acréscimo desta aula é a massa, cujo segundo item tem total zero.

**Regra de negócio:** a taxa de aprovação é a quantidade de casos que passaram dividida pelo total de casos, em porcentagem. A regra escrita não diz o que fazer quando o total é zero, e é exatamente aí que o programa quebra.

Leia o traceback de baixo para cima: a última linha diz **o que**, o andar de baixo diz **onde**, e os andares acima dizem **quem chamou**. O til embaixo da expressão marca os operandos e o circunflexo marca a operação, então o Python literalmente aponta o dedo na barra da divisão.

Repare também no `exit code 1` da última linha da janela Run. Zero é acabou bem, qualquer outro número é acabou mal, e é esse número que uma esteira de testes lê para decidir se o build passa.

```bash
python aulas/aula07/aula07_relatorio.py
```

Saída, com o caminho encurtado:

```
Aprovação: 80.0%
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_relatorio.py", line 39, in <module>
    imprimir_relatorio(execucoes)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
  File "...\aulas\aula07\aula07_relatorio.py", line 31, in imprimir_relatorio
    print(resumir_execucao(execucao))
          ~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "...\aulas\aula07\aula07_relatorio.py", line 26, in resumir_execucao
    return f"Aprovação: {taxa_de_aprovacao(passou, total):.1f}%"
                         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "...\aulas\aula07\aula07_relatorio.py", line 20, in taxa_de_aprovacao
    return passou / total * 100
           ~~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

## `aula07_erros_de_sintaxe.py`

Os três erros de sintaxe que toda turma comete: dois-pontos esquecido, aspas não fechadas, e tabulação misturada com espaço. Os três moram comentados no arquivo, com a mensagem exata que o Python devolveu ao lado de cada um, e a versão correta rodando embaixo.

Eles têm que ficar comentados: erro de sintaxe não deixa o arquivo nem abrir, então um deles solto derrubaria os outros dois. Para treinar, descomente uma linha por vez, rode, leia a mensagem, e comente de novo.

O terceiro é o mais confuso dos três, porque na tela o código parece perfeitamente alinhado: a linha do `return` foi recuada com tabulação e as outras com espaço. O olho não vê a diferença e o Python vê. A solução que resolve para sempre é configurar o editor para converter tabulação em quatro espaços.

```bash
python aulas/aula07/aula07_erros_de_sintaxe.py
```

Saída:

```
=== 1. dois-pontos esquecido ===
ok

=== 2. aspas não fechadas ===
Gaia

=== 3. tabulação misturada com espaço ===
calcular(2, 3) = 5
```

## `aula07_nome_errado.py`

O bônus de trinta segundos que economiza minutos: as versões recentes do Python sugerem a correção quando você erra um nome de variável.

O arquivo existe para mostrar uma diferença que decide qual função usar quando você captura um erro. `traceback.print_exc()` imprime a mensagem inteira, com o `Did you mean` incluído, igual ao que o Python mostra quando ninguém captura. Já `str(erro)` e `traceback.format_exception_only()` **perdem a sugestão**, e a sugestão é justamente o que resolve o problema.

Moral prática, e ela vale para o resto do curso: quando pedir ajuda, cole a última linha inteira do traceback, e não um resumo dela.

```bash
python aulas/aula07/aula07_nome_errado.py
```

Saída:

```
=== o que str(erro) entrega ===
NameError: name 'total_pedid' is not defined

=== o que o Python entrega de verdade ===
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_nome_errado.py", line 33, in <module>
    print(total_pedid)
          ^^^^^^^^^^^
NameError: name 'total_pedid' is not defined. Did you mean: 'total_pedido'?

Ele perguntou se você quis dizer total_pedido. E quis.
```

## Os quatro quebrados: `q1` a `q4`

Os quatro seguem a mesma forma e servem ao mesmo exercício. Rode um por vez e, para cada um, escreva três coisas: o tipo do erro, que é a última linha; a linha onde estourou; e uma frase sua dizendo a causa. **Não conserte nenhum.** O exercício é ler.

Nos quatro o erro vai dentro de `try/except` com `traceback.print_exc()`, para o arquivo seguir até o fim e mostrar a explicação depois do traceback real. Isso é recurso de demonstração e **não é padrão para copiar**: numa verificação de verdade a falha interrompe. É também por isso que os quatro saem com exit code 0, mesmo mostrando traceback na tela.

Dois dos quatro trazem a resposta escrita na própria mensagem, e é o achado mais barato da aula: o de atributo diz `Did you mean: 'strip'?`, e o de índice diz `list index out of range`, que já nomeia o problema. Quem lê a linha inteira resolve os dois sem sair do terminal.

| Arquivo | Tipo e mensagem | Linha |
|---|---|--:|
| `aula07_q1_indice.py` | `IndexError: list index out of range` | 23 |
| `aula07_q2_tipo.py` | `TypeError: can't multiply sequence by non-int of type 'float'` | 22 |
| `aula07_q3_atributo.py` | `AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?` | 19 |
| `aula07_q4_chave.py` | `KeyError: 'ignorado'` | 20 |

### `aula07_q1_indice.py`

**Regra de negócio:** a suíte tem três casos de teste cadastrados, e o relatório imprime um deles pela posição na lista.

A lista tem três itens, nas posições 0, 1 e 2, e o código pede a posição 3.

```bash
python aulas/aula07/aula07_q1_indice.py
```

Saída:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q1_indice.py", line 23, in <module>
    print(f"Quarto caso: {casos[3]}")
                          ~~~~~^^^
IndexError: list index out of range

A lista tem três itens, nas posições 0, 1 e 2.
```

### `aula07_q2_tipo.py`

**Regra de negócio:** o total do pedido é o preço do produto vezes a quantidade, mais dez reais de frete. A quantidade chega do formulário como texto.

É o mais interessante dos quatro: a mensagem fala de `sequence` e de `non-int` e nunca diz a palavra texto. Mesmo assim, a linha apontada tem uma multiplicação e duas variáveis, e olhar o tipo de cada uma resolve. Mensagem confusa não é motivo para desistir da mensagem.

```bash
python aulas/aula07/aula07_q2_tipo.py
```

Saída:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q2_tipo.py", line 22, in <module>
    print(f"Total: {preco * quantidade + 10}")
                    ~~~~~~^~~~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'float'

O tipo de quantidade é <class 'str'>, e não número.
Com int(quantidade), sai: 609.7
```

### `aula07_q3_atributo.py`

**Regra de negócio:** e-mail cadastrado é comparado sem espaço nas pontas e todo em minúscula, porque quem digita não é consistente e o sistema precisa ser.

O e-mail sujo com espaço nas pontas é o mesmo de `aulas/aula05/aula05_email_sujo.py`; o acréscimo é o método errado. Quem vem de outra linguagem escreve `trim()`, e em Python o nome é `strip()`.

```bash
python aulas/aula07/aula07_q3_atributo.py
```

Saída:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q3_atributo.py", line 19, in <module>
    print(email.trim().lower())
          ^^^^^^^^^^
AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?

Com strip(), sai: gaia@teste.com
```

### `aula07_q4_chave.py`

**Regra de negócio:** o relatório de execução mostra quantos casos passaram, quantos falharam e quantos foram ignorados. Ignorado é campo opcional: pode não vir.

É a Aula 05 cobrando o `.get()`: com `resultados.get("ignorado", 0)` o programa devolveria zero em vez de quebrar. A escolha entre quebrar e devolver zero é sua, e depende de o campo ser obrigatório ou opcional.

```bash
python aulas/aula07/aula07_q4_chave.py
```

Saída:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q4_chave.py", line 20, in <module>
    print(f"Ignorados: {resultados['ignorado']}")
                        ~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'ignorado'

Com .get('ignorado', 0), sai: 0
```

## `aula07_try_except_massa.py`

O `try/except` de tipo específico, no uso de verdade.

**Regra de negócio:** a idade vem do arquivo de massa como texto e precisa virar número. Linha fora do formato é recusada e registrada, e não derruba a execução das outras.

Três partes. A primeira mostra a forma com uma entrada só. A segunda roda a massa inteira, quatro entradas fixas e desenhadas à mão, duas boas e duas ruins, com a última sendo a string vazia, que é o caso que ninguém lembra de testar; o `as erro` guarda o erro numa variável, e a mensagem original do Python vira parte do relatório em vez de derrubar a execução.

A terceira parte mostra que vários `except` embaixo do mesmo `try` são uma escada, e a escada da Aula 03 vale igual: **desce, testa o tipo, e para no primeiro que casa.** Se o erro for de valor, o `except` de chave nem é olhado. É o mesmo mecanismo em roupa nova, e não conteúdo novo.

```bash
python aulas/aula07/aula07_try_except_massa.py
```

Saída:

```
=== uma entrada só, para ver a forma ===
Valor inválido para idade: 'cinquenta'

=== a massa inteira, que é o uso de verdade ===
'18' virou 18
'cinquenta' recusada. O Python disse: invalid literal for int() with base 10: 'cinquenta'
'42' virou 42
'' recusada. O Python disse: invalid literal for int() with base 10: ''

Quatro linhas de massa, duas boas, duas ruins, nenhuma parada.

=== a escada de except ===
passou: 12
a chave não existe: 'ignorado'
```

## `aula07_except_pelado.py`

O antipadrão proibido no curso, rodando, com as três versões lado a lado.

**Regra de negócio:** a soma dos valores da massa tem que incluir todos os valores. Valor fora do formato é recusado com o motivo na tela, nunca descartado em silêncio.

`except` sem tipo captura qualquer erro que apareça ali dentro e manda tudo para o `pass`, que é nada. A consequência que interessa a um QA: uma verificação assim passa mesmo quando o produto está quebrado. Ela não valida, ela silencia, e isso tem nome: **falso-verde**. É o pior resultado possível numa esteira de testes, pior que vermelho, porque vermelho você investiga e verde você confia.

A sequência das três versões é o raciocínio inteiro. Com `except:` pelado a soma sai 40,00 e nenhum aviso. Com `except ValueError as erro` a soma continua 40,00, e agora o motivo aparece na tela: **o `except` com tipo não consertou nada, ele mostrou o que consertar.** A terceira versão troca a vírgula por ponto na massa e a soma fecha em 60,00, que é o esperado que veio da regra. O conserto era do dado, e sem a mensagem ninguém sabia disso.

A regra do curso, dita como regra: capture o erro específico que você espera. Se você não sabe qual erro esperar, você ainda não entendeu o que está testando, e o `except` genérico está escondendo essa lacuna de você.

```bash
python aulas/aula07/aula07_except_pelado.py
```

Saída:

```
=== com except pelado ===
Soma: 40.0
Nenhum aviso. E o número está errado.

=== com except de tipo, e a mensagem na tela ===
    descartei '20,00': could not convert string to float: '20,00'
Soma: 40.0
O numero continua 40. O que mudou e que agora eu SEI por que.

=== e agora com a massa consertada ===
Massa: ['10.00', '20.00', '30.00']
Soma: 60.0
60,00, que e o esperado que veio da regra.

A regra do curso: capture o erro específico que você espera.
Se você não sabe qual erro esperar, você ainda não entendeu o que
está testando, e o except genérico está escondendo essa lacuna de você.
```

## `aula07_pedidos.py`

A função que levanta o erro de propósito.

**Regra de negócio:** item só é registrado com nome preenchido e quantidade positiva; cada recusa diz qual das duas regras foi violada. O frete é grátis a partir de 250,00.

Vocabulário novo, e é o giro conceitual da aula: em programação se diz que a função **levanta** um erro. A palavra em inglês é `raise`, que é levantar, e ela não sofre o erro, ela o levanta com a mão dela para avisar quem chamou que aquilo não vai dar.

E o reenquadramento que vem com isso: **nem todo erro é problema.** Quando a regra de negócio manda rejeitar, o erro é o comportamento esperado, e quem verifica precisa provar que ele aconteceu. Se o sistema aceitar quantidade negativa em silêncio, aí sim você tem um defeito. O sistema recusar é o acerto.

Repare que a mensagem é sua, escrita em português, dizendo qual regra foi violada. Quem receber esse erro sabe o que fazer. E o `nome.strip() == ""` é a Aula 05 pagando dividendo: campo com três espaços é campo vazio para o usuário e campo preenchido para o código.

O `calcular_frete` vem de `aulas/aula06/aula06_frete_funcao.py`, com o mesmo corte de 250,00. O acréscimo desta aula é o contraste: ele não valida nada e nunca levanta erro, e é essa característica que o `aula07_verifica_pedidos.py` usa para produzir a falha ao contrário.

Na Aula 08 este arquivo volta como `aulas/aula08/aula08_pedidos.py`, copiado sem alteração nenhuma. O que muda lá não é o produto, é quem verifica.

Este arquivo é só de funções e não imprime nada quando rodado direto, de propósito.

```bash
python aulas/aula07/aula07_pedidos.py
```

Saída: nenhuma, e exit code 0.

## `aula07_usa_pedidos.py`

Tempo 1 da prova de recusa: deixe estourar.

**Regra de negócio:** a mesma do `aula07_pedidos.py`. Aqui ela é chamada com quantidade zero de propósito.

O programa está certo: ele recusou o que devia recusar. O problema é que ele **parou**, e um programa que morre no meio não diz se o comportamento foi o esperado, e nem deixa o resto rodar.

Repare numa coisa que este traceback tem e o do `aula07_relatorio.py` não tinha: **ele atravessa dois arquivos.** O andar de baixo é onde o `raise` está, e o de cima é a linha que chamou. Aqui os dois são seus. Num projeto de verdade o de baixo costuma ser de uma biblioteca, e o que você conserta é o de cima.

```bash
python aulas/aula07/aula07_usa_pedidos.py
```

Saída:

```
2x Teclado
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_usa_pedidos.py", line 21, in <module>
    print(registrar_item("Teclado", 0))
          ~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "...\aulas\aula07\aula07_pedidos.py", line 30, in registrar_item
    raise ValueError("quantidade precisa ser positiva")
ValueError: quantidade precisa ser positiva
```

## `aula07_verifica_pedidos.py`

Tempo 2 da prova de recusa, e o ponto em que o conceito da aula fecha.

**Regra de negócio:** a função tem que recusar quantidade zero e nome em branco, cada um com a sua mensagem. E o cálculo de frete não recusa nada: ele sempre devolve um valor.

Nenhuma peça aqui é conteúdo novo além do `try/except`. A variável de estado é a mesma `logou` de `aulas/aula06/aula06_login_while.py`, com trabalho novo, porque lá ela dizia se o login aconteceu e aqui ela diz se o erro aconteceu. O `assert` é da Aula 04, com a mensagem depois da vírgula. E o `in` é da Aula 05, agora procurando um pedaço de texto dentro da mensagem do erro em vez de uma chave dentro do dicionário.

A frase que fixa o mecanismo, e vale ler devagar: **aqui o erro acontecendo é aprovação, e o erro não acontecendo é reprovação.** É a inversão da lógica de sempre. Se o `raise` vier, o `except` roda, `levantou` vira `True` e o `assert` passa. Se a função aceitasse quantidade zero, o `except` nunca rodaria, `levantou` continuaria `False`, e o `assert` reprovaria.

O terceiro caso confere o nome em branco, e existe para mostrar por que conferir a mensagem não é preciosismo: a função tem dois `raise ValueError`, e sem o `in` na mensagem o caso de quantidade passaria se ela recusasse pelo motivo errado.

O fim do arquivo é a falha ao contrário, apontada para uma função que nunca levanta erro. É a única falha do curso em que o problema é a **ausência** de erro. Ela vai dentro de `try/except AssertionError` com `print_exc()` para o arquivo mostrar as três verificações que passaram e a que reprovou na mesma execução. Aviso, e ele é o antipadrão da aula com outra roupa: numa verificação de verdade a falha interrompe, e engolir asserção é o oposto de verificar.

São nove linhas para provar uma recusa. Na Aula 08 elas viram uma.

```bash
python aulas/aula07/aula07_verifica_pedidos.py
```

Saída:

```
OK - item valido registrado
OK - recusou com a mensagem: quantidade precisa ser positiva
OK - recusou com a mensagem: nome do item é obrigatório

=== a falha ao contrario ===
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_verifica_pedidos.py", line 78, in <module>
    assert levantou, "a funcao NAO levantou ValueError"
           ^^^^^^^^
AssertionError: a funcao NAO levantou ValueError

Eu estava esperando um erro, ele nao veio, e isso reprovou a verificacao.
E a frase que apareceu na tela fui eu que escrevi, depois da virgula.
```

## `aula07_relatorio_bugado.py`

Três defeitos plantados, e nenhum deles quebra o programa. Ele roda, não tem traceback, não tem vermelho, não tem aviso, e os três números impressos estão errados. É o coração da aula.

**Regra de negócio, três delas:** a média de aprovação é a proporção de casos que passaram; o desconto precisa de aprovação gerencial quando **passa** de 50%; e a soma dos valores inclui todos os valores da massa.

O trabalho é achar os três e, para cada um, escrever **hipótese** (o que você acha antes de testar), **evidência** (o que você fez para confirmar) e **causa raiz** (a linha e o motivo). Comece pelo primeiro número impresso e pergunte se ele faz sentido: duas notas de "passou" em três deveriam dar 66,7%.

Repare no exit code da execução, porque ele é o falso-verde subindo um nível: os três números estão errados e o programa diz que acabou bem. Não é uma linha que mente, é o programa inteiro.

Não abra o `aula07_relatorio_corrigido.py` antes de tentar. O exercício é a investigação, não a resposta.

```bash
python aulas/aula07/aula07_relatorio_bugado.py
```

Saída:

```
Aprovacao: 0.0%
Desconto de 50 por cento precisa de aprovacao? True
Soma: 40.0
```

## `aula07_relatorio_corrigido.py`

Os três defeitos do arquivo acima, corrigidos. É o mesmo código, com três caracteres de diferença e um `except` que ganhou tipo. Cada correção vem com o comentário do que estava errado e de como o defeito se manifestava, porque a lição é a investigação e não a linha certa.

**Regra de negócio:** as mesmas três do `aula07_relatorio_bugado.py`, agora com um `assert` por regra. É ele que compara o esperado, que vem da regra, com o obtido, que vem do programa.

O **primeiro defeito** era `aprovados + 1` sem o igual: a linha calculava um valor e jogava no lixo, porque ninguém guardou o resultado. Para o Python isso é uma expressão perfeitamente legal, então nenhuma mensagem avisa. É o processo `CRIA ANTES → PERCORRE → MUDA DENTRO → USA DEPOIS` da Aula 04 com a etapa do meio quebrada.

O **segundo** é de fronteira. A regra escrita diz que precisa de aprovação quando o desconto passa de 50%, e o código dizia `>= 50`, que inclui o 50. Um caractere de diferença, e ele só aparece se alguém testar exatamente 50. Guarde a sensação: na Aula 09 ela ganha nome e vira técnica.

O **terceiro** era o `except` pelado, e a correção dele mostra uma coisa que vale mais que o conserto: dar tipo ao `except` não corrigiu a soma, corrigiu a **cegueira**. O valor com vírgula continua sendo recusado; a diferença é que agora ele aparece na tela, e aí dá para consertar o dado.

```bash
python aulas/aula07/aula07_relatorio_corrigido.py
```

Saída:

```
Aprovacao: 66.7%
Desconto de 50 por cento precisa de aprovacao? False
Desconto de 51 por cento precisa de aprovacao? True
    ATENCAO: 1 valor(es) fora do formato: ["20,00 (could not convert string to float: '20,00')"]
Soma, com o aviso na tela: 40.00
Soma, com a massa normalizada: 60.00

As tres verificacoes passaram.
```

## `aula07_defeitos_pos_aula.py`

A atividade pós-aula da Aula 07. **Prazo: 08/09/2026, às 23h59.**

Cinco defeitos plantados, e eles não são do mesmo tipo: **dois de execução**, que param o programa e o Python te diz onde, e **três de lógica**, que deixam o programa rodar até o fim e imprimir número errado.

Os dois de execução você acha rodando. Os três de lógica só aparecem se você declarar o resultado esperado antes de rodar, e é esse o exercício de verdade.

**Regra de negócio:** as quatro regras estão escritas por extenso no cabeçalho do arquivo, em português, e é de lá que sai o resultado esperado de cada número. Leia as quatro, calcule os quatro números de cabeça, e só então rode. Quem rodar primeiro vai achar os dois de execução e parar, achando que acabou.

Para cada um dos cinco, registre três linhas: **sintoma** (o que você viu), **causa** (a linha e o motivo) e **correção** (o que você escreveu no lugar). Entregue o arquivo corrigido e o registro dos cinco, mesmo que você não tenha achado todos. Vale mais registrar quatro bem que listar cinco no chute.

Este arquivo chega quebrado de propósito. O trabalho é fazer ele sair com exit code 0 e os quatro números certos.

```bash
python aulas/aula07/aula07_defeitos_pos_aula.py
```

Saída na primeira execução, antes de você consertar nada:

```
=== Relatorio de execucao ===
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_defeitos_pos_aula.py", line 75, in <module>
    imprimir_detalhe(CASOS)
    ~~~~~~~~~~~~~~~~^^^^^^^
  File "...\aulas\aula07\aula07_defeitos_pos_aula.py", line 71, in imprimir_detalhe
    print(f"  {caso['nome']}: {caso['status']}, {caso['tempo']}s")
                                                 ~~~~^^^^^^^^^
KeyError: 'tempo'
```
