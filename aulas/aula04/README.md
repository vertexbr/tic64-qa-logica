# Aula 04 - Uma massa, vários cenários

Demonstrações de código da Aula 04, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

## Arquivos

- `aula04_lista_status.py`
- `aula04_contagem_assert.py`
- `aula04_for_primeiro.py`
- `aula04_range.py`
- `aula04_classificar_status.py`
- `aula04_catraca.py`
- `aula04_catraca_sem_incremento.py`
- `aula04_foguete.py`
- `aula04_freio_de_mao.py`
- `aula04_unicidade.py`
- `aula04_laco_infinito.py`
- `aula04_resumo_execucao.py`
- `aula04_desafio_extra.py`

## `aula04_lista_status.py`

Primeira demonstração da Aula 04: a massa de teste inteira numa variável só. Antes desta aula
seriam seis variáveis com nomes quase iguais, e a regra de classificação escrita seis vezes. O
arquivo mostra a lista, o acesso por índice (que começa em zero), o índice negativo, o `len`, o
`in`, e provoca de propósito o `IndexError` de quem pede um item a mais do que a lista tem.

```bash
python aulas/aula04/aula04_lista_status.py
```

Saída:

```
[200, 201, 404, 500, 302, 403]
200
404
403
6
True
False
IndexError: list index out of range
403
```

## `aula04_contagem_assert.py`

O arquivo-âncora da Aula 04: a evidência da Aula 03 virando verificação automática. A mesma
comparação, `len(produtos) == 6`, aparece duas vezes: primeiro dentro de um `print`, no formato
esperado/obtido/confere? da aula passada, e depois entregue ao `assert`. A diferença está no que
acontece quando ela dá errado, e o arquivo mostra as duas falhas lado a lado: o `AssertionError`
sem mensagem, que chega vazio, e o mesmo erro com a mensagem depois da vírgula, que devolve o
esperado e o obtido.

```bash
python aulas/aula04/aula04_contagem_assert.py
```

Saída:

```
A listagem trouxe 6 produtos
esperado: 6 | obtido: 6 | confere? True
Verificação passou: a listagem trouxe 6 produtos
AssertionError sem mensagem: AssertionError()
AssertionError com mensagem: esperado 7, obtido 6
Resultado mais recente da suíte: falhou
Execução anterior a ela: passou
Verificação passou: a última execução falhou
```

## `aula04_for_primeiro.py`

O `for` na forma mais curta possível, sobre uma lista de casos de teste. A leitura é "para cada
caso da lista, execute o caso", que é o que o QA já faz à mão numa suíte de regressão: o `for`
só dá nome ao gesto. Quem decide o número de voltas é a lista, não o código.

```bash
python aulas/aula04/aula04_for_primeiro.py
```

Saída:

```
Executando: login válido
Executando: login com senha errada
Executando: login com usuário bloqueado
Verificação passou: 3 casos percorridos
```

## `aula04_range.py`

O `range` e o off-by-one que mora nele: `range(3)` gera zero, um e dois. O arquivo mostra as duas
formas de percorrer e diz qual usar: `for item in lista` em noventa por cento dos casos, e a
versão com `range(len(...))` só quando o número da posição faz parte do resultado, como em
"caso 3 de 3".

```bash
python aulas/aula04/aula04_range.py
```

Saída:

```
Volta número 0
Volta número 1
Volta número 2

Caso 1 de 3: login válido
Caso 2 de 3: login com senha errada
Caso 3 de 3: login com usuário bloqueado
Verificação passou: as duas formas deram o mesmo número de voltas
```

## `aula04_classificar_status.py`

A primeira demonstração guiada da aula: o `for` de hoje com a escada de `if` da Aula 03 dentro.
Seis códigos de status classificados por faixa, com a massa conferida antes de ser usada. O
pseudocódigo da Aula 01 está comentado no topo do arquivo, e o `print` final fica alinhado com o
`if`, e não dentro dele, que é o que faz ele rodar em toda volta.

```bash
python aulas/aula04/aula04_classificar_status.py
```

Saída:

```
Massa conferida: 6 códigos para classificar
Status 200: Sucesso
Status 201: Sucesso
Status 404: Erro do cliente
Status 500: Erro do servidor
Status 302: Redirecionamento ou outro
Status 403: Erro do cliente
```

## `aula04_catraca.py`

O contador, que é a catraca do ônibus: ela começa num número e soma um a cada pessoa que passa,
sem guardar quem passou. O arquivo traz o teste de mesa em comentário, volta por volta, porque é
essa tabela que resolve quando o número final sai errado. Duas regras saem daqui: o contador
nasce antes do laço, e `aprovados = aprovados + 1` se lê da direita para a esquerda.

```bash
python aulas/aula04/aula04_catraca.py
```

Saída:

```
Antes da catraca: aprovados = 0
Passou pela catraca 'passou': aprovados = 1
Passou pela catraca 'falhou': aprovados = 1
Passou pela catraca 'passou': aprovados = 2
Verificação passou: 2 aprovados em 3 execuções
```

## `aula04_catraca_sem_incremento.py`

O erro proposital da Aula 04, e o argumento de existência da automação: a mesma catraca com a
linha do incremento comentada. Ele não tem erro de sintaxe, não quebra, roda até o fim, e entrega
zero por cento de aprovação numa execução que teve dois testes aprovados. O `print` de dentro do
`if` aparece duas vezes, provando que a condição funciona, e é isso que faz o defeito ser difícil:
a parte visível funciona e a parte que importa não.

