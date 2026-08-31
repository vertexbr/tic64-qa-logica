# Aula 07 - o except pelado, e o falso-verde que ele produz
#
# PROIBIDO NESTE CURSO. Este arquivo existe para mostrar o antipadrão rodando,
# e a faixa vermelha do slide é minha, não do Python: o Python aceita except
# sem tipo sem reclamar nada, e é justamente esse o problema.
#
# except sem tipo captura QUALQUER erro que apareça ali dentro. O ValueError que
# você imaginava, e também o NameError de uma variável digitada errado, e o
# TypeError de um dado no formato errado. Todos vão para o mesmo lugar, que é o
# pass, que é nada.
#
# A consequência que interessa a um QA: uma verificação com except pelado passa
# mesmo quando o produto está quebrado. Ela não valida, ela silencia. Isso tem
# nome: falso-verde. É o pior resultado possível numa esteira de testes, pior
# que vermelho, porque vermelho você investiga e verde você confia.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A soma dos valores da massa tem que incluir todos os valores. Valor fora do formato
#   é recusado com o motivo na tela, nunca descartado em silêncio.

def somar_pelado(linhas):
    total = 0
    for linha in linhas:
        try:
            total = total + float(linha)
        except:
            pass
    return total


def somar_com_tipo(linhas):
    total = 0
    for linha in linhas:
        try:
            total = total + float(linha)
        except ValueError as erro:
            print(f"    descartei '{linha}': {erro}")
    return total


massa = ["10.00", "20,00", "30.00"]   # <- o segundo tem vírgula, não ponto

print("=== com except pelado ===")
print(f"Soma: {somar_pelado(massa)}")
print("Nenhum aviso. E o número está errado.")

print()
print("=== com except de tipo, e a mensagem na tela ===")
print(f"Soma: {somar_com_tipo(massa)}")
print("O numero continua 40. O que mudou e que agora eu SEI por que.")

# Toda saida de exemplo aparece, inclusive a da correcao. Descoberto o motivo, o
# conserto e do dado e nao do except: a massa tem virgula decimal, e o float()
# do Python le ponto. O except com tipo nao consertou nada, ele mostrou o que
# consertar, e e por isso que ele vale.
print()
print("=== e agora com a massa consertada ===")
massa_certa = []
for linha in massa:
    massa_certa.append(linha.replace(",", "."))
print(f"Massa: {massa_certa}")
print(f"Soma: {somar_com_tipo(massa_certa)}")
assert somar_com_tipo(massa_certa) == 60.00
print("60,00, que e o esperado que veio da regra.")

print()
print("A regra do curso: capture o erro específico que você espera.")
print("Se você não sabe qual erro esperar, você ainda não entendeu o que")
print("está testando, e o except genérico está escondendo essa lacuna de você.")
