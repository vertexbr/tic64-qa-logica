# Guia de estudo · Aula 12

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso): este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

**A tese da aula:** a lista que você escreveu na Aula 1, em português, sem computador, é o teste de hoje. Abrir é `goto`, achar é `get_by_algo`, digitar é `fill`, clicar é `click`, conferir se entrou é `expect`. Nenhum comando é novo, só o nome mudou. A dificuldade real não está nesses seis nomes: está em escrever o "acha", porque o código não olha a tela como você olha.

**O ritual que vale mais que qualquer sintaxe:** antes de colar um locator no teste, conte no console quantos elementos ele casa.

```javascript
document.querySelectorAll("input").length
```

Refine até dar exatamente um. Locator que casa mais de um elemento age no primeiro, e o primeiro raramente é o que você quer.

**A ordem de preferência de locator, para guardar:**

```
1. get_by_role          o papel do elemento: botão, título, campo
2. get_by_label         o rótulo amarrado a um campo
3. get_by_placeholder   o texto que aparece dentro do campo vazio
4. get_by_text          o texto solto na tela
```

Papel primeiro porque é a única coisa que não está escrita no código da página: ela vem do padrão de acessibilidade e não muda quando alguém reorganiza o HTML.

## `test_login_web.py`

O teste de login completo, com os três degraus de sempre.

```python
def test_login_com_sucesso(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    campo_usuario = page.get_by_label("Username")
    campo_usuario.fill("tomsmith")
    expect(campo_usuario).to_have_value("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area")
```

**Treino:** rode `pytest aulas/aula12/test_login_web.py --headed --slowmo 500` e observe o navegador digitando devagar. Depois comente a linha `from playwright.sync_api import Page, expect` e rode de novo: leia o `NameError` e escreva, com suas palavras, por que ele aparece. Repita tirando o parâmetro `page` da função.

**Treino 2:** troque `page.get_by_label("Username")` por `page.locator("input")` e rode. Leia a mensagem de `strict mode violation` inteira: ela diz quantos elementos achou e lista os dois. É o mesmo número que o console teria dito antes.

## `test_acoes.py`

Três comportamentos de ação, na página de caixas de seleção.

```python
def test_tres_comportamentos(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    caixas = page.get_by_role("checkbox")
    primeira = caixas.first
    segunda = caixas.last

    primeira.check()
    primeira.check()
    expect(primeira).to_be_checked()

    segunda.click()
    expect(segunda).not_to_be_checked()
```

**Treino:** troque os dois `.check()` por dois `.click()` na primeira caixa e preveja o resultado antes de rodar. Ele marca e desmarca, porque clicar alterna. Depois escreva, num comentário, o que aconteceria se você chamasse `.fill("x")` duas vezes seguidas num campo de texto contra o que aconteceria chamando um método que digita caractere por caractere duas vezes.

## A atividade

Dois testes seus, em `entregas/test_interacoes_web.py`, contra `/checkboxes` **ou** `/dropdown`, a sua escolha. A suíte de autoverificação está em `tests/test_interface_aula12.py`, na raiz do repositório, e ela roda os seus testes de verdade contra o navegador: não existe gabarito fixo para comparar, porque o produto desta atividade é o próprio teste.

**Treino antes de escrever a entrega:** para cada locator que você for usar, abra o console da página escolhida, conte quantos elementos ele casa, e só depois cole no teste. Escreva o número num comentário na linha de cima: é o primeiro critério que a correção olha.
