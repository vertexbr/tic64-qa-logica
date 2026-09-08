# Aula 10 - Primeira requisição, primeira validação

Demonstrações de código da Aula 10. Os quatro primeiros arquivos rodam com `python` a partir da
raiz do repositório (`(.venv)` ativo). Os dois últimos rodam com `pytest`, de dentro desta pasta,
nomeando o arquivo.

**Todos os seis dependem de uma API pública de verdade, `https://serverest.dev`.** Ela é
compartilhada com outros estudantes no mundo inteiro, então quantidades e conteúdos mudam a cada
execução. Isso não é defeito dos arquivos: é o assunto da aula, e volta com solução na Aula 11.

```bash
python aulas/aula10/aula10_primeiro_get.py
python aulas/aula10/aula10_consulta_api.py
python aulas/aula10/aula10_consulta_json.py
python aulas/aula10/aula10_erro_json.py
cd aulas/aula10
pytest test_api_consulta.py test_produtos.py -v
```

Da raiz do repositório, o mesmo comando de teste roda com o caminho completo,
`pytest aulas/aula10/test_api_consulta.py aulas/aula10/test_produtos.py -v`.

Contagem conferida rodando os seis arquivos contra a API real em 08/09/2026, com Python 3.13.5,
pytest 9.0.2 e requests 2.32.5: os quatro scripts saem com exit code 0, e os sete testes dos dois
arquivos de suíte passam.

## Arquivos

- `aula10_primeiro_get.py`
- `aula10_consulta_api.py`
- `aula10_consulta_json.py`
- `aula10_erro_json.py`
- `test_api_consulta.py`
- `test_produtos.py`

## `aula10_primeiro_get.py`

O primeiro GET da turma contra um servidor de verdade: status, cabeçalho de tipo de conteúdo, e a
lista de status da Aula 4 voltando com números vindos de uma API real em vez de digitados à mão.

```bash
python aulas/aula10/aula10_primeiro_get.py
```

```
Status code: 200
Content-Type: application/json; charset=utf-8
[200, 405, 400, 500]
```

A lista fecha sempre nesses quatro números, porque as quatro URLs testam contratos fixos da API
(rota que existe, rota que não existe, identificador com formato certo mas inexistente, e um 5xx
de propósito via `httpbin.org`). O que muda a cada execução é só a quantidade de usuários, que
este arquivo não imprime.

## `aula10_consulta_api.py`

O arquivo da primeira demonstração: dois GET, dois recursos, só olhando. Ele não valida nada de
propósito, e é isso que o professor nomeia na tela.

```bash
python aulas/aula10/aula10_consulta_api.py
```

```
Produtos, status: 200
Produtos, tipo: application/json; charset=utf-8
Usuários, status: 200
```

Quatro linhas fazem o que um clique fazia. Mas está imprimindo, e imprimir não julga nada: quem
julga é você olhando a tela. Do arquivo seguinte em diante o `print` sai e o `assert` entra.

O treino que vem com ele é pedir `/usuariosss`, com três esses, e ler a resposta: **405**, com a
mensagem apontando a documentação.

## `aula10_consulta_json.py`

Abre o corpo da resposta com `.json()`, mostra a leitura por chave e por posição, e fecha com o
filtro por `params`.

```bash
python aulas/aula10/aula10_consulta_json.py
```

O nome e a quantidade impressos variam a cada execução, porque vêm da API pública. O que não
varia é a estrutura: um dicionário com `quantidade` e `usuarios`, e dentro de `usuarios` uma
lista de dicionários, a mesma forma que a Aula 5 ensinou a ler.

Os dois erros propositais da aula não moram aqui: eles têm arquivo próprio,
`aula10_erro_json.py`, que roda de verdade em vez de ficar comentado.

## `aula10_erro_json.py`

Os dois erros propositais da aula, cada um numa função, com `try/except` para o arquivo seguir até
o fim e mostrar os dois na mesma execução.

```bash
python aulas/aula10/aula10_erro_json.py
```

