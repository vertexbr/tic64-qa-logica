"""Suíte de autoverificação da atividade da Aula 11.

Ela existe para você descobrir sozinho se acertou, sem esperar a correção. É a
quarta do curso: a da Aula 08 julgava o seu CÓDIGO, a da Aula 09 julgava a sua
MASSA, a da Aula 10 rodava os seus TESTES contra a API, e esta faz o mesmo e
acrescenta uma cobrança que só existe hoje: o seu arquivo precisa exercitar os
QUATRO VERBOS, porque a atividade é o ciclo completo e a limpeza faz parte dele.

COMO USAR

1. Escreva os seus testes num arquivo chamado exatamente
   `test_ciclo_serverest.py`, com cada função começando com `test_` e o nome
   descrevendo o caso, em português.

2. Salve o arquivo em `entregas/` na raiz do repositório. Se a pasta não
   existir, crie.

3. Rode, da raiz do repositório:

       pytest tests/test_ciclo_aula11.py -v

Se aparecer `2 passed`, esta suíte achou o seu arquivo, coletou pelo menos três
testes, todos passaram de verdade contra o ServeRest, e os quatro verbos estão
lá. Se ela falhar, a mensagem diz o que faltou.

Se aparecer `2 skipped`, ela não achou a sua entrega. Pulo não é reprovação: a
mensagem traz o caminho exato onde o arquivo precisa estar.

O QUE ESTA SUÍTE COBRA, E POR QUÊ

- Pelo menos três casos de teste coletados. É a quantidade que a atividade
  pede: o ciclo completo com alteração, mais dois cenários negativos. Quem
  escrever um `@pytest.mark.parametrize` da Aula 09 conta cada linha da massa
  como um caso, porque é assim que o pytest conta.
- Todos os testes do seu arquivo rodam de verdade, contra a API real, e
  precisam passar. Não existe massa fixa aqui para comparar: o teste que você
  escreveu é o produto sendo avaliado, então rodá-lo é a única forma de saber
  se ele reflete o que a API faz hoje.
- Os quatro verbos aparecem no arquivo. O `DELETE` é o que fecha a parte três
  da atividade, a limpeza, e ele é o único item de forma que esta suíte julga.
- Quem roda o seu arquivo é o pytest, num processo separado, com o mesmo
  comando que você usaria na mão. Esta suíte não chama as suas funções
  diretamente: fixture, `parametrize` e classe de teste funcionam aqui do
  mesmo jeito que funcionam no terminal, e nada que o curso ensinou é
  reprovado por causa da forma.
- Esta suíte NÃO confere que você apagou tudo o que criou, nem que a asserção
  do nome novo é a do valor certo, nem que o e-mail é único por execução. Isso
  é leitura humana, e é o que a correção olha. Um teste pode passar hoje e
  deixar lixo na base pública, e só quem lê o código percebe.
"""
import pathlib
import re
import subprocess
import sys

import pytest

RAIZ = pathlib.Path(__file__).resolve().parents[1]
CAMINHOS = (RAIZ / "entregas" / "test_ciclo_serverest.py",
            RAIZ / "test_ciclo_serverest.py",
            RAIZ / "tests" / "test_ciclo_serverest.py")

MINIMO_DE_CASOS = 3

# Cada verbo aceito na forma que o curso ensinou, `requests.verbo(...)`, e também na forma com
# um objeto de sessão, que ninguém ensinou mas que reprovar seria injusto. O segundo padrão
# exige que o primeiro argumento pareça uma URL: um literal que começa com http, ou uma
# f-string que abre com interpolação, como f"{BASE_URL}/usuarios". Sem essa exigência o
# `corpo.get("nome")` de qualquer entrega contaria como um GET.
VERBOS = {
    "POST": r"(?:requests\.post\s*\(|\.post\s*\(\s*f?[\"'](?:https?://|\{))",
    "GET": r"(?:requests\.get\s*\(|\.get\s*\(\s*f?[\"'](?:https?://|\{))",
    "PUT": r"(?:requests\.put\s*\(|\.put\s*\(\s*f?[\"'](?:https?://|\{))",
    "DELETE": r"(?:requests\.delete\s*\(|\.delete\s*\(\s*f?[\"'](?:https?://|\{))",
}

_ENTREGA = next((p for p in CAMINHOS if p.is_file()), None)

_FALTA = (
    "A entrega da Aula 11 ainda não está no lugar. Crie o arquivo "
    "'entregas/test_ciclo_serverest.py' na raiz do repositório, com pelo menos "
    "três funções começando com 'test_'. Depois rode de novo.")


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
    # O pulo acontece DENTRO do teste, e nao no modulo. Com pytest.skip de modulo o pytest
    # coleta zero itens e sai com exit code 5, que a IDE e qualquer automacao leem como
    # execucao quebrada. Assim ele coleta o item, pula, e sai com exit code 0.
    if _ENTREGA is None:
        pytest.skip(_FALTA)

    coleta = _pytest_na_entrega("--collect-only", "-q")
    # O padrao NAO pode exigir \S+ depois do ::. Com @pytest.mark.parametrize e ids legiveis,
    # que e o que a Aula 09 ensinou, o pytest imprime "arquivo.py::teste[CT-02 sem email]",
    # com ESPACO dentro do identificador. Medido em 09/09/2026: a entrega parametrizada com
    # tres casos era contada como um so, e a suite reprovava quem seguiu a aula anterior.
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
            f"pede pelo menos {MINIMO_DE_CASOS}: o ciclo completo com alteração, "
            f"e dois cenários negativos.\nCasos coletados:\n{achados}",
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


def test_a_entrega_exercita_os_quatro_verbos():
    if _ENTREGA is None:
        pytest.skip(_FALTA)

    fonte = _ENTREGA.read_text(encoding="utf-8")
    faltando = [verbo for verbo, padrao in VERBOS.items()
                if not re.search(padrao, fonte)]

    if faltando:
        pytest.fail(
            f"{_ENTREGA.name} não usa {', '.join(faltando)}. A atividade é o ciclo "
            f"completo: criar com POST, consultar com GET, alterar com PUT, excluir "
            f"com DELETE, e a parte três pede que todo teste que cria dado apague o "
            f"dado antes de terminar.\nA forma procurada é a da aula, "
            f"'requests.delete(f\"{{BASE_URL}}/usuarios/{{id}}\", timeout=10)'.",
            pytrace=False)

    print(f"\nOs quatro verbos aparecem em {_ENTREGA.name}: POST, GET, PUT e DELETE.")
