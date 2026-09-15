# Aula 11 - O ciclo CRUD completo pela API

Demonstrações de código da Aula 11. Os sete primeiros arquivos rodam com `python` a partir da
raiz do repositório (`(.venv)` ativo). Os três últimos rodam com `pytest`, de dentro desta pasta,
nomeando o arquivo.

**Todos os dez escrevem no banco de dados de uma API pública de verdade**, `https://serverest.dev`,
compartilhada com estudantes do mundo inteiro. Por isso **todos limpam o que criam**: cada arquivo
termina apagando o recurso que ele mesmo cadastrou, e é isso que faz qualquer um deles poder ser
rodado quantas vezes você quiser sempre com o mesmo resultado.

```bash
python aulas/aula11/aula11_problema_do_dia.py
python aulas/aula11/aula11_post_usuario.py
python aulas/aula11/aula11_status_nao_basta.py
python aulas/aula11/aula11_tres_quatrocentos.py
python aulas/aula11/aula11_massa_unica.py
python aulas/aula11/aula11_ciclo_completo.py
python aulas/aula11/aula11_put_fantasma.py
cd aulas/aula11
pytest test_cadastro.py test_veredito.py aula11_login_token.py -v
```

Da raiz do repositório, o mesmo comando de teste roda com o caminho completo,
`pytest aulas/aula11/test_cadastro.py aulas/aula11/test_veredito.py aulas/aula11/aula11_login_token.py -v`.

Contagem conferida rodando os dez arquivos contra a API real em 09/09/2026, com o `.venv` do
repositório: Python 3.13.5, pytest 9.1.1 e requests 2.34.2. Os sete scripts saem com exit code 0,
e os seis testes dos três arquivos de suíte passam.

## Arquivos

- `aula11_problema_do_dia.py`
- `aula11_post_usuario.py`
- `aula11_status_nao_basta.py`
- `aula11_tres_quatrocentos.py`
- `aula11_massa_unica.py`
- `aula11_ciclo_completo.py`
- `aula11_put_fantasma.py`
- `test_cadastro.py`
- `test_veredito.py`
- `aula11_login_token.py`

Cada arquivo termina com a explicação linha a linha no rodapé, gerada a partir do mesmo texto que
o guia do professor abre no popup. Não edite aquele bloco: a próxima geração substitui ele inteiro.

## `aula11_problema_do_dia.py`

O problema que a aula inteira existe para resolver. Ele manda o **mesmo cadastro duas vezes**,
com o mesmo e-mail, e as duas respostas são diferentes.

```bash
python aulas/aula11/aula11_problema_do_dia.py
```

```
Primeira chamada -> 201 {'message': 'Cadastro realizado com sucesso', '_id': 'nsrDogkSAwzhvQDE'}
Segunda chamada  -> 400 {'message': 'Este email já está sendo usado'}
```

Não mudou uma letra do código entre as duas linhas: mudou o **estado do servidor**, porque a
primeira chamada deixou um dado lá. Se isso estivesse dentro de um teste com
`assert status == 201`, ele passaria na primeira execução e falharia na segunda, e falharia pelo
motivo errado: não há defeito nenhum, a regra de e-mail único está funcionando.

O `_id` é diferente a cada execução. A última linha apaga o usuário criado, e é ela que faz o
arquivo poder rodar de novo. Se a primeira chamada já responder 400, alguém rodou antes e a
limpeza não chegou a acontecer: troque o `tic64` do e-mail e rode outra vez.

## `aula11_post_usuario.py`

O POST com corpo, e as três coisas novas em relação à Aula 10: o verbo mudou, apareceu o
`json=payload`, e a resposta trouxe um identificador.

```bash
python aulas/aula11/aula11_post_usuario.py
```

```
Status: 201
Mensagem: Cadastro realizado com sucesso
ID criado: mWKCOL0F867nQrfz
```

**Duzentos e um, e não duzentos.** 200 significa "entendi e respondi"; 201 significa "entendi,
respondi, e passei a guardar algo novo". É por isso que o corpo trouxe um identificador: ele é o
endereço do que acabou de nascer, e os três verbos seguintes precisam dele.

O `administrador` vai como **texto** com aspas, `"true"` ou `"false"`, e não como o booleano do
Python. É escolha desta API, e é o detalhe que mais derruba a primeira tentativa.

