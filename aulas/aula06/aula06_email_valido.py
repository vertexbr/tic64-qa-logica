# Aula 06 - a validação de e-mail que agora tem nome
#
# Aquela validação da Aula 05 era uma linha comprida perdida no meio do
# arquivo. Agora tem nome, entrada e saída, e ficou melhor: com retorno
# antecipado dá para separar quatro motivos de recusa, um por if, cada um
# legível.
#
# Sem arroba ou com duas arrobas, recusa. Nada antes da arroba, recusa. Sem
# ponto no domínio, recusa.
#
# Contem os assert: seis cenários, quatro deles negativos. Não é excesso, é
# olhar de QA, e quem só testa o caminho feliz descobre os outros quatro em
# produção.

def email_valido(email):
    limpo = email.strip().lower()
    partes = limpo.split("@")
    if len(partes) != 2:
        return False
    if partes[0] == "":
        return False
    if "." not in partes[1]:
        return False
    return True


print(f"  GAIA@Teste.COM   vale? {email_valido('  GAIA@Teste.COM  ')}")
print(f"beto@loja.com.br   vale? {email_valido('beto@loja.com.br')}")
print(f"gaia.teste.com     vale? {email_valido('gaia.teste.com')}")
print(f"@teste.com         vale? {email_valido('@teste.com')}")
print(f"gaia@teste         vale? {email_valido('gaia@teste')}")
print(f"a@b@c.com          vale? {email_valido('a@b@c.com')}")

assert email_valido("  GAIA@Teste.COM  ") == True
assert email_valido("beto@loja.com.br") == True
assert email_valido("gaia.teste.com") == False
assert email_valido("@teste.com") == False
assert email_valido("gaia@teste") == False
assert email_valido("a@b@c.com") == False
print("As seis verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-24.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 24 da apresentacao.
#
#      15  def email_valido(email):
#          Nome que é pergunta, e devolve verdadeiro ou falso.
#
#      16  limpo = email.strip().lower()
#          O strip e o lower da Aula 05, na mesma linha. O resultado vai para
#          uma variável nova porque método de texto devolve texto novo e não
#          mexe no original.
#
#      17  partes = limpo.split("@")
#          O split da Aula 05 corta no arroba e devolve uma lista. Com um
#          arroba a lista tem 2 itens; sem nenhum, tem 1; com dois arrobas,
#          tem 3.
#
#      18  if len(partes) != 2:
#          Primeiro motivo de recusa, e ele cobre dois casos de uma vez: sem
#          arroba e com mais de um. É o len da Aula 04 fazendo trabalho de
#          validação.
#
#      19  return False
#          Devolve e encerra. Nada abaixo executa.
#
#      20  if partes[0] == "":
#          Segundo motivo. partes[0] é o que vem antes do arroba, e a lista
#          usa número, que é a metade da Aula 05 que continua valendo.
#
#      21  return False
#          Segunda saída.
#
#      22  if "." not in partes[1]:
#          Terceiro motivo. partes[1] é o domínio, e domínio sem ponto não
#          existe. not in da Aula 05.
#
#      23  return False
#          Terceira saída.
#
#      24  return True
#          O único caminho de aprovação, e é o último. Quem chega aqui passou
#          pelas três recusas.
#
#      27  print(f"  GAIA@Teste.COM   vale? {email_valido('  GAIA@Teste.COM
#          ')}")
#          Espaços nas pontas e maiúsculas, e vale True, porque a linha 16
#          limpou antes de olhar.
#
#      28  print(f"beto@loja.com.br   vale?
#          {email_valido('beto@loja.com.br')}")
#          Dois pontos no domínio, e o in da linha 22 pede um. True.
#
#      29  print(f"gaia.teste.com     vale? {email_valido('gaia.teste.com')}")
#          Ponto no lugar do arroba. partes fica com 1 item, e a linha 18
#          recusa.
#
#      30  print(f"@teste.com         vale? {email_valido('@teste.com')}")
#          Arroba certo, nada antes dele. A linha 20 recusa.
#
#      31  print(f"gaia@teste         vale? {email_valido('gaia@teste')}")
#          Arroba certo, domínio sem ponto. A linha 22 recusa.
#
#      32  print(f"a@b@c.com          vale? {email_valido('a@b@c.com')}")
#          Dois arrobas, partes com 3 itens. A linha 18 recusa, e é o caso que
#          ninguém pensa em testar.
#
# 34 a 39  os seis assert
#          Um por cenário impresso acima, na mesma ordem.
#
#      40  print("As seis verificações passaram")
#          Fecha a execução.
#
# --- fim da explicacao linha a linha ---
