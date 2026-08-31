# Aula 08 - os mesmos quatro testes, contra a regra estragada
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO, e é o momento mais importante
# da aula. Um QA vai passar a carreira lendo relatório de falha, e é justo que a
# primeira leitura seja acompanhada.
#
# São os quatro testes do test_aula08_regras.py, copiados sem mudar uma vírgula.
# A ÚNICA diferença é a linha do import, que aponta para o módulo estragado. Os
# testes não sabem de nada: eles cobram a regra escrita, e a regra escrita não
# mudou.
#
# Antes de rodar, responda: quantos dos quatro ficam vermelhos? A resposta não é
# quatro, e o motivo de não ser quatro é o conteúdo do slide.
#
# Cinco informações saem de um comando só: o nome do teste que falhou, o corpo
# dele reimpresso, a seta apontando o assert exato, o E com o obtido e o
# esperado lado a lado, e a última linha com arquivo, linha e tipo do erro.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro é liberado a partir de 18 anos, e 18 entra. Só admin e gerente
#   têm permissão de administração; qualquer outro perfil não tem.
from aula08_regras_quebradas import validar_idade_minima, tem_permissao


def test_maior_de_idade_e_valido():
    # Preparação
    idade = 20
    # Ação
    resultado = validar_idade_minima(idade)
    # Validação
    assert resultado == True


def test_menor_de_idade_e_invalido():
    assert validar_idade_minima(16) == False


def test_admin_tem_permissao():
    assert tem_permissao("admin") == True


def test_visitante_nao_tem_permissao():
    assert tem_permissao("visitante") == False
