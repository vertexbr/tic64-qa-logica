# Aula 08 - o arquivo que se importa sozinho
#
# ESTE ARQUIVO MORA NUMA PASTA SÓ DELE, e a pasta existe por causa dele. Se este
# random.py estivesse ao lado dos outros arquivos da Aula 08, TODO arquivo
# daquela pasta que precisasse da biblioteca random pegaria este aqui no lugar
# dela. Um arquivo mal nomeado contamina a pasta inteira.
#
# O que acontece quando você roda: nome de arquivo também é nome de módulo. O
# Python procura random, encontra ESTE arquivo antes da biblioteca padrão,
# começa a executar ele, chega na linha do import random e encontra ele mesmo,
# ainda pela metade. O arquivo importa a si próprio, e é por isso que o
# traceback aponta duas vezes para o mesmo caminho: linha 31 e linha 33.
#
# Repare no traceback: o tipo do erro é AttributeError e ele fala de um atributo
# choice que não existe. Nada nessas duas informações aponta para o nome do
# arquivo. Quem entrega a causa é a última linha, entre parênteses, e ela existe
# porque o Python 3.12 em diante passou a sugerir a renomeação quando o nome
# bate com o de um módulo conhecido. É uma gentileza recente, chega depois do
# traceback inteiro, e ninguém lê o fim de uma mensagem vermelha na primeira vez.
#
# A regra que fica não depende da gentileza: nunca dê a um arquivo seu o nome de
# uma biblioteca. Na Aula 10 a gente vai usar a biblioteca requests, e
# requests.py na pasta do projeto é o caso mais comum desse defeito.
#
# ESTE ARQUIVO SAI COM exit code 1 DE PROPÓSITO. Não conserte: renomear ele
# apagaria a demonstração.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O relatório sorteia um perfil entre os três cadastrados. A regra é irrelevante
#   aqui: o arquivo nunca chega a executá-la.
import random

sorteado = random.choice(["admin", "gerente", "visitante"])
print(f"Perfil sorteado: {sorteado}")
