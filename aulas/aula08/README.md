# Aula 08 - O primeiro teste automatizado com pytest

Demonstrações de código da Aula 08. Os cinco arquivos de produto rodam com `python` a partir da raiz do repositório (`(.venv)` ativo). Os oito arquivos de teste rodam com `pytest`, de dentro desta pasta, **e sempre nomeando o arquivo**.

## A regra do comando, e ela vale para a pasta inteira

**Nunca rode `pytest -s -v` sozinho aqui dentro.** Sem o nome do arquivo o pytest coleta os oito arquivos de teste de uma vez, dá 22 testes com 7 falhas, e o relatório vira um muro que não ensina nada. Um arquivo por vez é o modo da aula:

```bash
cd aulas/aula08
pytest test_aula08_regras.py -s -v
```

Da raiz do repositório o mesmo teste roda com o caminho completo, `pytest aulas/aula08/test_aula08_regras.py -s -v`, e o relatório sai igual com o caminho na frente de cada nome.

**Seis dos oito arquivos de teste saem com exit code 1 de propósito.** Nas outras aulas a regra é que todo arquivo roda até o fim; aqui a falha é o conteúdo, e ela existe para ser lida:

| Arquivo | Resultado | Por quê |
|---|---|---|
| `test_aula08_regras.py` | 4 passed | os quatro primeiros verdes do curso |
| `test_aula08_escada.py` | 1 passed | os quatro degraus de asserção, num teste só |
| `test_aula08_atomico.py` | 1 failed | teste que faz três coisas não diz qual quebrou |
| `test_aula08_regressao.py` | 1 failed, 3 passed | a regra estragada, pegada pelo teste |
| `test_aula08_desconto.py` | 2 failed | o mesmo teste de dois jeitos, e o relatório de cada um |
| `test_aula08_loja.py` | 1 failed, 5 passed | o defeito do limite de 250,00 |
| `test_aula08_tipo_do_erro.py` | 1 failed | `TypeError` acusando o teste, e não o produto |
| `test_aula08_recusa.py` | 1 failed, 2 passed | `pytest.raises`, e a falha ao contrário |

Cada arquivo `.py` desta pasta termina com um bloco de explicação linha a linha, marcado como gerado. Ele é a mesma numeração que aparece na calha do PyCharm durante a aula, e não se edita à mão.

## Arquivos

- `aula08_regras.py`
- `test_aula08_regras.py`
- `test_aula08_escada.py`
- `test_aula08_atomico.py`
- `aula08_regras_quebradas.py`
- `test_aula08_regressao.py`
- `aula08_desconto.py`
- `test_aula08_desconto.py`
- `aula08_loja.py`
- `test_aula08_loja.py`
- `test_aula08_tipo_do_erro.py`
- `aula08_pedidos.py`
- `test_aula08_recusa.py`
- `colisao-de-nome/random.py`

## `aula08_regras.py`

O produto da Aula 08, e a primeira separação do curso: um arquivo com a regra, outro com a verificação da regra. Até aqui as duas moravam juntas, e o `assert` ficava colado no fim do mesmo arquivo, como em `aulas/aula06/aula06_funcoes_da_loja.py`.

**Regra de negócio:** cadastro é liberado a partir de 18 anos, e 18 entra. Só admin e gerente têm permissão de administração; qualquer outro perfil não tem.

Duas funções-pergunta, e as duas devolvem booleano. `idade >= 18` já é `True` ou `False` antes de o `return` tocar nele, então quem escreve `if idade >= 18: return True` está fazendo a mesma coisa em três linhas. O `in` da segunda função é o da Aula 05, agora procurando texto numa lista de dois itens.

O nome do arquivo não começa com `test_`, e isso é de propósito: se começasse, o pytest tentaria rodar as funções daqui como se fossem casos de teste.

```bash
python aulas/aula08/aula08_regras.py
```

Saída: nenhuma, e exit code 0. O arquivo é só de funções, e quem usa ele são os testes ao lado.

## `test_aula08_regras.py`

O primeiro arquivo de teste do curso, e os quatro primeiros verdes. Duas convenções, e são as duas únicas coisas que o pytest exige para encontrar um teste: o **arquivo** começa com `test_` e a **função** começa com `test_`. Fora delas o pytest não reclama, não dá erro, e diz `collected 0 items`.

