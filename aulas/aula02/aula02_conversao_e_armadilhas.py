# Aula 02 - conversão de tipo e as armadilhas mais comuns (segundo ciclo)
#
# Tudo que chega de fora do programa (teclado, arquivo, resposta de API)
# chega como texto (str). Comparar ou somar esse texto sem converter é a
# origem da maioria dos erros deste bloco.


# --- A calculadora que devolve 105 --------------------------------------
#
# Este é o único lugar do curso em que input() apareceria: teste automatizado
# não pode parar esperando alguém digitar numa esteira de integração.
#
#   primeiro = input("Primeiro número: ")
#   segundo = input("Segundo número: ")
#   print(primeiro + segundo)             # digitando 10 e 5, aparece 105
#   print(int(primeiro) + int(segundo))   # convertido, aparece 15
#
# A partir daqui, o curso simula dado externo com texto direto no código,
# no lugar do input():

qtd_da_tela = "10"      # veio da tela, então é texto
qtd_do_estoque = "5"    # veio de um arquivo, então é texto

print(f"Sem converter: {qtd_da_tela + qtd_do_estoque}")
print(f"Convertido: {int(qtd_da_tela) + int(qtd_do_estoque)}")


# --- O par 200 e "200" ---------------------------------------------------
#
# Na tela os dois valores parecem a mesma informação. Para o Python são
# tipos diferentes, e por isso o primeiro == abaixo dá falso.

codigo = 200
codigo_texto = "200"

print(f"codigo == codigo_texto? {codigo == codigo_texto}")
print(f"codigo == int(codigo_texto)? {codigo == int(codigo_texto)}")

# codigo.strip() tenta usar uma função de texto (remover espaço nas pontas)
# num número. Número não sabe fazer coisa de texto, e o erro é
# AttributeError: 'int' object has no attribute 'strip'.
#
# Mesmo padrão de try/except do arquivo aula02_tipos_e_nomes.py: o try tenta
# rodar a linha de dentro, e se ela lançar uma exceção do tipo indicado no
# except (aqui, AttributeError), o Python captura o erro numa variável em
# vez de deixar ele parar o script.
try:
    print(codigo.strip())
except AttributeError as erro:
    print(f"AttributeError: {erro}")

# Alternativa sem try/except: comente as quatro linhas acima e descomente
# uma linha por vez.
# print(codigo.strip())          # X: erro de verdade, o script PARA aqui com o traceback do AttributeError
# print(str(codigo).strip())     # Y: convertido para texto antes, valida e imprime 200

print(f"Corrigido, convertendo para texto antes: {str(codigo).strip()}")


# --- A armadilha do float -------------------------------------------------
#
# Float não se compara com igualdade exata. A solução formal, pytest.approx,
# é assunto da Aula 08; hoje o que importa é a desconfiança.

print(f"0.1 + 0.2 = {0.1 + 0.2}")   # 0.30000000000000004, não 0.3


# --- Nome da variável x conteúdo da variável -----------------------------
#
# A automação digita o CONTEÚDO da caixinha, nunca o nome dela. A aspa é a
# fronteira: com aspas é texto literal, sem aspas é o nome de uma gaveta e o
# Python busca o que tem dentro.

senha_informada = "JL1234!"

print(senha_informada)      # JL1234!          (o conteúdo da caixinha)
print("senha_informada")    # senha_informada  (um texto qualquer)


# --- O erro da vírgula ----------------------------------------------------
#
# Vírgula decimal brasileira não quebra o programa, e é justamente isso que
# a torna perigosa: vira uma tupla de dois números em vez de um decimal só.

valor = 599,90
print(f"valor: {valor} | tipo: {type(valor)}")   # (599, 90), tupla

# Convertendo com float(), o Python avisa em vez de aceitar em silêncio.
# De novo o mesmo padrão: o try tenta, o except captura o ValueError pelo
# tipo e deixa o script terminar normalmente em vez de travar aqui.
try:
    print(float("599,90"))
except ValueError as erro:
    print(f"ValueError: {erro}")

# Alternativa sem try/except: comente as quatro linhas acima e descomente
# uma linha por vez.
# print(float("599,90"))     # X: erro de verdade, o script PARA aqui com o traceback do ValueError (vírgula não é separador decimal para o Python)
# print(float("599.90"))     # Y: com o ponto no lugar da vírgula, valida e imprime 599.9
