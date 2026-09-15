# Aula 11 - massa única por execução, que é a solução do problema da abertura
#
# O que estraga o teste é o e-mail fixo, então o e-mail não pode ser fixo. Ele precisa ser
# diferente em cada execução. O jeito mais simples aqui é usar um UUID, um identificador
# aleatório criado pela biblioteca padrão do Python.
#
# O prefixo continua como parâmetro porque dá contexto ao dado: cadastro, duplicado ou
# veredito. A unicidade vem do UUID, então duas chamadas com o mesmo prefixo continuam gerando
# e-mails diferentes. É isso que a última linha mostra.
#
# Existe outro caminho, e ele aparece em todo lugar: biblioteca de geração de dados falsos,
# com localização brasileira, que devolve nome, e-mail e endereço plausíveis. Ela é útil quando
# a massa precisa parecer real, para relatório ou demonstração. E vem com um alerta que quase
# nenhum material dá: gerador de dados falsos SORTEIA de uma lista, e sorteio repete. Se o seu
# teste depende de unicidade, some um UUID mesmo usando a biblioteca.
#
# Esta é a função da Aula 6 de novo: parâmetro entra, valor sai, e ela é usada em três lugares
# diferentes nos arquivos de teste desta aula.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cada execução do teste cria o próprio dado, e o e-mail é o que garante isso. O UUID torna
#   cada valor praticamente único, mesmo quando dois testes rodam no mesmo instante.
# Um contador em segundos não serve para isso: duas execuções concorrentes podem receber o
# mesmo valor. O UUID evita essa dependência do relógio.

from uuid import uuid4


def email_unico(prefixo):
    return f"{prefixo}.{uuid4().hex}@qa.com.br"


print(email_unico("cadastro"))
print(email_unico("duplicado"))
print(email_unico("cadastro") == email_unico("cadastro"))

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-10.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 10 da apresentacao.
#
#      26  from uuid import uuid4
#          Traz uuid4 da biblioteca padrão do Python. Não há pacote para
#          instalar.
#
#      29  def email_unico(prefixo):
#          A função da Aula 6 de novo: parâmetro entra, valor sai. Ela é usada
#          em três arquivos desta aula.
#
#      30  return f"{prefixo}.{uuid4().hex}@qa.com.br"
#          uuid4() cria um identificador aleatório. O .hex devolve 32
#          caracteres sem hífen, prontos para entrar no e-mail.
#
#      33  print(email_unico("cadastro"))
#          Um e-mail com o prefixo cadastro.
#
#      34  print(email_unico("duplicado"))
#          Outro prefixo e outro UUID. O prefixo explica o papel do dado; o
#          UUID garante a unicidade.
#
#      35  print(email_unico("cadastro") == email_unico("cadastro"))
#          Duas chamadas com o mesmo prefixo produzem e-mails diferentes:
#          False.
#
# --- fim da explicacao linha a linha ---