```
Status: 200
JSONDecodeError: Expecting value: line 1 column 1 (char 0)
E o que voltou de verdade comeca assim: <!DOCTYPE html>

KeyError: 'quantidadee'
As chaves que existem de verdade: ['quantidade', 'usuarios']
```

O primeiro é o que confunde: status 200 e o programa quebrou, porque o que voltou foi HTML e
`.json()` só abre JSON. O segundo é o `KeyError` da Aula 5 com um motivo novo: pode ser o contrato
da API que mudou, e aí é defeito de verdade.

**Engolir erro com `try/except` aqui serve para demonstrar o erro, e é o oposto do que se faz num
teste.** Numa suíte, a falha interrompe, e é isso que faz o relatório significar alguma coisa.

## `test_api_consulta.py`

Os três degraus da asserção (status, existência do campo, valor do campo) virando código pela
primeira vez no curso. Um teste só, e ele é o modelo que toda suíte de API vai seguir daqui para
frente.

```bash
cd aulas/aula10
pytest test_api_consulta.py -v
```

```
collected 1 item

test_api_consulta.py::test_listar_usuarios_respeita_os_tres_degraus PASSED

============================== 1 passed in 0.74s ===============================
```

O último `assert` (`corpo["quantidade"] == len(corpo["usuarios"])`) é regra de negócio, não dado:
ele vale hoje com qualquer quantidade de usuários e continua valendo amanhã, porque compara o
que o servidor diz consigo mesmo, nunca com um número fixo.

## `test_produtos.py`

Variação do primeiro teste: outro recurso (`/produtos`), verificação de tipo (`preco` é `int`,
não string) e o primeiro cenário negativo do curso com API, `GET /usuarios/id_invalido`
esperando **400**. Os dois últimos testes são o gabarito do desafio extra da aula.

```bash
cd aulas/aula10
pytest test_produtos.py -v
```

```
collected 6 items

test_produtos.py::test_listar_produtos_retorna_200 PASSED
test_produtos.py::test_lista_de_produtos_tem_estrutura_esperada PASSED
test_produtos.py::test_produto_tem_campos_obrigatorios PASSED
test_produtos.py::test_buscar_usuario_com_id_invalido_retorna_400 PASSED
test_produtos.py::test_nenhum_produto_tem_preco_invalido PASSED
test_produtos.py::test_usuario_inexistente_avisa_que_nao_encontrou PASSED

============================== 6 passed in 4.61s ===============================
```

O quarto teste **passa quando o servidor recusa o pedido**. É a mesma inversão do cenário
negativo da Aula 9: o resultado esperado é a rejeição, então receber 400 é sucesso do teste.

Os dois últimos testes distinguem dois 400 por motivos diferentes: `id_invalido` não tem o
formato de um identificador (a API reclama do formato, chave `id`), e
`aaaaaaaaaaaaaaaa` tem o formato certo e não existe (a API reclama do conteúdo, chave `message`).

## A atividade desta aula

A entrega é código: três testes seus, no arquivo `entregas/test_consulta_serverest.py`. A suíte
que julga está em `tests/test_consulta_aula10.py`, e roda da raiz do repositório:

```bash
pytest tests/test_consulta_aula10.py -v
```

Diferente das suítes das Aulas 08 e 09, esta não compara sua entrega contra um gabarito fixo: ela
entrega os **seus** testes ao pytest, num processo separado, com o mesmo comando que você usaria
na mão. Ela cobra duas coisas, e só duas: pelo menos três casos de teste coletados, e todos
passando. Quem escrever um `@pytest.mark.parametrize` da Aula 9 conta cada linha da massa como um
caso, porque é assim que o pytest conta. Seguir a ordem canônica de
asserção (status, existência, valor) e nunca validar dado específico de outra pessoa são regras
da aula, e ficam para a correção humana ler, porque um teste pode passar hoje e estar errado do
mesmo jeito que a Aula 11 vai mostrar.
