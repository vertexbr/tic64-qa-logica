# Aula 12 - Da ação do usuário ao código E2E

Demonstrações de código da Aula 12, a primeira do curso que automatiza a **interface**, não a API.
Os dois arquivos rodam com `pytest`, a partir da raiz do repositório, com o `(.venv)` ativo.

```bash
pytest aulas/aula12/test_login_web.py -v
pytest aulas/aula12/test_acoes.py -v
```

## Arquivos

- `test_login_web.py`
- `test_acoes.py`

## `test_login_web.py`

A primeira automação de interface do curso, contra `https://the-internet.herokuapp.com/login`.
Três testes: login com sucesso, senha errada e usuário errado.

```bash
pytest aulas/aula12/test_login_web.py -v
```

```
collected 3 items

aulas/aula12/test_login_web.py::test_login_com_sucesso PASSED
aulas/aula12/test_login_web.py::test_login_com_senha_errada PASSED
aulas/aula12/test_login_web.py::test_login_com_usuario_errado PASSED

============================== 3 passed in 10.18s ==============================
```

Os seis passos são os mesmos da lista que a turma escreveu na Aula 1, um a um: `goto` abre,
`get_by_label` acha o campo pelo rótulo, `fill` digita, `get_by_role` acha o botão pelo papel,
`click` envia, `expect` confere se entrou. `get_by_label` funciona aqui porque esta página tem
rótulo de verdade nos dois campos, diferente do SauceDemo usado na explicação ao vivo.

**O heading da área segura precisa de `exact=True`.** A página trouxe um segundo texto que também
contém "Secure Area", o subtítulo de boas-vindas, e sem `exact=True` o locator por papel casa os
dois elementos e a ferramenta recusa por ambiguidade. Confirmado rodando contra o site real em
15/09/2026.

O primeiro teste também valida o campo depois de preencher (`expect(...).to_have_value(...)`),
antes de continuar para a senha: preencher não garante preenchido, e essa é a primeira verificação
de estado do curso.

Os dois cenários negativos usam `to_contain_text`, não igualdade exata, porque a mensagem da tela
carrega espaço e quebra de linha ao redor do texto. Os dois passam porque o resultado esperado
**é** a recusa: se um dia `test_login_com_senha_errada` falhar mostrando a área segura, aí sim há
defeito, e grave.

## `test_acoes.py`

Três comportamentos de ação que confundem quem está começando, contra
`https://the-internet.herokuapp.com/checkboxes`.

```bash
pytest aulas/aula12/test_acoes.py -v
```

```
collected 1 item

aulas/aula12/test_acoes.py::test_tres_comportamentos PASSED

============================== 1 passed in 5.1s ==============================
```

`check()` é idempotente: chamado duas vezes na mesma caixa, ela continua marcada. `click()`
alterna: a segunda caixa desta página já vem marcada, e um clique nela desmarca. O terceiro
comportamento, que `fill` limpa o campo antes de escrever e digitar caractere por caractere não
limpa, está descrito no guia da aula e não tem teste próprio aqui, porque esta página não tem
campo de texto.

## A atividade

O enunciado completo está no portal do aluno. O arquivo se chama `test_interacoes_web.py` e vai
em `entregas/`, na raiz do repositório. Confira sozinho, da raiz:

```bash
pytest tests/test_interface_aula12.py -v
```

A suíte cobra três coisas: pelo menos dois casos de teste coletados, todos passando de verdade
contra o navegador, e pelo menos uma chamada de `expect` no arquivo. Se ela não achar a sua
entrega, ela pula com o caminho exato na mensagem, e pulo não é reprovação.
