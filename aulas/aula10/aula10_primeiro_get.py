# Aula 10 - o primeiro GET contra uma API de verdade, e a lista de status ao vivo
#
# A BASE_URL numa variavel no topo e o mapa de ambientes da Aula 5 aparecendo de novo: um teste, e
# voce troca de ambiente mudando uma linha. O timeout=10 diz ao Requests para desistir depois de
# dez segundos, e sem ele um servidor travado deixa o programa pendurado para sempre.
import requests

BASE_URL = "https://serverest.dev"

resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)

print(f"Status code: {resposta.status_code}")
print(f"Content-Type: {resposta.headers.get('Content-Type')}")

# A lista de status da Aula 4 volta, so que agora os numeros vieram de um servidor de verdade em
# vez de terem sido digitados por mim. O codigo que classifica essa lista nao muda uma virgula.
urls = [
    f"{BASE_URL}/usuarios",
    f"{BASE_URL}/usuariosss",                      # rota que nao existe
    f"{BASE_URL}/usuarios/aaaaaaaaaaaaaaaa",        # id com formato certo, usuario que nao existe
    "https://httpbin.org/status/500",               # 5xx de proposito, para mostrar erro do servidor
]

codigos_status = []
for url in urls:
    codigos_status.append(requests.get(url, timeout=10).status_code)

print(codigos_status)

# --- fim ---
#
# Saida esperada no dia em que este arquivo foi escrito (verificado contra a API real em
# 08/09/2026): Status code: 200, Content-Type: application/json; charset=utf-8, e a lista de
# status fecha em [200, 405, 400, 500]. A quantidade de usuarios muda a cada execucao porque a
# instancia e publica e compartilhada: isso nao e defeito, e o assunto da Aula 11.
