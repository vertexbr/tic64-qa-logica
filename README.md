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

### `aulas/aula05/aula05_por_numero_por_nome.py`

Primeira demonstração da Aula 05: o mesmo registro guardado dos dois jeitos. A primeira metade
mostra o problema de guardar um usuário numa lista, com o dia em que o desenvolvedor inclui o
telefone entre o nome e o e-mail: a posição 2 continua respondendo e passa a responder a coisa
errada, sem erro nenhum. A segunda metade guarda o mesmo dado num dicionário, lê por nome, e
mostra que alterar uma chave que existe e criar uma que não existe são a mesma linha.

```bash
python aulas/aula05/aula05_por_numero_por_nome.py
```

Saída:

```
gaia@teste.com
82999990000
Gaia Silva
gaia@teste.com
{'id': 42, 'nome': 'Gaia Souza', 'email': 'gaia@teste.com', 'ativo': True}
Verificações passaram: a alteração e a criação aconteceram
```

### `aulas/aula05/aula05_chave_ausente_erro.py`

Os dois `KeyError` da aula, na ordem que importa: o `usuario[0]`, que é o hábito de lista da Aula
04 batendo num dicionário, e o `usuario["telefone"]`, que é o campo opcional ausente. A mensagem
de erro é o conteúdo, e nos dois casos ela diz exatamente qual chave o Python não achou.

Os dois estão dentro de `try/except` para o arquivo rodar até o fim e mostrar os dois na mesma
execução. **Numa suíte de verdade isso não se faz:** falha tem que interromper, e `except` largo é
a forma mais comum de um teste ficar verde sem ter testado nada. Aqui o `try/except` é recurso
didático, e o arquivo diz isso no topo.

```bash
python aulas/aula05/aula05_chave_ausente_erro.py
```

Saída:

```
KeyError: 0
Dicionário aceita chave numérica? True
KeyError: 'telefone'
As duas mensagens dizem exatamente qual chave o Python não achou
```

O `KeyError: 0` tem uma leitura errada que é a mais comum: ele **não** quer dizer que dicionário
recusa número. Aceita, e `{0: "ok"}` é dicionário válido, o que a segunda linha da saída prova. O
que aconteceu foi uma busca pela chave `0`, que este dicionário não tem. A regra é sobre nome
contra posição, não sobre texto contra número.

### `aulas/aula05/aula05_chave_ausente.py`

A resposta ao arquivo anterior, em três ferramentas: `in` responde se a chave existe e devolve
booleano, `get` devolve o valor ou `None` sem quebrar, e `get` com segundo argumento devolve o
padrão que você escolher. O rótulo de prioridade é o que vale guardar: colchete quando o campo é
obrigatório e a ausência dele é defeito que você quer que estoure, `get` quando o campo é
opcional.

```bash
python aulas/aula05/aula05_chave_ausente.py
```

Saída:

```
Tem chave telefone? False
Com get: None
Com get e padrão: não informado
O id, que é obrigatório: 42
As três verificações passaram
```

### `aulas/aula05/aula05_aninhado.py`

A estrutura mais importante do curso: dicionário dentro de dicionário e lista dentro de
dicionário, no mesmo registro. `usuario['endereco']['cidade']` se lê da esquerda para a direita,
e cada colchete desce um andar. O `perfis` é uma lista dentro do dicionário, e por isso ele volta
a usar número: os dois modos convivem, um por andar.

O arquivo também nomeia o erro mais provável da aula, que é pedir a chave certa no andar errado:
`usuario["cidade"]` devolve `KeyError: 'cidade'` mesmo com a cidade existindo dentro de
`endereco`.

```bash
python aulas/aula05/aula05_aninhado.py
```

Saída:

```
Cidade: Fortaleza
Primeiro perfil: admin
Quantidade de perfis: 2
É admin? True
As três verificações passaram
O andar de fora: {'cidade': 'Fortaleza', 'uf': 'CE'}
```

### `aulas/aula05/aula05_suite_casos.py`

Lista de dicionários, que é literalmente uma suíte de casos de teste: a lista dá a ordem, o
dicionário dá os campos de cada caso. Toda resposta de listagem de API tem esta cara, e é por
isso que ela volta nas Aulas 10 e 11. O `suite[-1]['resultado']` traz o índice negativo da Aula
04 de volta, agora entregando um dicionário do qual se pega um campo por nome.

```bash
python aulas/aula05/aula05_suite_casos.py
```

Saída:

```
login válido: passou
senha errada: passou
usuário bloqueado: falhou
Resultado mais recente: falhou
Verificações passaram
```

### `aulas/aula05/aula05_mapa_ambientes.py`

O dicionário que quem testa usa mais do que qualquer outro, e ele não é dicionário de pessoa: é
mapa de ambientes. Um teste, três endereços, e para apontar a suíte inteira para homologação você
troca uma linha. O `assert ambiente_atual != "producao"` é barato e evita a pior tarde da
carreira. Percorrer um dicionário com `for` entrega as chaves, não os valores, e é por isso que
`ambientes[nome]` aparece dentro do laço.

Este arquivo volta na Aula 10 como o endereço base das requisições.

```bash
python aulas/aula05/aula05_mapa_ambientes.py
```

Saída:

```
teste: https://teste.loja.com
homologacao: https://homologacao.loja.com
producao: https://loja.com
Rodando a suíte contra: https://teste.loja.com
Endereço de login: https://teste.loja.com/login
Verificações passaram: a suíte não está apontada para produção
```

### `aulas/aula05/aula05_json_minusculo_erro.py`

JSON e dicionário Python são visualmente quase idênticos, e a diferença são três palavras: `true`
para `True`, `false` para `False`, e `null` para `None`. É exatamente aqui que quebra quando
alguém copia um JSON de resposta e cola no editor para virar massa de teste.

O arquivo roda com a versão corrigida e deixa a linha do JSON cru **comentada**. Para ver o erro,
descomente ela e rode: o Python para na linha e a mensagem vem com a correção sugerida.

```
NameError: name 'true' is not defined. Did you mean: 'True'?
```

A sugestão só aparece assim, num erro que interrompe de verdade: capturar com `try/except` deixa
só `name 'true' is not defined` e come justamente a parte que ensina. Por isso aqui a linha fica
comentada em vez de embrulhada, ao contrário do arquivo dos dois `KeyError`, onde a mensagem
capturada já entrega o nome da chave e nada se perde.

```bash
python aulas/aula05/aula05_json_minusculo_erro.py
```

Saída:

```
{'nome': 'Gaia', 'ativo': True, 'telefone': None}
Ativo? True
Telefone: None
O telefone é None? True
O telefone é texto vazio? False
Verificações passaram: o resto é igual ao dicionário de sempre
```

As duas últimas linhas antes das verificações existem porque campo que veio nulo e campo que veio
em branco são dois defeitos diferentes, e a distinção aparece em resposta de API todo dia.

### `aulas/aula05/aula05_resposta_listagem.py`

A resposta de listagem copiada da aba de rede do navegador e transcrita para dicionário Python.
O `assert resposta["quantidade"] == len(resposta["produtos"])` é um teste de verdade, do tipo que
acha defeito real: a API afirma uma quantidade num campo e entrega uma lista noutro, e nada
garante que os dois batem. O `len` da Aula 04 acabou de virar validação de contrato de API.

Traz também dois degraus que a Aula 08 recicla dentro de uma escada de asserções: a lista não veio
vazia, e o campo obrigatório está presente no primeiro registro.

```bash
python aulas/aula05/aula05_resposta_listagem.py
```

Saída:

```
A API disse que trouxe 3 produtos
A lista tem de verdade 3 produtos
Verificação passou: o campo quantidade bate com o tamanho da lista
Primeiro produto: Api de teste
Verificações passaram: a lista não veio vazia e o registro tem _id
```

### `aulas/aula05/aula05_usuario_beto.py`

Primeira demonstração guiada da Aula 05, e o arquivo para refazer em casa: os campos de um
usuário, inclusive os aninhados. Seis linhas de saída e três verificações, com a regra numerada
no topo do arquivo. Os dois tropeços previstos estão comentados no fim: aspas duplas dentro de
f-string de aspas duplas, e colchete em `telefone` no lugar do `get`.

```bash
python aulas/aula05/aula05_usuario_beto.py
```

Saída:

```
Nome: Beto Nunes
Cidade: Maceió
UF: AL
Primeiro perfil: editor
Tem telefone? False
Telefone: não informado
As três verificações passaram
```

### `aulas/aula05/aula05_email_sujo.py`

O antídoto de uma família inteira de testes instáveis. Dado que vem de fora vem sujo, e comparar
sem normalizar é a causa número um de teste que falha sem explicação. O valor aparece entre
apóstrofos dentro do `print` de propósito: espaço não aparece na tela, e o apóstrofo revela ele.

Mostra `strip`, `lower`, as duas juntas, e a linha que prova que string é imutável: o original
continua sujo depois de tudo. Depois `split` no arroba, a validação que se lê em português, e o
`join`, que é o contrário exato do `split` e é o que a segunda demonstração usa.

```bash
python aulas/aula05/aula05_email_sujo.py
```

Saída:

```
Original: '  GAIA@Teste.COM  '
Tamanho original: 18
Só com strip: 'GAIA@Teste.COM'
Só com lower: '  gaia@teste.com  '
Normalizado: 'gaia@teste.com'
O original continua sujo? '  GAIA@Teste.COM  '
Comparação sem normalizar: False
Comparação com normalizar: True
Verificação passou: o e-mail normalizado bate com o esperado
Partes: ['gaia', 'teste.com']
Antes do arroba: gaia
Depois do arroba: teste.com
E-mail válido? True
Juntando com join: sem nome, inativo, sem perfil
Verificações passaram
```

### `aulas/aula05/aula05_codigos_status.py`

Pertinência com lista de códigos, que é o jeito legível de validar status. Compare o `assert` com
o que se escreveria sem a lista, `codigo == 200 or codigo == 201 or codigo == 204`: a versão com
lista tem menos lugar para errar e se lê como frase. O `not in` é a mesma coisa ao contrário, para
o cenário negativo. Os dois voltam na Aula 08 como asserção de pytest sem mudar uma vírgula.

