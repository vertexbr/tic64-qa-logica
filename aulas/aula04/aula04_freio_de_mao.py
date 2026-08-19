# Aula 04 - break e continue, o freio de mão e o irmão educado dele
#
# break desliga o laço: você puxa o freio de mão e o carro para, não
# importa o que o resto estava fazendo.
# continue desliga a volta: pula só esta e segue para a próxima.
#
# Frase para guardar: break desliga o laço, continue desliga a volta.

usuarios = ["standard_user", "problem_user", "locked_out_user", "visual_user"]

# --- break: achei o que procurava, não preciso varrer o resto ---
for usuario in usuarios:
    print(f"Tentando login com {usuario}")
    if usuario == "locked_out_user":
        print("Usuário bloqueado encontrado. Freio de mão: parando a varredura.")
        break

print("Varredura encerrada")

# O visual_user estava na lista e não foi testado, porque o laço morreu
# antes de chegar nele. Isso é o comportamento esperado do break, e não um
# defeito: quem usa break aceita não visitar o resto.
assert usuarios[-1] == "visual_user"
print("Verificação passou: o último usuário da lista não chegou a ser visitado")

print()

# --- continue: pula esta volta e segue para a próxima ---
for usuario in usuarios:
    if usuario == "standard_user":
        continue
    print(f"Usuário que merece investigação: {usuario}")