## `aula11_status_nao_basta.py`

O melhor argumento que existe contra validar só o status, e ele é real.

```bash
python aulas/aula11/aula11_status_nao_basta.py
```

```
Status: 200
Mensagem: Nenhum registro excluído
```

O servidor respondeu com **sucesso** para uma exclusão que não excluiu nada, e ele está sendo
honesto: a mensagem diz exatamente isso. Um teste que só olhasse o número teria escrito "exclusão
validada" no relatório sem que nada tivesse sido apagado.

Separe os dois tipos de validação e use o nome dos dois. **Validação técnica:** o campo existe, o
tipo está certo, o status está na faixa. **Validação funcional:** o valor obedece à regra de
negócio. Um teste que só faz a técnica aprova sistema quebrado com elegância.

## `aula11_tres_quatrocentos.py`

Três casos que o padrão HTTP descreveria com três números diferentes, e esta API responde 400 nos
três.

```bash
python aulas/aula11/aula11_tres_quatrocentos.py
```

```
e-mail repetido     -> 400 {'message': 'Este email já está sendo usado'}
sem o campo email   -> 400 {'email': 'email é obrigatório'}
usuário inexistente -> 400 {'message': 'Usuário não encontrado'}
```

Alguns contratos usam **409, conflito**, no primeiro caso, **422, conteúdo inválido**, no segundo,
e **404** no terceiro. O ServeRest responde 400 nos três exemplos. Antes de escrever a asserção,
consulte a documentação. Se ela prometer um status e a API responder outro, registre a divergência
como defeito. Quando o caso não estiver documentado, observe a resposta e alinhe a regra com o
time antes de fixar o resultado esperado.

E repare que **os três corpos são diferentes**: dois trazem a chave `message` e o do meio traz a
chave `email`. O status sozinho não distingue os casos nem quando o número é o mesmo.

## `aula11_massa_unica.py`

A solução do problema da abertura, e é o único arquivo da aula que não faz requisição nenhuma.

```bash
python aulas/aula11/aula11_massa_unica.py
```

```
cadastro.9906519a925544d2a63328ead398709d@qa.com.br
duplicado.da13f6f9a9c94fab98ef73fd268d64ca@qa.com.br
False
```

`uuid4().hex` cria um identificador novo com 32 caracteres hexadecimais. A chance de colisão é
desprezível para a massa de teste desta aula, mesmo quando duas execuções começam no mesmo segundo.
Rode o arquivo duas vezes e compare os valores.

A terceira linha mostra que duas chamadas seguidas recebem identificadores diferentes. O prefixo
continua útil para explicar a finalidade do dado, mas não é ele que garante a unicidade.

Biblioteca de geração de dados falsos é o outro caminho, e ele é útil quando a massa precisa
parecer real. Vem com um alerta que quase nenhum material dá: ela **sorteia** de uma lista, e
sorteio repete. Se o seu teste depende de unicidade, acrescente um UUID ao campo que precisa ser
único, mesmo usando a biblioteca.

## `aula11_ciclo_completo.py`

O ciclo inteiro, e ele tem **seis** passos, não quatro.

```bash
python aulas/aula11/aula11_ciclo_completo.py
```

```
POST      -> 201 Cadastro realizado com sucesso
GET       -> 200 nome=Gaia Silva
PUT       -> 200 Registro alterado com sucesso
GET       -> 200 nome=Gaia Silva Atualizada
DELETE    -> 200 Registro excluído com sucesso
GET final -> 400 Usuário não encontrado
```

Os dois que quase todo mundo esquece são o quarto e o sexto. O quarto não confia na mensagem
"Registro alterado com sucesso": ele consulta de novo e confere o nome. O sexto é a validação do
DELETE, porque excluir e receber 200 não prova que sumiu, como o `aula11_status_nao_basta.py`
mostra. O que prova é procurar depois e não achar.

**Mensagem de sucesso é o servidor dizendo que fez. O GET seguinte é você conferindo que ele fez.**

O PUT manda o recurso **inteiro**, e não só o campo que mudou: os campos que você não mandar podem
sumir. É por isso que o arquivo mexe no `payload` completo antes de alterar.

## `aula11_put_fantasma.py`

Alterar um recurso que não existe faz o recurso passar a existir.

