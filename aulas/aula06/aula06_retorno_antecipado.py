# Aula 06 - retorno antecipado, ou "chegou no return, acabou"
#
# Os print com espaço na frente estão aqui só para vocês verem por onde a
# função passou. Rode e compare as três chamadas.
#
# Na primeira aparece só o "checando o nome", e mais nada. Está provado na
# tela: chegou no return, acabou a função, e o resto do corpo não roda, mesmo
# que tenha vinte linhas embaixo.
#
# Isso tem nome, retorno antecipado, e é o jeito honesto de escrever
# validação: campo obrigatório vazio devolve o erro na primeira linha e nem
# tenta o resto. A alternativa é um if gigante aninhado dentro de outro, com
# quatro níveis de indentação e ninguém entendendo mais quem manda em quem.
#
# Repare que os assert do fim comparam VARIÁVEIS, e não chamam a função de
# novo. Chamar de novo dentro do assert imprimiria o rastro outra vez e a
# saída viraria sopa. É um cuidado que vale para toda função que imprime.

def validar_cadastro(nome, email):
    print("  checando o nome...")
    if nome.strip() == "":
        return "nome obrigatório"
    print("  checando o e-mail...")
    if "@" not in email:
        return "e-mail inválido"
    print("  tudo checado")
    return "ok"


print("Chamada 1, nome vazio:")
sem_nome = validar_cadastro("", "gaia@teste.com")
print(f"  devolveu: {sem_nome}")

print("Chamada 2, e-mail sem arroba:")
email_torto = validar_cadastro("Gaia", "gaia.teste.com")
print(f"  devolveu: {email_torto}")

print("Chamada 3, tudo certo:")
tudo_certo = validar_cadastro("Gaia", "gaia@teste.com")
print(f"  devolveu: {tudo_certo}")

assert sem_nome == "nome obrigatório"
assert email_torto == "e-mail inválido"
assert tudo_certo == "ok"
print("As três verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-11.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 11 da apresentacao.
#
#      19  def validar_cadastro(nome, email):
#          Dois parâmetros, e três caminhos de saída lá dentro.
#
#      20  print("  checando o nome...")
#          Rastro. Ele aparece sempre, porque é a primeira linha do corpo.
#
#      21  if nome.strip() == "":
#          O strip da Aula 05 de volta, e ele importa: um nome que é só espaço
#          passaria por um == "" sem o strip.
#
#      22  return "nome obrigatório"
#          Devolve e encerra a função ali. Nada abaixo desta linha executa
#          nesta chamada, nem os print, nem os outros if.
#
#      23  print("  checando o e-mail...")
#          Só chega aqui quem passou pela primeira validação.
#
#      24  if "@" not in email:
#          O not in da Aula 05, agora dentro de uma função.
#
#      25  return "e-mail inválido"
#          Segundo ponto de saída.
#
#      26  print("  tudo checado")
#          Só chega aqui quem passou pelas duas.
#
#      27  return "ok"
#          Terceiro ponto de saída, e é o único que significa aprovação.
#
#      30  print("Chamada 1, nome vazio:")
#          Rótulo, para a saída ficar legível na gravação.
#
#      31  sem_nome = validar_cadastro("", "gaia@teste.com")
#          Uma linha de rastro só. O e-mail está perfeito e nem foi olhado,
#          porque o return da linha 22 encerrou a função antes.
#
#      32  print(f"  devolveu: {sem_nome}")
#          Sai nome obrigatório.
#
#      34  print("Chamada 2, e-mail sem arroba:")
#          Rótulo.
#
#      35  email_torto = validar_cadastro("Gaia", "gaia.teste.com")
#          Duas linhas de rastro. Passou pelo nome, parou no e-mail.
#
#      36  print(f"  devolveu: {email_torto}")
#          Sai e-mail inválido.
#
#      38  print("Chamada 3, tudo certo:")
#          Rótulo.
#
#      39  tudo_certo = validar_cadastro("Gaia", "gaia@teste.com")
#          Três linhas de rastro. O caminho completo.
#
#      40  print(f"  devolveu: {tudo_certo}")
#          Sai ok.
#
#      42  assert sem_nome == "nome obrigatório"
#          Compara a variável, não chama a função de novo.
#
#      43  assert email_torto == "e-mail inválido"
#          Idem.
#
#      44  assert tudo_certo == "ok"
#          Idem.
#
#      45  print("As três verificações passaram")
#          Fecha a execução.
#
# --- fim da explicacao linha a linha ---