O `assert` é o de `aulas/aula04/aula04_contagem_assert.py`, sem uma vírgula de diferença. O acréscimo desta aula é a casa dele: ele saiu do fim de um script solto e entrou numa função com nome, que uma ferramenta encontra e roda. Nenhum teste daqui imprime nada, porque teste que passa é silencioso e quem fala é o relatório do pytest.

O primeiro teste traz `# Preparação`, `# Ação` e `# Validação` em linhas separadas, para nomear o padrão. Os outros três fazem as três coisas de uma vez, numa linha, que é como a maioria dos testes fica no dia a dia.

```bash
pytest test_aula08_regras.py -s -v
```

Saída, com os caminhos encurtados:

```
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0 -- ...\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: ...\qa-logica-programacao-testes
configfile: pytest.ini
plugins: base-url-2.1.0, playwright-0.8.0
collecting ... collected 4 items

test_aula08_regras.py::test_maior_de_idade_e_valido PASSED
test_aula08_regras.py::test_menor_de_idade_e_invalido PASSED
test_aula08_regras.py::test_admin_tem_permissao PASSED
test_aula08_regras.py::test_visitante_nao_tem_permissao PASSED

============================== 4 passed in 0.02s ==============================
```

Nas seções abaixo o cabeçalho do pytest fica de fora da saída, porque ele repete igual.

## `test_aula08_escada.py`

A escada de asserções, quatro degraus dentro de um teste só. Nenhum degrau é conteúdo novo: a igualdade é da Aula 04, o `isinstance` é o `type()` de `aulas/aula02/aula02_tipos_e_nomes.py` com outro nome, e os dois últimos são o `in` e o `not in` de `aulas/aula05/aula05_codigos_status.py`, onde eles conferiam se um código HTTP estava na lista de sucesso. O acréscimo é a casa: os quatro moram dentro de uma função de teste, e uma ferramenta encontra e roda os quatro.

O `isinstance` confere o tipo e não o valor, e essa distinção pega gente: `isinstance(False, bool)` também é `True`. E cuidado com a ordem das palavras no quarto degrau: é `not in`, junto, e não `not "visitante" in [...]`. As duas funcionam e a segunda é ilegível.

A lista completa do que se pode asseverar é para consultar. Estes quatro são para guardar, e o primeiro resolve a maioria dos casos que você vai escrever.

```bash
pytest test_aula08_escada.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 1 item

test_aula08_escada.py::test_escada_de_assercoes PASSED

============================== 1 passed in 0.03s ==============================
```

## `test_aula08_atomico.py`

O teste que faz três coisas, e por que ele não serve. **Sai com exit code 1 de propósito**, e a falha é o conteúdo: ela não tem conserto e existe para mostrar duas coisas de uma vez.

A primeira: o pytest **para no primeiro `assert` que falha**, e os seguintes daquela função não rodam. O terceiro `assert` deste arquivo também está errado e não aparece em lugar nenhum do relatório. Em casa isso vira a sensação de ter criado defeito novo depois de consertar o primeiro. Você não criou, só chegou no segundo.

A segunda: teste que valida três coisas não diz qual delas quebrou. Você lê o relatório, vê um nome vermelho, e ainda precisa abrir o código para descobrir. A versão certa é uma função por comportamento, como no `test_aula08_regras.py`, em que o nome do teste já é o diagnóstico.

A regra, e ela cabe em quatro palavras: **prepara, age, valida, acabou.** Se você precisa agir de novo, é outro teste.

```bash
pytest test_aula08_atomico.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 1 item

test_aula08_atomico.py::test_tres_validacoes_no_mesmo_teste FAILED

================================== FAILURES ===================================
_____________________ test_tres_validacoes_no_mesmo_teste _____________________

    def test_tres_validacoes_no_mesmo_teste():
        assert validar_idade_minima(20) == True
>       assert tem_permissao("visitante") == True
E       AssertionError: assert False == True
E        +  where False = tem_permissao('visitante')

test_aula08_atomico.py:27: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_atomico.py::test_tres_validacoes_no_mesmo_teste - Assertio...
============================== 1 failed in 0.07s ==============================
```

## `aula08_regras_quebradas.py`

O `aula08_regras.py` com uma diferença: o 18 virou 21 na linha da idade. O resto é igual palavra por palavra.

