# Aula 10 - o primeiro GET contra uma API de verdade, e a lista de status ao vivo
#
# A BASE_URL numa variável no topo é o mapa de ambientes da Aula 5 aparecendo de novo: um
# teste, e você troca de ambiente mudando uma linha. O timeout=10 diz ao Requests para
# desistir depois de dez segundos, e sem ele um servidor travado deixa o programa pendurado
# para sempre.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Uma requisição GET consulta e não altera nada. Toda resposta traz status, cabeçalhos e
#   corpo. O timeout de 10 segundos é o que impede o teste de ficar pendurado para sempre.
#   Status 200 é sucesso, 4xx é erro do cliente e 5xx é erro do servidor.

import requests

BASE_URL = "https://serverest.dev"

resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)

print(f"Status code: {resposta.status_code}")
print(f"Content-Type: {resposta.headers.get('Content-Type')}")

# A lista de status da Aula 4 volta, só que agora os números vieram de um servidor de verdade em
# vez de terem sido digitados por mim. O código que classifica essa lista não muda uma vírgula.
urls = [
    f"{BASE_URL}/usuarios",
    f"{BASE_URL}/usuariosss",                      # rota que não existe
    f"{BASE_URL}/usuarios/aaaaaaaaaaaaaaaa",        # formato certo, usuário que não existe
    "https://httpbin.org/status/500",               # 5xx de propósito, erro do servidor
]

codigos_status = []
for url in urls:
    codigos_status.append(requests.get(url, timeout=10).status_code)

print(codigos_status)

# --- fim ---
#
# Saída conferida contra a API real em 08/09/2026: Status code: 200, Content-Type:
# application/json; charset=utf-8, e a lista de status fecha em [200, 405, 400, 500]. Esses
# quatro números não mudam, porque as quatro URLs batem em contratos fixos da API. O que muda a
# cada execução é a quantidade de usuários, que este arquivo não imprime: a instância é pública
# e compartilhada, isso não é defeito, e é o assunto da Aula 11.