```bash
python aulas/aula05/aula05_codigos_status.py
```

Saída:

```
Status recebido: 201
Está entre os de sucesso? True
Está entre os erros de servidor? False
Verificações passaram
```

### `aulas/aula05/aula05_contagem_por_chave.py`

Contagem por chave nas duas formas, e é a técnica que sustenta o desafio final da Aula 15. Sete
resultados possíveis não pedem sete variáveis: o dicionário vira o próprio contador, com a chave
sendo o resultado e o valor sendo a catraca daquele resultado. A forma longa usa `if`/`else`; a
forma curta faz o mesmo em uma linha, com `contagem.get(resultado, 0) + 1`, onde o zero do `get`
é justamente o ponto de partida do contador.

O mnemônico da Aula 04 continua valendo, com dicionário no lugar do número: cria antes, percorre,
muda dentro, usa depois. Se o `contagem = {}` nascer dentro do `for`, a contagem dá 1 em tudo.

```bash
python aulas/aula05/aula05_contagem_por_chave.py
```

Saída:

```
{'passou': 3, 'falhou': 2, 'ignorado': 1}
passou: 3
falhou: 2
ignorado: 1
Verificações da forma longa passaram
{'passou': 3, 'falhou': 2, 'ignorado': 1}
As duas formas deram o mesmo resultado
Verificações da forma curta passaram
```

### `aulas/aula05/aula05_data_em_partes.py`

Trabalho de QA todo dia: a API devolve data num formato, a tela mostra em outro, e alguém precisa
provar que as duas dizem a mesma coisa. O `split` no hífen resolve a separação, e
`len(partes) == 3` verifica que o formato veio como o combinado.

O fim do arquivo mostra a armadilha do zero à esquerda com os dois caminhos na tela:
`str(int("00"))` devolve `'0'`, e `"00".lstrip("0")` devolve texto vazio. Um campo que chega como
"0" desaparece do relatório sem nenhum erro. Os apóstrofos são o que faz o vazio ficar visível.

```bash
python aulas/aula05/aula05_data_em_partes.py
```

Saída:

```
Dia: 06, mês: 08, ano: 2026
Mês sem o zero à esquerda: 8
Formato brasileiro: 06/08/2026
Rótulo do relatório: 06/8/2026
Verificações passaram
Com str(int()): '0'
Com lstrip:     ''
Verificação passou: o lstrip come o zero que era o dado
```

### `aulas/aula05/aula05_validar_usuarios.py`

Segunda demonstração guiada da Aula 05, e o arquivo que junta as três estruturas do curso até
aqui: lista da Aula 04, dicionário e string desta aula, no mesmo lugar. Quatro regras de
validação por usuário, o `", ".join(problemas)` para juntar os problemas numa frase, e a contagem
final num dicionário.

Três coisas na saída merecem leitura, e nenhuma é sobre sintaxe. A Ana tem o e-mail mais sujo da
massa e passa, porque a normalização vem antes da comparação: sem ela, um defeito que não existe
seria aberto, e isso tem nome, é falso positivo. O usuário 3 acumula três problemas numa volta só,
e é para isso que existem quatro `if` independentes em vez de uma escada com `elif`. E está
escrito `if len(problemas) > 0` e não `if problemas`, pela regra da Aula 03 de nunca escrever
condição sem comparação explícita.

```bash
python aulas/aula05/aula05_validar_usuarios.py
```

Saída:

```
Usuário 1: OK
Usuário 2: sem nome
Usuário 3: inativo, sem perfil, e-mail inválido
Usuário 4: OK
Resumo: {'ok': 2, 'com problema': 2}
Verificações passaram
```

### `aulas/aula05/aula05_pedido.json`

Arquivo de apoio da atividade da Aula 05, e o único do repositório que não é Python. Ele é uma
resposta crua, como uma API devolveria, com `true`, `false` e `null` em minúsculo e com o e-mail
do cliente sujo de propósito.

**Ele existe para ser transcrito, não carregado.** A tarefa é passar esse JSON para um dicionário
Python à mão, trocando `true` por `True` e `null` por `None`, que é a demonstração do `NameError`
aplicada em casa. Ler arquivo com biblioteca é assunto de outra aula.

### `aulas/aula06/aula06_regra_repetida.py`

O problema do dia da Aula 06, e ele existe para doer. A regra de frete grátis está escrita três
vezes, uma por cliente, e as três são idênticas palavra por palavra. Se o negócio mudar de 250
para 199, são três lugares para editar, e esquecer um deixa o sistema com duas regras ao mesmo
tempo sem nada quebrar.

**Este é o único arquivo do repositório escrito para não ser copiado.** A versão certa dele é o
`aula06_frete_funcao.py`, logo abaixo.

```bash
python aulas/aula06/aula06_regra_repetida.py
```

Saída:

```
Ana:  R$ 599.70 | frete R$ 0.00
Beto: R$ 49.90 | frete R$ 20.00
Cris: R$ 179.80 | frete R$ 20.00
A regra está escrita 3 vezes neste arquivo
```

### `aulas/aula06/aula06_frete_funcao.py`

O mesmo problema resolvido com uma função. Quinze linhas viraram quatro, e a regra passa a existir
num lugar só: mudar de 250 para 199 é editar uma linha, e os três clientes obedecem.

Os três `assert` do fim são a primeira vez no curso em que três cenários são verificados sem
copiar nenhuma linha de lógica. O terceiro, o de 250 exato, é o único que pega alguém trocando
`>=` por `>`.

```bash
python aulas/aula06/aula06_frete_funcao.py
```

Saída:

```
Frete da Ana:  R$ 0.00
Frete do Beto: R$ 20.00
Frete da Cris: R$ 20.00
As três verificações passaram
```

### `aulas/aula06/aula06_tres_partes.py`

As três partes de uma função, escritas na coluna de comentário e alinhadas com as linhas que
fazem cada uma: `RECEBE` na linha do `def`, `CALCULA` no corpo, `DEVOLVE` no `return`. A sequência
vale para função de um caminho só; validação tem vários, e é o `aula06_retorno_antecipado.py`.

A segunda metade prova a coisa que confunde todo mundo uma vez: **definir não executa.** Existem
duas funções no arquivo, só uma é chamada, e a saída tem duas linhas. A penúltima linha escreve o
nome de uma função sem os parênteses, o que não chama nada e não reclama de nada.

```bash
python aulas/aula06/aula06_tres_partes.py
```

Saída:

```
Frete de 300: R$ 0.00
O arquivo terminou, e a nunca_chamada não imprimiu nada
```

### `aulas/aula06/aula06_valor_padrao.py`

`desconto=0.0` na definição significa "se ninguém passar desconto, use zero". Chamada com dois
argumentos funciona, chamada com três funciona, e o caso comum fica curto sem perder a opção.

Parâmetro com valor padrão aparece em toda biblioteca do curso, e reconhecer a forma vale mais
que decorar a regra.

```bash
python aulas/aula06/aula06_valor_padrao.py
```

Saída:

```
Sem desconto: R$ 300.00
Com desconto: R$ 250.00
A diferença é o 3o argumento: R$ 50.00
As duas verificações passaram
```

### `aulas/aula06/aula06_print_contra_return.py`

O momento pedagógico da Aula 06. Duas funções somam dois mais dois, as duas parecem funcionar, e
só uma devolve o resultado. A que imprime devolve `None`, que é a ausência de valor da Aula 02.

`print` fala em voz alta, `return` entrega um documento. E a consequência para quem testa é o
ponto todo: teste precisa de valor para comparar, então função que só imprime não é testável.

O `TypeError` do fim está em `try/except` para o arquivo rodar até o fim e mostrar o erro e a
correção na mesma execução. **Numa suíte de verdade a falha interrompe**, e engolir exceção é o
oposto de verificar.

```bash
python aulas/aula06/aula06_print_contra_return.py
```

Saída:

```
4
Com print, resultado_print vale: None
Com return, resultado_return vale: 4
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
E com return a mesma conta funciona: 40
As duas verificações passaram
```

### `aulas/aula06/aula06_comando_e_pergunta.py`

As duas famílias de função, com nome. Função-comando faz algo e não devolve nada: registrar
evidência, imprimir relatório, clicar num botão. Função-pergunta devolve uma resposta, e você
guarda o resultado.

O último `assert` é o mais interessante do arquivo: ele verifica que a função-comando devolve
`None`. É a única verificação possível contra ela, e ela não verifica comportamento nenhum. É o
retrato de por que o teste só conversa com função-pergunta.

```bash
python aulas/aula06/aula06_comando_e_pergunta.py
```

Saída:

```
[EVIDÊNCIA] login válido: passou
JL12345! tem 8 ou mais? True
JL1234! tem 8 ou mais?  False
[EVIDÊNCIA] senha errada: passou
O que registrar_evidencia devolve: None
As três verificações passaram
```

### `aulas/aula06/aula06_retorno_antecipado.py`

Chegou no `return`, acabou a função. As três chamadas produzem uma, duas e três linhas de rastro,
e na primeira o e-mail está perfeito e nem foi olhado, porque o `return` da segunda linha encerrou
a função antes.

Os `assert` do fim comparam **variáveis**, e não chamam a função de novo. Isso é de propósito e
vale para toda função que imprime: chamar de novo dentro do `assert` imprimiria o rastro outra vez
e a saída viraria sopa.

```bash
python aulas/aula06/aula06_retorno_antecipado.py
```

Saída:

```
Chamada 1, nome vazio:
  checando o nome...
  devolveu: nome obrigatório
Chamada 2, e-mail sem arroba:
  checando o nome...
  checando o e-mail...
  devolveu: e-mail inválido
Chamada 3, tudo certo:
  checando o nome...
  checando o e-mail...
  tudo checado
  devolveu: ok
As três verificações passaram
```

### `aulas/aula06/aula06_escopo.py`

Um quadrado dentro de outro: o de fora é o programa, o de dentro é a função. Quem está dentro vê
o que está fora; quem está fora não vê o que está dentro, e a única coisa que atravessa a parede é
o que o `return` entrega.

