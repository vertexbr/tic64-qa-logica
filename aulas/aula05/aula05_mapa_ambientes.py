# Aula 05 - o mapa de ambientes
#
# Este é o dicionário que vocês vão usar mais do que qualquer outro, e ele não
# é dicionário de pessoa: é mapa de ambientes. Um teste, três endereços.
#
# Para apontar a suíte inteira para homologação, você troca UMA linha, a que
# define ambiente_atual, e nada mais. Guardem este arquivo: na Aula 10 ele
# volta como o endereço base das requisições.

ambientes = {
    "teste": "https://teste.loja.com",
    "homologacao": "https://homologacao.loja.com",
    "producao": "https://loja.com",
}

# Percorrer um dicionário com for entrega as CHAVES, não os valores, e é por
# isso que ambientes[nome] aparece dentro do laço para ver o endereço.
for nome in ambientes:
    print(f"{nome}: {ambientes[nome]}")

ambiente_atual = "teste"
url_base = ambientes[ambiente_atual]

print(f"Rodando a suíte contra: {url_base}")
print(f"Endereço de login: {url_base}/login")

# Esta linha existe em suíte de gente que já rodou teste de escrita em
# produção uma vez na vida. Ela é barata e evita a pior tarde da carreira.
assert ambiente_atual != "producao"
assert url_base == "https://teste.loja.com"
print("Verificações passaram: a suíte não está apontada para produção")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/aula05_mapa_ambientes.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo, a mesma da calha do PyCharm.
# Este arquivo NAO tem slide no deck: ele ficou no repositorio quando o
# slide dele foi cortado por tempo, e a explicacao vive aqui.
#
#      10  ambientes = {
#          Abre o mapa. Um teste, três endereços.
#
#      11  "teste": "https://teste.loja.com",
#          A chave é o nome do ambiente, o valor é a URL dele.
#
#      12  "homologacao": "https://homologacao.loja.com",
#          Chave sem acento e sem cedilha de propósito: nome de chave é dado
#          de código, e acento em chave é fonte de erro de digitação que só
#          aparece em runtime.
#
#      13  "producao": "https://loja.com",
#          A vírgula no último par é legal em Python e é hábito bom:
#          acrescentar uma linha depois não obriga a mexer nesta.
#
#      14  }
#          Fecha o mapa.
#
#      15  Linha em branco
#          Separa o mapa do laço.
#
#      18  for nome in ambientes:
#          Percorrer um dicionário com for entrega as CHAVES, não os valores.
#          É a pegadinha de sintaxe desta fatia, e ela surpreende quem
#          esperava os endereços.
#
#      19  print(f"{nome}: {ambientes[nome]}")
#          Sai uma linha por ambiente. É por isso que ambientes[nome] aparece
#          dentro do laço: a variável do for é a chave, e o valor se busca com
#          ela.
#
#      20  Linha em branco
#          Separa o laço da escolha do ambiente.
#
#      21  ambiente_atual = "teste"
#          Esta é a única linha que se troca para mudar de ambiente. Toda a
#          suíte passa a apontar para outro lugar, e nada mais no arquivo
#          muda.
#
#      22  url_base = ambientes[ambiente_atual]
#          Busca a URL do ambiente escolhido. O nome url_base é o mesmo que
#          volta na Aula 10 como o endereço base das requisições.
#
#      23  Linha em branco
#          Separa a escolha do uso.
#
#      24  print(f"Rodando a suíte contra: {url_base}")
#          Sai https://teste.loja.com. É a linha que um relatório de execução
#          real imprime no começo, e que evita a dúvida de contra qual
#          ambiente o teste rodou.
#
#      25  print(f"Endereço de login: {url_base}/login")
#          Sai https://teste.loja.com/login. Montar o caminho a partir da base
#          é o padrão que a Aula 10 usa em cada requisição.
#
# --- fim da explicacao linha a linha ---