A troca não foi sabotagem. Alguém achou que estava melhorando a regra, salvou, e não rodou nada. É assim que regressão entra em produção, e é esse o argumento de existir teste: ele é o ponto de controle que avisa que o contrato mudou, mesmo quando ninguém teve má intenção.

**Regra de negócio:** a regra escrita continua a mesma, cadastro liberado a partir de 18 anos. O código é que passou a dizer 21, e nenhuma mensagem de erro avisa isso.

Em aula o professor faz a troca ao vivo no `aula08_regras.py` e desfaz com Ctrl+Z. Este arquivo existe para você repetir a demonstração em casa sem precisar estragar o original.

```bash
python aulas/aula08/aula08_regras_quebradas.py
```

Saída: nenhuma, e exit code 0. Quem acusa a troca é o teste da próxima seção.

## `test_aula08_regressao.py`

Os quatro testes do `test_aula08_regras.py`, copiados sem mudar uma vírgula, apontados para o módulo estragado. A única diferença é a linha do `import`. **Sai com exit code 1 de propósito**, e é a primeira leitura de relatório de falha do curso.

Antes de rodar, responda: quantos dos quatro ficam vermelhos? A resposta não é quatro, e o motivo de não ser quatro é o conteúdo. `validar_idade_minima(16)` continua devolvendo `False` com 21 no lugar de 18, e as duas verificações de perfil nem tocam na linha alterada. Um teste que passa não prova que o código está certo; ele prova que **aquele caso** está certo.

Cinco informações saem de um comando só: o nome do teste que falhou, o corpo dele reimpresso, a seta apontando o `assert` exato, o `E` com o obtido e o esperado lado a lado, e a última linha com arquivo, linha e tipo do erro.

```bash
pytest test_aula08_regressao.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 4 items

test_aula08_regressao.py::test_maior_de_idade_e_valido FAILED
test_aula08_regressao.py::test_menor_de_idade_e_invalido PASSED
test_aula08_regressao.py::test_admin_tem_permissao PASSED
test_aula08_regressao.py::test_visitante_nao_tem_permissao PASSED

================================== FAILURES ===================================
________________________ test_maior_de_idade_e_valido _________________________

    def test_maior_de_idade_e_valido():
        # Preparação
        idade = 20
        # Ação
        resultado = validar_idade_minima(idade)
        # Validação
>       assert resultado == True
E       assert False == True

test_aula08_regressao.py:31: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_regressao.py::test_maior_de_idade_e_valido - assert False ...
========================= 1 failed, 3 passed in 0.08s =========================
```

## `aula08_desconto.py`

A regra de desconto de `aulas/aula03/aula03_desconto.py`, a mesma escada que a turma escreveu na Aula 03, agora embalada em função com `return` e testável de fora.

**Regra de negócio:** cliente VIP acima de 200 tem 20% de desconto e VIP até 200 tem 10%. Cupom válido dá 5%, e quem não é VIP nem tem cupom não ganha desconto nenhum.

Os 20 do primeiro degrau não são defeito plantado: 20 é o que a regra do curso sempre disse. Quem erra é o **teste** da próxima seção, que cobra 25, e é essa diferença que produz o vermelho da demonstração.

```bash
python aulas/aula08/aula08_desconto.py
```

Saída: nenhuma, e exit code 0.

## `test_aula08_desconto.py`

O mesmo teste escrito de dois jeitos, e o relatório de cada um. **Sai com exit code 1 de propósito:** os dois testes falham, e falham pelo mesmo motivo, porque esperam 25 e a função devolve 20. A diferença está inteira no que o relatório consegue contar sobre a falha.

O comando leva a opção `-l`, que lista as variáveis locais no momento da falha. No primeiro teste o pytest imprime o conteúdo de cada variável com o nome que você deu, e você lê o relatório sabendo qual era a entrada, qual era a expectativa e o que veio. No segundo sai `assert 20 == 25` e nada mais, porque não existe variável nenhuma para listar.

Os dois dizem **que** falhou. Só o primeiro diz **por que**, e custa três linhas. A regra prática: dê nome ao dado de entrada, ao esperado e ao obtido. Quem vai ler isso na esteira de integração às onze da noite não vai abrir o seu código.

