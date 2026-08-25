# Aula 02 - Dados de teste virando variáveis

Demonstrações de código da Aula 02, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

## Arquivos

- `aula02.py`
- `aula02_login.py`
- `aula02_tipos_e_nomes.py`
- `aula02_conversao_e_armadilhas.py`

## `aula02.py`

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

## `aula02_login.py`

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

## `aula02_tipos_e_nomes.py`

Demonstrações do primeiro ciclo da Aula 02: nomes de variável em snake_case, os cinco tipos do curso (`str`, `int`, `float`, `bool`, `None`) com o vocabulário do curso, a distinção entre `200` e `"200"`, o contraste de f-string com e sem o `f`, e o primeiro erro proposital (`"58" + 1`), capturado com `try/except` para o arquivo terminar sem travar.

```bash
python aulas/aula02/aula02_tipos_e_nomes.py
```

## `aula02_conversao_e_armadilhas.py`

Demonstrações do segundo ciclo da Aula 02: a simulação de dado externo que vem como texto (o lugar do `input()` da calculadora que devolve `105`), a comparação `codigo == codigo_texto`, o erro `AttributeError` de `codigo.strip()` num número, a armadilha do `0.1 + 0.2`, a diferença entre o nome de uma variável e o seu conteúdo, e o erro da vírgula decimal (`599,90` virando tupla). Os erros propositais ficam em `try/except` para o arquivo rodar do início ao fim.

```bash
python aulas/aula02/aula02_conversao_e_armadilhas.py
```

## Rodar tudo desta aula

Os quatro arquivos da Aula 02 em sequência, num comando só:

```bash
python aulas/aula02/aula02.py; python aulas/aula02/aula02_login.py; python aulas/aula02/aula02_tipos_e_nomes.py; python aulas/aula02/aula02_conversao_e_armadilhas.py
```

No PowerShell do Windows use `;` como separador. O `&&` só funciona no PowerShell 7 ou no bash.

---

Este README é gerado a partir da seção correspondente do [`README.md`](../../README.md) da raiz do repositório. Para alterar a explicação de um arquivo, edite lá e regenere aqui, para as duas fontes não divergirem.
