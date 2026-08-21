# Aula 05 - dividir uma data em partes, e a armadilha do zero à esquerda
#
# Isto é trabalho de QA todo santo dia: a API devolve data num formato, a tela
# mostra em outro, e alguém precisa provar que as duas dizem a mesma coisa.
#
# split no hífen já resolve a separação, e len(partes) == 3 é a verificação de
# que o formato veio como o combinado.

data_texto = "2026-08-06"
partes = data_texto.split("-")

ano = partes[0]
mes = partes[1]
dia = partes[2]

print(f"Dia: {dia}, mês: {mes}, ano: {ano}")

# Para tirar o zero de "08" eu converti para número e voltei para texto. O int
# joga o zero fora porque zero à esquerda não significa nada em número.
mes_sem_zero = str(int(mes))
data_brasileira = f"{dia}/{mes}/{ano}"
rotulo = f"{dia}/{mes_sem_zero}/{ano}"

print(f"Mês sem o zero à esquerda: {mes_sem_zero}")
print(f"Formato brasileiro: {data_brasileira}")
print(f"Rótulo do relatório: {rotulo}")

assert len(partes) == 3
assert mes_sem_zero == "8"
assert data_brasileira == "06/08/2026"
print("Verificações passaram")

# --- a armadilha, com os dois caminhos na tela ---
# lstrip("0") também devolve "8" para "08", e funciona na maioria dos casos.
# Mas "00".lstrip("0") devolve texto VAZIO, e um campo que chega como "0"
# desaparece do seu relatório sem nenhum erro.
#
# Os apóstrofos são o truque do arquivo do e-mail sujo, e é ele que faz o
# vazio ficar visível. Isto é para consultar, não para decorar: o que é para
# guardar é que existe armadilha aí.
print(f"Com str(int()): '{str(int('00'))}'")
print(f"Com lstrip:     '{'00'.lstrip('0')}'")

assert str(int("00")) == "0"
assert "00".lstrip("0") == ""
print("Verificação passou: o lstrip come o zero que era o dado")