```bash
pytest test_aula08_desconto.py -l
```

Saída, sem o cabeçalho do pytest:

```
collected 2 items

test_aula08_desconto.py FF                                               [100%]

================================== FAILURES ===================================
________________________ test_desconto_de_cliente_vip _________________________

    def test_desconto_de_cliente_vip():
        valor_compra = 300.00
        desconto_esperado = 25
        desconto_obtido = calcular_desconto(valor_compra, cliente_vip=True)
>       assert desconto_obtido == desconto_esperado
E       assert 20 == 25

desconto_esperado = 25
desconto_obtido = 20
valor_compra = 300.0

test_aula08_desconto.py:31: AssertionError
_________________ test_desconto_de_cliente_vip_sem_variaveis __________________

    def test_desconto_de_cliente_vip_sem_variaveis():
>       assert calcular_desconto(300.00, True) == 25
E       assert 20 == 25
E        +  where 20 = calcular_desconto(300.0, True)


test_aula08_desconto.py:35: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_desconto.py::test_desconto_de_cliente_vip - assert 20 == 25
FAILED test_aula08_desconto.py::test_desconto_de_cliente_vip_sem_variaveis - ...
============================== 2 failed in 0.06s ==============================
```

## `aula08_loja.py`

As três funções da loja, como elas chegaram para testar, e uma delas chegou com defeito.

**Regra de negócio:** o total é valor vezes quantidade, menos o desconto em reais. O frete é grátis **a partir** de 250,00, e 250,00 exato tem frete grátis.

**Atenção ao `tem_frete_gratis`.** Ele não é a versão que a turma escreveu: em `aulas/aula06/aula06_funcoes_da_loja.py` a comparação é `>= 250.00`, e está certa lá. Aqui ela é `> 250.00`. O defeito não se anuncia, e é esse o ponto: o arquivo roda, não dá erro nenhum, e a função devolve `False` para exatamente 250,00. Quem escrever o teste a partir da **regra escrita** encontra o defeito; quem escrever o teste olhando o código escreve um teste que concorda com o erro.

O `calcular_total` é o total de `aulas/aula02/aula02.py` com desconto opcional, e o `aplicar_desconto` é a conta de percentual de `aulas/aula03/aula03_desconto.py`. O acréscimo dos dois é a embalagem em função, que é a Aula 06.

```bash
python aulas/aula08/aula08_loja.py
```

Saída: nenhuma, e exit code 0.

## `test_aula08_loja.py`

A suíte da loja, seis testes, e **exit code 1 de propósito**: cinco passam e o que falha achou um defeito de verdade no produto.

Os seis saíram da regra escrita, e não do código. É por isso que o `test_frete_gratis_no_limite` existe: a regra diz "frete grátis a partir de 250,00", então 250,00 exato tem que ter frete grátis. Os outros dois testes de frete, o de 300 e o de 100, passam com `>` e passariam com `>=`, e não distinguem as duas versões. O do limite distingue, e o cliente que gasta exatamente duzentos e cinquenta reais paga frete e liga para o suporte.

Aplique a heurística do dia no vermelho que sai daqui: o erro é `AssertionError`, então o código rodou até o fim e o resultado veio diferente do esperado. Suspeite do produto. E o produto está errado mesmo: a correção é trocar `>` por `>=`, e é uma tecla.

O último teste fecha uma conta aberta na Aula 02. Um desconto de 10% sobre 99,90 dá 89,91 na sua cabeça e 89.91000000000001 em ponto flutuante. O `pytest.approx` compara com tolerância, e é a resposta que ficou prometida seis aulas atrás.

Por que 250 e não 249 nem 251? A pergunta tem nome técnico e é a Aula 09.

```bash
pytest test_aula08_loja.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 6 items

test_aula08_loja.py::test_total_sem_desconto PASSED
test_aula08_loja.py::test_total_com_desconto PASSED
test_aula08_loja.py::test_frete_gratis_acima_de_250 PASSED
test_aula08_loja.py::test_sem_frete_gratis_abaixo_de_250 PASSED
test_aula08_loja.py::test_frete_gratis_no_limite FAILED
test_aula08_loja.py::test_desconto_aplicado_com_centavos PASSED

================================== FAILURES ===================================
_________________________ test_frete_gratis_no_limite _________________________

    def test_frete_gratis_no_limite():
        total_no_limite = 250.00
>       assert tem_frete_gratis(total_no_limite) == True
E       assert False == True
E        +  where False = tem_frete_gratis(250.0)

test_aula08_loja.py:49: AssertionError
=========================== short test summary info ===========================
FAILED test_aula08_loja.py::test_frete_gratis_no_limite - assert False == True
========================= 1 failed, 5 passed in 0.06s =========================
```

