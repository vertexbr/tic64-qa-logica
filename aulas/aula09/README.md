# Aula 09 - Valores-limite e cenários em escala

Demonstrações de código da Aula 09. Os dois arquivos de produto rodam com `python` a partir da raiz do repositório (`(.venv)` ativo). Os oito arquivos de teste rodam com `pytest`, de dentro desta pasta, **e sempre nomeando o arquivo**.

## A regra do comando, e aqui ela é mais dura que na Aula 08

**Nunca rode `pytest` sozinho aqui dentro.** Nesta pasta a consequência é pior que na Aula 08: dois arquivos erram na **coleta** de propósito, e erro de coleta **interrompe a execução inteira**. O resultado é uma tela vermelha em que nenhum teste rodou.

```bash
cd aulas/aula09
pytest test_aula09_idade_na_mao.py -s -v
```

Da raiz do repositório o mesmo teste roda com o caminho completo, `pytest aulas/aula09/test_aula09_idade_na_mao.py -s -v`, e o relatório sai igual com o caminho na frente de cada nome.

**Três dos oito arquivos de teste não saem verdes, e os três são conteúdo:**

| Arquivo | Resultado | Por quê |
|---|---|---|
| `test_aula09_idade_na_mao.py` | 5 passed | os cinco casos escritos um por um, e o incômodo que a aula usa |
| `test_aula09_idade_parametrizado.py` | 5 passed | os mesmos cinco, numa função só |
| `test_aula09_tabela_decisao.py` | 4 passed | a tabela de decisão virando massa, com `ids` |
| `test_aula09_senha_e_frete.py` | 7 passed | dois `parametrize` no mesmo arquivo |
| `test_aula09_do_csv.py` | 4 passed | o desafio extra: a massa vinda de arquivo |
| `test_aula09_frete_quebrado.py` | 1 failed, 2 passed | o nome do caso dentro da falha |
| `test_aula09_nome_errado.py` | erro de coleta | `parameterize` escrito com "e" no meio |
| `test_aula09_massa_desalinhada.py` | erro de coleta | dois nomes para uma tupla de três valores |

Contagem conferida rodando os oito na `.venv` do repositório em 03/09/2026, com Python 3.13.5 e pytest 9.1.1.

## Arquivos

- `aula09_regras.py`
- `aula09_regras_frete_quebrado.py`
- `test_aula09_idade_na_mao.py`
- `test_aula09_idade_parametrizado.py`
- `test_aula09_tabela_decisao.py`
- `test_aula09_senha_e_frete.py`
- `test_aula09_frete_quebrado.py`
- `test_aula09_nome_errado.py`
- `test_aula09_massa_desalinhada.py`
- `test_aula09_do_csv.py`
- `aula09_massa_frete.csv`
- `aula09_massa_notas.csv`
- `test_exemplo_playwright.py`

## `aula09_regras.py`

O produto. Quatro regras que já existem no curso, reunidas aqui porque esta aula não é sobre escrever regra nova: é sobre escolher **quais dados** usar para testar regra que já existe.

```bash
python aulas/aula09/aula09_regras.py
```

Ele não imprime nada, e é de propósito: arquivo de produto não tem `print`. Quem chama são os testes.

As quatro funções, e de onde cada uma vem:

| Função | Vem de | O que esta aula acrescenta |
|---|---|---|
| `validar_idade_minima` | `aulas/aula08/aula08_regras.py` | a escolha de quais idades testar: 17, 18 e 19 |
| `tem_frete_gratis` | `aulas/aula06/aula06_funcoes_da_loja.py` | a massa 249.99, 250.00 e 300.00 |
| `senha_valida` | `aulas/aula06/aula06_senha_valida.py` | uma massa que mistura valor-limite e partição |
| `classificar_nota` | a escada da Aula 03, com o retorno antecipado da Aula 06 | enxergar que ela tem três fronteiras, não uma |

Tem uma quinta, `desconto_vip`, que é a regra de desconto da Aula 03 reduzida às duas condições que cabem numa tabela de decisão projetável. **O nome não é `calcular_desconto` de propósito:** aquele nome foi fixado pela atividade da Aula 08, com quatro parâmetros, e reaproveitar o nome com outra assinatura uma aula depois faria você importar a função errada.

