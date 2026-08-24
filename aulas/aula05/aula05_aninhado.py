# Aula 05 - cada colchete desce um andar
#
# Esta é a estrutura mais importante do curso, e é a que nenhum curso de
# Python que eu li demonstra: dicionário dentro de dicionário, e lista dentro
# de dicionário, no mesmo registro.
#
# Leia usuario['endereco']['cidade'] da esquerda para a direita, em voz alta:
# pega o usuário, dentro dele pega o endereço, dentro dele pega a cidade.
#
# Repare que perfis é uma LISTA dentro de um dicionário, e por isso ela volta
# a usar número. Os dois convivem, e quem decide qual você usa é o que está
# guardado ali, não o gosto.

usuario = {
    "id": 42,
    "nome": "Gaia Silva",
    "email": "  GAIA@Teste.COM  ",
    "situacao": "ativo",
    "perfis": ["admin", "editor"],
    "endereco": {"cidade": "Fortaleza", "uf": "CE"}
}

print(f"Cidade: {usuario['endereco']['cidade']}")
print(f"Primeiro perfil: {usuario['perfis'][0]}")
print(f"Quantidade de perfis: {len(usuario['perfis'])}")
print(f"É admin? {'admin' in usuario['perfis']}")

assert usuario["endereco"]["uf"] == "CE"
assert len(usuario["perfis"]) == 2
assert "admin" in usuario["perfis"]
print("As três verificações passaram")

# A regra chata de hoje, e ela aparece uma vez só na vida de cada um: dentro
# da f-string as chaves vão com aspas SIMPLES, porque a f-string já está
# delimitada por aspas duplas. Misturar as duas dá SyntaxError.
#
# O erro mais provável desta aula, e nenhum curso do acervo prevê ele: pedir a
# chave certa no andar errado. usuario["cidade"] devolve KeyError: 'cidade'
# mesmo com a cidade existindo, porque ela existe dentro de endereco, não na
# raiz. A mensagem aponta uma chave que existe no documento, só não ali.
# Antes de descer um andar, imprima o andar de fora sozinho e veja o que você
# tem na mão:
print(f"O andar de fora: {usuario['endereco']}")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-08.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 8 da apresentacao.
#
#      14  usuario = {
#          Abre o registro. Dicionário de várias linhas é a forma normal
#          quando os campos não caberiam numa linha só, e é a forma em que uma
#          resposta de API chega.
#
#      15  "id": 42,
#          Campo simples, valor número.
#
#      16  "nome": "Gaia Silva",
#          Campo simples, valor texto.
#
#      17  "email": "  GAIA@Teste.COM  ",
#          Campo sujo de propósito, com espaço nas duas pontas e maiúscula no
#          meio. Ele fica sujo aqui e é limpo no slide 16, e é a mesma pessoa
#          nos dois arquivos.
#
#      18  "situacao": "ativo",
#          Campo simples, e é ele que a demonstração guiada 2 vai validar.
#
#      19  "perfis": ["admin", "editor"],
#          Uma LISTA dentro do dicionário. É aqui que os dois modos de acesso
#          passam a conviver no mesmo registro.
#
#      20  "endereco": {"cidade": "Fortaleza", "uf": "CE"}
#          Um DICIONÁRIO dentro do dicionário. Sem vírgula no fim porque é o
#          último par.
#
#      21  }
#          Fecha o registro.
#
#      22  Linha em branco
#          Separa a massa das leituras.
#
#      23  print(f"Cidade: {usuario['endereco']['cidade']}")
#          Sai Fortaleza. Leia da esquerda para a direita, em voz alta: pega o
#          usuário, dentro dele pega o endereço, dentro dele pega a cidade.
#          Cada colchete desce um andar.
#
#      24  print(f"Primeiro perfil: {usuario['perfis'][0]}")
#          Sai admin. O primeiro colchete usa nome, porque usuario é
#          dicionário; o segundo usa número, porque perfis é lista. Esta é a
#          linha em que a turma congela, e é onde o mnemônico do dia é
#          recuperado em voz alta.
#
#      25  print(f"Quantidade de perfis: {len(usuario['perfis'])}")
#          Sai 2. O len da Aula 04 funciona igual, e o que ele conta é a lista
#          de dentro, não o dicionário de fora.
#
#      26  print(f"É admin? {'admin' in usuario['perfis']}")
#          Sai True. O in de lista da Aula 04, aplicado num andar de baixo.
#
#      27  Linha em branco
#          Separa as leituras das verificações.
#
#      28  assert usuario["endereco"]["uf"] == "CE"
#          Prova o acesso de dois andares. Fora da f-string as aspas voltam a
#          ser duplas, e é por isso que a regra das aspas simples vale só
#          dentro dela.
#
#      29  assert len(usuario["perfis"]) == 2
#          Prova o tamanho da lista de dentro.
#
#      30  assert "admin" in usuario["perfis"]
#          Prova a presença na lista de dentro.
#
#      31  print("As três verificações passaram")
#          Confirma que os três assert passaram.
#
#      43  print(f"O andar de fora: {usuario['endereco']}")
#          Sai o dicionário {'cidade': 'Fortaleza', 'uf': 'CE'} inteiro. Esta
#          linha é a técnica de diagnóstico do erro mais provável da aula:
#          antes de descer um andar, imprima o andar de fora sozinho e veja o
#          que você tem na mão.
#
# --- fim da explicacao linha a linha ---
