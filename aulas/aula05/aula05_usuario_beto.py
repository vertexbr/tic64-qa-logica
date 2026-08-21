# Aula 05 - demonstração guiada 1: os campos de um usuário, inclusive os aninhados
#
# Reprodução do que o primeiro ciclo mostrou, num registro novo. Este é o
# arquivo para refazer em casa: escreva do zero, sem copiar, e confira contra
# a saída que está no README.
#
# A regra, em seis linhas de saída e três verificações:
#
#   1. um dicionário de usuário com id, nome, email, situacao, perfis e endereco
#   2. o email entra sujo de propósito, com espaço e maiúscula
#   3. perfis é uma lista com um item, endereco é outro dicionário
#   4. imprimir nome, cidade, UF, primeiro perfil, presença de telefone e o
#      telefone com get e padrão
#   5. fechar com assert na UF, na quantidade de perfis e no padrão do get

usuario = {
    "id": 7,
    "nome": "Beto Nunes",
    "email": "  BETO@Loja.COM  ",
    "situacao": "ativo",
    "perfis": ["editor"],
    "endereco": {"cidade": "Maceió", "uf": "AL"}
}

print(f"Nome: {usuario['nome']}")
print(f"Cidade: {usuario['endereco']['cidade']}")
print(f"UF: {usuario['endereco']['uf']}")
print(f"Primeiro perfil: {usuario['perfis'][0]}")
print(f"Tem telefone? {'telefone' in usuario}")
print(f"Telefone: {usuario.get('telefone', 'não informado')}")

assert usuario["endereco"]["uf"] == "AL"
assert len(usuario["perfis"]) == 1
assert usuario.get("telefone", "não informado") == "não informado"
print("As três verificações passaram")

# Os dois tropeços que vão acontecer quando você refizer isto em casa:
#
#   1. aspas duplas dentro de uma f-string que já está entre aspas duplas.
#      Dá SyntaxError, e a correção é usar aspas simples na chave.
#   2. colchete em telefone no lugar do get. Dá KeyError: 'telefone', porque
#      este usuário não tem telefone, e telefone é campo opcional.
#
# Print do erro no canal do curso. Ninguém fica travado sozinho às onze da noite.
