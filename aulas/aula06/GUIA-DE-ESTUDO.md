# Guia de estudo · Aula 06

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso) — este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

## `aula06_regra_repetida.py`

O problema do dia da Aula 06, e ele existe para doer.

```python
subtotal_ana = 199.90 * 3
if subtotal_ana >= 250:
    frete_ana = 0.0
else:
    frete_ana = 20.0

subtotal_beto = 49.90 * 1
if subtotal_beto >= 250:
    frete_beto = 0.0
else:
    frete_beto = 20.0

subtotal_cris = 89.90 * 2
if subtotal_cris >= 250:
    frete_cris = 0.0
else:
# ...
```

Arquivo completo: `aulas/aula06/aula06_regra_repetida.py` (36 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_frete_funcao.py`

O mesmo problema resolvido com uma função.

```python
def calcular_frete(subtotal):
    if subtotal >= 250:
        return 0.0
    return 20.0

print(f"Frete da Ana:  R$ {calcular_frete(199.90 * 3):.2f}")
print(f"Frete do Beto: R$ {calcular_frete(49.90):.2f}")
print(f"Frete da Cris: R$ {calcular_frete(89.90 * 2):.2f}")

# Três cenários verificados sem copiar nenhuma linha de lógica, incluindo o
# 250 exato, que é a fronteira da regra. É a primeira vez no curso que isso
# acontece: até a Aula 05, verificar três cenários exigia três blocos.
assert calcular_frete(300.00) == 0.0
assert calcular_frete(100.00) == 20.0
assert calcular_frete(250.00) == 0.0
# ...
```

Arquivo completo: `aulas/aula06/aula06_frete_funcao.py` (96 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_tres_partes.py`

As três partes de uma função, escritas na coluna de comentário e alinhadas com as linhas que fazem cada uma:

```python
def calcular_frete(subtotal):    # RECEBE
    if subtotal >= 250:          # CALCULA
        return 0.0               # DEVOLVE
    return 20.0                  # DEVOLVE, pelo outro caminho

def nunca_chamada(valor):
    print(f"Se isto aparecer, a função executou: {valor}")
    return valor * 2

# Acima existem DUAS funções definidas. Só uma é chamada, e a linha abaixo é a
# chamada: nome, parênteses, e o argumento dentro dos parênteses. O 300 é o
# argumento; o subtotal lá em cima é o parâmetro. Parâmetro é o nome na
# definição, argumento é o valor na chamada, e é só isso que separa as duas
# palavras.
# ...
```

Arquivo completo: `aulas/aula06/aula06_tres_partes.py` (38 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_valor_padrao.py`

`desconto=0.0` na definição significa "se ninguém passar desconto, use zero".

```python
def calcular_total(valor, quantidade, desconto=0.0):
    return valor * quantidade - desconto

sem_desconto = calcular_total(100.00, 3)
com_desconto = calcular_total(100.00, 3, 50.00)

print(f"Sem desconto: R$ {sem_desconto:.2f}")
print(f"Com desconto: R$ {com_desconto:.2f}")
print(f"A diferença é o 3o argumento: R$ {sem_desconto - com_desconto:.2f}")

assert calcular_total(100.00, 3) == 300.00
assert calcular_total(100.00, 3, 50.00) == 250.00
print("As duas verificações passaram")
```

Arquivo completo: `aulas/aula06/aula06_valor_padrao.py` (23 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_print_contra_return.py`

O momento pedagógico da Aula 06.

```python
def soma_com_print(a, b):
    print(a + b)

def soma_com_return(a, b):
    return a + b

resultado_print = soma_com_print(2, 2)
resultado_return = soma_com_return(2, 2)

print(f"Com print, resultado_print vale: {resultado_print}")
print(f"Com return, resultado_return vale: {resultado_return}")

# Agora o erro que fecha o assunto. Usar numa conta o retorno de uma função que
# não retorna produz um nome de erro que vocês vão ver muito: NoneType.
# ...
```

Arquivo completo: `aulas/aula06/aula06_print_contra_return.py` (41 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_comando_e_pergunta.py`

As duas famílias de função, com nome.

```python
def registrar_evidencia(caso, resultado):
    print(f"[EVIDÊNCIA] {caso}: {resultado}")

def senha_tem_tamanho_minimo(senha):
    return len(senha) >= 8

# A de cima é comando: chamou, apareceu na tela, e nada volta.
registrar_evidencia("login válido", "passou")

# A de baixo é pergunta: chamou, guardou, e agora dá para comparar.
tamanho_ok = senha_tem_tamanho_minimo("JL12345!")
tamanho_curto = senha_tem_tamanho_minimo("JL1234!")

print(f"JL12345! tem 8 ou mais? {tamanho_ok}")
# ...
```

Arquivo completo: `aulas/aula06/aula06_comando_e_pergunta.py` (112 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_retorno_antecipado.py`

Chegou no `return`, acabou a função.

```python
def validar_cadastro(nome, email):
    print("  checando o nome...")
    if nome.strip() == "":
        return "nome obrigatório"
    print("  checando o e-mail...")
    if "@" not in email:
        return "e-mail inválido"
    print("  tudo checado")
    return "ok"

print("Chamada 1, nome vazio:")
sem_nome = validar_cadastro("", "gaia@teste.com")
print(f"  devolveu: {sem_nome}")

print("Chamada 2, e-mail sem arroba:")
# ...
```

Arquivo completo: `aulas/aula06/aula06_retorno_antecipado.py` (124 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_escopo.py`

Um quadrado dentro de outro:

```python
def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    return subtotal

total = calcular_total(10.00, 3)
print(f"Total: {total}")

# O subtotal existiu, fez o trabalho e foi embora. Não é bug: é o escopo
# funcionando. A mensagem do Python diz exatamente isso.
try:
    print(subtotal)
except NameError as erro:
    print(f"NameError: {erro}")

# ...
```

Arquivo completo: `aulas/aula06/aula06_escopo.py` (49 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_funcoes_da_loja.py`

Quatro funções, e nenhuma delas é conteúdo novo.

```python
def tem_frete_gratis(total):
    return total >= 250.00

# Este if é o mesmo de aulas/aula03/aula03_defeitos.py, que por sua vez veio do
# pseudocódigo de aulas/aula01/aula01_classificar_defeito.py. Nada mudou na
# lógica: o acréscimo é o def e o return, que é o que torna ela chamável.
def classificar_severidade(impede_producao, tem_workaround):
    if impede_producao and not tem_workaround:
        return "CRÍTICA"
    if impede_producao and tem_workaround:
        return "ALTA"
    return "MÉDIA"

# As mesmas faixas de aulas/aula04/aula04_classificar_status.py, onde elas
# ...
```

Arquivo completo: `aulas/aula06/aula06_funcoes_da_loja.py` (68 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_duas_funcoes.py`

O arquivo da primeira demonstração guiada da Aula 06, escrito ao vivo na frente da turma.

```python
def tem_frete_gratis(total):
    return total >= 250.00

def gerar_email_teste(nome):
    limpo = nome.strip().lower().replace(" ", ".")
    return f"{limpo}@qatest.com"

print(f"300 tem frete grátis? {tem_frete_gratis(300.00)}")
print(f"100 tem frete grátis? {tem_frete_gratis(100.00)}")
print(f"250 tem frete grátis? {tem_frete_gratis(250.00)}")
print(f"E-mail gerado: {gerar_email_teste('  Gaia Silva  ')}")

# O terceiro assert é o que vale mais: 250 é a fronteira da regra, e é lá que
# o >= se separa do >. Valor-limite se escolhe, não se sorteia.
# ...
```

Arquivo completo: `aulas/aula06/aula06_duas_funcoes.py` (30 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_login_while.py`

O `while` entra pelo requisito, e não como teoria:

```python
senha_correta = "JL1234!"
tentativas = ["errada1", "errada2", "JL1234!"]   # <- a massa

numero = 0
logou = False

while numero < len(tentativas) and not logou:
    senha = tentativas[numero]
    # Esta é a catraca do ônibus da Aula 04 de volta, com trabalho novo: ela é
    # o que garante que a condição um dia vira falsa. Ela vem ANTES de qualquer
    # if, então roda em toda volta. Apague esta linha e o terminal enche.
    # Esta linha é a catraca de aulas/aula04/aula04_catraca.py, igual letra por
    # letra. O acréscimo é o trabalho que ela faz aqui: lá ela contava, e aqui
    # ela é o que garante que a condição do while um dia vira falsa. Em
    # aulas/aula04/aula04_catraca_sem_incremento.py está o que acontece sem ela.
    numero = numero + 1
# ...
```

Arquivo completo: `aulas/aula06/aula06_login_while.py` (130 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_tentar_login.py`

O mesmo `while`, agora embalado numa função.

```python
def tentar_login(senha_correta, tentativas):
    numero = 0
    while numero < len(tentativas):
        senha = tentativas[numero]
        numero = numero + 1
        if senha == senha_correta:
            return numero
    return 0

acertou = tentar_login("JL1234!", ["errada1", "errada2", "JL1234!"])
bloqueou = tentar_login("JL1234!", ["errada1", "errada2", "errada3"])

print(f"Logou na tentativa: {acertou}")
print(f"Bloqueado, devolveu: {bloqueou}")

# ...
```

Arquivo completo: `aulas/aula06/aula06_tentar_login.py` (106 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_palindromo.py`

Função chamando função.

```python
def inverter(texto):
    invertido = ""
    for letra in texto:
        invertido = letra + invertido
    return invertido

def eh_palindromo(texto):
    limpo = texto.strip().lower().replace(" ", "")
    return limpo == inverter(limpo)

print(f"'abc' invertido: {inverter('abc')}")
print(f"'  Arara  ' é palíndromo? {eh_palindromo('  Arara  ')}")
print(f"'teste' é palíndromo? {eh_palindromo('teste')}")
frase = "Socorram me subi no onibus em Marrocos"
# ...
```

Arquivo completo: `aulas/aula06/aula06_palindromo.py` (42 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_email_valido.py`

A validação de e-mail da Aula 05, que era uma linha comprida perdida no meio de um arquivo, agora com nome, entrada e saída.

```python
def email_valido(email):
    limpo = email.strip().lower()
    partes = limpo.split("@")
    if len(partes) != 2:
        return False
    if partes[0] == "":
        return False
    if "." not in partes[1]:
        return False
    return True

print(f"  GAIA@Teste.COM   vale? {email_valido('  GAIA@Teste.COM  ')}")
print(f"beto@loja.com.br   vale? {email_valido('beto@loja.com.br')}")
print(f"gaia.teste.com     vale? {email_valido('gaia.teste.com')}")
print(f"@teste.com         vale? {email_valido('@teste.com')}")
# ...
```

Arquivo completo: `aulas/aula06/aula06_email_valido.py` (123 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_fechar_pedido.py`

O arquivo da segunda demonstração guiada da Aula 06, e o único do repositório em que uma função chama outras três.

```python
def calcular_subtotal(preco, quantidade):
    return preco * quantidade

def aplicar_desconto(subtotal, percentual):
    return subtotal - (subtotal * percentual / 100)

def calcular_frete(total, cliente_vip):
    if cliente_vip or total >= 250:
        return 0.0
    return 20.0

def fechar_pedido(preco, quantidade, percentual, cliente_vip):
    subtotal = calcular_subtotal(preco, quantidade)
# ...
```

Arquivo completo: `aulas/aula06/aula06_fechar_pedido.py` (54 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula06_senha_valida.py`

O extra de casa da Aula 06.

```python
def senha_valida(senha):
    if len(senha) < 8:
        return False
    tem_numero = False
    tem_maiuscula = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isupper():
            tem_maiuscula = True
    return tem_numero and tem_maiuscula

print(f"Senha123 vale? {senha_valida('Senha123')}")
print(f"JL1234!  vale? {senha_valida('JL1234!')}  (7 caracteres)")
print(f"jl123456 vale? {senha_valida('jl123456')}  (sem maiúscula)")
# ...
```

Arquivo completo: `aulas/aula06/aula06_senha_valida.py` (34 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.
