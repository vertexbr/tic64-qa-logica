# Aula 06 - Funções: organizando as verificações

Demonstrações de código da Aula 06, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

## Arquivos

- `aula06_regra_repetida.py`
- `aula06_frete_funcao.py`
- `aula06_tres_partes.py`
- `aula06_valor_padrao.py`
- `aula06_print_contra_return.py`
- `aula06_comando_e_pergunta.py`
- `aula06_retorno_antecipado.py`
- `aula06_escopo.py`
- `aula06_funcoes_da_loja.py`
- `aula06_duas_funcoes.py`
- `aula06_login_while.py`
- `aula06_tentar_login.py`
- `aula06_palindromo.py`
- `aula06_email_valido.py`
- `aula06_fechar_pedido.py`
- `aula06_senha_valida.py`

## `aula06_regra_repetida.py`

O problema do dia da Aula 06, e ele existe para doer. A regra de frete grátis está escrita três
vezes, uma por cliente, e as três são idênticas palavra por palavra. Se o negócio mudar de 250
para 199, são três lugares para editar, e esquecer um deixa o sistema com duas regras ao mesmo
tempo sem nada quebrar.

**Este é o único arquivo do repositório escrito para não ser copiado.** A versão certa dele é o
`aula06_frete_funcao.py`, logo abaixo.

```bash
python aulas/aula06/aula06_regra_repetida.py
```

Saída:

```
Ana:  R$ 599.70 | frete R$ 0.00
Beto: R$ 49.90 | frete R$ 20.00
Cris: R$ 179.80 | frete R$ 20.00
A regra está escrita 3 vezes neste arquivo
```

## `aula06_frete_funcao.py`

O mesmo problema resolvido com uma função. Quinze linhas viraram quatro, e a regra passa a existir
num lugar só: mudar de 250 para 199 é editar uma linha, e os três clientes obedecem.

Os três `assert` do fim são a primeira vez no curso em que três cenários são verificados sem
copiar nenhuma linha de lógica. O terceiro, o de 250 exato, é o único que pega alguém trocando
`>=` por `>`.

```bash
python aulas/aula06/aula06_frete_funcao.py
```

Saída:

```
Frete da Ana:  R$ 0.00
Frete do Beto: R$ 20.00
Frete da Cris: R$ 20.00
As três verificações passaram
```

## `aula06_tres_partes.py`

As três partes de uma função, escritas na coluna de comentário e alinhadas com as linhas que
fazem cada uma: `RECEBE` na linha do `def`, `CALCULA` no corpo, `DEVOLVE` no `return`. A sequência
vale para função de um caminho só; validação tem vários, e é o `aula06_retorno_antecipado.py`.

A segunda metade prova a coisa que confunde todo mundo uma vez: **definir não executa.** Existem
duas funções no arquivo, só uma é chamada, e a saída tem duas linhas. A penúltima linha escreve o
nome de uma função sem os parênteses, o que não chama nada e não reclama de nada.

```bash
python aulas/aula06/aula06_tres_partes.py
```

Saída:

```
Frete de 300: R$ 0.00
O arquivo terminou, e a nunca_chamada não imprimiu nada
```

## `aula06_valor_padrao.py`

`desconto=0.0` na definição significa "se ninguém passar desconto, use zero". Chamada com dois
argumentos funciona, chamada com três funciona, e o caso comum fica curto sem perder a opção.

Parâmetro com valor padrão aparece em toda biblioteca do curso, e reconhecer a forma vale mais
que decorar a regra.

```bash
python aulas/aula06/aula06_valor_padrao.py
```

Saída:

```
Sem desconto: R$ 300.00
Com desconto: R$ 250.00
A diferença é o 3o argumento: R$ 50.00
As duas verificações passaram
```

## `aula06_print_contra_return.py`

O momento pedagógico da Aula 06. Duas funções somam dois mais dois, as duas parecem funcionar, e
só uma devolve o resultado. A que imprime devolve `None`, que é a ausência de valor da Aula 02.

`print` fala em voz alta, `return` entrega um documento. E a consequência para quem testa é o
ponto todo: teste precisa de valor para comparar, então função que só imprime não é testável.

O `TypeError` do fim está em `try/except` para o arquivo rodar até o fim e mostrar o erro e a
correção na mesma execução. **Numa suíte de verdade a falha interrompe**, e engolir exceção é o
oposto de verificar.

```bash
python aulas/aula06/aula06_print_contra_return.py
```

Saída:

```
4
Com print, resultado_print vale: None
Com return, resultado_return vale: 4
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
E com return a mesma conta funciona: 40
As duas verificações passaram
```

## `aula06_comando_e_pergunta.py`

As duas famílias de função, com nome. Função-comando faz algo e não devolve nada: registrar
evidência, imprimir relatório, clicar num botão. Função-pergunta devolve uma resposta, e você
guarda o resultado.

O último `assert` é o mais interessante do arquivo: ele verifica que a função-comando devolve
`None`. É a única verificação possível contra ela, e ela não verifica comportamento nenhum. É o
retrato de por que o teste só conversa com função-pergunta.

```bash
python aulas/aula06/aula06_comando_e_pergunta.py
```

Saída:

```
[EVIDÊNCIA] login válido: passou
JL12345! tem 8 ou mais? True
JL1234! tem 8 ou mais?  False
[EVIDÊNCIA] senha errada: passou
O que registrar_evidencia devolve: None
As três verificações passaram
```

## `aula06_retorno_antecipado.py`

Chegou no `return`, acabou a função. As três chamadas produzem uma, duas e três linhas de rastro,
e na primeira o e-mail está perfeito e nem foi olhado, porque o `return` da segunda linha encerrou
a função antes.

Os `assert` do fim comparam **variáveis**, e não chamam a função de novo. Isso é de propósito e
vale para toda função que imprime: chamar de novo dentro do `assert` imprimiria o rastro outra vez
e a saída viraria sopa.

```bash
python aulas/aula06/aula06_retorno_antecipado.py
```

Saída:

```
Chamada 1, nome vazio:
  checando o nome...
  devolveu: nome obrigatório
Chamada 2, e-mail sem arroba:
  checando o nome...
  checando o e-mail...
  devolveu: e-mail inválido
Chamada 3, tudo certo:
  checando o nome...
  checando o e-mail...
  tudo checado
  devolveu: ok
As três verificações passaram
```

## `aula06_escopo.py`

Um quadrado dentro de outro: o de fora é o programa, o de dentro é a função. Quem está dentro vê
o que está fora; quem está fora não vê o que está dentro, e a única coisa que atravessa a parede é
o que o `return` entrega.

A primeira metade mostra o `NameError` de tentar usar por fora uma variável criada dentro, que não
é bug e sim o escopo funcionando. A segunda mostra a parte que confunde de verdade: duas variáveis
com o mesmo nome, em quadrados diferentes, são coisas diferentes.

A regra prática que decide onde a variável mora: dado usado em mais de um lugar sobe para parâmetro
ou para retorno, e dado usado num lugar só fica dentro da função.

Os dois `try/except` existem para os dois casos caberem na mesma execução. **Numa suíte de verdade
a falha interrompe.**

```bash
python aulas/aula06/aula06_escopo.py
```

Saída:

```
Total: 30.0
NameError: name 'subtotal' is not defined
Dentro da função o valor virou 20, e devolveu 20
Fora da função, valor continua 10
As duas verificações passaram
```

## `aula06_funcoes_da_loja.py`

Quatro funções, e nenhuma delas é conteúdo novo. A classificação de severidade foi escrita em
português na Aula 01 e virou `if` na Aula 03. A classificação de status era o `for` da Aula 04. A
geração de e-mail é o `strip` e o `lower` da Aula 05, agora com `replace`. **Nada de novo além da
embalagem, e a embalagem é a função.**

A última linha é uma descoberta que não foi plantada: `lower` põe em minúscula e não tira acento
nenhum, então a função gera `joão.silva@qatest.com`, e e-mail com acento é recusado por boa parte
dos sistemas. Consertar não é assunto da aula; o que é assunto é que o dado que você escolhe para
testar decide o que você encontra.

**Guarde este arquivo.** Ele é o material de trabalho da aula que organiza as verificações com
ferramenta.

```bash
python aulas/aula06/aula06_funcoes_da_loja.py
```

Saída:

```
250 tem frete grátis? True
Severidade:  CRÍTICA
Código 302:  outro
E-mail sujo: gaia.silva@qatest.com
Todas as verificações passaram
Com acento:  joão.silva@qatest.com
```

## `aula06_duas_funcoes.py`

O arquivo da primeira demonstração guiada da Aula 06, escrito ao vivo na frente da turma. Duas
funções e quatro `assert`, e o terceiro é o do 250 exato, a fronteira da regra: valor-limite se
escolhe, não se sorteia.