```bash
python aulas/aula11/aula11_put_fantasma.py
```

```
Status: 201
Corpo: {'message': 'Cadastro realizado com sucesso', '_id': 'U3YEG8YH1Uorig27'}
Limpeza feita: o usuário criado sem querer foi apagado.
```

Isso é comportamento previsto no padrão HTTP, e várias APIs fazem. Quem escreve um teste negativo
esperando recusa aqui vê o teste falhar, e não há defeito nenhum: o teste é que estava supondo a
coisa errada.

Repare no identificador que voltou: ele é **outro**, e não as dezesseis letras `b` que foram
pedidas. Por isso a limpeza usa `resposta.json()['_id']`, e não a constante enviada: apagar pelo
identificador pedido responderia 200 com "Nenhum registro excluído", e o usuário criado por engano
ficaria lá para sempre.

## `test_cadastro.py`

A primeira demonstração da aula: cadastrar, conferir e limpar. São dois testes.

```bash
cd aulas/aula11
pytest test_cadastro.py::test_cadastro_de_usuario_com_sucesso -v   # 1 passed
pytest test_cadastro.py -v                                          # 2 passed
```

O primeiro valida na ordem canônica da Aula 10: status, existência do campo, valor do campo. E a
mensagem do primeiro `assert` carrega o status **e o corpo inteiro**, para o relatório dizer o que
o servidor respondeu sem ninguém precisar rodar de novo com `print`.

O segundo **passa quando recebe 400**. O resultado esperado dele é a rejeição, e se um dia ele
falhar dizendo que veio 201, aí sim há defeito, e grave: a loja passou a aceitar dois clientes com
o mesmo e-mail.

A asserção do e-mail duplicado é **dupla**, status e mensagem. Esta API devolve 400 para meia dúzia
de motivos diferentes: validando só o número, o teste continua verde no dia em que a recusa passar
a ser por outro motivo.

Os dois prefixos de e-mail são diferentes de propósito. Eles rodam em sequência, dentro do mesmo
segundo, e prefixo igual faria os dois colidirem.

## `test_veredito.py`

A segunda demonstração, e ela é o fechamento da unidade de API.

```bash
cd aulas/aula11
pytest test_veredito.py -v      # 2 passed
```

A função `validar_resposta_de_usuario` recebe um dado, aplica um monte de regras, junta os
problemas numa lista e devolve um veredito. Lista vazia significa aprovado. **É exatamente o
exercício da Aula 5**, o da lista de usuários com nome vazio, com o dado vindo de um servidor pela
internet em vez de digitado à mão. A lógica não mudou; só a origem do dado mudou.

Duas escolhas de projeto que vale ler no código:

- O `return` dentro do primeiro `if` é o **retorno antecipado** da Aula 6. Status errado, para
  tudo: o corpo que voltou é uma mensagem de erro, e procurar o nome do usuário dentro dela só
  produz confusão. Assim o degrau um é respeitado por construção.
- No degrau dois **não** há `return`: ele acumula todos os campos ausentes em vez de parar no
  primeiro. Parar cedo serve para fluxo; acumular serve para contrato.

E a linha da limpeza está **antes** do assert final, de propósito. Se o assert vem primeiro e
falha, o programa para ali e o usuário nunca é apagado. **Apague antes de julgar, sempre.**

## `aula11_login_token.py`

Treino em casa, e ele fecha o desafio deixado no fim da Aula 10. Não passa na apresentação.

```bash
cd aulas/aula11
pytest aula11_login_token.py -v     # 2 passed
```

O login devolve um token, e o token é a chave que endpoints protegidos exigem. O 401 do segundo
teste é o único caso da aula em que esta API não responde 400, e ele é honesto: senha errada é
problema de autenticação, não de formato.

## A atividade

O enunciado completo está no portal do aluno. O arquivo se chama `test_ciclo_serverest.py` e vai
em `entregas/`, na raiz do repositório. Confira sozinho, da raiz:

```bash
pytest tests/test_ciclo_aula11.py -v
```

A suíte cobra três coisas: pelo menos três casos de teste coletados, todos passando contra a API,
e os **quatro verbos** presentes no arquivo. Se ela não achar a sua entrega, ela pula com o caminho
exato na mensagem, e pulo não é reprovação.