A primeira metade mostra o `NameError` de tentar usar por fora uma variável criada dentro, que não
é bug e sim o escopo funcionando. A segunda mostra a parte que confunde de verdade: duas variáveis
com o mesmo nome, em quadrados diferentes, são coisas diferentes.

A regra prática que decide onde a variável mora: dado usado em mais de um lugar sobe para parâmetro
ou para retorno, e dado usado num lugar só fica dentro da função.

Os dois `try/except` existem para os dois casos caberem na mesma execução. **Numa suíte de verdade
a falha interrompe.**

```bash
python aulas/aula06/aula06_escopo.py
```

Saída:

```
Total: 30.0
NameError: name 'subtotal' is not defined
Dentro da função o valor virou 20, e devolveu 20
Fora da função, valor continua 10
As duas verificações passaram
```

### `aulas/aula06/aula06_funcoes_da_loja.py`

Quatro funções, e nenhuma delas é conteúdo novo. A classificação de severidade foi escrita em
português na Aula 01 e virou `if` na Aula 03. A classificação de status era o `for` da Aula 04. A
geração de e-mail é o `strip` e o `lower` da Aula 05, agora com `replace`. **Nada de novo além da
embalagem, e a embalagem é a função.**

A última linha é uma descoberta que não foi plantada: `lower` põe em minúscula e não tira acento
nenhum, então a função gera `joão.silva@qatest.com`, e e-mail com acento é recusado por boa parte
dos sistemas. Consertar não é assunto da aula; o que é assunto é que o dado que você escolhe para
testar decide o que você encontra.

**Guarde este arquivo.** Ele é o material de trabalho da aula que organiza as verificações com
ferramenta.

```bash
python aulas/aula06/aula06_funcoes_da_loja.py
```

Saída:

```
250 tem frete grátis? True
Severidade:  CRÍTICA
Código 302:  outro
E-mail sujo: gaia.silva@qatest.com
Todas as verificações passaram
Com acento:  joão.silva@qatest.com
```

### `aulas/aula06/aula06_duas_funcoes.py`

O arquivo da primeira demonstração guiada da Aula 06, escrito ao vivo na frente da turma. Duas
funções e quatro `assert`, e o terceiro é o do 250 exato, a fronteira da regra: valor-limite se
escolhe, não se sorteia.

Os dois tropeços mais prováveis ao refazer este arquivo em casa: `print` no lugar de `return`
dentro da função, que faz ela parecer funcionar e devolver `None`, e a chamada escrita sem os
parênteses, que não executa nada e não reclama de nada.

```bash
python aulas/aula06/aula06_duas_funcoes.py
```

Saída:

```
300 tem frete grátis? True
100 tem frete grátis? False
250 tem frete grátis? True
E-mail gerado: gaia.silva@qatest.com
As quatro verificações passaram
```

### `aulas/aula06/aula06_login_while.py`

O `while` entra pelo requisito, e não como teoria: "o sistema deve permitir até três tentativas de
senha, e bloquear o usuário na terceira falha". Tem "até", tem condição de parada, e o acerto pode
vir na primeira tentativa.

A condição tem duas partes ligadas por `and`, que são os operadores lógicos da Aula 03. E a linha
`numero = numero + 1` é a catraca da Aula 04 com trabalho novo: ela é o que garante que a condição
um dia vira falsa, e está antes de qualquer `if`, então roda em toda volta.

**Troque `"JL1234!"` por `"errada3"` na linha da massa e rode de novo** para ver o caminho do
bloqueio. Mesma lógica, massa diferente, resultado diferente, e nenhuma linha de lógica alterada.

O primeiro `assert` não diz `== True`, ele diz a regra: `logou == (senha_correta in tentativas)`.
Esperado vem da regra, obtido vem do programa, e escrito assim ele continua valendo nas duas
massas.

```bash
python aulas/aula06/aula06_login_while.py
```

Saída:

```
Tentativa 1 falhou
Tentativa 2 falhou
Login OK na tentativa 3
Tentativas consumidas: 3
As duas verificações passaram
```

### `aulas/aula06/aula06_tentar_login.py`

O mesmo `while`, agora embalado numa função. O bloco solto não era testável: para ver o caminho do
bloqueio era preciso editar o arquivo e rodar de novo. Aqui os dois cenários são duas linhas.

A condição perdeu metade e a variável `logou` desapareceu, porque o `return` sai do laço **e** da
função de uma vez. E a função devolve o número da tentativa em que logou, não `True`: `True`
responde uma pergunta, o número responde duas.

```bash
python aulas/aula06/aula06_tentar_login.py
```

Saída:

```
Logou na tentativa: 3
Bloqueado, devolveu: 0
As três verificações passaram
```

### `aulas/aula06/aula06_palindromo.py`

Função chamando função. `inverter` é um acumulador de texto, irmão do acumulador de lista da Aula
04: a cada volta ela cola a letra nova na frente do que já tinha. `eh_palindromo` chama `inverter`,
porque é assim que se monta lógica grande a partir de peças pequenas, cada uma testável sozinha.

`eh_palindromo` é função-pergunta que devolve verdadeiro ou falso, e essa é a mais fácil de testar
que existe, porque o esperado só tem dois valores possíveis.

```bash
python aulas/aula06/aula06_palindromo.py
```

Saída:

```
'abc' invertido: cba
'  Arara  ' é palíndromo? True
'teste' é palíndromo? False
A frase inteira: True
As três verificações passaram
```

### `aulas/aula06/aula06_email_valido.py`

A validação de e-mail da Aula 05, que era uma linha comprida perdida no meio de um arquivo, agora
com nome, entrada e saída. E ela ficou melhor: com retorno antecipado, os quatro motivos de recusa
ficam separados, um por `if`, cada um legível sozinho.

Seis cenários, quatro deles negativos, e cada cenário negativo aponta para um `if` específico:
um `assert` que falha diz qual regra quebrou.

Esta função não valida e-mail de verdade, e não é para isso que ela existe. A regra completa de
endereço de e-mail é longa e cheia de exceção, e existe biblioteca para isso. O que ela faz é o
que um teste precisa: recusar as quatro formas de errado que aparecem em massa de teste.

```bash
python aulas/aula06/aula06_email_valido.py
```

Saída:

```
  GAIA@Teste.COM   vale? True
beto@loja.com.br   vale? True
gaia.teste.com     vale? False
@teste.com         vale? False
gaia@teste         vale? False
a@b@c.com          vale? False
As seis verificações passaram
```

### `aulas/aula06/aula06_fechar_pedido.py`

O arquivo da segunda demonstração guiada da Aula 06, e o único do repositório em que uma função
chama outras três. Cada função tem uma responsabilidade só, e `fechar_pedido` não recalcula nada:
ela chama as três anteriores na ordem e junta o resultado.

É por isso que ela obedece a uma mudança de regra sem ser tocada: se o frete mudar, você mexe em
`calcular_frete` e mais nada. Essa é a resposta técnica para a pergunta que abre a aula, dos cem
testes que fazem login numa tela que mudou.

O quarto `assert` vale mais que os outros: cliente VIP com total baixo é o único cenário que testa
a **segunda** metade do `or` de `calcular_frete`. Sem ele, um `or` escrito como `and` passaria os
outros quatro sem reclamar.

E repare no escopo: `subtotal`, `com_desconto` e `frete` aparecem duas vezes no arquivo, uma dentro
de `fechar_pedido` e uma na margem. São variáveis diferentes, em quadrados diferentes.

```bash
python aulas/aula06/aula06_fechar_pedido.py
```

Saída:

```
Subtotal:     R$ 300.00
Com desconto: R$ 270.00
Frete:        R$ 0.00
Total final:  R$ 270.00
Todas as verificações passaram
```

### `aulas/aula06/aula06_senha_valida.py`

O extra de casa da Aula 06. Três coisas juntas, e as três já apareceram no curso: retorno
antecipado no primeiro `if`, duas variáveis de bandeira que começam falsas e podem virar
verdadeiras dentro do laço, e um `and` no `return` para exigir as duas.

A senha `JL1234!`, que atravessou o curso inteiro, é recusada, porque tem sete caracteres. Testar
a regra na fronteira encontrou isso em dois segundos.

```bash
python aulas/aula06/aula06_senha_valida.py
```

Saída:

```
Senha123 vale? True
JL1234!  vale? False  (7 caracteres)
jl123456 vale? False  (sem maiúscula)
JLABCDEF vale? False  (sem número)
As quatro verificações passaram
```

### `aulas/aula07/aula07_relatorio.py`

O arquivo que abre a Aula 07, com o terminal vermelho. As três funções vêm de
`aulas/aula06/aula06_duas_funcoes.py`, com a mesma embalagem de função-pergunta que recebe,
calcula e devolve. O acréscimo desta aula é a massa: o segundo item da lista tem total zero.

**Regra de negócio:** a taxa de aprovação é a quantidade de casos que passaram dividida pelo total
de casos, em porcentagem. A regra escrita não diz o que fazer quando o total é zero, e é
exatamente aí que o programa quebra.

**Três arquivos da Aula 07 saem com exit code 1 de propósito**, e esta é a única pasta do
repositório em que isso acontece. Nas outras aulas todo arquivo roda do início ao fim, e erro
proposital vai dentro de `try/except`. Aqui a parada é o conteúdo, e não existe saída nenhuma
depois dela para alguém perder:

| Arquivo | Exit code | Por quê |
|---|--:|---|
| `aulas/aula07/aula07_relatorio.py` | 1 | o traceback é a última coisa da tela, e é a aula inteira |
| `aulas/aula07/aula07_usa_pedidos.py` | 1 | o ponto é que o programa **parou**; embrulhar em `try/except` apagaria isso |
| `aulas/aula07/aula07_defeitos_pos_aula.py` | 1 | é a atividade, e ela chega quebrada na sua mão de propósito |

Os outros doze arquivos da pasta saem 0.

Leia o traceback de baixo para cima: a última linha diz **o que**, o andar de baixo diz **onde**, e
os andares acima dizem **quem chamou**. O til embaixo da expressão marca os operandos e o
circunflexo marca a operação, então o Python literalmente aponta o dedo na barra da divisão.

