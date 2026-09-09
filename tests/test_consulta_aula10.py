"""Suíte de autoverificação da atividade da Aula 10.

Ela existe para você descobrir sozinho se acertou, sem esperar a correção. É a
terceira do curso, e ela julga uma coisa diferente das duas primeiras: a da
Aula 08 julgava o seu CÓDIGO, a da Aula 09 julgava a sua MASSA, esta roda os
SEUS TESTES de verdade contra a API real e confere que todos passaram.

COMO USAR

1. Escreva os seus três testes num arquivo chamado exatamente
   `test_consulta_serverest.py`, com cada função começando com `test_` e o
   nome descrevendo o caso, em português.

2. Salve o arquivo em `entregas/` na raiz do repositório. Se a pasta não
   existir, crie.

3. Rode, da raiz do repositório:

       pytest tests/test_consulta_aula10.py -v

Se aparecer `1 passed`, esta suíte achou o seu arquivo, coletou pelo menos três
testes e todos passaram de verdade contra o ServeRest. Se ela falhar, a
mensagem diz o que faltou: arquivo não encontrado, menos de três testes, ou o
relatório do pytest apontando qual teste não passou e por quê.

O QUE ESTA SUÍTE COBRA, E POR QUÊ

- Pelo menos três casos de teste coletados. É a quantidade que a atividade
  pede: produto existente, produto inexistente, filtro por nome. Quem escrever
  um `@pytest.mark.parametrize` da Aula 09 conta cada linha da massa como um
  caso, porque é assim que o pytest conta.
- Todos os testes do seu arquivo rodam de verdade, contra a API real, e
  precisam passar. Não existe massa fixa aqui para comparar: o teste que você
  escreveu é o produto sendo avaliado, então rodá-lo é a única forma de saber
  se ele reflete o que a API faz hoje.
- Quem roda o seu arquivo é o pytest, num processo separado, com o mesmo
  comando que você usaria na mão. Esta suíte não chama as suas funções
  diretamente: fixture, `parametrize` e classe de teste funcionam aqui do
  mesmo jeito que funcionam no pytest, e nada que o curso ensinou é reprovado
  por causa da forma.
- Esta suíte não confere se você seguiu os três degraus (status, existência,
  valor) nem se evitou validar dado específico de outra pessoa. Isso é
  orientação de leitura humana, não checagem automática: dois testes podem
  passar hoje e um deles pode estar validando dado que muda amanhã, e só a
  correção lê o código para achar essa diferença.
"""
import pathlib
import re
import subprocess
import sys

import pytest

RAIZ = pathlib.Path(__file__).resolve().parents[1]
CAMINHOS = (RAIZ / "entregas" / "test_consulta_serverest.py",
            RAIZ / "test_consulta_serverest.py",
            RAIZ / "tests" / "test_consulta_serverest.py")

MINIMO_DE_CASOS = 3

_ENTREGA = next((p for p in CAMINHOS if p.is_file()), None)

if _ENTREGA is None:
    pytest.skip(
        "A entrega da Aula 10 ainda não está no lugar. Crie o arquivo "
        "'entregas/test_consulta_serverest.py' na raiz do repositório, com pelo "
        "menos três funções começando com 'test_'. Depois rode de novo.",
        allow_module_level=True)


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


def test_a_entrega_tem_pelo_menos_tres_testes_e_todos_passam():
    coleta = _pytest_na_entrega("--collect-only", "-q")
    # O padrao NAO pode exigir \S+ depois do ::. Com @pytest.mark.parametrize e ids legiveis,
    # que e o que a Aula 09 ensinou, o pytest imprime "arquivo.py::teste[CT-02 sem email]",
    # com ESPACO dentro do identificador. Medido em 09/09/2026 na suite da Aula 11: a entrega
    # parametrizada com tres casos era contada como UM, e a suite reprovava justamente quem
    # seguiu a aula anterior. Corrigido aqui pelo mesmo motivo, antes de a Aula 10 ser dada.
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
            f"{_ENTREGA.name} tem {len(casos)} caso(s) de teste, e a atividade "
            f"pede pelo menos {MINIMO_DE_CASOS} (produto existente, produto "
            f"inexistente, filtro por nome).\nCasos coletados:\n{achados}",
            pytrace=False)

    execucao = _pytest_na_entrega("-v")

    if execucao.returncode != 0:
        pytest.fail(
            f"O pytest rodou os {len(casos)} caso(s) de {_ENTREGA.name} contra "
            f"a API e não terminou verde. O relatório dele está abaixo, e a "
            f"linha do 'short test summary info' diz qual caso "
            f"quebrou.\n\n{_ultimas_linhas(execucao.stdout)}",
            pytrace=False)

    print(f"\n{len(casos)} caso(s) de teste em {_ENTREGA.name}, todos passaram:")
    for caso in casos:
        print(f"  {caso}")
