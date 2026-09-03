"""Suíte de autoverificação da atividade da Aula 09.

Ela existe para você descobrir sozinho se acertou, sem esperar a correção. É a
segunda do curso, e ela julga uma coisa diferente da primeira: a da Aula 08
julgava o seu CÓDIGO, esta julga a sua MASSA DE TESTE.

COMO USAR

1. Abra `aulas/aula09/aula09_massa_notas.csv`. É a planilha de casos que o time
   de negócio mandou, com quatro linhas, e ela testa só o meio de cada faixa.

2. Escreva a SUA massa num arquivo chamado exatamente `massa_aula09.csv`, com
   as mesmas três colunas e o mesmo separador ponto e vírgula:

       id;nota;esperado

   Uma linha por caso, e o `id` é o nome que vai aparecer entre colchetes no
   relatório. Nome de caso é diagnóstico: `fronteira_70_entra` diz o que
   quebrou, `caso_3` não diz nada.

3. Salve o arquivo em `entregas/` na raiz do repositório. Se a pasta não
   existir, crie.

4. Rode, da raiz do repositório:

       pytest tests/test_massa_aula09.py -v

O que aparece verde é a sua massa rodando de verdade contra a regra, uma linha
por vez, com o SEU nome em cada uma. É o mesmo relatório que a aula mostrou.

A REGRA QUE A SUA MASSA PRECISA COBRIR

    Nota de 90 para cima é "excelente".
    De 80 a 89 é "bom".
    De 70 a 79 é "suficiente".
    Abaixo de 70 é "insuficiente".

    def classificar_nota(nota):
        if nota >= 90:
            return "excelente"
        if nota >= 80:
            return "bom"
        if nota >= 70:
            return "suficiente"
        return "insuficiente"

O QUE ESTA SUÍTE COBRA, E POR QUÊ

- Três fronteiras, três pares. A regra tem 70, 80 e 90 escritos nela, e cada
  fronteira pede o próprio valor e o vizinho de baixo. São seis linhas
  obrigatórias, e é onde o defeito mora.
- Todo `esperado` correto. Massa com linha inválida esperando falhar é entrega
  recusada: o esperado é a última coluna, e a suíte fica toda verde. Falha
  significa defeito, nunca "essa linha era pra falhar".
- Massa enxuta. Entre 6 e 10 linhas. Cinco notas na mesma partição são cinco
  testes rodando e uma informação só.
- `id` legível e único em cada linha.
"""
import csv
import pathlib

import pytest

# Onde procurar a entrega. A primeira é a pasta que a atividade pede; as outras
# duas existem porque salvar na raiz e salvar dentro de tests/ são os dois
# enganos mais prováveis, e falhar por causa da pasta ensina a coisa errada.
RAIZ = pathlib.Path(__file__).resolve().parents[1]
CAMINHOS = (RAIZ / "entregas" / "massa_aula09.csv",
            RAIZ / "massa_aula09.csv",
            RAIZ / "tests" / "massa_aula09.csv")

# As três fronteiras da regra, cada uma com o par que ela obriga: o vizinho de
# baixo e o valor da fronteira. Escolhidas à mão, não sorteadas, porque
# valor-limite se escolhe.
FRONTEIRAS = ((69, 70), (79, 80), (89, 90))

MINIMO_DE_LINHAS = 6
MAXIMO_DE_LINHAS = 10

_ENTREGA = next((p for p in CAMINHOS if p.is_file()), None)

if _ENTREGA is None:
    pytest.skip(
        "A entrega da Aula 09 ainda não está no lugar. Crie o arquivo "
        "'entregas/massa_aula09.csv' na raiz do repositório, com as colunas "
        "id;nota;esperado separadas por ponto e vírgula, uma linha por caso de "
        "teste. Use 'aulas/aula09/aula09_massa_notas.csv' como modelo de "
        "formato. Depois rode de novo.",
        allow_module_level=True)


def classificar_nota(nota):
    """A regra, escrita aqui para a suíte não depender da sua cópia dela.

    É a mesma de aulas/aula09/aula09_regras.py, sem uma vírgula de diferença.
    """
    if nota >= 90:
        return "excelente"
    if nota >= 80:
        return "bom"
    if nota >= 70:
        return "suficiente"
    return "insuficiente"


