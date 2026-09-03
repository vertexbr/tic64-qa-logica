# Aula 09 - a mesma massa do frete, apontada para o arquivo estragado
#
# A massa é idêntica à de test_aula09_senha_e_frete.py. O que muda é o import:
# aqui ele vem de aula09_regras_frete_quebrado, onde o >= virou >.
#
# Este arquivo sai com exit code 1 de propósito, e a falha é o conteúdo. Leia o
# nome entre colchetes no relatório:
#
#   FAILED test_aula09_frete_quebrado.py::test_frete_gratis[exatamente_no_limite]
#
# "exatamente no limite falhou" já diz qual é o defeito, sem abrir o código.
# Compare com o que o relatório diria sem o ids: "caso 2 falhou". A regra
# prática cabe numa frase: dê nome a cada linha da massa.
#
# REGRA DE NEGÓCIO (a escrita no cartão, que é a que vale):
#   Frete é grátis A PARTIR de R$ 250,00, e 250,00 exato tem frete grátis.
import pytest

from aula09_regras_frete_quebrado import tem_frete_gratis


@pytest.mark.parametrize("total,esperado", [
    (249.99, False),
    (250.00, True),
    (300.00, True),
], ids=[
    "um_centavo_abaixo",
    "exatamente_no_limite",
    "bem_acima",
])
def test_frete_gratis(total, esperado):
    assert tem_frete_gratis(total) == esperado
