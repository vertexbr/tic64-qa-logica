# Aula 09 - o teste que prova que o Playwright ficou instalado
#
# Ele NÃO é aula de Playwright. Hoje ele existe para você ver "1 passed" na
# tela e saber que a sua máquina está pronta para a Aula 12. De onde vem a
# page, o que é get_by_role e o que é expect são assunto daquela aula.
#
# Antes de rodar este arquivo, os dois comandos precisam ter terminado:
#
#     pip install pytest-playwright
#     playwright install chromium
#
# O primeiro instala a biblioteca. O segundo baixa o navegador que ela vai
# dirigir, e é um download grande. São coisas diferentes.
#
# O endereço é um site público de treino, mantido para estudo de automação. Se
# ele estiver fora do ar o teste falha por tempo esgotado, e aí o problema não
# é seu: abra o endereço no navegador para confirmar.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O ambiente está pronto quando este teste sai com 1 passed. Não é regra de
#   produto: é o critério de aceite da instalação de hoje, e é a única coisa
#   que precisa estar verdadeira na sua máquina antes da Aula 12.
from playwright.sync_api import Page, expect


def test_abre_pagina_de_treino(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-26.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 26 da apresentacao.
#
#      23  from playwright.sync_api import Page, expect
#          O mesmo from ... import da Aula 06, agora trazendo duas coisas de
#          uma biblioteca instalada em vez de um arquivo ao lado. Se esta
#          linha der ModuleNotFoundError, o pip install pytest-playwright não
#          completou.
#
#      26  def test_abre_pagina_de_treino(page: Page):
#          Uma função de teste, com o test_ de sempre. O parâmetro page não
#          vem de massa nenhuma, e é aí que ele é diferente de tudo que você
#          viu hoje: quem entrega ele é o plugin pytest-playwright. A
#          explicação disso tem data, e é a Aula 12.
#
#      27  page.goto("https://the-internet.herokuapp.com/login")
#          Abre o navegador, num processo separado, e navega até o endereço. É
#          a linha que leva a maior parte dos segundos da execução.
#
#      28  expect(page.get_by_role("heading", name="Login
#          Page")).to_be_visible()
#          A validação. Ela procura na página um título com o texto Login Page
#          e confere que ele está visível. Se não achar, ela espera um tempo
#          antes de reprovar, e essa espera automática é metade do motivo de o
#          curso usar Playwright.
#
# --- fim da explicacao linha a linha ---
