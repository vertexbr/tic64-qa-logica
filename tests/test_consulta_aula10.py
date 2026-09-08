"""Suíte de autoverificação da atividade da Aula 10.

Ela existe para você descobrir sozinho se acertou, sem esperar a correção. É a
terceira do curso, e ela julga uma coisa diferente das duas primeiras: a da
Aula 08 julgava o seu CÓDIGO, a da Aula 09 julgava a sua MASSA, esta roda os
SEUS TESTES de verdade contra a API real e conta quantos passaram.

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
nome e o resultado de cada teste que não passou.

O QUE ESTA SUÍTE COBRA, E POR QUÊ

- Pelo menos três funções começando com `test_`. É a quantidade que a
  atividade pede: produto existente, produto inexistente, filtro por nome.
- Todos os testes do seu arquivo rodam de verdade, contra a API real, e
  precisam passar. Não existe massa fixa aqui para comparar: o teste que você
  escreveu é o produto sendo avaliado, então rodá-lo é a única forma de saber
  se ele reflete o que a API faz hoje.
- Esta suíte não confere se você seguiu os três degraus (status, existência,
  valor) nem se evitou validar dado específico de outra pessoa. Isso é
  orientação de leitura humana, não checagem automática: dois testes podem
  passar hoje e um deles pode estar validando dado que muda amanhã, e só a
  correção lê o código para achar essa diferença.
"""
import importlib.util
import inspect
import pathlib
import sys

import pytest

RAIZ = pathlib.Path(__file__).resolve().parents[1]
CAMINHOS = (RAIZ / "entregas" / "test_consulta_serverest.py",
            RAIZ / "test_consulta_serverest.py",
            RAIZ / "tests" / "test_consulta_serverest.py")

_ENTREGA = next((p for p in CAMINHOS if p.is_file()), None)

if _ENTREGA is None:
    pytest.skip(
        "A entrega da Aula 10 ainda não está no lugar. Crie o arquivo "
        "'entregas/test_consulta_serverest.py' na raiz do repositório, com pelo "
        "menos três funções começando com 'test_'. Depois rode de novo.",
        allow_module_level=True)


def _carregar_modulo():
    spec = importlib.util.spec_from_file_location("consulta_serverest_entrega", _ENTREGA)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo  # inspect.getmodule() so acha funcao em modulo registrado
    try:
        spec.loader.exec_module(modulo)
    except Exception as erro:
        pytest.fail(
            f"O arquivo {_ENTREGA.name} não chegou a carregar: "
            f"{type(erro).__name__}: {erro}\n"
            f"O erro não é desta suíte, é do seu arquivo. Rode "
            f"'python {_ENTREGA.name}' e conserte antes de voltar aqui.",
            pytrace=False)
    return modulo


def _testes_do_modulo(modulo):
    return [(nome, funcao) for nome, funcao in inspect.getmembers(modulo, inspect.isfunction)
            if nome.startswith("test_") and inspect.getmodule(funcao) is modulo]


def test_a_entrega_tem_pelo_menos_tres_testes_e_todos_passam():
    modulo = _carregar_modulo()
    testes = _testes_do_modulo(modulo)

    if len(testes) < 3:
        nomes = [n for n, _ in testes] or ["nenhuma"]
        pytest.fail(
            f"{_ENTREGA.name} tem {len(testes)} função(ões) começando com 'test_', "
            f"e a atividade pede pelo menos três (produto existente, produto "
            f"inexistente, filtro por nome).\nFunções encontradas: {', '.join(nomes)}",
            pytrace=False)

    falhas = []
    for nome, funcao in testes:
        try:
            funcao()
        except Exception as erro:
            falhas.append(f"  {nome}: {type(erro).__name__}: {erro}")

    if falhas:
        pytest.fail(
            f"{len(falhas)} de {len(testes)} teste(s) não passaram ao rodar de "
            f"verdade contra a API:\n" + "\n".join(falhas),
            pytrace=False)

    print(f"\n{len(testes)} teste(s) encontrados em {_ENTREGA.name}, todos passaram: "
          + ", ".join(n for n, _ in testes))
