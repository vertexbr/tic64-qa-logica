"""Suíte de autoverificação da atividade da Aula 08.

Esta é a primeira suíte de autoverificação do curso, e ela existe para você
descobrir sozinho se acertou, sem esperar a correção.

COMO USAR

1. Escreva a sua solução num arquivo chamado exatamente `regras_desconto.py`,
   com uma função chamada exatamente `calcular_desconto`, recebendo os quatro
   parâmetros nesta ordem:

       calcular_desconto(valor_compra, cliente_vip, cupom_valido, produto_em_promocao)

   A função tem que DEVOLVER o percentual com `return`. Função que só imprime
   devolve `None` e não é testável, que é a lição da Aula 06.

2. Salve o arquivo em `entregas/` na raiz do repositório. Se a pasta não
   existir, crie.

3. Rode, da raiz do repositório:

       pytest tests/test_desconto_aula08.py -v

Se aparecer `6 passed`, a sua função obedece a regra em todos os casos que a
atividade cobra. Se algum ficar vermelho, a mensagem diz a entrada, o esperado,
o obtido e a regra que aquele caso cobra. Leia a mensagem antes de mexer no
código: na maioria das vezes ela já diz o que está errado.

A REGRA QUE ESTA SUÍTE COBRA (critério de aceite CA-018, o mesmo da Aula 03)

    Cliente VIP com compra acima de R$ 200,00 recebe 20% de desconto.
    Cliente VIP com compra de até R$ 200,00 recebe 10%.
    Cupom válido ou produto em promoção, para cliente comum, recebe 5%.
    Nenhuma das condições acima: sem desconto.

SOBRE A FORMA DESTE ARQUIVO

São seis funções de teste quase idênticas, uma por caso, escritas na mão de
propósito. Repare no incômodo: muda o dado e o resultado esperado, e o resto é
copiado. Guarde esse incômodo, porque a Aula 09 é sobre colapsar as seis numa só.
"""
import importlib.util
import pathlib

import pytest

# Onde procurar a entrega. A primeira é a pasta que a atividade pede; as outras
# duas existem porque salvar na raiz e salvar dentro de tests/ são os dois
# enganos mais prováveis, e falhar por causa da pasta ensina a coisa errada.
RAIZ = pathlib.Path(__file__).resolve().parents[1]
CAMINHOS = (RAIZ / "entregas" / "regras_desconto.py",
            RAIZ / "regras_desconto.py",
            RAIZ / "tests" / "regras_desconto.py")

# A massa é fixa e desenhada à mão, não sorteada: valor-limite se escolhe. Os
# seis casos são os cinco CT da planilha da Aula 03 mais o cenário negativo que
# a atividade cobra, e cada linha traz um identificador legível, para o
# relatório dizer QUAL caso falhou em vez de mostrar um índice.
#
# CT-03 é o caso que separa quem leu a regra de quem leu o código: a regra diz
# ACIMA de 200, então 200 exato NÃO passa e cai no degrau de 10%.
CT01 = ("CT-01", "cliente VIP em compra acima de 200",
        (300.00, True, False, False), 20,
        "Cliente VIP com compra acima de R$ 200,00 recebe 20% de desconto.")
CT02 = ("CT-02", "cliente VIP em compra abaixo de 200",
        (150.00, True, False, False), 10,
        "Cliente VIP com compra de até R$ 200,00 recebe 10%.")
CT03 = ("CT-03", "cliente VIP em compra de exatamente 200",
        (200.00, True, False, False), 10,
        "A regra diz ACIMA de 200, então 200 exato não entra no degrau de 20% "
        "e cai no de 10%.")
CT04 = ("CT-04", "cliente comum com cupom válido",
        (180.00, False, True, False), 5,
        "Cupom válido ou produto em promoção, para cliente comum, recebe 5%.")
CT05 = ("CT-05", "cliente comum com produto em promoção",
        (180.00, False, False, True), 5,
        "Cupom válido ou produto em promoção, para cliente comum, recebe 5%.")
CT06 = ("CT-06", "cenário negativo: cliente comum sem cupom e sem promoção",
        (180.00, False, False, False), 0,
        "Nenhuma das condições acima: sem desconto. Este é o cenário negativo "
        "que a atividade cobra, e ele PASSA quando o desconto é zero.")

_ENTREGA = next((p for p in CAMINHOS if p.is_file()), None)

if _ENTREGA is None:
    pytest.skip(
        "A entrega da Aula 08 ainda não está no lugar. Crie o arquivo "
        "'entregas/regras_desconto.py' na raiz do repositório, com a função "
        "calcular_desconto(valor_compra, cliente_vip, cupom_valido, "
        "produto_em_promocao) devolvendo o percentual com return. Depois rode "
        "de novo.",
        allow_module_level=True)