Repare também no exit code que a janela Run mostra no fim. Zero é acabou bem, qualquer outro número
é acabou mal, e é esse número que uma esteira de testes lê para decidir se o build passa.

```bash
python aulas/aula07/aula07_relatorio.py
```

Saída, com o caminho encurtado para `...`:

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

### `aulas/aula07/aula07_erros_de_sintaxe.py`

Os três erros de sintaxe que toda turma comete: dois-pontos esquecido, aspas não fechadas, e
tabulação misturada com espaço. Os três moram comentados no arquivo, com a mensagem exata que o
Python devolveu ao lado de cada um, e a versão correta rodando embaixo.

Eles têm que ficar comentados: erro de sintaxe não deixa o arquivo nem abrir, então um deles solto
derrubaria os outros dois. Para treinar, descomente uma linha por vez, rode, leia a mensagem, e
comente de novo.

O terceiro é o mais confuso, porque na tela o código parece perfeitamente alinhado: a linha do
`return` foi recuada com tabulação e as outras com espaço. O olho não vê a diferença e o Python vê.
A solução que resolve para sempre é configurar o editor para converter tabulação em quatro espaços.

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

### `aulas/aula07/aula07_nome_errado.py`

O bônus de trinta segundos que economiza minutos: as versões recentes do Python sugerem a correção
quando você erra um nome de variável.

O arquivo mostra uma diferença que decide qual função usar quando você captura um erro.
`traceback.print_exc()` imprime a mensagem inteira, com o `Did you mean` incluído, igual ao que o
Python mostra quando ninguém captura. Já `str(erro)` e `traceback.format_exception_only()` **perdem
a sugestão**, e a sugestão é justamente o que resolve o problema.

A moral prática vale para o resto do curso: quando pedir ajuda, cole a última linha inteira do
traceback, e não um resumo dela.

```bash
python aulas/aula07/aula07_nome_errado.py
```

Saída, com o caminho encurtado para `...`:

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

### `aulas/aula07/aula07_q1_indice.py`

O primeiro dos quatro arquivos quebrados. Os quatro seguem a mesma forma e servem ao mesmo
exercício: rode um por vez e, para cada um, escreva três coisas. O tipo do erro, que é a última
linha; a linha onde estourou; e uma frase sua dizendo a causa. **Não conserte nenhum.** O exercício
é ler.

Nos quatro o erro vai dentro de `try/except` com `traceback.print_exc()`, para o arquivo seguir até
o fim e mostrar a explicação depois do traceback real. Isso é recurso de demonstração e **não é
padrão para copiar**: numa verificação de verdade a falha interrompe. Os quatro saem com exit code
0 por causa disso.

Dois dos quatro trazem a resposta escrita na própria mensagem, e é o achado mais barato da aula: o
de atributo diz `Did you mean: 'strip'?`, e o de índice diz `list index out of range`, que já nomeia
o problema. Quem lê a linha inteira resolve os dois sem sair do terminal.

| Arquivo | Tipo e mensagem | Linha |
|---|---|--:|
| `aula07_q1_indice.py` | `IndexError: list index out of range` | 23 |
| `aula07_q2_tipo.py` | `TypeError: can't multiply sequence by non-int of type 'float'` | 22 |
| `aula07_q3_atributo.py` | `AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?` | 19 |
| `aula07_q4_chave.py` | `KeyError: 'ignorado'` | 20 |

**Regra de negócio:** a suíte tem três casos de teste cadastrados, e o relatório imprime um deles
pela posição na lista.

A lista tem três itens, nas posições 0, 1 e 2, e o código pede a posição 3.

```bash
python aulas/aula07/aula07_q1_indice.py
```

Saída, com o caminho encurtado para `...`:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q1_indice.py", line 23, in <module>
    print(f"Quarto caso: {casos[3]}")
                          ~~~~~^^^
IndexError: list index out of range

A lista tem três itens, nas posições 0, 1 e 2.
```

### `aulas/aula07/aula07_q2_tipo.py`

O segundo dos quatro quebrados.

**Regra de negócio:** o total do pedido é o preço do produto vezes a quantidade, mais dez reais de
frete. A quantidade chega do formulário como texto.

É o mais interessante dos quatro: a mensagem fala de `sequence` e de `non-int` e nunca diz a palavra
texto. Mesmo assim, a linha apontada tem uma multiplicação e duas variáveis, e olhar o tipo de cada
uma resolve. Mensagem confusa não é motivo para desistir da mensagem.

```bash
python aulas/aula07/aula07_q2_tipo.py
```

Saída, com o caminho encurtado para `...`:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q2_tipo.py", line 22, in <module>
    print(f"Total: {preco * quantidade + 10}")
                    ~~~~~~^~~~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'float'

O tipo de quantidade é <class 'str'>, e não número.
Com int(quantidade), sai: 609.7
```

### `aulas/aula07/aula07_q3_atributo.py`

O terceiro dos quatro quebrados.

**Regra de negócio:** e-mail cadastrado é comparado sem espaço nas pontas e todo em minúscula,
porque quem digita não é consistente e o sistema precisa ser.

O e-mail sujo com espaço nas pontas é o mesmo de `aulas/aula05/aula05_email_sujo.py`; o acréscimo é
o método errado. Quem vem de outra linguagem escreve `trim()`, e em Python o nome é `strip()`.

```bash
python aulas/aula07/aula07_q3_atributo.py
```

Saída, com o caminho encurtado para `...`:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q3_atributo.py", line 19, in <module>
    print(email.trim().lower())
          ^^^^^^^^^^
AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?

Com strip(), sai: gaia@teste.com
```

### `aulas/aula07/aula07_q4_chave.py`

O quarto dos quatro quebrados.

**Regra de negócio:** o relatório de execução mostra quantos casos passaram, quantos falharam e
quantos foram ignorados. Ignorado é campo opcional: pode não vir.

É a Aula 05 cobrando o `.get()`: com `resultados.get("ignorado", 0)` o programa devolveria zero em
vez de quebrar. A escolha entre quebrar e devolver zero é sua, e depende de o campo ser obrigatório
ou opcional.

```bash
python aulas/aula07/aula07_q4_chave.py
```

Saída, com o caminho encurtado para `...`:

```
Traceback (most recent call last):
  File "...\aulas\aula07\aula07_q4_chave.py", line 20, in <module>
    print(f"Ignorados: {resultados['ignorado']}")
                        ~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'ignorado'

