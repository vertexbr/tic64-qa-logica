"""Suíte de autoverificação da atividade da Aula 12.

Ela existe para você descobrir sozinho se acertou, sem esperar a correção. É a
primeira suíte do curso que roda contra a INTERFACE, não contra uma API: os
seus testes abrem um navegador de verdade contra o the-internet.herokuapp.com
e esta suíte só confirma que eles passam e que a atividade tem o mínimo de
cenários pedido.

COMO USAR

1. Escreva os seus testes num arquivo chamado exatamente
   `test_interacoes_web.py`, com cada função começando com `test_` e o nome
   descrevendo o cenário, em português.

2. Salve o arquivo em `entregas/` na raiz do repositório. Se a pasta não
   existir, crie.

3. Rode, da raiz do repositório:

       pytest tests/test_interface_aula12.py -v

Se aparecer `1 passed`, esta suíte achou o seu arquivo, coletou pelo menos
dois testes, e todos passaram de verdade contra a página escolhida. Se ela
falhar, a mensagem diz o que faltou.

Se aparecer `1 skipped`, ela não achou a sua entrega. Pulo não é reprovação: a
mensagem traz o caminho exato onde o arquivo precisa estar.

O QUE ESTA SUÍTE COBRA, E POR QUÊ

- Pelo menos dois casos de teste coletados, um por cenário pedido no
  enunciado (a página de caixas de seleção OU a de lista de opções).
- Todos os testes do seu arquivo rodam de verdade, num processo separado,
  contra o navegador real. Não existe massa fixa aqui para comparar: o teste
  que você escreveu é o produto sendo avaliado.
- Pelo menos uma chamada de `expect` em cada caso. Teste sem validação é robô
  de tarefa, e isso vale desde a primeira aula.

O QUE ESTA SUÍTE NÃO COBRA, PORQUE É LEITURA HUMANA

- Se antes de cada locator existe um comentário com o número que o console
  deu. Isso é o critério de correção que o professor lê, não algo que dá
  para verificar automaticamente sem repetir a contagem por você.
- Se o locator escolhido é o mais simples que identifica um único elemento,
  ou um que só funciona por sorte hoje.
"""
import ast
import pathlib
import re
import subprocess
import sys

import pytest

RAIZ = pathlib.Path(__file__).resolve().parents[1]
CAMINHOS = (RAIZ / "entregas" / "test_interacoes_web.py",
            RAIZ / "test_interacoes_web.py",
            RAIZ / "tests" / "test_interacoes_web.py")

MINIMO_DE_CASOS = 2

_ENTREGA = next((p for p in CAMINHOS if p.is_file()), None)

_FALTA = (
    "A entrega da Aula 12 ainda não está no lugar. Crie o arquivo "
    "'entregas/test_interacoes_web.py' na raiz do repositório, com pelo "
    "menos duas funções começando com 'test_'. Depois rode de novo.")


def _pytest_na_entrega(*extra):
    """Roda o pytest no arquivo do aluno, num processo separado.

    Processo separado por dois motivos: as opcoes do pytest.ini deste
    repositorio nao interferem, e um erro de coleta no arquivo do aluno nao
    derruba esta suite junto.
    """
    return subprocess.run(
        [sys.executable, "-m", "pytest", str(_ENTREGA),
         "-p", "no:cacheprovider", "--no-header", *extra],
        cwd=RAIZ, capture_output=True, text=True,
        encoding="utf-8", errors="replace")


def _ultimas_linhas(texto, quantas=25):
    linhas = [l for l in texto.splitlines() if l.strip()]
    return "\n".join(linhas[-quantas:])


def test_a_entrega_tem_pelo_menos_dois_testes_e_todos_passam():
    # O pulo acontece DENTRO do teste, e nao no modulo, pela mesma razao da
    # suite da Aula 11: pytest.skip de modulo sai com exit code 5, que a IDE
    # le como execucao quebrada. Assim ela coleta o item, pula, e sai com 0.
    if _ENTREGA is None:
        pytest.skip(_FALTA)

    coleta = _pytest_na_entrega("--collect-only", "-q")
    # Mesmo padrao da suite da Aula 11: nao pode exigir \S+ depois do ::,
    # porque ids legiveis de parametrize trazem espaco dentro.
    casos = re.findall(r"^\S+\.py::.+$", coleta.stdout, re.M)

    if coleta.returncode != 0 and not casos:
        pytest.fail(
            f"O pytest não conseguiu coletar os testes de {_ENTREGA.name}. "
            f"O erro não é desta suíte, é do seu arquivo: rode "
            f"'pytest {_ENTREGA.relative_to(RAIZ).as_posix()} -v' e conserte "
            f"antes de voltar aqui.\n\n{_ultimas_linhas(coleta.stdout)}",
            pytrace=False)

    if len(casos) < MINIMO_DE_CASOS:
        achados = "\n".join(f"  {c}" for c in casos) or "  nenhum"
        pytest.fail(
            f"{_ENTREGA.name} tem {len(casos)} caso(s) de teste, e a "
            f"atividade pede pelo menos {MINIMO_DE_CASOS}: um cenário para "
            f"cada ação pedida na página escolhida.\nCasos coletados:\n"
            f"{achados}",
            pytrace=False)

    execucao = _pytest_na_entrega("-v")

    if execucao.returncode != 0:
        pytest.fail(
            f"O pytest rodou os {len(casos)} caso(s) de {_ENTREGA.name} "
            f"contra o navegador e não terminou verde. O relatório dele está "
            f"abaixo, e a linha do 'short test summary info' diz qual caso "
            f"quebrou.\n\n{_ultimas_linhas(execucao.stdout)}",
            pytrace=False)

    fonte = _ENTREGA.read_text(encoding="utf-8")
    arvore = ast.parse(fonte, filename=str(_ENTREGA))
    casos_sem_expect = []
    for funcao in (n for n in ast.walk(arvore)
                   if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                   and n.name.startswith("test_")):
        tem_expect = any(
            isinstance(no, ast.Call)
            and isinstance(no.func, ast.Name)
            and no.func.id == "expect"
            for no in ast.walk(funcao))
        if not tem_expect:
            casos_sem_expect.append(funcao.name)

    if casos_sem_expect:
        lista = ", ".join(casos_sem_expect)
        pytest.fail(
            f"{_ENTREGA.name} passou, mas estes casos não têm chamada de "
            f"'expect(...)': {lista}. Cada cenário precisa terminar com uma "
            f"validação; acrescente pelo menos um expect em cada função.",
            pytrace=False)

    print(f"\n{len(casos)} caso(s) de teste em {_ENTREGA.name}, todos passaram:")
    for caso in casos:
        print(f"  {caso}")