def _carregar_funcao():
    """A função da sua entrega, ou uma mensagem dizendo o que faltou nela."""
    spec = importlib.util.spec_from_file_location("regras_desconto", _ENTREGA)
    modulo = importlib.util.module_from_spec(spec)
    # A mensagem sai do except e o pytest.fail acontece FORA dele, para o
    # relatório não abrir com "During handling of the above exception..." em
    # inglês antes do texto que o aluno precisa ler.
    nao_carregou = None
    try:
        spec.loader.exec_module(modulo)
    except Exception as erro:
        nao_carregou = f"{type(erro).__name__}: {erro}"

    if nao_carregou is not None:
        pytest.fail(
            f"O arquivo {_ENTREGA.name} não chegou a carregar: {nao_carregou}\n"
            f"O erro não é do teste, é do seu arquivo. Rode "
            f"'python {_ENTREGA.name}' na pasta dele e conserte antes de voltar aqui.",
            pytrace=False)
    if not hasattr(modulo, "calcular_desconto"):
        disponiveis = [n for n in dir(modulo) if not n.startswith("_")] or ["nenhuma"]
        pytest.fail(
            f"O arquivo {_ENTREGA.name} carregou, mas não tem uma função chamada "
            f"'calcular_desconto'. O nome precisa ser exatamente esse, porque é ele "
            f"que a suíte importa.\nO que existe no arquivo: {', '.join(disponiveis)}",
            pytrace=False)
    return modulo.calcular_desconto


def _conferir(caso):
    """Roda um caso e reprova com a entrada, o esperado, o obtido e a regra.

    ESPERADO vem da regra. OBTIDO vem do seu programa. CONFERE é a comparação
    entre os dois, e é ela que esta função faz.
    """
    identificador, descricao, entrada, esperado, regra = caso
    calcular_desconto = _carregar_funcao()
    valor_compra, cliente_vip, cupom_valido, produto_em_promocao = entrada

    # A mensagem sai do except e o pytest.fail acontece FORA dele, senão o
    # relatório imprime "During handling of the above exception..." antes do
    # texto em português, e a primeira coisa que o aluno lê volta a ser inglês.
    recusou_os_parametros = None
    obtido = None
    try:
        obtido = calcular_desconto(valor_compra, cliente_vip, cupom_valido,
                                   produto_em_promocao)
    except TypeError as erro:
        recusou_os_parametros = str(erro)

    if recusou_os_parametros is not None:
        pytest.fail(
            f"{identificador} · {descricao}\n"
            f"  A sua calcular_desconto não aceitou os quatro parâmetros na ordem que a\n"
            f"  atividade fixou: valor_compra, cliente_vip, cupom_valido, produto_em_promocao.\n"
            f"  O Python disse: {recusou_os_parametros}",
            pytrace=False)

    if obtido is None:
        pytest.fail(
            f"{identificador} · {descricao}\n"
            f"  A sua calcular_desconto devolveu None, que é o que acontece quando a\n"
            f"  função imprime o resultado em vez de devolver. Troque o print pelo\n"
            f"  return: é a lição da Aula 06, e sem return não há o que comparar.",
            pytrace=False)

    if not isinstance(obtido, (int, float)) or isinstance(obtido, bool):
        pytest.fail(
            f"{identificador} · {descricao}\n"
            f"  A sua calcular_desconto devolveu {obtido!r}, que é do tipo "
            f"{type(obtido).__name__}.\n"
            f"  O esperado é o percentual em número, como 20, e não em texto nem em\n"
            f"  booleano. Devolver \"20%\" quebra qualquer conta que venha depois.",
            pytrace=False)

    if obtido != esperado:
        pytest.fail(
            f"{identificador} · {descricao}\n"
            f"  entrada ..... valor_compra={valor_compra}, cliente_vip={cliente_vip}, "
            f"cupom_valido={cupom_valido}, produto_em_promocao={produto_em_promocao}\n"
            f"  esperado .... {esperado}\n"
            f"  obtido ...... {obtido}\n"
            f"  a regra ..... {regra}",
            pytrace=False)


def test_ct01_vip_acima_de_200_ganha_20():
    _conferir(CT01)


def test_ct02_vip_abaixo_de_200_ganha_10():
    _conferir(CT02)


def test_ct03_vip_em_200_exato_ganha_10():
    _conferir(CT03)


def test_ct04_comum_com_cupom_ganha_5():
    _conferir(CT04)


def test_ct05_comum_com_promocao_ganha_5():
    _conferir(CT05)


def test_ct06_comum_sem_nada_nao_ganha_desconto():
    _conferir(CT06)