## `aula09_regras_frete_quebrado.py`

A mesma loja, com uma linha mudada: o `>= 250.00` virou `> 250.00`. É o mesmo defeito de `aulas/aula08/aula08_loja.py`.

Ele existe para o `test_aula09_frete_quebrado.py` ficar vermelho, e o que interessa não é achar o defeito: é ler o **nome** da linha que o denunciou.

## `test_aula09_idade_na_mao.py`

Os cinco casos escritos um por um, cada um na própria função.

```bash
cd aulas/aula09
pytest test_aula09_idade_na_mao.py -s -v
```

```
collected 5 items

test_aula09_idade_na_mao.py::test_idade_17_e_rejeitada PASSED
test_aula09_idade_na_mao.py::test_idade_18_e_aceita PASSED
test_aula09_idade_na_mao.py::test_idade_19_e_aceita PASSED
test_aula09_idade_na_mao.py::test_idade_0_e_rejeitada PASSED
test_aula09_idade_na_mao.py::test_idade_120_e_aceita PASSED

============================== 5 passed in 0.04s ==============================
```

Está correto e está completo. Olhe as cinco funções e responda o que muda de uma para a outra: um número e um `True` ou `False`. O `def`, a chamada e o `assert` aparecem **cinco vezes cada um**, para carregar dez valores.

## `test_aula09_idade_parametrizado.py`

Os mesmos cinco casos, numa função só.

```
collected 5 items

test_aula09_idade_parametrizado.py::test_idade_minima[17-False] PASSED
test_aula09_idade_parametrizado.py::test_idade_minima[18-True] PASSED
test_aula09_idade_parametrizado.py::test_idade_minima[19-True] PASSED
test_aula09_idade_parametrizado.py::test_idade_minima[0-False] PASSED
test_aula09_idade_parametrizado.py::test_idade_minima[120-True] PASSED

============================== 5 passed in 0.05s ==============================
```

Continuam sendo cinco testes, e não um: o `collected 5 items` prova.

**E o arquivo não ficou menor.** Medido em 03/09/2026, os dois têm onze linhas de código. Com cinco casos o `parametrize` não encurta nada.

| O que comparar | Na mão | Parametrizado |
|---|--:|--:|
| linhas de código | 11 | 11 |
| vezes que o `def`, a chamada e o `assert` aparecem | 5 | 1 |
| **custo do próximo caso** | **2 linhas** | **1 linha** |

O ganho de tamanho só aparece quando a massa cresce. Com poucos casos o ganho é repetição e custo de manutenção.

## `test_aula09_tabela_decisao.py`

A tabela de decisão de duas condições virando massa de quatro linhas, com `ids`. As quatro passam, e é isso que faz a suíte valer alguma coisa: massa com dado inválido esperando falhar destrói a suíte, porque no dia em que aparecer uma falha de verdade ninguém vai olhar.

```
collected 4 items

test_aula09_tabela_decisao.py::test_tabela_de_decisao_do_desconto[vip_acima_de_200] PASSED
test_aula09_tabela_decisao.py::test_tabela_de_decisao_do_desconto[vip_abaixo_de_200] PASSED
test_aula09_tabela_decisao.py::test_tabela_de_decisao_do_desconto[comum_acima_de_200] PASSED
test_aula09_tabela_decisao.py::test_tabela_de_decisao_do_desconto[comum_abaixo_de_200] PASSED

============================== 4 passed in 0.04s ==============================
```

## `test_aula09_senha_e_frete.py`

Dois `parametrize` no mesmo arquivo, sete testes no relatório. Cada decorador governa só a função imediatamente abaixo dele.

A massa da senha mistura as duas técnicas de propósito: as duas primeiras linhas são valor-limite (7 e 8 caracteres), e as duas últimas são partição de outra natureza, porque "sem maiúscula" e "sem número" são grupos de comportamento, não vizinhos de número.

## `test_aula09_frete_quebrado.py`

A mesma massa do frete, apontada para o arquivo estragado. **Sai com exit code 1 de propósito.**

