# Aula 05 - demonstração guiada 2: validar a lista de usuários
#
# O arquivo que junta as três estruturas do curso até aqui: lista da Aula 04,
# dicionário e string desta aula, no mesmo lugar. É o mais importante da aula,
# e é o que vale refazer em casa.
#
# As quatro regras, e o texto exato de cada problema:
#
#   1. nome vazio            -> "sem nome"
#   2. situação inativa      -> "inativo"
#   3. lista de perfis vazia -> "sem perfil"
#   4. e-mail sem arroba depois de normalizado -> "e-mail inválido"
#
# No fim de cada usuário: se a lista de problemas tem algo, imprime o id e os
# problemas separados por vírgula; se não tem nada, imprime o id e "OK". E uma
# contagem, num dicionário, de quantos ficaram OK e quantos ficaram com
# problema.

usuarios = [
    {"id": 1, "nome": "Ana",  "email": "  ANA@Loja.COM  ", "situacao": "ativo",   "perfis": ["admin"]},
    {"id": 2, "nome": "",     "email": "beto@loja.com",    "situacao": "ativo",   "perfis": ["editor"]},
    {"id": 3, "nome": "Cris", "email": "cris.loja.com",    "situacao": "inativo", "perfis": []},
    {"id": 4, "nome": "Dani", "email": "dani@loja.com",    "situacao": "ativo",   "perfis": ["admin"]},
]

contagem = {}

for usuario in usuarios:
    problemas = []

    if usuario["nome"] == "":
        problemas.append("sem nome")
    if usuario["situacao"] == "inativo":
        problemas.append("inativo")
    if len(usuario["perfis"]) == 0:
        problemas.append("sem perfil")

    email = usuario.get("email", "").strip().lower()
    if "@" not in email:
        problemas.append("e-mail inválido")

    if len(problemas) > 0:
        print(f"Usuário {usuario['id']}: {', '.join(problemas)}")
        contagem["com problema"] = contagem.get("com problema", 0) + 1
    else:
        print(f"Usuário {usuario['id']}: OK")
        contagem["ok"] = contagem.get("ok", 0) + 1

print(f"Resumo: {contagem}")

assert contagem["ok"] == 2
assert contagem["com problema"] == 2
assert contagem["ok"] + contagem["com problema"] == len(usuarios)
print("Verificações passaram")

# Três comentários sobre a saída, e nenhum é sobre sintaxe.
#
# 1. A Ana tem o e-mail mais sujo da massa e passou, porque eu normalizei antes
#    de olhar. Comparando o valor cru, ela apareceria como problema e eu abriria
#    um defeito que não existe. Isso tem nome no trabalho de vocês: falso
#    positivo.
#
# 2. O usuário 3 acumulou três problemas numa volta só. Repare que não tem elif
#    aqui. Com elif, ele reportaria só o primeiro problema e vocês descobririam
#    os outros dois na semana seguinte. Quatro if independentes existem para isso.
#
# 3. Está escrito if len(problemas) > 0 e não if problemas. As duas funcionam
#    em Python. A primeira é a que segue a regra da Aula 03: nunca escreva
#    condição sem comparação explícita. Custa oito caracteres e evita a família
#    de bugs mais silenciosa do curso.
#
# Extra de casa, para quem quiser: acrescente uma quinta regra à sua escolha e
# um assert que prove que ela pegou alguém.