Com .get('ignorado', 0), sai: 0
```

### `aulas/aula07/aula07_try_except_massa.py`

O `try/except` de tipo específico, no uso de verdade.

**Regra de negócio:** a idade vem do arquivo de massa como texto e precisa virar número. Linha fora
do formato é recusada e registrada, e não derruba a execução das outras.

Três partes. A primeira mostra a forma com uma entrada só. A segunda roda a massa inteira, quatro
entradas fixas e desenhadas à mão, duas boas e duas ruins, com a última sendo a string vazia, que é
o caso que ninguém lembra de testar. O `as erro` guarda o erro numa variável, e a mensagem original
do Python vira parte do relatório em vez de derrubar a execução.

A terceira parte mostra que vários `except` embaixo do mesmo `try` são uma escada, e a escada da
Aula 03 vale igual: **desce, testa o tipo, e para no primeiro que casa.** Se o erro for de valor, o
`except` de chave nem é olhado. É o mesmo mecanismo em roupa nova, e não conteúdo novo.

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

### `aulas/aula07/aula07_except_pelado.py`

O antipadrão proibido no curso, rodando, com as três versões lado a lado.

**Regra de negócio:** a soma dos valores da massa tem que incluir todos os valores. Valor fora do
formato é recusado com o motivo na tela, nunca descartado em silêncio.

`except` sem tipo captura qualquer erro que apareça ali dentro e manda tudo para o `pass`, que é
nada. A consequência que interessa a um QA: uma verificação assim passa mesmo quando o produto está
quebrado. Ela não valida, ela silencia, e isso tem nome: **falso-verde**. É o pior resultado
possível numa esteira de testes, pior que vermelho, porque vermelho você investiga e verde você
confia.

A sequência das três versões é o raciocínio inteiro. Com `except:` pelado a soma sai 40,00 e nenhum
aviso. Com `except ValueError as erro` a soma continua 40,00, e agora o motivo aparece na tela: **o
`except` com tipo não consertou nada, ele mostrou o que consertar.** A terceira versão troca a
vírgula por ponto na massa e a soma fecha em 60,00, que é o esperado que veio da regra. O conserto
era do dado, e sem a mensagem ninguém sabia disso.

A regra do curso, dita como regra: capture o erro específico que você espera. Se você não sabe qual
erro esperar, você ainda não entendeu o que está testando, e o `except` genérico está escondendo
essa lacuna de você.

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

### `aulas/aula07/aula07_pedidos.py`

A função que levanta o erro de propósito.

**Regra de negócio:** item só é registrado com nome preenchido e quantidade positiva; cada recusa
diz qual das duas regras foi violada. O frete é grátis a partir de 250,00.

Vocabulário novo, e é o giro conceitual da aula: em programação se diz que a função **levanta** um
erro. A palavra em inglês é `raise`, que é levantar, e ela não sofre o erro, ela o levanta com a mão
dela para avisar quem chamou que aquilo não vai dar.

E o reenquadramento que vem com isso: **nem todo erro é problema.** Quando a regra de negócio manda
rejeitar, o erro é o comportamento esperado, e quem verifica precisa provar que ele aconteceu. Se o
sistema aceitar quantidade negativa em silêncio, aí sim você tem um defeito. O sistema recusar é o
acerto.

Repare que a mensagem é sua, escrita em português, dizendo qual regra foi violada. Quem receber esse
erro sabe o que fazer. E o `nome.strip() == ""` é a Aula 05 pagando dividendo: campo com três
espaços é campo vazio para o usuário e campo preenchido para o código.

O `calcular_frete` vem de `aulas/aula06/aula06_frete_funcao.py`, com o mesmo corte de 250,00. O
acréscimo desta aula é o contraste: ele não valida nada e nunca levanta erro, e é essa
característica que o `aulas/aula07/aula07_verifica_pedidos.py` usa para produzir a falha ao
contrário. Na Aula 08 este mesmo arquivo volta como `aulas/aula08/aula08_pedidos.py`, copiado sem
alteração nenhuma, e o que muda é quem verifica.

```bash
python aulas/aula07/aula07_pedidos.py
```

Saída: nenhuma, e exit code 0. O arquivo é só de funções, e quem usa ele são os dois arquivos
seguintes.

### `aulas/aula07/aula07_usa_pedidos.py`

Tempo 1 da prova de recusa: deixe estourar. **Sai com exit code 1 de propósito.**

**Regra de negócio:** a mesma do `aulas/aula07/aula07_pedidos.py`. Aqui ela é chamada com quantidade
zero de propósito.

O programa está certo: ele recusou o que devia recusar. O problema é que ele **parou**, e um
programa que morre no meio não diz se o comportamento foi o esperado, e nem deixa o resto rodar.

Repare numa coisa que este traceback tem e o do `aulas/aula07/aula07_relatorio.py` não tinha: **ele
atravessa dois arquivos.** O andar de baixo é onde o `raise` está, e o de cima é a linha que chamou.
Aqui os dois são seus. Num projeto de verdade o de baixo costuma ser de uma biblioteca, e o que você
conserta é o de cima.

```bash
python aulas/aula07/aula07_usa_pedidos.py
```

Saída, com o caminho encurtado para `...`:

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

### `aulas/aula07/aula07_verifica_pedidos.py`

Tempo 2 da prova de recusa, e o ponto em que o conceito da aula fecha.

**Regra de negócio:** a função tem que recusar quantidade zero e nome em branco, cada um com a sua
mensagem. E o cálculo de frete não recusa nada: ele sempre devolve um valor.

Nenhuma peça aqui é conteúdo novo além do `try/except`. A variável de estado é a mesma `logou` de
`aulas/aula06/aula06_login_while.py`, com trabalho novo, porque lá ela dizia se o login aconteceu e
aqui ela diz se o erro aconteceu. O `assert` é da Aula 04, com a mensagem depois da vírgula. E o
`in` é da Aula 05, agora procurando um pedaço de texto dentro da mensagem do erro em vez de uma
chave dentro do dicionário.

A frase que fixa o mecanismo, e vale ler devagar: **aqui o erro acontecendo é aprovação, e o erro
não acontecendo é reprovação.** É a inversão da lógica de sempre. Se o `raise` vier, o `except`
roda, `levantou` vira `True` e o `assert` passa. Se a função aceitasse quantidade zero, o `except`
nunca rodaria, `levantou` continuaria `False`, e o `assert` reprovaria.

O terceiro caso confere o nome em branco, e existe para mostrar por que conferir a mensagem não é
preciosismo: a função tem dois `raise ValueError`, e sem o `in` na mensagem o caso de quantidade
passaria se ela recusasse pelo motivo errado.

O fim do arquivo é a falha ao contrário, apontada para uma função que nunca levanta erro. É a única
falha do curso em que o problema é a **ausência** de erro. Ela vai dentro de `try/except
AssertionError` com `print_exc()` para o arquivo mostrar as três verificações que passaram e a que
reprovou na mesma execução, e por isso ele sai com exit code 0. O aviso é o antipadrão da aula com
outra roupa: numa verificação de verdade a falha interrompe, e engolir asserção é o oposto de
verificar.

São nove linhas para provar uma recusa. Em `aulas/aula08/test_aula08_recusa.py` elas viram uma.

```bash
python aulas/aula07/aula07_verifica_pedidos.py
```

Saída, com o caminho encurtado para `...`:

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

### `aulas/aula07/aula07_relatorio_bugado.py`

Três defeitos plantados, e nenhum deles quebra o programa. Ele roda, não tem traceback, não tem
vermelho, não tem aviso, e os três números impressos estão errados. É o coração da aula.

**Regra de negócio, três delas:** a média de aprovação é a proporção de casos que passaram; o
desconto precisa de aprovação gerencial quando **passa** de 50%; e a soma dos valores inclui todos
os valores da massa.

O trabalho é achar os três e, para cada um, escrever **hipótese** (o que você acha antes de testar),
**evidência** (o que você fez para confirmar) e **causa raiz** (a linha e o motivo). Comece pelo
primeiro número impresso e pergunte se ele faz sentido: duas notas de "passou" em três deveriam dar
66,7%.

Repare no exit code da execução, porque ele é o falso-verde subindo um nível: os três números estão
errados e o programa diz que acabou bem. Não é uma linha que mente, é o programa inteiro.

Não abra o `aulas/aula07/aula07_relatorio_corrigido.py` antes de tentar. O exercício é a
investigação, não a resposta.

```bash
python aulas/aula07/aula07_relatorio_bugado.py
```

Saída, e ela sai com exit code 0:

```
Aprovacao: 0.0%
Desconto de 50 por cento precisa de aprovacao? True
Soma: 40.0
```

### `aulas/aula07/aula07_relatorio_corrigido.py`

Os três defeitos do arquivo acima, corrigidos. É o mesmo código, com três caracteres de diferença e
um `except` que ganhou tipo. Cada correção vem com o comentário do que estava errado e de como o
defeito se manifestava, porque a lição é a investigação e não a linha certa.

**Regra de negócio:** as mesmas três do `aulas/aula07/aula07_relatorio_bugado.py`, agora com um
`assert` por regra. É ele que compara o esperado, que vem da regra, com o obtido, que vem do
programa.

O **primeiro defeito** era `aprovados + 1` sem o igual: a linha calculava um valor e jogava no lixo,
porque ninguém guardou o resultado. Para o Python isso é uma expressão perfeitamente legal, então
nenhuma mensagem avisa. É o processo `CRIA ANTES → PERCORRE → MUDA DENTRO → USA DEPOIS` da Aula 04
com a etapa do meio quebrada.

O **segundo** é de fronteira. A regra escrita diz que precisa de aprovação quando o desconto passa
de 50%, e o código dizia `>= 50`, que inclui o 50. Um caractere de diferença, e ele só aparece se
alguém testar exatamente 50. Guarde a sensação: na Aula 09 ela ganha nome e vira técnica.

O **terceiro** era o `except` pelado, e a correção dele mostra uma coisa que vale mais que o
conserto: dar tipo ao `except` não corrigiu a soma, corrigiu a **cegueira**. O valor com vírgula
continua sendo recusado; a diferença é que agora ele aparece na tela, e aí dá para consertar o dado.

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

### `aulas/aula07/aula07_defeitos_pos_aula.py`

A atividade pós-aula da Aula 07. **Prazo: 08/09/2026, às 23h59.**

Cinco defeitos plantados, e eles não são do mesmo tipo: **dois de execução**, que param o programa e
o Python te diz onde, e **três de lógica**, que deixam o programa rodar até o fim e imprimir número
errado.

Os dois de execução você acha rodando. Os três de lógica só aparecem se você declarar o resultado
esperado antes de rodar, e é esse o exercício de verdade.

**Regra de negócio:** as quatro regras estão escritas por extenso no cabeçalho do arquivo, em
português, e é de lá que sai o resultado esperado de cada número. Leia as quatro, calcule os quatro
números de cabeça, e só então rode. Quem rodar primeiro vai achar os dois de execução e parar,
achando que acabou.

Para cada um dos cinco, registre três linhas: **sintoma** (o que você viu), **causa** (a linha e o
motivo) e **correção** (o que você escreveu no lugar). Entregue o arquivo corrigido e o registro dos
cinco, mesmo que você não tenha achado todos. Vale mais registrar quatro bem que listar cinco no
chute.

Este arquivo chega quebrado de propósito e **sai com exit code 1 na primeira execução**. O trabalho
é fazer ele sair 0 com os quatro números certos.

```bash
python aulas/aula07/aula07_defeitos_pos_aula.py
```

Saída na primeira execução, antes de você consertar nada, com o caminho encurtado para `...`:

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

### `aulas/aula08/aula08_regras.py`

O produto da Aula 08, e a primeira separação do curso: um arquivo com a regra, outro com a
verificação da regra. Até aqui as duas moravam juntas, e o `assert` ficava colado no fim do mesmo
arquivo, como em `aulas/aula06/aula06_funcoes_da_loja.py`.

**Regra de negócio:** cadastro é liberado a partir de 18 anos, e 18 entra. Só admin e gerente têm
permissão de administração; qualquer outro perfil não tem.

Duas funções-pergunta, e as duas devolvem booleano. `idade >= 18` já é `True` ou `False` antes de o
`return` tocar nele, então quem escreve `if idade >= 18: return True` está fazendo a mesma coisa em
três linhas. O `in` da segunda função é o da Aula 05, agora procurando texto numa lista de dois
itens.

O nome do arquivo não começa com `test_`, e isso é de propósito: se começasse, o pytest examinaria
o arquivo durante a descoberta. As funções ainda não seriam testes, porque seus nomes não começam
com `test_`, mas produto e teste ficariam misturados.

```bash
python aulas/aula08/aula08_regras.py
```

Saída: nenhuma, e exit code 0. O arquivo é só de funções, e quem usa ele são os testes ao lado.

### `aulas/aula08/test_aula08_regras.py`

O primeiro arquivo de teste do curso, e os quatro primeiros verdes. Duas convenções, e são as duas
únicas coisas que o pytest exige para encontrar um teste: o **arquivo** começa com `test_` e a
**função** começa com `test_`. Fora delas o pytest não reclama, não dá erro, e diz
`collected 0 items`.

O `assert` é o de `aulas/aula04/aula04_contagem_assert.py`, sem uma vírgula de diferença. O
acréscimo desta aula é a casa dele: ele saiu do fim de um script solto e entrou numa função com
nome, que uma ferramenta encontra e roda. Nenhum teste daqui imprime nada, porque teste que passa é
silencioso e quem fala é o relatório do pytest.

O primeiro teste traz `# Preparação`, `# Ação` e `# Validação` em linhas separadas, para nomear o
padrão. Os outros três fazem as três coisas de uma vez, numa linha, que é como a maioria dos testes
fica no dia a dia.

