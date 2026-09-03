# Aula 09 - a mesma loja, com o frete estragado de propósito
#
# Uma linha muda em relação a aula09_regras.py: o >= 250.00 virou > 250.00.
# É o mesmo defeito de aulas/aula08/aula08_loja.py, e ele está aqui de novo
# porque nesta aula o que interessa não é achar o defeito, é ler o NOME da
# linha que o denunciou no relatório.
#
# O arquivo roda, não levanta erro nenhum, e devolve False para exatamente
# 250,00. Quem escrever a massa a partir do código não vê nada; quem escrever
# a partir da regra escrita testa 250,00 e o vermelho aparece.
#
# REGRA DE NEGÓCIO (a escrita no cartão, que é a que vale):
#   Frete é grátis A PARTIR de R$ 250,00, e 250,00 exato tem frete grátis.


def tem_frete_gratis(total):
    return total > 250.00
