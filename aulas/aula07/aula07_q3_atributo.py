# Aula 07 - quebrado 3 de 4: método que não existe naquele tipo
#
# Rode, leia a ÚLTIMA linha primeiro, e responda o tipo, a linha e a causa.
#
# O e-mail sujo com espaço nas pontas é o mesmo de aulas/aula05/aula05_email_sujo.py.
# O acréscimo desta aula é o método errado: quem vem de outra linguagem escreve
# trim(), e em Python o nome é strip(). O próprio Python sugere o certo.
#
# Estrutura de demonstração igual à dos outros três quebrados.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   E-mail cadastrado é comparado sem espaço nas pontas e todo em minúscula, porque
#   quem digita não é consistente e o sistema precisa ser.
import traceback

email = "  GAIA@Teste.com  "

try:
    print(email.trim().lower())
except AttributeError:
    traceback.print_exc()

print()
print(f"Com strip(), sai: {email.strip().lower()}")