**Os comandos de teste desta aula rodam de dentro de `aulas/aula08`, e sempre nomeando o arquivo.**
Nunca rode `pytest -s -v` sozinho dentro dessa pasta: sem o nome do arquivo o pytest coleta os oito
arquivos de teste de uma vez, dá 22 testes com 7 falhas, e o relatório vira um muro. Seis dos oito
arquivos falham de propósito, e um por vez é o modo da aula.

```bash
cd aulas/aula08
pytest test_aula08_regras.py -s -v
```

Saída, com os caminhos encurtados:

```
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0 -- ...\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: ...\qa-logica-programacao-testes
configfile: pytest.ini
plugins: base-url-2.1.0, playwright-0.8.0
collecting ... collected 4 items

test_aula08_regras.py::test_maior_de_idade_e_valido PASSED
test_aula08_regras.py::test_menor_de_idade_e_invalido PASSED
test_aula08_regras.py::test_admin_tem_permissao PASSED
test_aula08_regras.py::test_visitante_nao_tem_permissao PASSED

============================== 4 passed in 0.02s ==============================
```

Da raiz do repositório o mesmo teste roda com o caminho completo,
`pytest aulas/aula08/test_aula08_regras.py -s -v`, e o relatório sai igual com o caminho na frente
de cada nome. Nas seções abaixo o cabeçalho do pytest fica de fora da saída, porque ele repete.

### `aulas/aula08/test_aula08_escada.py`

A escada de asserções, quatro degraus dentro de um teste só. Nenhum degrau é conteúdo novo: a
igualdade é da Aula 04, o `isinstance` é o `type()` de `aulas/aula02/aula02_tipos_e_nomes.py` com
outro nome, e os dois últimos são o `in` e o `not in` de `aulas/aula05/aula05_codigos_status.py`,
onde eles conferiam se um código HTTP estava na lista de sucesso. O acréscimo é a casa: os quatro
moram dentro de uma função de teste, e uma ferramenta encontra e roda os quatro.

O `isinstance` confere o tipo e não o valor, e essa distinção pega gente: `isinstance(False, bool)`
também é `True`. E cuidado com a ordem das palavras no quarto degrau: é `not in`, junto, e não
`not "visitante" in [...]`. As duas funcionam e a segunda é ilegível.

A lista completa do que se pode asseverar é para consultar. Estes quatro são para guardar, e o
primeiro resolve a maioria dos casos que você vai escrever.

```bash
pytest test_aula08_escada.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 1 item

test_aula08_escada.py::test_escada_de_assercoes PASSED

============================== 1 passed in 0.03s ==============================
```

### `aulas/aula08/test_aula08_atomico.py`

O teste que faz três coisas, e por que ele não serve. **Sai com exit code 1 de propósito**, e a
falha é o conteúdo: ela não tem conserto e existe para mostrar duas coisas de uma vez.

A primeira: o pytest **para no primeiro `assert` que falha**, e os seguintes daquela função não
rodam. O terceiro `assert` deste arquivo também está errado e não aparece em lugar nenhum do
relatório. Em casa isso vira a sensação de ter criado defeito novo depois de consertar o primeiro.
Você não criou, só chegou no segundo.

A segunda: teste que valida três coisas não diz qual delas quebrou. Você lê o relatório, vê um nome
vermelho, e ainda precisa abrir o código para descobrir. A versão certa é uma função por
comportamento, como no `test_aula08_regras.py`, em que o nome do teste já é o diagnóstico.

A regra, e ela cabe em quatro palavras: **prepara, age, valida, acabou.** Se você precisa agir de
novo, é outro teste.

```bash
pytest test_aula08_atomico.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 1 item

test_aula08_atomico.py::test_tres_validacoes_no_mesmo_teste FAILED

================================== FAILURES ===================================
_____________________ test_tres_validacoes_no_mesmo_teste _____________________

    def test_tres_validacoes_no_mesmo_teste():
        assert validar_idade_minima(20) == True
>       assert tem_permissao("visitante") == True
E       AssertionError: assert False == True
E        +  where False = tem_permissao('visitante')

test_aula08_atomico.py:27: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_atomico.py::test_tres_validacoes_no_mesmo_teste - Assertio...
============================== 1 failed in 0.07s ==============================
```

### `aulas/aula08/aula08_regras_quebradas.py`

O `aula08_regras.py` com uma diferença: o 18 virou 21 na linha da idade. O resto é igual palavra por
palavra.

A troca não foi sabotagem. Alguém achou que estava melhorando a regra, salvou, e não rodou nada. É
assim que regressão entra em produção, e é esse o argumento de existir teste: ele é o ponto de
controle que avisa que o contrato mudou, mesmo quando ninguém teve má intenção.

**Regra de negócio:** a regra escrita continua a mesma, cadastro liberado a partir de 18 anos. O
código é que passou a dizer 21, e nenhuma mensagem de erro avisa isso.

Em aula o professor faz a troca ao vivo no `aula08_regras.py` e desfaz com Ctrl+Z. Este arquivo
existe para você repetir a demonstração em casa sem precisar estragar o original.

```bash
python aulas/aula08/aula08_regras_quebradas.py
```

Saída: nenhuma, e exit code 0. Quem acusa a troca é o teste da próxima seção.

### `aulas/aula08/test_aula08_regressao.py`

Os quatro testes do `test_aula08_regras.py`, copiados sem mudar uma vírgula, apontados para o módulo
estragado. A única diferença é a linha do `import`. **Sai com exit code 1 de propósito**, e é a
primeira leitura de relatório de falha do curso.

Antes de rodar, responda: quantos dos quatro ficam vermelhos? A resposta não é quatro, e o motivo de
não ser quatro é o conteúdo. `validar_idade_minima(16)` continua devolvendo `False` com 21 no lugar
de 18, e as duas verificações de perfil nem tocam na linha alterada. Um teste que passa não prova
que o código está certo; ele prova que **aquele caso** está certo.

Cinco informações saem de um comando só: o nome do teste que falhou, o corpo dele reimpresso, a seta
apontando o `assert` exato, o `E` com o obtido e o esperado lado a lado, e a última linha com
arquivo, linha e tipo do erro.

```bash
pytest test_aula08_regressao.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 4 items

test_aula08_regressao.py::test_maior_de_idade_e_valido FAILED
test_aula08_regressao.py::test_menor_de_idade_e_invalido PASSED
test_aula08_regressao.py::test_admin_tem_permissao PASSED
test_aula08_regressao.py::test_visitante_nao_tem_permissao PASSED

================================== FAILURES ===================================
________________________ test_maior_de_idade_e_valido _________________________

    def test_maior_de_idade_e_valido():
        # Preparação
        idade = 20
        # Ação
        resultado = validar_idade_minima(idade)
        # Validação
>       assert resultado == True
E       assert False == True

test_aula08_regressao.py:31: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_regressao.py::test_maior_de_idade_e_valido - assert False ...
========================= 1 failed, 3 passed in 0.08s =========================
```

### `aulas/aula08/aula08_desconto.py`

A regra de desconto de `aulas/aula03/aula03_desconto.py`, a mesma escada que a turma escreveu na
Aula 03, agora embalada em função com `return` e testável de fora.

**Regra de negócio:** cliente VIP acima de 200 tem 20% de desconto e VIP até 200 tem 10%. Cupom
válido dá 5%, e quem não é VIP nem tem cupom não ganha desconto nenhum.

Os 20 do primeiro degrau não são defeito plantado: 20 é o que a regra do curso sempre disse. Quem
erra é o **teste** da próxima seção, que cobra 25, e é essa diferença que produz o vermelho da
demonstração.

```bash
python aulas/aula08/aula08_desconto.py
```

Saída: nenhuma, e exit code 0.

### `aulas/aula08/test_aula08_desconto.py`

O mesmo teste escrito de dois jeitos, e o relatório de cada um. **Sai com exit code 1 de propósito:**
os dois testes falham, e falham pelo mesmo motivo, porque esperam 25 e a função devolve 20. A
diferença está inteira no que o relatório consegue contar sobre a falha.

O comando leva a opção `-l`, que lista as variáveis locais no momento da falha. No primeiro teste o
pytest imprime o conteúdo de cada variável com o nome que você deu, e você lê o relatório sabendo
qual era a entrada, qual era a expectativa e o que veio. No segundo sai `assert 20 == 25` e nada
mais, porque não existe variável nenhuma para listar.

Os dois dizem **que** falhou. Só o primeiro diz **por que**, e custa três linhas. A regra prática: dê
nome ao dado de entrada, ao esperado e ao obtido. Quem vai ler isso na esteira de integração às onze
da noite não vai abrir o seu código.

```bash
pytest test_aula08_desconto.py -l
```

Saída, sem o cabeçalho do pytest:

```
collected 2 items

test_aula08_desconto.py FF                                               [100%]

================================== FAILURES ===================================
________________________ test_desconto_de_cliente_vip _________________________

    def test_desconto_de_cliente_vip():
        valor_compra = 300.00
        desconto_esperado = 25
        desconto_obtido = calcular_desconto(valor_compra, cliente_vip=True)
>       assert desconto_obtido == desconto_esperado
E       assert 20 == 25

desconto_esperado = 25
desconto_obtido = 20
valor_compra = 300.0

test_aula08_desconto.py:31: AssertionError
_________________ test_desconto_de_cliente_vip_sem_variaveis __________________

    def test_desconto_de_cliente_vip_sem_variaveis():
>       assert calcular_desconto(300.00, True) == 25
E       assert 20 == 25
E        +  where 20 = calcular_desconto(300.0, True)


test_aula08_desconto.py:35: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_desconto.py::test_desconto_de_cliente_vip - assert 20 == 25
FAILED test_aula08_desconto.py::test_desconto_de_cliente_vip_sem_variaveis - ...
============================== 2 failed in 0.06s ==============================
```

### `aulas/aula08/aula08_loja.py`

As três funções da loja, como elas chegaram para testar, e uma delas chegou com defeito.

**Regra de negócio:** o total é valor vezes quantidade, menos o desconto em reais. O frete é grátis
**a partir** de 250,00, e 250,00 exato tem frete grátis.

