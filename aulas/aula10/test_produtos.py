# Aula 10 - segundo bloco de pratica: produtos, estrutura e o primeiro cenario negativo
#
# Rodar de dentro da pasta: pytest test_produtos.py -v
# Rodar da raiz do repositorio: pytest aulas/aula10/test_produtos.py -v
#
# Os dois ultimos testes sao o gabarito do desafio extra, para quem terminou antes.
import requests

BASE_URL = "https://serverest.dev"


def test_listar_produtos_retorna_200():
    resposta = requests.get(f"{BASE_URL}/produtos", timeout=10)
    assert resposta.status_code == 200


def test_lista_de_produtos_tem_estrutura_esperada():
    resposta = requests.get(f"{BASE_URL}/produtos", timeout=10)
    assert resposta.status_code == 200

    dados = resposta.json()
    assert "quantidade" in dados
    assert "produtos" in dados
    assert dados["quantidade"] == len(dados["produtos"])


def test_produto_tem_campos_obrigatorios():
    resposta = requests.get(f"{BASE_URL}/produtos", timeout=10)
    assert resposta.status_code == 200

    produto = resposta.json()["produtos"][0]
    assert "nome" in produto
    assert "preco" in produto
    assert isinstance(produto["preco"], int), f"preço veio como {type(produto['preco'])}"


def test_buscar_usuario_com_id_invalido_retorna_400():
    resposta = requests.get(f"{BASE_URL}/usuarios/id_invalido", timeout=10)
    assert resposta.status_code == 400
    assert "id" in resposta.json()


# --- gabarito do desafio extra ---

def test_nenhum_produto_tem_preco_invalido():
    resposta = requests.get(f"{BASE_URL}/produtos", timeout=10)
    assert resposta.status_code == 200

    for produto in resposta.json()["produtos"]:
        assert produto["preco"] > 0, f"produto {produto['nome']} com preço {produto['preco']}"


def test_usuario_inexistente_avisa_que_nao_encontrou():
    resposta = requests.get(f"{BASE_URL}/usuarios/aaaaaaaaaaaaaaaa", timeout=10)
    assert resposta.status_code == 400
    assert resposta.json()["message"] == "Usuário não encontrado"
