# Fundamentos de Lógica de Programação para Analista de Qualidade

Repositório de código do curso VERTEX QA-TIC64.

Aqui ficam os arquivos que rodam: as demonstrações feitas em aula, a massa de dados dos exercícios e as suítes que verificam as atividades pós-aula. São 15 aulas, e o repositório cresce junto com elas.

## Stack

Python 3.12 ou superior, com pytest, Requests e Playwright pelo plugin `pytest-playwright`. Chromium é o único navegador do curso, então não precisa instalar Firefox nem WebKit.

## Setup

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/vertexbr/tic64-qa-logica.git
cd tic64-qa-logica
```

Crie o ambiente virtual e ative:

```bash
python -m venv .venv

.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS e Linux
```

Quando aparecer `(.venv)` no começo da linha do terminal, o ambiente está ativo. Com ele ativo, instale as bibliotecas e o navegador:

```bash
pip install -r requirements.txt
playwright install chromium
```

O `requirements.txt` traz as três dependências diretas do curso, com a versão travada para que toda a turma rode o mesmo ambiente durante as 15 aulas. O `playwright install chromium` é um passo separado porque baixa o navegador, que não é pacote Python e não entra no `pip install`.

No macOS e no Linux o comando pode ser `python3` em vez de `python`. Se for o seu caso, troque nos comandos acima.

## Como rodar

Sempre da raiz do projeto, com o `(.venv)` ativo. Sem o ambiente ativo, o `pytest` que responde pode ser o do sistema, que não tem as bibliotecas do curso instaladas, e o erro aparece como um `ModuleNotFoundError` difícil de entender.

```bash
pytest                                    # tudo que estiver em tests/
pytest tests/test_isca_aula01.py          # um arquivo só
pytest -k compra                          # só os testes cujo nome casa com "compra"
pytest -v                                 # uma linha por teste, com o nome de cada um
```

Sem argumento, o pytest varre a pasta e roda todo arquivo `test_*.py` que encontrar. Passar o caminho é o jeito de limitar a um arquivo.

Nos testes de interface, o navegador roda escondido por padrão. Duas flags do `pytest-playwright` mudam isso:

```bash
pytest tests/test_isca_aula01.py --headed --slowmo 500
```

O `--headed` abre a janela do Chromium na tela. O `--slowmo 500` põe meio segundo de pausa entre as ações, o suficiente para acompanhar o que está acontecendo. As duas juntas servem para ver o teste trabalhar. Sem elas, o teste roda em silêncio e mais rápido, que é o modo normal do dia a dia.

Quando um teste falha, o pytest imprime a linha exata do `assert` que não passou, junto com o valor que ele encontrou. Leia essa saída antes de mexer no código: na maioria das vezes ela já diz o que está errado.

## O que tem aqui

### `tests/test_isca_aula01.py`

Um teste de interface ponta a ponta. Ele faz login no SauceDemo, adiciona um produto ao carrinho e verifica que o carrinho ficou com um item. Roda em cerca de 15 segundos.

O SauceDemo é uma aplicação pública de terceiros, feita para servir de alvo de treino. Isso traz um efeito colateral que é conteúdo do curso: teste que depende de site de terceiro quebra por motivo que não é seu, e a Aula 13 trata de como lidar com isso.

### `aulas/aula01/aula01_classificar_defeito.py`

A Aula 01 não escreve Python: a turma sai dela com o pseudocódigo no papel. Este arquivo é a tradução, em código, do algoritmo `classificar_defeito` ensinado em aula, com a regra de negócio e o pseudocódigo comentados no topo do arquivo antes da função.

Regra: defeito que impede o uso do sistema é severidade CRÍTICA; se não impede o uso mas afeta uma funcionalidade, é ALTA; qualquer outra coisa é BAIXA.

O arquivo também traz o "erro proposital" da aula: a mesma função com as duas condições invertidas, para mostrar que a ordem das condições muda o resultado sem gerar nenhum erro de execução.

```bash
python aulas/aula01/aula01_classificar_defeito.py
```

Saída:

```
Severidade: CRÍTICA
Severidade com a ordem trocada: ALTA
```

### `aulas/aula01/aula01_validar_login.py`

Tradução, em código, do algoritmo `validar_login` ditado pela turma na Aula 01, com a regra de negócio e o pseudocódigo comentados no topo do arquivo.

Regra: o login é aprovado se o usuário está ativo E a senha está correta; ao errar a senha três vezes o usuário é bloqueado, e depois de bloqueado não entra nem com a senha certa.

Executa os quatro casos do teste de mesa feito em aula.

```bash
python aulas/aula01/aula01_validar_login.py
```

Saída:

```
Caso 1 -> resultado: APROVADO | tentativas: 0
Caso 2 -> resultado: NEGADO | tentativas: 3
Caso 3 -> resultado: BLOQUEADO | tentativas: 3
Caso 4 -> resultado: NEGADO | tentativas: 1
```

### `aulas/aula02/aula02.py`

Demonstração da Aula 02, o cenário de compra. Declara as variáveis do carrinho (valor do produto, quantidade, cliente ativo e o valor mínimo para frete grátis), calcula o total numa variável e imprime cinco linhas de evidência com f-string. No fim mostra o `type()` de três variáveis, para a turma ver `float`, `int` e `bool` saindo na tela.

```bash
python aulas/aula02/aula02.py
```

Saída:

```
Produto: R$ 199.90
Quantidade: 3
Total da compra: R$ 599.70
Cliente ativo? True
Frete grátis a partir de R$ 250.00
<class 'float'>
<class 'int'>
<class 'bool'>
```

### `aulas/aula02/aula02_login.py`

Segunda demonstração da Aula 02, o caso de teste de login. Separa o dado informado do dado esperado em variáveis distintas, que é a ideia central do exercício, e guarda ainda o contador de tentativas e o token da sessão. A comparação usa `==`, o operador que compara valores, diferente do `=` que atribui.

O `token = None` está ali de propósito: `None` é ausência de valor, não string vazia, e imprime literalmente `None`.

```bash
python aulas/aula02/aula02_login.py
```

Saída:

```
Usuário informado: Nadinha
Usuário esperado: Nadinha
Usuários iguais? True
Senhas iguais? True
Tentativas: 0 | Token: None
```

### `aulas/aula02/aula02_tipos_e_nomes.py`

Demonstrações do primeiro ciclo da Aula 02: nomes de variável em snake_case, os cinco tipos do curso (`str`, `int`, `float`, `bool`, `None`) com o vocabulário do curso, a distinção entre `200` e `"200"`, o contraste de f-string com e sem o `f`, e o primeiro erro proposital (`"58" + 1`), capturado com `try/except` para o arquivo terminar sem travar.

```bash
python aulas/aula02/aula02_tipos_e_nomes.py
```

### `aulas/aula02/aula02_conversao_e_armadilhas.py`

Demonstrações do segundo ciclo da Aula 02: a simulação de dado externo que vem como texto (o lugar do `input()` da calculadora que devolve `105`), a comparação `codigo == codigo_texto`, o erro `AttributeError` de `codigo.strip()` num número, a armadilha do `0.1 + 0.2`, a diferença entre o nome de uma variável e o seu conteúdo, e o erro da vírgula decimal (`599,90` virando tupla). Os erros propositais ficam em `try/except` para o arquivo rodar do início ao fim.

```bash
python aulas/aula02/aula02_conversao_e_armadilhas.py
```

Os quatro arquivos da Aula 02 em sequência, num comando só:

```bash
python aulas/aula02/aula02.py; python aulas/aula02/aula02_login.py; python aulas/aula02/aula02_tipos_e_nomes.py; python aulas/aula02/aula02_conversao_e_armadilhas.py
```

No PowerShell do Windows use `;` como separador. O `&&` só funciona no PowerShell 7 ou no bash.

### `aulas/aula03/aula03_operadores.py`

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

### `aulas/aula03/aula03_login_evidencia.py`

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

### `aulas/aula03/aula03_desconto.py`

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

### `aulas/aula03/aula03_desconto_invertido.py`

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

### `aulas/aula03/aula03_gate_release.py`

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

### `aulas/aula03/aula03_defeitos.py`

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

### `aulas/aula03/quadro_erro4.py`

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

Os seis arquivos de demonstração da Aula 03 em sequência, num comando só, que é a bateria que
fecha a aula:

```bash
python aulas/aula03/aula03_operadores.py; python aulas/aula03/aula03_login_evidencia.py; python aulas/aula03/aula03_desconto.py; python aulas/aula03/aula03_desconto_invertido.py; python aulas/aula03/aula03_gate_release.py; python aulas/aula03/aula03_defeitos.py
```

### `aulas/aula04/aula04_lista_status.py`

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

### `aulas/aula04/aula04_contagem_assert.py`

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

### `aulas/aula04/aula04_for_primeiro.py`

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

### `aulas/aula04/aula04_range.py`

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

### `aulas/aula04/aula04_classificar_status.py`

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

### `aulas/aula04/aula04_catraca.py`

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

### `aulas/aula04/aula04_catraca_sem_incremento.py`

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

### `aulas/aula04/aula04_foguete.py`

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

### `aulas/aula04/aula04_freio_de_mao.py`

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

### `aulas/aula04/aula04_unicidade.py`

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

### `aulas/aula04/aula04_laco_infinito.py`

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

### `aulas/aula04/aula04_resumo_execucao.py`

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

### `aulas/aula04/aula04_desafio_extra.py`

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

Os treze arquivos de demonstração da Aula 04 em sequência, num comando só:

```bash
python aulas/aula04/aula04_lista_status.py; python aulas/aula04/aula04_contagem_assert.py; python aulas/aula04/aula04_for_primeiro.py; python aulas/aula04/aula04_range.py; python aulas/aula04/aula04_classificar_status.py; python aulas/aula04/aula04_catraca.py; python aulas/aula04/aula04_catraca_sem_incremento.py; python aulas/aula04/aula04_foguete.py; python aulas/aula04/aula04_freio_de_mao.py; python aulas/aula04/aula04_unicidade.py; python aulas/aula04/aula04_laco_infinito.py; python aulas/aula04/aula04_resumo_execucao.py; python aulas/aula04/aula04_desafio_extra.py
```

## Convenção de arquivos

O repositório tem duas pastas com propósitos diferentes.

Em `tests/` ficam as suítes que o pytest roda, um arquivo por aula, no padrão `tests/test_<assunto>_aula<NN>.py`, com o número da aula em dois dígitos. O nome de cada teste dentro do arquivo começa com `test_` e descreve o que está sendo verificado, em português, como em `test_compra_um_produto`.

Em `aulas/` ficam as demonstrações feitas ao vivo, uma subpasta por aula, no padrão `aulas/aula<NN>/aula<NN>_<assunto>.py`, com o número da aula em dois dígitos nos dois níveis. Esses arquivos rodam pelo `python` e são script de estudo, não suíte de verificação. Deixá-los fora de `tests/` evita que o pytest tente coletá-los.

A subpasta por aula existe porque o repositório cresce durante as 15 aulas e a raiz de `aulas/` ficaria com dezenas de arquivos misturados. Quem procura o material de uma aula abre a pasta dela:

```
aulas/
├── aula01/    aula01_classificar_defeito.py, aula01_validar_login.py
├── aula02/    aula02.py, aula02_login.py, aula02_tipos_e_nomes.py, aula02_conversao_e_armadilhas.py
├── aula03/    aula03_operadores.py, aula03_login_evidencia.py, aula03_desconto.py,
│              aula03_desconto_invertido.py, aula03_gate_release.py, aula03_defeitos.py,
│              quadro_erro4.py
└── aula04/    aula04_lista_status.py, aula04_contagem_assert.py, aula04_for_primeiro.py,
               aula04_range.py, aula04_classificar_status.py, aula04_catraca.py,
               aula04_catraca_sem_incremento.py, aula04_foguete.py, aula04_freio_de_mao.py,
               aula04_unicidade.py, aula04_laco_infinito.py, aula04_resumo_execucao.py,
               aula04_desafio_extra.py
```

O nome do arquivo repete o número da aula de propósito: os comandos do curso são copiados e colados no terminal e no chat, e `python aulas/aula03/aula03_desconto.py` diz de qual aula é o arquivo mesmo fora do contexto da pasta. O `quadro_erro4.py` é a exceção do padrão, porque é o scratch do quadro de erros, não uma demonstração numerada da aula.

A Aula 01 é a única exceção: nela a turma não digita Python, só pseudocódigo no papel. Os arquivos `aulas/aula01/aula01_classificar_defeito.py` e `aulas/aula01/aula01_validar_login.py` existem para dar à regra de negócio e ao algoritmo da aula uma forma executável, com o pseudocódigo comentado no topo do arquivo e o código correspondente embaixo.