**Atenção ao `tem_frete_gratis`.** Ele não é a versão que a turma escreveu: em
`aulas/aula06/aula06_funcoes_da_loja.py` a comparação é `>= 250.00`, e está certa lá. Aqui ela é
`> 250.00`. O defeito não se anuncia, e é esse o ponto: o arquivo roda, não dá erro nenhum, e a
função devolve `False` para exatamente 250,00. Quem escrever o teste a partir da **regra escrita**
encontra o defeito; quem escrever o teste olhando o código escreve um teste que concorda com o erro.

O `calcular_total` é o total de `aulas/aula02/aula02.py` com desconto opcional, e o
`aplicar_desconto` é a conta de percentual de `aulas/aula03/aula03_desconto.py`. O acréscimo dos
dois é a embalagem em função, que é a Aula 06.

```bash
python aulas/aula08/aula08_loja.py
```

Saída: nenhuma, e exit code 0.

### `aulas/aula08/test_aula08_loja.py`

A suíte da loja, seis testes, e **exit code 1 de propósito**: cinco passam e o que falha achou um
defeito de verdade no produto.

Os seis saíram da regra escrita, e não do código. É por isso que o `test_frete_gratis_no_limite`
existe: a regra diz "frete grátis a partir de 250,00", então 250,00 exato tem que ter frete grátis.
Os outros dois testes de frete, o de 300 e o de 100, passam com `>` e passariam com `>=`, e não
distinguem as duas versões. O do limite distingue, e o cliente que gasta exatamente duzentos e
cinquenta reais paga frete e liga para o suporte.

Aplique a heurística do dia no vermelho que sai daqui: o erro é `AssertionError`, então a comparação
chegou ao fim e o resultado veio diferente. Agora volte à regra escrita. Ela inclui o 250, e o
produto exclui. Neste caso, o produto está errado: a correção é trocar `>` por `>=`, e é uma tecla.

O último teste fecha uma conta aberta na Aula 02. Um desconto de 10% sobre 99,90 dá 89,91 na sua
cabeça e 89.91000000000001 em ponto flutuante. O `pytest.approx` compara com tolerância, e é a
resposta que ficou prometida seis aulas atrás.

Por que 250 e não 249 nem 251? A pergunta tem nome técnico e é a Aula 09.

```bash
pytest test_aula08_loja.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 6 items

test_aula08_loja.py::test_total_sem_desconto PASSED
test_aula08_loja.py::test_total_com_desconto PASSED
test_aula08_loja.py::test_frete_gratis_acima_de_250 PASSED
test_aula08_loja.py::test_sem_frete_gratis_abaixo_de_250 PASSED
test_aula08_loja.py::test_frete_gratis_no_limite FAILED
test_aula08_loja.py::test_desconto_aplicado_com_centavos PASSED

================================== FAILURES ===================================
_________________________ test_frete_gratis_no_limite _________________________

    def test_frete_gratis_no_limite():
        total_no_limite = 250.00
>       assert tem_frete_gratis(total_no_limite) == True
E       assert False == True
E        +  where False = tem_frete_gratis(250.0)

test_aula08_loja.py:49: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_loja.py::test_frete_gratis_no_limite - assert False == True
========================= 1 failed, 5 passed in 0.06s =========================
```

### `aulas/aula08/test_aula08_tipo_do_erro.py`

O outro lado do vermelho: quando o defeito é do seu teste. **Exit code 1 de propósito**, e este
vermelho não acusa o produto.

A heurística, e ela é para guardar:

| Tipo do erro no relatório | O que aconteceu | Por onde começar |
|---|---|---|
| `AssertionError` | a comparação chegou ao fim e obtido e esperado diferem | volte à **regra escrita** e compare produto, entrada e expectativa |
| `TypeError`, `IndexError`, `KeyError`, `NameError`, `AttributeError` | a execução quebrou antes da validação | confira a **entrada do teste** e o contrato da função |

Aqui a quantidade foi passada como `"3"`, entre aspas, e o teste nunca chegou no `assert`. Leia a
mensagem com atenção, porque ela é mais interessante do que parece: a multiplicação não reclamou de
nada, já que `100 * "3"` em Python repete o texto três vezes e devolve `"333"`. Quem estourou foi a
subtração do desconto, e é por isso que a última linha diz
`unsupported operand type(s) for -: 'str' and 'float'`.

Repare também em qual arquivo o pytest aponta no fim: `aula08_loja.py`, que é o produto. O erro
estourou lá dentro, mas quem entregou o dado errado foi o teste, e é o teste que se conserta. Abrir
relatório de bug com isso é devolução na certa, e com razão.

São os tipos de erro da Aula 07 dentro do relatório do pytest. O tipo mostra onde a execução parou.
A regra escrita decide se o defeito está no produto ou no teste.

```bash
pytest test_aula08_tipo_do_erro.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 1 item

test_aula08_tipo_do_erro.py::test_total_com_quantidade_em_texto FAILED

================================== FAILURES ===================================
_____________________ test_total_com_quantidade_em_texto ______________________

    def test_total_com_quantidade_em_texto():
>       assert calcular_total(100, "3") == 300
               ^^^^^^^^^^^^^^^^^^^^^^^^

test_aula08_tipo_do_erro.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

valor = 100, quantidade = '3', desconto = 0.0

    def calcular_total(valor, quantidade, desconto=0.0):
>       return valor * quantidade - desconto
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: unsupported operand type(s) for -: 'str' and 'float'

aula08_loja.py:23: TypeError
=========================== short test summary info ===========================
FAILED test_aula08_tipo_do_erro.py::test_total_com_quantidade_em_texto - Type...
============================== 1 failed in 0.05s ==============================
```

### `aulas/aula08/aula08_pedidos.py`

O `registrar_item` de `aulas/aula07/aula07_pedidos.py`, copiado sem alteração nenhuma. O acréscimo
desta aula não está no arquivo: está em quem verifica.

**Regra de negócio:** item só é registrado com nome preenchido e quantidade positiva; cada recusa
diz qual das duas regras foi violada.

Vale relembrar o reenquadramento da Aula 07, porque ele é o que faz a verificação de hoje ter
sentido: quando a regra de negócio manda rejeitar, o erro é o comportamento **esperado**. O sistema
recusar é o acerto, e quem verifica precisa provar que a recusa aconteceu.

```bash
python aulas/aula08/aula08_pedidos.py
```

Saída: nenhuma, e exit code 0. Quem usa este arquivo é o `test_aula08_recusa.py`.

### `aulas/aula08/test_aula08_recusa.py`

As nove linhas da Aula 07 viram uma. **Exit code 1 de propósito:** dois testes passam e o terceiro
falha, e é o terceiro que ensina.

Na aula passada, provar que `registrar_item` recusou quantidade zero custou nove linhas em
`aulas/aula07/aula07_verifica_pedidos.py`: uma variável de estado começando em `False`, um `try`, a
chamada, um `except` que muda a variável para `True`, a mensagem guardada, e dois `assert` no fim.
Aquelas nove continuam certas e continuam valendo. Elas são o mecanismo, e quem entendeu o mecanismo
lê a linha de hoje e sabe o que ela faz por baixo.

`with pytest.raises(ValueError)` diz: eu **espero** um `ValueError` aqui dentro. Se vier, o teste
passa. Se não vier nada, o pytest reprova o teste sozinho, e essa é a metade que a turma escreveu na
mão semana passada com o `assert levantou`.

O segundo teste guarda o erro numa variável com `as erro` e confere a mensagem, porque não basta
recusar: tem que recusar pelo motivo certo. A função tem dois `raise ValueError`, e sem conferir a
mensagem um caso passaria com a recusa vindo do motivo errado. Repare que esse `assert` fica **fora**
do `with`, e tem que ficar: dentro do bloco, a linha depois da que estourou nunca executa.

O terceiro é a falha ao contrário da Aula 07, agora numa linha. A quantidade é válida, a função
devolve o texto e não levanta erro nenhum, então o pytest reprova porque o erro esperado não
aconteceu. A mensagem sai em inglês e é bem literal: `DID NOT RAISE ValueError`.

```bash
pytest test_aula08_recusa.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 3 items

test_aula08_recusa.py::test_recusa_quantidade_zero PASSED
test_aula08_recusa.py::test_recusa_diz_o_motivo PASSED
test_aula08_recusa.py::test_quantidade_valida_nao_deveria_ser_recusada FAILED

================================== FAILURES ===================================
_______________ test_quantidade_valida_nao_deveria_ser_recusada _______________

    def test_quantidade_valida_nao_deveria_ser_recusada():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

test_aula08_recusa.py:44: Failed
=========================== short test summary info ===========================
FAILED test_aula08_recusa.py::test_quantidade_valida_nao_deveria_ser_recusada
========================= 1 failed, 2 passed in 0.06s =========================
```

### `aulas/aula08/colisao-de-nome/random.py`

O arquivo que se importa sozinho. **Sai com exit code 1 de propósito, e não conserte: renomear ele
apagaria a demonstração.**

Ele mora numa pasta só dele, e a pasta existe por causa dele. Se este `random.py` estivesse ao lado
dos outros arquivos da Aula 08, todo arquivo daquela pasta que precisasse da biblioteca `random`
pegaria este aqui no lugar dela. Um arquivo mal nomeado contamina a pasta inteira.

Nome de arquivo também é nome de módulo. O Python procura `random`, encontra **este** arquivo antes
da biblioteca padrão, começa a executar ele, chega na linha do `import random` e encontra ele mesmo,
ainda pela metade. O arquivo importa a si próprio, e é por isso que o traceback aponta duas vezes
para o mesmo caminho: linha 31 e linha 33.

Repare no tipo do erro: `AttributeError`, falando de um atributo `choice` que não existe. Nada
nessas duas informações aponta para o nome do arquivo. Quem entrega a causa é a última linha, entre
parênteses, e ela existe porque o Python 3.12 em diante passou a sugerir a renomeação quando o nome
bate com o de um módulo conhecido. É uma gentileza recente, chega depois do traceback inteiro, e
ninguém lê o fim de uma mensagem vermelha na primeira vez.

A regra que fica não depende da gentileza: nunca dê a um arquivo seu o nome de uma biblioteca. Na
Aula 10 o curso usa a biblioteca Requests, e um `requests.py` na pasta do projeto é o caso mais
comum desse defeito.

