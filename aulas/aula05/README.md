# Aula 05 - Lendo JSON com olhar de QA

Demonstrações de código da Aula 05, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

## Arquivos

- `aula05_por_numero_por_nome.py`
- `aula05_chave_ausente_erro.py`
- `aula05_chave_ausente.py`
- `aula05_aninhado.py`
- `aula05_suite_casos.py`
- `aula05_mapa_ambientes.py`
- `aula05_json_minusculo_erro.py`
- `aula05_resposta_listagem.py`
- `aula05_usuario_beto.py`
- `aula05_email_sujo.py`
- `aula05_codigos_status.py`
- `aula05_contagem_por_chave.py`
- `aula05_data_em_partes.py`
- `aula05_validar_usuarios.py`
- `aula05_pedido.json`

## `aula05_por_numero_por_nome.py`

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

## `aula05_chave_ausente_erro.py`

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

## `aula05_chave_ausente.py`

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

## `aula05_aninhado.py`

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

## `aula05_suite_casos.py`

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

## `aula05_mapa_ambientes.py`

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

## `aula05_json_minusculo_erro.py`

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

## `aula05_resposta_listagem.py`

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

## `aula05_usuario_beto.py`

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

## `aula05_email_sujo.py`

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

## `aula05_codigos_status.py`

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

## `aula05_contagem_por_chave.py`

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

## `aula05_data_em_partes.py`

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

## `aula05_validar_usuarios.py`

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

## `aula05_pedido.json`

Arquivo de apoio da atividade da Aula 05, e o único do repositório que não é Python. Ele é uma
resposta crua, como uma API devolveria, com `true`, `false` e `null` em minúsculo e com o e-mail
do cliente sujo de propósito.

**Ele existe para ser transcrito, não carregado.** A tarefa é passar esse JSON para um dicionário
Python à mão, trocando `true` por `True` e `null` por `None`, que é a demonstração do `NameError`
aplicada em casa. Ler arquivo com biblioteca é assunto de outra aula.

---

Este README é gerado a partir da seção correspondente do [`README.md`](../../README.md) da raiz do repositório. Para alterar a explicação de um arquivo, edite lá e regenere aqui, para as duas fontes não divergirem.