## `test_aula08_tipo_do_erro.py`

O outro lado do vermelho: quando o defeito é do seu teste. **Exit code 1 de propósito**, e este vermelho não acusa o produto.

A heurística, e ela é para guardar:

| Tipo do erro no relatório | O que aconteceu | De quem suspeitar |
|---|---|---|
| `AssertionError` | o código rodou até o fim e o resultado veio diferente | do **produto** |
| `TypeError`, `IndexError`, `KeyError`, `NameError`, `AttributeError` | o teste quebrou antes de chegar na validação | do **seu teste** |

Aqui a quantidade foi passada como `"3"`, entre aspas, e o teste nunca chegou no `assert`. Leia a mensagem com atenção, porque ela é mais interessante do que parece: a multiplicação não reclamou de nada, já que `100 * "3"` em Python repete o texto três vezes e devolve `"333"`. Quem estourou foi a subtração do desconto, e é por isso que a última linha diz `unsupported operand type(s) for -: 'str' and 'float'`.

Repare também em qual arquivo o pytest aponta no fim: `aula08_loja.py`, que é o produto. O erro estourou lá dentro, mas quem entregou o dado errado foi o teste, e é o teste que se conserta. Abrir relatório de bug com isso é devolução na certa, e com razão.

São os três tipos de erro da Aula 07 aplicados a relatório de teste: `AssertionError` é erro de lógica do produto, e os outros são erro de execução do seu próprio código.

```bash
pytest test_aula08_tipo_do_erro.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 1 item

test_aula08_tipo_do_erro.py::test_total_com_quantidade_em_texto FAILED

================================== FAILURES ===================================
_____________________ test_total_com_quantidade_em_texto ______________________

    def test_total_com_quantidade_em_texto():
>       assert calcular_total(100, "3") == 300
               ^^^^^^^^^^^^^^^^^^^^^^^^

test_aula08_tipo_do_erro.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

valor = 100, quantidade = '3', desconto = 0.0

    def calcular_total(valor, quantidade, desconto=0.0):
>       return valor * quantidade - desconto
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: unsupported operand type(s) for -: 'str' and 'float'

aula08_loja.py:23: TypeError
=========================== short test summary info ===========================
FAILED test_aula08_tipo_do_erro.py::test_total_com_quantidade_em_texto - Type...
============================== 1 failed in 0.05s ==============================
```

## `aula08_pedidos.py`

O `registrar_item` de `aulas/aula07/aula07_pedidos.py`, copiado sem alteração nenhuma. O acréscimo desta aula não está no arquivo: está em quem verifica.

**Regra de negócio:** item só é registrado com nome preenchido e quantidade positiva; cada recusa diz qual das duas regras foi violada.

Vale relembrar o reenquadramento da Aula 07, porque ele é o que faz a verificação de hoje ter sentido: quando a regra de negócio manda rejeitar, o erro é o comportamento **esperado**. O sistema recusar é o acerto, e quem verifica precisa provar que a recusa aconteceu.

```bash
python aulas/aula08/aula08_pedidos.py
```

Saída: nenhuma, e exit code 0. Quem usa este arquivo é o `test_aula08_recusa.py`.

## `test_aula08_recusa.py`

As nove linhas da Aula 07 viram uma. **Exit code 1 de propósito:** dois testes passam e o terceiro falha, e é o terceiro que ensina.

Na aula passada, provar que `registrar_item` recusou quantidade zero custou nove linhas em `aulas/aula07/aula07_verifica_pedidos.py`: uma variável de estado começando em `False`, um `try`, a chamada, um `except` que muda a variável para `True`, a mensagem guardada, e dois `assert` no fim. Aquelas nove continuam certas e continuam valendo. Elas são o mecanismo, e quem entendeu o mecanismo lê a linha de hoje e sabe o que ela faz por baixo.