```bash
python aulas/aula08/colisao-de-nome/random.py
```

Saída, com o caminho encurtado:

```
Traceback (most recent call last):
  File "...\aulas\aula08\colisao-de-nome\random.py", line 31, in <module>
    import random
  File "...\aulas\aula08\colisao-de-nome\random.py", line 33, in <module>
    sorteado = random.choice(["admin", "gerente", "visitante"])
               ^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'choice' (consider renaming '...\aulas\aula08\colisao-de-nome\random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```

### `tests/test_setup.py`

A verificação de ambiente do guia de setup, agora dentro do repositório. Da Aula 08 em diante o
pytest existe para a turma, e não faz mais sentido cada um digitar o arquivo na mão.

Três testes, e cada um confere uma coisa diferente. O `test_python_funciona` confere que o Python e
o pytest respondem, e não usa rede. O `test_requests_funciona` confere que a Requests está instalada
e que a sua máquina alcança o serverest, e precisa de internet. O `test_playwright_funciona` confere
que o Chromium abre pela automação, e precisa do navegador baixado com `playwright install
chromium`. Se aparecer `3 passed`, o ambiente está pronto para as 15 aulas.

Os dois últimos dependem de coisa que não é o seu código: rede fora do ar e navegador não instalado
deixam eles vermelhos sem que exista defeito nenhum. É o primeiro exemplo real da heurística desta
aula, porque o vermelho aqui não acusa o produto, acusa o ambiente.

```bash
pytest tests/test_setup.py -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 3 items

tests/test_setup.py::test_python_funciona PASSED                         [ 33%]
tests/test_setup.py::test_requests_funciona PASSED                       [ 66%]
tests/test_setup.py::test_playwright_funciona[chromium] PASSED           [100%]

============================== 3 passed in 5.94s ==============================
```

O `[chromium]` no nome do terceiro é o plugin `pytest-playwright` dizendo em qual navegador ele
rodou. Para ver a janela abrindo, em vez de rodar escondido:

```bash
pytest tests/test_setup.py::test_playwright_funciona --headed --slowmo 1000
```

### `tests/test_desconto_aula08.py`

A primeira suíte de autoverificação do curso. Ela julga a entrega da atividade da Aula 08, e existe
para você descobrir sozinho se acertou, sem esperar a correção. **Prazo da atividade: 08/09/2026, às
23h59.**

Como usar, em três passos:

1. Escreva a sua solução num arquivo chamado exatamente `regras_desconto.py`, com uma função chamada
   exatamente `calcular_desconto`, recebendo os quatro parâmetros nesta ordem: `valor_compra`,
   `cliente_vip`, `cupom_valido`, `produto_em_promocao`. A função tem que **devolver** o percentual
   com `return`. Função que só imprime devolve `None` e não é testável, que é a lição da Aula 06.
2. Salve o arquivo em `entregas/`, na raiz do repositório. Se a pasta não existir, crie.
3. Rode, da raiz do repositório:

```bash
pytest tests/test_desconto_aula08.py -v
```

Se aparecer `6 passed`, a sua função obedece a regra em todos os casos que a atividade cobra. Se
algum ficar vermelho, a mensagem diz a entrada, o esperado, o obtido e a regra que aquele caso
cobra. Leia a mensagem antes de mexer no código: na maioria das vezes ela já diz o que está errado.
A regra cobrada é o critério de aceite CA-018, o mesmo da Aula 03, e ela está escrita por extenso no
cabeçalho do próprio arquivo de teste.

Enquanto a entrega não estiver no lugar, a suíte inteira pula e a mensagem diz o que falta:

```
collected 0 items / 1 skipped

=========================== short test summary info ===========================
SKIPPED [1] tests\test_desconto_aula08.py:86: A entrega da Aula 08 ainda não está no lugar. Crie o arquivo 'entregas/regras_desconto.py' na raiz do repositório, com a função calcular_desconto(valor_compra, cliente_vip, cupom_valido, produto_em_promocao) devolvendo o percentual com return. Depois rode de novo.
============================= 1 skipped in 0.02s ==============================
```

São seis funções de teste quase idênticas, uma por caso, escritas na mão de propósito. Repare no
incômodo: muda o dado e o resultado esperado, e o resto é copiado. Guarde esse incômodo, porque a
Aula 09 é sobre colapsar as seis numa só.

### `pytest.ini`

Duas linhas de configuração, e cada uma resolve um problema concreto que apareceu nesta aula.

**`testpaths = tests`** diz ao pytest onde procurar quando ninguém passa caminho nenhum. Sem essa
linha o pytest varre o repositório inteiro e coleta também os `test_*.py` de `aulas/aula08/`, que
existem para ser rodados um por vez durante a aula e seis deles falham de propósito. Com ela,
`pytest` sem argumento roda só o que está em `tests/`, que é o que este README promete. Rodar um
arquivo de demonstração continua funcionando: basta passar o caminho dele.

**`addopts = -rfEs`** acrescenta o motivo dos testes pulados ao resumo do fim. O pytest esconde esse
motivo por padrão, e a suíte de autoverificação da Aula 08 pula com uma mensagem que diz onde salvar
a entrega; sem essa linha o aluno lê só `1 skipped` e não descobre o que faltou. São quatro letras e
não uma: o padrão do pytest é `-rfE`, e escrever só `-rs` **substitui** esse padrão em vez de somar
a ele, o que apaga o `short test summary info` das falhas.

Para ver as duas trabalhando juntas, sem rodar nada:

```bash
pytest --collect-only -q
```

Saída, com a pasta `entregas/` ainda vazia:

```
tests/test_isca_aula01.py::test_compra_um_produto[chromium]
tests/test_setup.py::test_playwright_funciona[chromium]
tests/test_setup.py::test_python_funciona
tests/test_setup.py::test_requests_funciona

=========================== short test summary info ===========================
SKIPPED [1] tests\test_desconto_aula08.py:86: A entrega da Aula 08 ainda não está no lugar. Crie o arquivo 'entregas/regras_desconto.py' na raiz do repositório, com a função calcular_desconto(valor_compra, cliente_vip, cupom_valido, produto_em_promocao) devolvendo o percentual com return. Depois rode de novo.
4 tests collected in 0.06s
```

Nenhum arquivo de `aulas/aula08/` aparece na lista, que é o `testpaths` fazendo o trabalho dele, e o
motivo do `skipped` aparece por extenso, que é o `addopts`.

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
├── aula04/    aula04_lista_status.py, aula04_contagem_assert.py, aula04_for_primeiro.py,
│              aula04_range.py, aula04_classificar_status.py, aula04_catraca.py,
│              aula04_catraca_sem_incremento.py, aula04_foguete.py, aula04_freio_de_mao.py,
│              aula04_unicidade.py, aula04_laco_infinito.py, aula04_resumo_execucao.py,
│              aula04_desafio_extra.py
├── aula05/    aula05_por_numero_por_nome.py, aula05_chave_ausente_erro.py,
│              aula05_chave_ausente.py, aula05_aninhado.py, aula05_suite_casos.py,
│              aula05_mapa_ambientes.py, aula05_json_minusculo_erro.py,
│              aula05_resposta_listagem.py, aula05_usuario_beto.py, aula05_email_sujo.py,
│              aula05_codigos_status.py, aula05_contagem_por_chave.py,
│              aula05_data_em_partes.py, aula05_validar_usuarios.py, aula05_pedido.json
├── aula06/    aula06_regra_repetida.py, aula06_frete_funcao.py, aula06_tres_partes.py,
│              aula06_valor_padrao.py, aula06_print_contra_return.py,
│              aula06_comando_e_pergunta.py, aula06_retorno_antecipado.py, aula06_escopo.py,
│              aula06_funcoes_da_loja.py, aula06_duas_funcoes.py, aula06_login_while.py,
│              aula06_tentar_login.py, aula06_palindromo.py, aula06_email_valido.py,
│              aula06_fechar_pedido.py, aula06_senha_valida.py
├── aula07/    aula07_relatorio.py, aula07_erros_de_sintaxe.py, aula07_nome_errado.py,
│              aula07_q1_indice.py, aula07_q2_tipo.py, aula07_q3_atributo.py,
│              aula07_q4_chave.py, aula07_try_except_massa.py, aula07_except_pelado.py,
│              aula07_pedidos.py, aula07_usa_pedidos.py, aula07_verifica_pedidos.py,
│              aula07_relatorio_bugado.py, aula07_relatorio_corrigido.py,
│              aula07_defeitos_pos_aula.py
└── aula08/    aula08_regras.py, test_aula08_regras.py, test_aula08_escada.py,
               test_aula08_atomico.py, aula08_regras_quebradas.py, test_aula08_regressao.py,
               aula08_desconto.py, test_aula08_desconto.py, aula08_loja.py,
               test_aula08_loja.py, test_aula08_tipo_do_erro.py, aula08_pedidos.py,
               test_aula08_recusa.py, colisao-de-nome/random.py
```

O nome do arquivo repete o número da aula de propósito: os comandos do curso são copiados e colados no terminal e no chat, e `python aulas/aula03/aula03_desconto.py` diz de qual aula é o arquivo mesmo fora do contexto da pasta. O `quadro_erro4.py` é a exceção do padrão, porque é o scratch do quadro de erros, não uma demonstração numerada da aula.

Em `aulas/aula08/` duas coisas fogem do padrão, e as duas são de propósito. Os arquivos que começam com `test_` precisam desse prefixo, porque é ele que o pytest exige para encontrar um teste. E o `colisao-de-nome/random.py` mora numa subpasta só dele, porque o nome colide com o de uma biblioteca do Python e contaminaria a pasta inteira se ficasse ao lado dos outros.

A Aula 01 é exceção por outro motivo: nela a turma não digita Python, só pseudocódigo no papel. Os arquivos `aulas/aula01/aula01_classificar_defeito.py` e `aulas/aula01/aula01_validar_login.py` existem para dar à regra de negócio e ao algoritmo da aula uma forma executável, com o pseudocódigo comentado no topo do arquivo e o código correspondente embaixo.
