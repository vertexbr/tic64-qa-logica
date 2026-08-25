# Aula 03 - Regras de negócio virando decisões

Demonstrações de código da Aula 03, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

## Arquivos

- `aula03_operadores.py`
- `aula03_login_evidencia.py`
- `aula03_desconto.py`
- `aula03_desconto_invertido.py`
- `aula03_gate_release.py`
- `aula03_defeitos.py`
- `quadro_erro4.py`

## `aula03_operadores.py`

Primeira demonstração da Aula 03: as três famílias de operadores, com a previsão antes da
execução. Os matemáticos (a barra simples devolve float mesmo em divisão exata, a barra dupla é
divisão inteira e o `%` é o resto), os de comparação (devolvem sempre um booleano, nunca outra
coisa) e os lógicos, no vocabulário de triagem: `bug_corrigido` e `regressao_encontrada`.

```bash
python aulas/aula03/aula03_operadores.py
```

Saída:

```
15
2.0
3
1
True
False
True
True
True
True
False
```

## `aula03_login_evidencia.py`

A evidência esperado x obtido no caso de teste de login da Aula 02, com a mesma massa do
`aulas/aula02/aula02_login.py`. Cada linha agora compara o esperado com o obtido e imprime o veredito:
o `confere?` é a comparação com `==` rodando dentro da f-string. O arquivo termina com o defeito
plantado da aula, um espaço no fim do texto esperado, e com a linha de `!r` que revela ele.

```bash
python aulas/aula03/aula03_login_evidencia.py
```

Saída:

```
CT-01 | usuário | esperado: Nadinha | obtido: Nadinha | confere? True
CT-01 | senha   | esperado: JL1234! | obtido: JL1234! | confere? True
CT-01 | total   | esperado: 599.70 | obtido: 599.7 | confere? True
CT-01 | usuário | esperado: Nadinha  | obtido: Nadinha | confere? False
CT-01 | usuário | esperado: 'Nadinha ' | obtido: 'Nadinha' | confere? False
```

## `aula03_desconto.py`

O arquivo-âncora da Aula 03: a regra de desconto da loja virtual (critério de aceite CA-018) em
3 camadas, com o pseudocódigo da Aula 01 comentado no topo, a massa do caso em variáveis, e a
cadeia `if`, `elif` e `else` embaixo. A regra: cliente VIP acima de R$ 200,00 recebe 20%; VIP
até R$ 200,00 recebe 10%; cupom válido ou promoção, para cliente comum, 5%; nada disso, sem
desconto. A planilha dos 5 casos está comentada no arquivo: para treinar, troque a massa e rode
de novo, um caso por execução.

```bash
python aulas/aula03/aula03_desconto.py
```

Saída:

```
CT-01 | esperado: 20% | obtido: 20% | confere? True
CT-01 | valor final: R$ 240.00
```

## `aula03_desconto_invertido.py`

O erro proposital da Aula 03: a mesma regra de desconto com os dois primeiros ramos trocados.
Nada quebra e nenhum aviso aparece, e o cliente VIP de R$ 300,00 recebe 10% em vez de 20%,
porque a primeira condição é genérica demais e engole todos os casos VIP. O ramo de 20% vira
código morto, e no depurador dá para ver o destaque pulando direto por cima dele. É o primeiro
`confere? False` do curso com o programa terminando sem erro.

```bash
python aulas/aula03/aula03_desconto_invertido.py
```

Saída:

```
CT-01 | esperado: 20% | obtido: 10% | confere? False
```

## `aula03_gate_release.py`

A escada de faixas da Aula 03, no contexto que a turma vai viver a carreira inteira: a suíte
rodou, e o gate decide se a release sai. Taxa de aprovação de 90% ou mais libera; 80% ou mais
libera com ressalva; 70% ou mais segura para revisão; abaixo disso bloqueia. A massa de
fronteira está comentada no arquivo (90, 89, 80, 79, 70, 69): troque a taxa e a decisão esperada
e rode de novo, um caso por execução.

```bash
python aulas/aula03/aula03_gate_release.py
```

Saída:

```
Taxa 85% | esperado: libera com ressalva | obtido: libera com ressalva | confere? True
```

## `aula03_defeitos.py`

A classificação de defeitos da Aula 01 virando Python, com a regra numa forma que evoluiu desde
lá: na Aula 01 as severidades eram CRÍTICA, ALTA e BAIXA; na Aula 03 a regra ganha o workaround,
como em triagem de verdade. Impede produção e não tem workaround: CRÍTICA. Impede produção e tem
workaround: ALTA. Qualquer outro caso: MÉDIA. Dois booleanos dão 4 combinações, sempre, e a
planilha das 4 está comentada no arquivo.

```bash
python aulas/aula03/aula03_defeitos.py
```

Saída:

```
CT-01 | esperado: CRÍTICA | obtido: CRÍTICA | confere? True
```

## `quadro_erro4.py`

O quarto erro do quadro da Aula 03, o pior do curso: `idade_texto == 18` com a idade vinda de
formulário, como texto. Roda sem erro e sem aviso, nunca entra no `if`, e classifica a pessoa de
18 anos como menor de idade. O professor usa este arquivo ao vivo na demonstração, com
breakpoint na linha do `if` para o painel do depurador mostrar o tipo.

```bash
python aulas/aula03/quadro_erro4.py
```

Saída:

```
menor de idade
```

## Rodar tudo desta aula

Os seis arquivos de demonstração da Aula 03 em sequência, num comando só, que é a bateria que
fecha a aula:

```bash
python aulas/aula03/aula03_operadores.py; python aulas/aula03/aula03_login_evidencia.py; python aulas/aula03/aula03_desconto.py; python aulas/aula03/aula03_desconto_invertido.py; python aulas/aula03/aula03_gate_release.py; python aulas/aula03/aula03_defeitos.py
```

---

Este README é gerado a partir da seção correspondente do [`README.md`](../../README.md) da raiz do repositório. Para alterar a explicação de um arquivo, edite lá e regenere aqui, para as duas fontes não divergirem.