```bash
python aulas/aula04/aula04_catraca_sem_incremento.py
```

Saída:

```
achei um que passou
achei um que passou
aprovados = 0
AssertionError: esperado 2, obtido 0
```

## `aula04_foguete.py`

O contador andando para trás. A catraca sobe, o foguete desce, mecanismo idêntico com o sinal
trocado. Os dois juntos ensinam a lição do dia: a variável de controle precisa mudar dentro do
laço, senão o número final está errado ou o laço não acaba.

```bash
python aulas/aula04/aula04_foguete.py
```

Saída:

```
5...
4...
3...
2...
1...
Lançamento!
Verificação passou: a contagem chegou a zero
```

## `aula04_freio_de_mao.py`

`break` e `continue` na mesma execução. O `break` é o freio de mão: puxa e o laço para, e o
`visual_user` da lista não chega a ser testado, o que é o comportamento esperado e não um defeito.
O `continue` desliga só a volta atual e segue para a próxima.

```bash
python aulas/aula04/aula04_freio_de_mao.py
```

Saída:

```
Tentando login com standard_user
Tentando login com problem_user
Tentando login com locked_out_user
Usuário bloqueado encontrado. Freio de mão: parando a varredura.
Varredura encerrada
Verificação passou: o último usuário da lista não chegou a ser visitado

Usuário que merece investigação: problem_user
Usuário que merece investigação: locked_out_user
Usuário que merece investigação: visual_user
```

## `aula04_unicidade.py`

O acumulador e a unicidade. Em vez de contar, o acumulador guarda: a lista vazia do começo é o
ponto de partida, o mesmo papel do zero no contador, e `.append` acrescenta no fim. A segunda
metade traz a linha `len(lista) == len(set(lista))`, que responde a uma regra de negócio presente
em quase todo sistema: identificador não pode repetir. O arquivo roda a verificação duas vezes,
com a massa limpa e com um id duplicado.

```bash
python aulas/aula04/aula04_unicidade.py
```

Saída:

```
Códigos de falha encontrados: [404, 500, 403]
Verificação passou: 3 códigos de falha na execução

Itens na lista: 5
Valores distintos: 5
Verificação passou: todo id da listagem é único

Itens na lista: 5
Valores distintos: 4
AssertionError: esperado 5 distintos, obtido 4
```

## `aula04_laco_infinito.py`

A vacina contra o travamento que todo iniciante provoca em casa. **O arquivo roda e termina**: a
versão que trava está comentada no topo, junto com a instrução de como sair dela. Basta comentar
a linha do decremento para reproduzir o travamento, e a saída é **Ctrl+C** no terminal. O
`KeyboardInterrupt` que aparece é inofensivo: ele só diz que você mandou parar.

O `while` não é conteúdo da Aula 04, ele chega na Aula 06. Aqui ele aparece uma vez só, porque é
o formato em que o laço infinito acontece.

```bash
python aulas/aula04/aula04_laco_infinito.py
```

Saída:

```
5...
4...
3...
2...
1...
Lançamento!
Verificação passou: a contagem terminou em zero e o laço acabou
```

## `aula04_resumo_execucao.py`

A segunda demonstração guiada: os números que aparecem no relatório de execução. Dois contadores
em vez de um, um percentual calculado a partir deles, e um acumulador de tipo diferente, que
guarda o maior valor visto em vez de somar. O detector do mais lento começa valendo `tempos[0]`, e
não zero, porque zero só funciona se você souber de antemão que nenhum valor da lista é
negativo, e essa suposição não sobrevive ao próximo detector.

```bash
python aulas/aula04/aula04_resumo_execucao.py
```

Saída:

```
Total de testes: 5
Aprovados: 3
Falhas: 2
Percentual de aprovação: 60.0%
Tempo do teste mais lento: 3.45s
Todas as verificações passaram
```

## `aula04_desafio_extra.py`

O desafio extra da aula: `continue` e `break` no mesmo laço. O `continue` pula os 200 e o `break`
mata a varredura no primeiro 500, então o último 200 da lista nunca é visitado. A variável
`interrompida` existe para que isso possa ser verificado com uma linha, em vez de lido na tela:
ausência de linha impressa não se compara com nada.

```bash
python aulas/aula04/aula04_desafio_extra.py
```

Saída:

```
Código fora do esperado: 404
Código fora do esperado: 500
Erro de servidor. A suíte foi interrompida.
Suíte interrompida? True
Verificação passou: a varredura parou no primeiro erro de servidor
```

## Rodar tudo desta aula

Os treze arquivos de demonstração da Aula 04 em sequência, num comando só:

```bash
python aulas/aula04/aula04_lista_status.py; python aulas/aula04/aula04_contagem_assert.py; python aulas/aula04/aula04_for_primeiro.py; python aulas/aula04/aula04_range.py; python aulas/aula04/aula04_classificar_status.py; python aulas/aula04/aula04_catraca.py; python aulas/aula04/aula04_catraca_sem_incremento.py; python aulas/aula04/aula04_foguete.py; python aulas/aula04/aula04_freio_de_mao.py; python aulas/aula04/aula04_unicidade.py; python aulas/aula04/aula04_laco_infinito.py; python aulas/aula04/aula04_resumo_execucao.py; python aulas/aula04/aula04_desafio_extra.py
```

---

Este README é gerado a partir da seção correspondente do [`README.md`](../../README.md) da raiz do repositório. Para alterar a explicação de um arquivo, edite lá e regenere aqui, para as duas fontes não divergirem.
