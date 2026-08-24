# Aula 06 - print contra return, o momento mais importante da aula
#
# As duas funções somam dois mais dois, e as duas parecem funcionar. Rode antes
# de ler o resto deste comentário e olhe as três linhas da saída.
#
# print fala em voz alta; return entrega um documento. Quem estava ouvindo
# escutou o 4, mas ninguém tem papel na mão para levar embora. A consequência
# de QA é o ponto todo: teste precisa de valor para comparar, e teste contra
# None é teste contra o nada.

def soma_com_print(a, b):
    print(a + b)


def soma_com_return(a, b):
    return a + b


resultado_print = soma_com_print(2, 2)
resultado_return = soma_com_return(2, 2)

print(f"Com print, resultado_print vale: {resultado_print}")
print(f"Com return, resultado_return vale: {resultado_return}")

# Agora o erro que fecha o assunto. Usar numa conta o retorno de uma função que
# não retorna produz um nome de erro que vocês vão ver muito: NoneType.
#
# AVISO: este try/except existe para o arquivo seguir até o fim e mostrar o
# erro na mesma execução. Numa suíte de verdade a falha interrompe, e engolir
# exceção é o oposto de verificar.
try:
    print(resultado_print * 10)
except TypeError as erro:
    print(f"TypeError: {erro}")

# O return é o que faz a conta ser possível.
print(f"E com return a mesma conta funciona: {resultado_return * 10}")

assert resultado_print == None
assert resultado_return == 4
print("As duas verificações passaram")
