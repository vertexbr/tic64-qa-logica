# Aula 06 - o extra de casa
#
# Três coisas juntas aqui, e as três já apareceram no curso: retorno antecipado
# no primeiro if, duas variáveis de bandeira que começam falsas e podem virar
# verdadeiras dentro do laço (que é o acumulador da Aula 04 com valor
# booleano), e um and no return para exigir as duas.
#
# E olhem que a senha JL1234!, que atravessou o curso inteiro, é recusada,
# porque tem sete caracteres. Testar a regra na fronteira encontrou isso em
# dois segundos.

def senha_valida(senha):
    if len(senha) < 8:
        return False
    tem_numero = False
    tem_maiuscula = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isupper():
            tem_maiuscula = True
    return tem_numero and tem_maiuscula


print(f"Senha123 vale? {senha_valida('Senha123')}")
print(f"JL1234!  vale? {senha_valida('JL1234!')}  (7 caracteres)")
print(f"jl123456 vale? {senha_valida('jl123456')}  (sem maiúscula)")
print(f"JLABCDEF vale? {senha_valida('JLABCDEF')}  (sem número)")

assert senha_valida("Senha123") == True
assert senha_valida("JL1234!") == False
assert senha_valida("jl123456") == False
assert senha_valida("JLABCDEF") == False
print("As quatro verificações passaram")
