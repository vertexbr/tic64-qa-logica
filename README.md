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

## Convenção de arquivos

O repositório tem duas pastas com propósitos diferentes.

Em `tests/` ficam as suítes que o pytest roda, um arquivo por aula, no padrão `tests/test_<assunto>_aula<NN>.py`, com o número da aula em dois dígitos. O nome de cada teste dentro do arquivo começa com `test_` e descreve o que está sendo verificado, em português, como em `test_compra_um_produto`.

Em `aulas/` ficam as demonstrações feitas ao vivo, uma subpasta por aula, no padrão `aulas/aula<NN>/aula<NN>_<assunto>.py`, com o número da aula em dois dígitos nos dois níveis. Esses arquivos rodam pelo `python` e são script de estudo, não suíte de verificação. Deixá-los fora de `tests/` evita que o pytest tente coletá-los.

A subpasta por aula existe porque o repositório cresce durante as 15 aulas e a raiz de `aulas/` ficaria com dezenas de arquivos misturados. Quem procura o material de uma aula abre a pasta dela:

```
aulas/
├── aula01/    aula01_classificar_defeito.py, aula01_validar_login.py
├── aula02/    aula02.py, aula02_login.py, aula02_tipos_e_nomes.py, aula02_conversao_e_armadilhas.py
└── aula03/    aula03_operadores.py, aula03_login_evidencia.py, aula03_desconto.py,
               aula03_desconto_invertido.py, aula03_gate_release.py, aula03_defeitos.py,
               quadro_erro4.py
```

O nome do arquivo repete o número da aula de propósito: os comandos do curso são copiados e colados no terminal e no chat, e `python aulas/aula03/aula03_desconto.py` diz de qual aula é o arquivo mesmo fora do contexto da pasta. O `quadro_erro4.py` é a exceção do padrão, porque é o scratch do quadro de erros, não uma demonstração numerada da aula.

A Aula 01 é a única exceção: nela a turma não digita Python, só pseudocódigo no papel. Os arquivos `aulas/aula01/aula01_classificar_defeito.py` e `aulas/aula01/aula01_validar_login.py` existem para dar à regra de negócio e ao algoritmo da aula uma forma executável, com o pseudocódigo comentado no topo do arquivo e o código correspondente embaixo.