def _ler_entrega():
    """A sua massa, ou uma mensagem dizendo o que faltou no arquivo."""
    # A mensagem sai do except e o pytest.fail acontece FORA dele, para o
    # relatório não abrir com "During handling of the above exception..." em
    # inglês antes do texto que você precisa ler.
    nao_abriu = None
    linhas = []
    try:
        with _ENTREGA.open(encoding="utf-8-sig", newline="") as f:
            leitor = csv.DictReader(f, delimiter=";")
            colunas = leitor.fieldnames
            linhas = list(leitor)
    except Exception as erro:
        nao_abriu = f"{type(erro).__name__}: {erro}"

    if nao_abriu is not None:
        pytest.fail(
            f"O arquivo {_ENTREGA.name} não chegou a ser lido: {nao_abriu}\n"
            f"Salve como texto puro, com codificação UTF-8, e não como planilha "
            f"do Excel renomeada.",
            pytrace=False)

    esperadas = ["id", "nota", "esperado"]
    if colunas is None or [c.strip() for c in colunas] != esperadas:
        pytest.fail(
            f"A primeira linha do {_ENTREGA.name} precisa ser exatamente o "
            f"cabeçalho 'id;nota;esperado'.\n"
            f"  esperado .... {esperadas}\n"
            f"  obtido ...... {colunas}\n"
            f"  Se saiu tudo numa coluna só, o separador está errado: é ponto e "
            f"vírgula, não vírgula.",
            pytrace=False)
    if not linhas:
        pytest.fail(
            f"O {_ENTREGA.name} tem o cabeçalho e nenhuma linha de caso abaixo "
            f"dele. A massa é o conteúdo da entrega.",
            pytrace=False)
    return linhas


def _converter(linhas):
    """Transforma o texto do CSV nos tipos certos, reclamando com a linha exata.

    Tudo que sai de arquivo de texto chega como texto, inclusive número. Essa
    conversão não é detalhe de implementação: é a armadilha da massa em arquivo.
    """
    massa = []
    for numero, linha in enumerate(linhas, start=2):
        bruto = (linha.get("nota") or "").strip()
        identificador = (linha.get("id") or "").strip()
        esperado = (linha.get("esperado") or "").strip()

        nota_invalida = None
        nota = None
        try:
            nota = int(bruto)
        except ValueError as erro:
            nota_invalida = str(erro)

        if nota_invalida is not None:
            pytest.fail(
                f"Linha {numero} do {_ENTREGA.name}: a coluna 'nota' precisa ser um "
                f"número inteiro, e veio {bruto!r}.\n"
                f"  O Python disse: {nota_invalida}",
                pytrace=False)
        massa.append((identificador, nota, esperado, numero))
    return massa


_LINHAS = _ler_entrega()
_MASSA = _converter(_LINHAS)

# A massa da SUA entrega alimenta o parametrize abaixo, com os SEUS ids. É o
# mesmo mecanismo da aula: uma função de teste, uma linha por caso, e o nome de
# cada linha aparecendo no relatório.
_IDS = [f"{item[0] or 'linha_' + str(item[3])}" for item in _MASSA]


@pytest.mark.parametrize("identificador,nota,esperado,numero", _MASSA, ids=_IDS)
def test_cada_linha_da_massa_tem_o_esperado_certo(identificador, nota, esperado, numero):
    """O esperado de cada linha bate com o que a regra manda.

    Este é o teste que recusa a massa com dado inválido esperando falhar. Se ele
    ficar vermelho, a linha está errada na SUA planilha, e não no produto.
    """
    correto = classificar_nota(nota)
    if esperado != correto:
        pytest.fail(
            f"Linha {numero} do {_ENTREGA.name}, caso '{identificador}'\n"
            f"  entrada ..... nota={nota}\n"
            f"  esperado .... {esperado!r}, que foi o que você escreveu\n"
            f"  correto ..... {correto!r}, que é o que a regra manda\n"
            f"  a regra ..... 90 para cima é excelente, 80 a 89 é bom, 70 a 79 é\n"
            f"                suficiente, abaixo de 70 é insuficiente.\n"
            f"  Se você escreveu essa linha esperando que ela falhasse, é esse o\n"
            f"  hábito que a aula pede para largar: o esperado é a última coluna, e\n"
            f"  a suíte fica toda verde.",
            pytrace=False)


