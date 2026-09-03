# Aula 09 - o desafio extra: a massa sai de um arquivo, não do código
#
# Este é o formato que a atividade pede, e ele existe por um motivo prático: a
# massa passa a ser editável por quem não escreve Python. Analista de negócio
# abre o arquivo, acrescenta uma linha, e o teste roda com um caso a mais sem
# ninguém tocar no código.
#
# O separador é ponto e vírgula, e não vírgula, porque valor em real leva ponto
# ou vírgula decimal e a vírgula brigaria com a separação das colunas.
#
# A ARMADILHA, e ela é a única coisa realmente nova aqui: TUDO que sai de um
# arquivo de texto chega como texto. A string "False" não é o booleano False,
# e ela é VERDADEIRA num if, porque toda string não vazia é verdadeira. Por
# isso as duas conversões abaixo existem, e por isso elas não são opcionais.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Frete é grátis a partir de R$ 250,00, e 250,00 entra.
import csv
import pathlib

import pytest

from aula09_regras import tem_frete_gratis

ARQUIVO = pathlib.Path(__file__).with_name("aula09_massa_frete.csv")


def carregar_massa():
    """Lê o CSV e devolve a massa e os ids, no formato que o parametrize pede."""
    massa = []
    ids = []
    with ARQUIVO.open(encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f, delimiter=";"):
            massa.append((float(linha["total"]), linha["esperado"] == "True"))
            ids.append(linha["id"])
    return massa, ids


MASSA, IDS = carregar_massa()


@pytest.mark.parametrize("total,esperado", MASSA, ids=IDS)
def test_frete_gratis_vindo_do_csv(total, esperado):
    assert tem_frete_gratis(total) == esperado
