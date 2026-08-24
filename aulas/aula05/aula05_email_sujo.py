# Aula 05 - o e-mail sujo, e o antídoto de uma família de testes instáveis
#
# Dado que vem de fora vem sujo, e comparar dado sujo sem normalizar é a causa
# número um de teste instável.
#
# Repare por que o valor aparece entre apóstrofos dentro do print: espaço não
# aparece na tela, e espaço invisível no fim de um campo é uma das causas mais
# comuns de teste que falha sem explicação. Os apóstrofos revelam ele. Esse
# truque vale a aula.

email_bruto = "  GAIA@Teste.COM  "

print(f"Original: '{email_bruto}'")
print(f"Tamanho original: {len(email_bruto)}")
print(f"Só com strip: '{email_bruto.strip()}'")
print(f"Só com lower: '{email_bruto.lower()}'")

# strip tira espaço das duas pontas, lower põe tudo em minúscula, e as duas
# juntas na mesma linha são o que se chama normalizar. Funciona porque cada
# método devolve uma string nova, e o método seguinte age sobre esse resultado.
email_limpo = email_bruto.strip().lower()

print(f"Normalizado: '{email_limpo}'")

# String em Python é IMUTÁVEL: método de texto nunca muda o original, ele
# devolve um texto novo. Se você escrever email.strip() sozinho numa linha e
# não guardar o resultado em nada, você não fez nada.
print(f"O original continua sujo? '{email_bruto}'")

print(f"Comparação sem normalizar: {email_bruto == 'gaia@teste.com'}")
print(f"Comparação com normalizar: {email_limpo == 'gaia@teste.com'}")

assert email_limpo == "gaia@teste.com"
print("Verificação passou: o e-mail normalizado bate com o esperado")

# --- split corta, e devolve lista ---
# Voltamos para a lista da Aula 04, com número na posição, e é por isso que
# aquela aula vinha antes desta.
partes = email_limpo.split("@")

print(f"Partes: {partes}")
print(f"Antes do arroba: {partes[0]}")
print(f"Depois do arroba: {partes[-1]}")

# A validação se lê em português: tem arroba, e depois do arroba tem ponto.
# Não é validação completa de e-mail, e ninguém neste curso vai escrever uma,
# mas pega os casos que aparecem em massa de teste.
email_valido = "@" in email_limpo and "." in email_limpo.split("@")[-1]

print(f"E-mail válido? {email_valido}")

assert email_valido == True

# --- join cola, e é o contrário exato do split ---
# Ele aparece aqui porque a demonstração guiada 2 usa ", ".join(problemas)
# para juntar os problemas de um usuário numa frase só.
problemas_exemplo = ["sem nome", "inativo", "sem perfil"]

print(f"Juntando com join: {', '.join(problemas_exemplo)}")

assert ", ".join(problemas_exemplo) == "sem nome, inativo, sem perfil"
print("Verificações passaram")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-16.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 16 da apresentacao.
#
#      11  email_bruto = "  GAIA@Teste.COM  "
#          Dois espaços na frente, dois atrás, e maiúscula no meio. É como o
#          dado chega de um formulário, de uma planilha de massa ou de uma
#          API.
#
#      12  Linha em branco
#          Separa a massa das leituras.
#
#      13  print(f"Original: '{email_bruto}'")
#          Sai Original: '  GAIA@Teste.COM  '. Repare nos apóstrofos dentro do
#          print: espaço não aparece na tela, e sem eles a turma não vê o
#          problema. Este truque vale a aula.
#
#      14  print(f"Tamanho original: {len(email_bruto)}")
#          Sai 18. O len da Aula 04 prova o que os apóstrofos mostram: são 14
#          caracteres visíveis e 18 de verdade. Número é mais difícil de
#          discutir que impressão visual.
#
#      15  print(f"Só com strip: '{email_bruto.strip()}'")
#          Sai 'GAIA@Teste.COM'. O strip tira espaço das duas pontas, e só
#          isso: a maiúscula continua.
#
#      16  print(f"Só com lower: '{email_bruto.lower()}'")
#          Sai '  gaia@teste.com  '. O lower põe em minúscula, e só isso: os
#          espaços continuam. Uma ferramenta por problema.
#
#      17  Linha em branco
#          Separa as ferramentas isoladas da combinação.
#
#      21  email_limpo = email_bruto.strip().lower()
#          As duas na mesma linha são o que se chama normalizar. Funciona
#          porque cada método devolve uma string nova, e o método seguinte age
#          sobre esse resultado: o lower recebe o texto que o strip já limpou.
#
#      22  Linha em branco
#          Separa a normalização da prova de que ela funcionou.
#
#      23  print(f"Normalizado: '{email_limpo}'")
#          Sai 'gaia@teste.com'. Sem espaço e em minúscula, e é este valor que
#          se compara.
#
#      28  print(f"O original continua sujo? '{email_bruto}'")
#          Sai '  GAIA@Teste.COM  ' outra vez. String em Python é imutável:
#          método de texto nunca muda o original, ele devolve um texto novo.
#          Esta linha existe só para provar isso na tela.
#
#      29  Linha em branco
#          Separa a prova da imutabilidade das duas comparações.
#
#      30  print(f"Comparação sem normalizar: {email_bruto ==
#          'gaia@teste.com'}")
#          Sai False. O sistema está certo, o cadastro está certo, e o teste
#          estava errado. É a causa número um de teste instável.
#
#      31  print(f"Comparação com normalizar: {email_limpo ==
#          'gaia@teste.com'}")
#          Sai True. A mesma comparação, com o dado limpo antes.
#
#      32  Linha em branco
#          Separa as comparações da verificação.
#
#      33  assert email_limpo == "gaia@teste.com"
#          Prova a normalização.
#
#      34  print("Verificação passou: o e-mail normalizado bate com o
#          esperado")
#          Confirma que o assert passou.
#
# --- fim da explicacao linha a linha ---