def test_as_tres_fronteiras_estao_cobertas():
    """Cada número escrito na regra pede o próprio valor e o vizinho de baixo."""
    notas = {nota for _i, nota, _e, _n in _MASSA}
    faltando = []
    for vizinho, fronteira in FRONTEIRAS:
        if fronteira not in notas:
            faltando.append(f"{fronteira} (a fronteira em si)")
        if vizinho not in notas:
            faltando.append(f"{vizinho} (o vizinho de baixo de {fronteira})")

    if faltando:
        pytest.fail(
            "A sua massa não cobre as três fronteiras da regra.\n"
            "  notas que você escolheu ... " + ", ".join(str(n) for n in sorted(notas)) + "\n"
            "  o que falta ............... " + "; ".join(faltando) + "\n"
            "  a regra ................... a regra tem 70, 80 e 90 escritos nela.\n"
            "                              Achou um número no critério de aceite,\n"
            "                              teste o número e o anterior. É onde o >=\n"
            "                              trocado por > aparece, e é o defeito mais\n"
            "                              comum que existe.",
            pytrace=False)


def test_a_massa_e_enxuta():
    """Cada linha da massa é um teste a mais rodando, e repetição não informa."""
    quantidade = len(_MASSA)
    if quantidade < MINIMO_DE_LINHAS:
        pytest.fail(
            f"A sua massa tem {quantidade} linhas, e as três fronteiras sozinhas já\n"
            f"  pedem {MINIMO_DE_LINHAS}: 69, 70, 79, 80, 89 e 90.",
            pytrace=False)
    if quantidade > MAXIMO_DE_LINHAS:
        # Duas notas na mesma faixa testam a mesma coisa duas vezes.
        por_faixa = {}
        for _i, nota, _e, _n in _MASSA:
            por_faixa.setdefault(classificar_nota(nota), []).append(nota)
        repetidas = {faixa: sorted(ns) for faixa, ns in por_faixa.items() if len(ns) > 3}
        pytest.fail(
            f"A sua massa tem {quantidade} linhas, e o teto desta atividade é "
            f"{MAXIMO_DE_LINHAS}.\n"
            f"  por faixa ... {por_faixa}\n"
            f"  faixas com sobra ... {repetidas or 'nenhuma óbvia, revise linha a linha'}\n"
            f"  a regra ..... notas na mesma faixa se comportam igual, então testar\n"
            f"                75 e 76 é testar a mesma coisa duas vezes. Se você não\n"
            f"                consegue dizer o que uma linha testa que as outras não\n"
            f"                testam, apague a linha.",
            pytrace=False)


def test_cada_linha_tem_um_id_legivel_e_unico():
    """O id é o que faz o relatório dizer QUAL caso falhou."""
    identificadores = [i for i, _n, _e, _num in _MASSA]

    vazios = [numero for i, _n, _e, numero in _MASSA if not i]
    if vazios:
        pytest.fail(
            "Estas linhas estão sem 'id': " + ", ".join(str(v) for v in vazios) + "\n"
            "  Sem o id o relatório mostra o índice da linha, e 'caso 3 falhou' não\n"
            "  diz nada para quem abre o relatório sem ter escrito a massa.",
            pytrace=False)

    repetidos = sorted({i for i in identificadores if identificadores.count(i) > 1})
    if repetidos:
        pytest.fail(
            "Estes 'id' aparecem em mais de uma linha: " + ", ".join(repetidos) + "\n"
            "  Dois casos com o mesmo nome tornam o relatório ambíguo, que é\n"
            "  exatamente o problema que o id existe para resolver.",
            pytrace=False)

    numericos = sorted(i for i in identificadores if i.isdigit())
    if numericos:
        pytest.fail(
            "Estes 'id' são só número: " + ", ".join(numericos) + "\n"
            "  Número é o que o pytest já mostraria sozinho. O id serve para dizer o\n"
            "  que a linha exercita, como 'fronteira_70_entra' ou 'vizinho_de_baixo_69'.",
            pytrace=False)
