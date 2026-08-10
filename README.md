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

## Convenção de arquivos

Um arquivo por aula, no padrão `tests/test_<assunto>_aula<NN>.py`, com o número da aula em dois dígitos. O nome de cada teste dentro do arquivo começa com `test_` e descreve o que está sendo verificado, em português, como em `test_compra_um_produto`.
