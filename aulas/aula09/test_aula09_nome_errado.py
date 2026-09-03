# Aula 09 - a primeira armadilha, dita antes de a turma cair nela
#
# Escreve-se parametrize, sem "e" no meio. parameterize não existe.
#
# Este arquivo sai com exit code 1 de propósito, e a mensagem é o conteúdo. O
# pytest atual recusa o marcador desconhecido e sugere o nome certo na própria
# mensagem. Em versões mais antigas isso passava como aviso e o teste
# simplesmente sumia do relatório sem ninguém notar, que é bem pior.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos, e 18 entra.
import pytest

from aula09_regras import validar_idade_minima


@pytest.mark.parameterize("idade,esperado", [
    (17, False),
    (18, True),
])
def test_idade_minima(idade, esperado):
    assert validar_idade_minima(idade) == esperado
