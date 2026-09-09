# Aula 11 - massa única por execução, que é a solução do problema da abertura
#
# O que estraga o teste é o e-mail fixo, então o e-mail não pode ser fixo. Ele precisa ser
# diferente em cada execução, e o jeito mais simples que existe é colar a marca de tempo:
# int(time.time()) é a quantidade de segundos desde o começo de 1970, e nunca repete, porque
# o tempo não volta.
#
# O prefixo é parâmetro por um motivo medido, e não por elegância: a marca de tempo tem
# precisão de SEGUNDO. Dois testes que rodam dentro do mesmo segundo geram o mesmo número, e é
# isso que a última linha mostra. Prefixo diferente por teste resolve, sem nada novo.
#
# Existe outro caminho, e ele aparece em todo lugar: biblioteca de geração de dados falsos,
# com localização brasileira, que devolve nome, e-mail e endereço plausíveis. Ela é útil quando
# a massa precisa parecer real, para relatório ou demonstração. E vem com um alerta que quase
# nenhum material dá: gerador de dados falsos SORTEIA de uma lista, e sorteio repete. Se o seu
# teste depende de unicidade, some a marca de tempo mesmo usando a biblioteca.
#
# Esta é a função da Aula 6 de novo: parâmetro entra, valor sai, e ela é usada em três lugares
# diferentes nos arquivos de teste desta aula.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cada execução do teste cria o próprio dado, e o e-mail é o que garante isso. A marca de
#   tempo em segundos nunca repete entre execuções, e o prefixo é o que separa dois testes que
#   rodam dentro do mesmo segundo.

import time


def email_unico(prefixo):
    return f"{prefixo}.{int(time.time())}@qa.com.br"


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
#      26  import time
#          Biblioteca padrão do Python, nada para instalar.
#
#      29  def email_unico(prefixo):
#          A função da Aula 6 de novo: parâmetro entra, valor sai. Ela é usada
#          em três arquivos desta aula.
#
#      30  return f"{prefixo}.{int(time.time())}@qa.com.br"
#          time.time() devolve os segundos desde o começo de 1970, com casas
#          decimais. O int() corta as casas e deixa o número inteiro, que é a
#          Aula 2.
#
#      33  print(email_unico("cadastro"))
#          Um e-mail com o prefixo cadastro.
#
#      34  print(email_unico("duplicado"))
#          Outro prefixo, e o mesmo número, porque as duas chamadas
#          aconteceram dentro do mesmo segundo.
#
#      35  print(email_unico("cadastro") == email_unico("cadastro"))
#          Duas chamadas com o mesmo prefixo, no mesmo segundo: True. É por
#          isso que o prefixo é parâmetro.
#
# --- fim da explicacao linha a linha ---
