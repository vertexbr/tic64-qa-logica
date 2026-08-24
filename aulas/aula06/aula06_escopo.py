# Aula 06 - escopo, ou o que atravessa a parede da função
#
# Um quadrado dentro de outro: o de fora é o programa, o de dentro é a função.
# Quem está dentro consegue ver o que está fora; quem está fora não consegue
# ver o que está dentro. Variável criada dentro da função nasce quando a função
# é chamada e morre quando ela termina.
#
# A única coisa que atravessa a parede é o que o return entrega.
#
# AVISO: os try/except deste arquivo existem para ele seguir até o fim e
# mostrar os dois casos na mesma execução. Numa suíte de verdade a falha
# interrompe, e engolir exceção é o oposto de verificar.

def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    return subtotal


total = calcular_total(10.00, 3)
print(f"Total: {total}")

# O subtotal existiu, fez o trabalho e foi embora. Não é bug: é o escopo
# funcionando. A mensagem do Python diz exatamente isso.
try:
    print(subtotal)
except NameError as erro:
    print(f"NameError: {erro}")


# Agora a parte que confunde de verdade: duas variáveis com o MESMO nome, em
# quadrados diferentes, são coisas diferentes.
def dobrar(valor):
    valor = valor * 2
    return valor


valor = 10
resultado = dobrar(valor)

print(f"Dentro da função o valor virou 20, e devolveu {resultado}")
print(f"Fora da função, valor continua {valor}")

# A regra prática que decide onde a variável mora, e é ela que responde noventa
# por cento das dúvidas de "onde eu declaro isso": dado usado em mais de um
# lugar sobe para parâmetro ou para retorno, e dado usado num lugar só fica
# dentro da função.
assert valor == 10
assert resultado == 20
print("As duas verificações passaram")
