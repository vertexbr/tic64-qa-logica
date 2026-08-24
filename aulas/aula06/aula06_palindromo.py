# Aula 06 - função chamando função
#
# GUARDEM ESTAS DUAS com nome e sobrenome: na Aula 08 elas vão ser as primeiras
# coisas que a ferramenta de verificação vai rodar.
#
# inverter é um acumulador de texto, irmão do acumulador de lista da Aula 04: a
# cada volta ela cola a letra nova NA FRENTE do que já tinha, e no fim o texto
# está de trás para frente. Cria antes, percorre, muda dentro, usa depois.
#
# eh_palindromo chama inverter, porque função chamando função é normal, e é
# assim que se monta lógica grande a partir de peças pequenas, cada uma
# testável sozinha.

def inverter(texto):
    invertido = ""
    for letra in texto:
        invertido = letra + invertido
    return invertido


def eh_palindromo(texto):
    limpo = texto.strip().lower().replace(" ", "")
    return limpo == inverter(limpo)


print(f"'abc' invertido: {inverter('abc')}")
print(f"'  Arara  ' é palíndromo? {eh_palindromo('  Arara  ')}")
print(f"'teste' é palíndromo? {eh_palindromo('teste')}")
frase = "Socorram me subi no onibus em Marrocos"
print(f"A frase inteira: {eh_palindromo(frase)}")

# O nome eh_palindromo é pergunta, e devolve True ou False. Função-pergunta
# booleana é a mais fácil de testar que existe, porque o esperado só tem dois
# valores possíveis.
assert inverter("abc") == "cba"
assert eh_palindromo("  Arara  ") == True
assert eh_palindromo("teste") == False
print("As três verificações passaram")
