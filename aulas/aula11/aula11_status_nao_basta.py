# Aula 11 - duzentos, e nada foi excluído
#
# Este é o melhor argumento que existe contra validar só o status, e ele é real: não é exemplo
# inventado. O servidor responde 200 para uma exclusão que não excluiu nada, e ele está sendo
# honesto, porque a mensagem diz exatamente isso. Um teste que só olhasse o número teria
# escrito "exclusão validada" no relatório sem que nada tivesse sido apagado.
#
# Separe os dois tipos de validação e use o nome dos dois. Validação técnica: o campo existe,
# o tipo está certo, o status está na faixa. Validação funcional: o valor obedece à regra de
# negócio. Um teste que só faz a técnica aprova sistema quebrado com elegância.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Excluir um identificador que não existe responde 200 com a mensagem Nenhum registro
#   excluído. O número diz sucesso e nada foi apagado, então quem separa os dois casos é o
#   corpo da resposta, nunca o status sozinho.

import requests

BASE_URL = "https://serverest.dev"
ID_INEXISTENTE = "aaaaaaaaaaaaaaaa"

apagar = requests.delete(f"{BASE_URL}/usuarios/{ID_INEXISTENTE}", timeout=10)

print(f"Status: {apagar.status_code}")
print(f"Mensagem: {apagar.json()['message']}")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-07.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 7 da apresentacao.
#
#      17  import requests
#          Nada de novo.
#
#      19  BASE_URL = "https://serverest.dev"
#          Nada de novo.
#
#      20  ID_INEXISTENTE = "aaaaaaaaaaaaaaaa"
#          Dezesseis letras a. O formato é o mesmo dos identificadores de
#          verdade, então a API aceita o formato e vai procurar. Um
#          identificador com formato errado seria recusado antes, por outro
#          motivo, e a demonstração não funcionaria.
#
#      22  apagar = requests.delete(f"{BASE_URL}/usuarios/{ID_INEXISTENTE}",
#          timeout=10)
#          O DELETE vai à rede. O servidor procura, não acha, e responde mesmo
#          assim.
#
#      24  print(f"Status: {apagar.status_code}")
#          200.
#
#      25  print(f"Mensagem: {apagar.json()['message']}")
#          Nenhum registro excluído.
#
# --- fim da explicacao linha a linha ---
