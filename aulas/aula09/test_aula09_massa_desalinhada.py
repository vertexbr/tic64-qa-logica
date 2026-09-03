# Aula 09 - a segunda armadilha, e ela acontece na COLETA
#
# A quantidade de nomes tem que bater com o tamanho de cada tupla. Dois nomes,
# dois valores por linha. Aqui a segunda linha tem três.
#
# Este arquivo sai com exit code 1 de propósito. A mensagem do pytest é boa e
# diz os dois números, mas ela aparece na coleta: nada roda, nem os testes dos
# outros arquivos, e a turma acha que quebrou tudo.
#
# A conferência antes de rodar cabe numa frase: conte os nomes da string, conte
# os valores da primeira linha, e veja se são iguais.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos, e 18 entra.
import pytest

from aula09_regras import validar_idade_minima


@pytest.mark.parametrize("idade,esperado", [
    (17, False),
    (18, True, "extra"),
])
def test_massa_desalinhada(idade, esperado):
    assert validar_idade_minima(idade) == esperado