```
test_aula09_frete_quebrado.py::test_frete_gratis[um_centavo_abaixo] PASSED
test_aula09_frete_quebrado.py::test_frete_gratis[exatamente_no_limite] FAILED
test_aula09_frete_quebrado.py::test_frete_gratis[bem_acima] PASSED

================================== FAILURES ===================================
___________________ test_frete_gratis[exatamente_no_limite] ___________________

total = 250.0, esperado = True

>       assert tem_frete_gratis(total) == esperado
E       assert False == True
E        +  where False = tem_frete_gratis(250.0)

========================= 1 failed, 2 passed in 0.09s =========================
```

"Exatamente no limite falhou." Você leu isso e já sabe o defeito, sem abrir o código. Sem o `ids`, o relatório diria "caso 2 falhou".

Repare também na linha `total = 250.0, esperado = True`, no topo da falha: os nomes das colunas viraram nomes de variável no relatório, de graça.

## `test_aula09_nome_errado.py`

A primeira armadilha. Escreve-se `parametrize`, sem "e" no meio. **Erra na coleta de propósito.**

```
E   Failed: Unknown 'parameterize' mark, did you mean 'parametrize'?
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
```

O pytest atual recusa e sugere o nome certo. Em versões mais antigas isso passava como aviso e o teste simplesmente sumia do relatório sem ninguém notar, o que é bem pior.

## `test_aula09_massa_desalinhada.py`

A segunda armadilha. Dois nomes na string e três valores numa linha da massa. **Erra na coleta de propósito.**

```
in "parametrize" the number of names (2):
  ['idade', 'esperado']
must be equal to the number of values (3):
  (18, True, 'extra')
```

A mensagem é boa e diz os dois números, mas ela aparece na coleta: nada roda, nem os testes dos outros arquivos.

## `aula09_massa_frete.csv` e `test_aula09_do_csv.py`

O desafio extra: a massa sai de um arquivo em vez de estar no código, e passa a ser editável por quem não escreve Python.

```
id;total;esperado
um_centavo_abaixo;249.99;False
exatamente_no_limite;250.00;True
bem_acima;300.00;True
zero_reais;0.00;False
```

O separador é ponto e vírgula, e não vírgula, porque valor em real leva ponto ou vírgula decimal e a vírgula brigaria com a separação das colunas.

**A armadilha, e ela é a única coisa realmente nova aqui:** tudo que sai de um arquivo de texto chega como texto. A string `"False"` não é o booleano `False`, e ela é **verdadeira** num `if`, porque toda string não vazia é verdadeira. Por isso as duas conversões do arquivo não são opcionais.

## `aula09_massa_notas.csv`

A planilha de casos que o time de negócio mandou, e **é ela que a atividade desta aula manda corrigir**. Quatro linhas, e nenhuma delas encosta em 70, 80 ou 90.

```
id;nota;esperado
aluno_otimo;95;excelente
aluno_bom;85;bom
aluno_mediano;75;suficiente
aluno_ruim;50;insuficiente
```

## `test_exemplo_playwright.py`

O teste que prova que o Playwright ficou instalado. **Não é aula de Playwright**: ele existe para você ver `1 passed` na tela e saber que a sua máquina está pronta para a Aula 12.

Antes de rodar, os dois comandos precisam ter terminado:

```bash
pip install pytest-playwright
playwright install chromium
```

O primeiro instala a biblioteca. O segundo baixa o navegador que ela vai dirigir, e são cerca de 190 MB.

```bash
cd aulas/aula09
pytest test_exemplo_playwright.py
```

```
collected 1 item

test_exemplo_playwright.py .                                             [100%]

============================== 1 passed in 5.11s ==============================
```

O tempo varia de máquina para máquina e de rede para rede. O que importa é o `1 passed`.

Se o comando `playwright` não for reconhecido, rode `python -m playwright install chromium`: essa forma usa o mesmo Python em que o pacote foi instalado.

## A atividade desta aula

A entrega não é código: é **massa de teste**, no arquivo `entregas/massa_aula09.csv`. A suíte que julga está em `tests/test_massa_aula09.py`, e roda da raiz do repositório:

```bash
pytest tests/test_massa_aula09.py -v
```
