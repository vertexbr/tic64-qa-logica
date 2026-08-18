# Aula 02 - caso de teste de login: dado informado x dado esperado

usuario_informado = "Nadinha"
senha_informada = "JL1234!"
usuario_esperado = "Nadinha"
senha_esperada = "JL1234!"
tentativas = 0
token = None

print(f"Usuário informado: {usuario_informado}")
print(f"Usuário esperado: {usuario_esperado}")
print(f"Usuários iguais? {usuario_informado == usuario_esperado}")
print(f"Senhas iguais? {senha_informada == senha_esperada}")
print(f"Tentativas: {tentativas} | Token: {token}")
