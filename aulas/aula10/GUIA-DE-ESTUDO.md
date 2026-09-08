# Guia de estudo · Aula 10

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso): este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

**A tese da aula:** todo dado que apareceu no curso até aqui foi digitado à mão, num arquivo. A partir de hoje o dado vem de um servidor de verdade, que responde diferente a cada consulta e não tem obrigação de cooperar com o seu teste. O navegador já é um cliente de API desde sempre, o Requests só faz o mesmo pedido sem a maquiagem da tela, e a resposta sempre traz três coisas: status, cabeçalhos e corpo.

**A ordem canônica de asserção, e ela vale para toda API que você vai testar na vida:**

```
1. o status          2. a existência do campo          3. o valor do campo
```

Nunca pule um degrau. Validar o valor de um campo antes de saber se ele existe estoura o programa com um erro que não explica nada; validar o corpo antes do status faz você ler uma mensagem de erro pensando que é dado.

## `aula10_primeiro_get.py`

O primeiro GET, com `timeout` e a `BASE_URL` numa variável no topo.

```python
import requests

BASE_URL = "https://serverest.dev"

resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)

print(f"Status code: {resposta.status_code}")
```

**Treino:** troque `/usuarios` por `/produtos` e pelo endpoint de login, `/login`, sem enviar corpo nenhum. O status que volta de um `GET /login` sem credencial já te diz alguma coisa sobre o contrato da API antes de você ler a documentação.

A `BASE_URL` numa variável é o mapa de ambientes da Aula 5 de novo: um teste, e você troca de ambiente mudando uma linha.

## `aula10_consulta_json.py`

Abrir o corpo com `.json()`, e os dois jeitos de quebrar isso.

```python
dados = resposta.json()

print(f"Tipo do que voltou: {type(dados)}")
primeiro = dados["usuarios"][0]
print(f"Nome: {primeiro['nome']}")
```

**Treino:** `dados['usuarios'][0]['nome']` se lê da esquerda para a direita, como um endereço. Escreva a leitura em português, uma palavra por colchete, antes de rodar. Depois compare com o que a Aula 5 já ensinou sobre chave (usa nome) e posição (usa número): é a mesma estrutura, só que quem digitou os dados foi um servidor.

**Os dois erros de propósito estão comentados no arquivo.** Descomente o primeiro sozinho: `.json()` numa página HTML derruba com `JSONDecodeError`, mesmo o status vindo 200. Depois comente de volta e troque uma chave por outra que não existe, para ver o `KeyError` da Aula 5 de novo, só que agora ele pode significar que o contrato da API mudou.

## `test_api_consulta.py`

Um teste, três degraus.

```python
def test_listar_usuarios_respeita_os_tres_degraus():
    resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)
    assert resposta.status_code == 200

    corpo = resposta.json()
    assert "quantidade" in corpo
    assert "usuarios" in corpo
    assert corpo["quantidade"] == len(corpo["usuarios"])
```

**Treino:** aponte para cada `assert` e diga em voz alta qual dos três degraus ele é. O último não compara com um número fixo, compara o servidor consigo mesmo: é regra, não é dado, e por isso continua verdadeiro amanhã com outra quantidade de usuários.

## `test_produtos.py`

Mesma forma, outro recurso, mais uma verificação de tipo e o primeiro cenário negativo do curso batendo numa API real.

```python
def test_buscar_usuario_com_id_invalido_retorna_400():
    resposta = requests.get(f"{BASE_URL}/usuarios/id_invalido", timeout=10)
    assert resposta.status_code == 400
    assert "id" in resposta.json()
```

**Treino:** este teste passa quando o servidor **recusa**. Escreva ao lado, com suas palavras, por que 400 aqui é sucesso do teste e não falha. Depois leia os dois últimos testes do arquivo e ache a diferença entre os dois 400: um reclama de formato (`id_invalido`, chave `id`), o outro reclama de conteúdo (dezesseis letras `a`, chave `message`). São dois defeitos diferentes se um dia isso parar de funcionar.

## A atividade

Três testes seus, em `entregas/test_consulta_serverest.py`, contra `/produtos` e `/usuarios`. A suíte de autoverificação está em `tests/test_consulta_aula10.py`, na raiz do repositório, e ela roda os seus testes de verdade contra a API: não existe gabarito fixo para comparar, porque o produto desta atividade é o próprio teste.

**Treino antes de escrever a entrega:** para cada um dos três testes que o enunciado pede, escreva primeiro a frase em português do que ele confere, depois o `assert` do status, depois o `assert` de existência, depois o `assert` de valor. Só depois disso abra o editor.
