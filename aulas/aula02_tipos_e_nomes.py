# Aula 02 - nomes de variável, os cinco tipos e f-string (primeiro ciclo)
#
# Nomes de variável: convenção snake_case (tudo minúsculo, palavras separadas
# por underscore) e um nome que descreve o conteúdo. Nomes genéricos como x
# ou dado1 são proibidos neste curso porque escondem o que a variável guarda.

valor_produto = 199.90      # certo: o nome descreve o conteúdo

# x = 199.90                  # proibido neste curso: não diz o que guarda
# dado1 = True                 # proibido neste curso: não diz o que guarda


# Os cinco tipos que este curso usa, com um exemplo do vocabulário do curso
# para cada um:

endpoint = "/api/login"     # str, texto, sempre entre aspas
status_code = 200           # int, número inteiro, sem aspas
tempo_resposta = 1.42       # float, decimal, com PONTO
cliente_ativo = True        # bool, True ou False, com maiúscula
token = None                 # None, ausência de valor

print(f"endpoint: {endpoint} | tipo: {type(endpoint)}")
print(f"status_code: {status_code} | tipo: {type(status_code)}")
print(f"tempo_resposta: {tempo_resposta} | tipo: {type(tempo_resposta)}")
print(f"cliente_ativo: {cliente_ativo} | tipo: {type(cliente_ativo)}")
print(f"token: {token} | tipo: {type(token)}")


# A distinção que vale a aula toda: 200 (número) e "200" (texto que parece
# número) são coisas diferentes para o Python. Isso derruba validação de
# resposta de API na Aula 10, quando "200" (texto) não bate com 200 (número).

codigo = 200
codigo_texto = "200"
print(f"codigo: {codigo} | tipo: {type(codigo)}")
print(f"codigo_texto: {codigo_texto} | tipo: {type(codigo_texto)}")

# Micropergunta da aula: que tipo é "58", com aspas? Texto. Mesmo parecendo
# número, tudo que está entre aspas é str.
idade_como_texto = "58"
print(f"idade_como_texto: {idade_como_texto} | tipo: {type(idade_como_texto)}")


# f-string: o "f" antes da aspa permite colocar uma variável dentro do texto,
# entre chaves. Sem o "f", as chaves aparecem soltas na tela.

total = 599.70
print("Total da compra: R$ {total}")       # sai literalmente com as chaves
print(f"Total da compra: R$ {total}")      # sai 599.7
print(f"Total da compra: R$ {total:.2f}")  # sai 599.70, formatado com duas casas


# Erro proposital: somar texto com número. Tudo que vem de fora (teclado,
# arquivo, resposta de API) chega como texto, e o Python não adivinha que
# "58" deveria virar número antes de somar. O erro é TypeError.
#
# try/except: o Python executa o que está dentro do try. Se uma linha ali
# lançar uma exceção (um erro em tempo de execução, como o TypeError daqui),
# ele não quebra o script — pula direto para o except, que captura o erro
# pelo tipo (TypeError) e deixa o programa seguir em vez de parar. É por
# isso que este arquivo consegue rodar do início ao fim mesmo tendo um erro
# proposital no meio.

idade = "58"
try:
    print(idade + 1)
except TypeError as erro:
    print(f"TypeError: {erro}")

# Alternativa sem try/except, para ver exatamente o que aconteceu ao vivo em
# aula: comente as quatro linhas do try/except acima e descomente uma linha
# abaixo por vez.
# print(idade + 1)          # X: erro de verdade, o script PARA aqui com o traceback do TypeError
# print(int(idade) + 1)     # Y: com a conversão, valida e imprime 59

print(f"Corrigido, convertendo antes de somar: {int(idade) + 1}")
