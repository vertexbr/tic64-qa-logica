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

### `aulas/aula01_classificar_defeito.py`

A Aula 01 não escreve Python: a turma sai dela com o pseudocódigo no papel. Este arquivo é a tradução, em código, do algoritmo `classificar_defeito` ensinado em aula, com a regra de negócio e o pseudocódigo comentados no topo do arquivo antes da função.

Regra: defeito que impede o uso do sistema é severidade CRÍTICA; se não impede o uso mas afeta uma funcionalidade, é ALTA; qualquer outra coisa é BAIXA.

O arquivo também traz o "erro proposital" da aula: a mesma função com as duas condições invertidas, para mostrar que a ordem das condições muda o resultado sem gerar nenhum erro de execução.

```bash
python aulas/aula01_classificar_defeito.py
```

Saída:

```
Severidade: CRÍTICA
Severidade com a ordem trocada: ALTA
```

### `aulas/aula01_validar_login.py`

Tradução, em código, do algoritmo `validar_login` ditado pela turma na Aula 01, com a regra de negócio e o pseudocódigo comentados no topo do arquivo.

Regra: o login é aprovado se o usuário está ativo E a senha está correta; ao errar a senha três vezes o usuário é bloqueado, e depois de bloqueado não entra nem com a senha certa.

Executa os quatro casos do teste de mesa feito em aula.

```bash
python aulas/aula01_validar_login.py
```

Saída:

```
Caso 1 -> resultado: APROVADO | tentativas: 0
Caso 2 -> resultado: NEGADO | tentativas: 3
Caso 3 -> resultado: BLOQUEADO | tentativas: 3
Caso 4 -> resultado: NEGADO | tentativas: 1
```

### `aulas/aula02.py`

Demonstração da Aula 02, o cenário de compra. Declara as variáveis do carrinho (valor do produto, quantidade, cliente ativo e o valor mínimo para frete grátis), calcula o total numa variável e imprime cinco linhas de evidência com f-string. No fim mostra o `type()` de três variáveis, para a turma ver `float`, `int` e `bool` saindo na tela.

```bash
python aulas/aula02.py
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

### `aulas/aula02_login.py`

Segunda demonstração da Aula 02, o caso de teste de login. Separa o dado informado do dado esperado em variáveis distintas, que é a ideia central do exercício, e guarda ainda o contador de tentativas e o token da sessão. A comparação usa `==`, o operador que compara valores, diferente do `=` que atribui.

O `token = None` está ali de propósito: `None` é ausência de valor, não string vazia, e imprime literalmente `None`.

```bash
python aulas/aula02_login.py
```

Saída:

```
Usuário informado: Nadinha
Usuário esperado: Nadinha
Usuários iguais? True
Senhas iguais? True
Tentativas: 0 | Token: None
```

### `aulas/aula02_tipos_e_nomes.py`

Demonstrações do primeiro ciclo da Aula 02: nomes de variável em snake_case, os cinco tipos do curso (`str`, `int`, `float`, `bool`, `None`) com o vocabulário do curso, a distinção entre `200` e `"200"`, o contraste de f-string com e sem o `f`, e o primeiro erro proposital (`"58" + 1`), capturado com `try/except` para o arquivo terminar sem travar.

```bash
python aulas/aula02_tipos_e_nomes.py
```

### `aulas/aula02_conversao_e_armadilhas.py`

Demonstrações do segundo ciclo da Aula 02: a simulação de dado externo que vem como texto (o lugar do `input()` da calculadora que devolve `105`), a comparação `codigo == codigo_texto`, o erro `AttributeError` de `codigo.strip()` num número, a armadilha do `0.1 + 0.2`, a diferença entre o nome de uma variável e o seu conteúdo, e o erro da vírgula decimal (`599,90` virando tupla). Os erros propositais ficam em `try/except` para o arquivo rodar do início ao fim.

```bash
python aulas/aula02_conversao_e_armadilhas.py
```

Os quatro arquivos da Aula 02 em sequência, num comando só:

```bash
python aulas/aula02.py; python aulas/aula02_login.py; python aulas/aula02_tipos_e_nomes.py; python aulas/aula02_conversao_e_armadilhas.py
```

No PowerShell do Windows use `;` como separador. O `&&` só funciona no PowerShell 7 ou no bash.

## Convenção de arquivos

O repositório tem duas pastas com propósitos diferentes.

Em `tests/` ficam as suítes que o pytest roda, um arquivo por aula, no padrão `tests/test_<assunto>_aula<NN>.py`, com o número da aula em dois dígitos. O nome de cada teste dentro do arquivo começa com `test_` e descreve o que está sendo verificado, em português, como em `test_compra_um_produto`.

Em `aulas/` ficam as demonstrações feitas ao vivo, no padrão `aulas/aula<NN>.py`, com um sufixo quando a aula tem mais de um script, como `aulas/aula02_login.py`. Esses arquivos rodam pelo `python` e são script de estudo, não suíte de verificação. Deixá-los fora de `tests/` evita que o pytest tente coletá-los.

A Aula 01 é a única exceção: nela a turma não digita Python, só pseudocódigo no papel. Os arquivos `aulas/aula01_classificar_defeito.py` e `aulas/aula01_validar_login.py` existem para dar à regra de negócio e ao algoritmo da aula uma forma executável, com o pseudocódigo comentado no topo do arquivo e o código correspondente embaixo.