Os dois tropeços mais prováveis ao refazer este arquivo em casa: `print` no lugar de `return`
dentro da função, que faz ela parecer funcionar e devolver `None`, e a chamada escrita sem os
parênteses, que não executa nada e não reclama de nada.

```bash
python aulas/aula06/aula06_duas_funcoes.py
```

Saída:

```
300 tem frete grátis? True
100 tem frete grátis? False
250 tem frete grátis? True
E-mail gerado: gaia.silva@qatest.com
As quatro verificações passaram
```

## `aula06_login_while.py`

O `while` entra pelo requisito, e não como teoria: "o sistema deve permitir até três tentativas de
senha, e bloquear o usuário na terceira falha". Tem "até", tem condição de parada, e o acerto pode
vir na primeira tentativa.

A condição tem duas partes ligadas por `and`, que são os operadores lógicos da Aula 03. E a linha
`numero = numero + 1` é a catraca da Aula 04 com trabalho novo: ela é o que garante que a condição
um dia vira falsa, e está antes de qualquer `if`, então roda em toda volta.

**Troque `"JL1234!"` por `"errada3"` na linha da massa e rode de novo** para ver o caminho do
bloqueio. Mesma lógica, massa diferente, resultado diferente, e nenhuma linha de lógica alterada.

O primeiro `assert` não diz `== True`, ele diz a regra: `logou == (senha_correta in tentativas)`.
Esperado vem da regra, obtido vem do programa, e escrito assim ele continua valendo nas duas
massas.

```bash
python aulas/aula06/aula06_login_while.py
```

Saída:

```
Tentativa 1 falhou
Tentativa 2 falhou
Login OK na tentativa 3
Tentativas consumidas: 3
As duas verificações passaram
```

## `aula06_tentar_login.py`

O mesmo `while`, agora embalado numa função. O bloco solto não era testável: para ver o caminho do
bloqueio era preciso editar o arquivo e rodar de novo. Aqui os dois cenários são duas linhas.

A condição perdeu metade e a variável `logou` desapareceu, porque o `return` sai do laço **e** da
função de uma vez. E a função devolve o número da tentativa em que logou, não `True`: `True`
responde uma pergunta, o número responde duas.

```bash
python aulas/aula06/aula06_tentar_login.py
```

Saída:

```
Logou na tentativa: 3
Bloqueado, devolveu: 0
As três verificações passaram
```

## `aula06_palindromo.py`

Função chamando função. `inverter` é um acumulador de texto, irmão do acumulador de lista da Aula
04: a cada volta ela cola a letra nova na frente do que já tinha. `eh_palindromo` chama `inverter`,
porque é assim que se monta lógica grande a partir de peças pequenas, cada uma testável sozinha.

`eh_palindromo` é função-pergunta que devolve verdadeiro ou falso, e essa é a mais fácil de testar
que existe, porque o esperado só tem dois valores possíveis.

```bash
python aulas/aula06/aula06_palindromo.py
```

Saída:

```
'abc' invertido: cba
'  Arara  ' é palíndromo? True
'teste' é palíndromo? False
A frase inteira: True
As três verificações passaram
```

## `aula06_email_valido.py`

A validação de e-mail da Aula 05, que era uma linha comprida perdida no meio de um arquivo, agora
com nome, entrada e saída. E ela ficou melhor: com retorno antecipado, os quatro motivos de recusa
ficam separados, um por `if`, cada um legível sozinho.

Seis cenários, quatro deles negativos, e cada cenário negativo aponta para um `if` específico:
um `assert` que falha diz qual regra quebrou.

Esta função não valida e-mail de verdade, e não é para isso que ela existe. A regra completa de
endereço de e-mail é longa e cheia de exceção, e existe biblioteca para isso. O que ela faz é o
que um teste precisa: recusar as quatro formas de errado que aparecem em massa de teste.

```bash
python aulas/aula06/aula06_email_valido.py
```

Saída:

```
  GAIA@Teste.COM   vale? True
beto@loja.com.br   vale? True
gaia.teste.com     vale? False
@teste.com         vale? False
gaia@teste         vale? False
a@b@c.com          vale? False
As seis verificações passaram
```

## `aula06_fechar_pedido.py`

O arquivo da segunda demonstração guiada da Aula 06, e o único do repositório em que uma função
chama outras três. Cada função tem uma responsabilidade só, e `fechar_pedido` não recalcula nada:
ela chama as três anteriores na ordem e junta o resultado.