`with pytest.raises(ValueError)` diz: eu **espero** um `ValueError` aqui dentro. Se vier, o teste passa. Se não vier nada, o pytest reprova o teste sozinho, e essa é a metade que a turma escreveu na mão semana passada com o `assert levantou`.

O segundo teste guarda o erro numa variável com `as erro` e confere a mensagem, porque não basta recusar: tem que recusar pelo motivo certo. A função tem dois `raise ValueError`, e sem conferir a mensagem um caso passaria com a recusa vindo do motivo errado. Repare que esse `assert` fica **fora** do `with`, e tem que ficar: dentro do bloco, a linha depois da que estourou nunca executa.

O terceiro é a falha ao contrário da Aula 07, agora numa linha. A quantidade é válida, a função devolve o texto e não levanta erro nenhum, então o pytest reprova porque o erro esperado não aconteceu. A mensagem sai em inglês e é bem literal: `DID NOT RAISE ValueError`.

```bash
pytest test_aula08_recusa.py -s -v
```

Saída, sem o cabeçalho do pytest:

```
collecting ... collected 3 items

test_aula08_recusa.py::test_recusa_quantidade_zero PASSED
test_aula08_recusa.py::test_recusa_diz_o_motivo PASSED
test_aula08_recusa.py::test_quantidade_valida_nao_deveria_ser_recusada FAILED

================================== FAILURES ===================================
_______________ test_quantidade_valida_nao_deveria_ser_recusada _______________

    def test_quantidade_valida_nao_deveria_ser_recusada():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

test_aula08_recusa.py:44: Failed
=========================== short test summary info ===========================
FAILED test_aula08_recusa.py::test_quantidade_valida_nao_deveria_ser_recusada
========================= 1 failed, 2 passed in 0.06s =========================
```

## `colisao-de-nome/random.py`

O arquivo que se importa sozinho. **Sai com exit code 1 de propósito, e não conserte: renomear ele apagaria a demonstração.**

Ele mora numa pasta só dele, e a pasta existe por causa dele. Se este `random.py` estivesse ao lado dos outros arquivos desta pasta, todo arquivo daqui que precisasse da biblioteca `random` pegaria este aqui no lugar dela. Um arquivo mal nomeado contamina a pasta inteira.

Nome de arquivo também é nome de módulo. O Python procura `random`, encontra **este** arquivo antes da biblioteca padrão, começa a executar ele, chega na linha do `import random` e encontra ele mesmo, ainda pela metade. O arquivo importa a si próprio, e é por isso que o traceback aponta duas vezes para o mesmo caminho: linha 31 e linha 33.

Repare no tipo do erro: `AttributeError`, falando de um atributo `choice` que não existe. Nada nessas duas informações aponta para o nome do arquivo. Quem entrega a causa é a última linha, entre parênteses, e ela existe porque o Python 3.12 em diante passou a sugerir a renomeação quando o nome bate com o de um módulo conhecido. É uma gentileza recente, chega depois do traceback inteiro, e ninguém lê o fim de uma mensagem vermelha na primeira vez.

A regra que fica não depende da gentileza: nunca dê a um arquivo seu o nome de uma biblioteca. Na Aula 10 o curso usa a biblioteca Requests, e um `requests.py` na pasta do projeto é o caso mais comum desse defeito.

```bash
python aulas/aula08/colisao-de-nome/random.py
```

Saída, com o caminho encurtado:

```
Traceback (most recent call last):
  File "...\aulas\aula08\colisao-de-nome\random.py", line 31, in <module>
    import random
  File "...\aulas\aula08\colisao-de-nome\random.py", line 33, in <module>
    sorteado = random.choice(["admin", "gerente", "visitante"])
               ^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'choice' (consider renaming '...\aulas\aula08\colisao-de-nome\random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```

## A atividade pós-aula

A atividade da Aula 08 não mora nesta pasta. Você escreve a sua solução em `entregas/regras_desconto.py`, na raiz do repositório, e confere sozinho com a suíte de autoverificação:

```bash
pytest tests/test_desconto_aula08.py -v
```

**Prazo: 08/09/2026, às 23h59.** O [README.md](../../README.md) da raiz explica o passo a passo, e o cabeçalho do próprio `tests/test_desconto_aula08.py` traz a regra cobrada por extenso.