É por isso que ela obedece a uma mudança de regra sem ser tocada: se o frete mudar, você mexe em
`calcular_frete` e mais nada. Essa é a resposta técnica para a pergunta que abre a aula, dos cem
testes que fazem login numa tela que mudou.

O quarto `assert` vale mais que os outros: cliente VIP com total baixo é o único cenário que testa
a **segunda** metade do `or` de `calcular_frete`. Sem ele, um `or` escrito como `and` passaria os
outros quatro sem reclamar.

E repare no escopo: `subtotal`, `com_desconto` e `frete` aparecem duas vezes no arquivo, uma dentro
de `fechar_pedido` e uma na margem. São variáveis diferentes, em quadrados diferentes.

```bash
python aulas/aula06/aula06_fechar_pedido.py
```

Saída:

```
Subtotal:     R$ 300.00
Com desconto: R$ 270.00
Frete:        R$ 0.00
Total final:  R$ 270.00
Todas as verificações passaram
```

## `aula06_senha_valida.py`

O extra de casa da Aula 06. Três coisas juntas, e as três já apareceram no curso: retorno
antecipado no primeiro `if`, duas variáveis de bandeira que começam falsas e podem virar
verdadeiras dentro do laço, e um `and` no `return` para exigir as duas.

A senha `JL1234!`, que atravessou o curso inteiro, é recusada, porque tem sete caracteres. Testar
a regra na fronteira encontrou isso em dois segundos.

```bash
python aulas/aula06/aula06_senha_valida.py
```

Saída:

```
Senha123 vale? True
JL1234!  vale? False  (7 caracteres)
jl123456 vale? False  (sem maiúscula)
JLABCDEF vale? False  (sem número)
As quatro verificações passaram
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
├── aula03/    aula03_operadores.py, aula03_login_evidencia.py, aula03_desconto.py,
│              aula03_desconto_invertido.py, aula03_gate_release.py, aula03_defeitos.py,
│              quadro_erro4.py
├── aula04/    aula04_lista_status.py, aula04_contagem_assert.py, aula04_for_primeiro.py,
│              aula04_range.py, aula04_classificar_status.py, aula04_catraca.py,
│              aula04_catraca_sem_incremento.py, aula04_foguete.py, aula04_freio_de_mao.py,
│              aula04_unicidade.py, aula04_laco_infinito.py, aula04_resumo_execucao.py,
│              aula04_desafio_extra.py
├── aula05/    aula05_por_numero_por_nome.py, aula05_chave_ausente_erro.py,
               aula05_chave_ausente.py, aula05_aninhado.py, aula05_suite_casos.py,
               aula05_mapa_ambientes.py, aula05_json_minusculo_erro.py,
               aula05_resposta_listagem.py, aula05_usuario_beto.py, aula05_email_sujo.py,
               aula05_codigos_status.py, aula05_contagem_por_chave.py,
               aula05_data_em_partes.py, aula05_validar_usuarios.py, aula05_pedido.json
└── aula06/    aula06_regra_repetida.py, aula06_frete_funcao.py, aula06_tres_partes.py,
               aula06_valor_padrao.py, aula06_print_contra_return.py,
               aula06_comando_e_pergunta.py, aula06_retorno_antecipado.py, aula06_escopo.py,
               aula06_funcoes_da_loja.py, aula06_duas_funcoes.py, aula06_login_while.py,
               aula06_tentar_login.py, aula06_palindromo.py, aula06_email_valido.py,
               aula06_fechar_pedido.py, aula06_senha_valida.py
```

O nome do arquivo repete o número da aula de propósito: os comandos do curso são copiados e colados no terminal e no chat, e `python aulas/aula03/aula03_desconto.py` diz de qual aula é o arquivo mesmo fora do contexto da pasta. O `quadro_erro4.py` é a exceção do padrão, porque é o scratch do quadro de erros, não uma demonstração numerada da aula.

A Aula 01 é a única exceção: nela a turma não digita Python, só pseudocódigo no papel. Os arquivos `aulas/aula01/aula01_classificar_defeito.py` e `aulas/aula01/aula01_validar_login.py` existem para dar à regra de negócio e ao algoritmo da aula uma forma executável, com o pseudocódigo comentado no topo do arquivo e o código correspondente embaixo.

---

Este README é gerado a partir da seção correspondente do [`README.md`](../../README.md) da raiz do repositório. Para alterar a explicação de um arquivo, edite lá e regenere aqui, para as duas fontes não divergirem.
