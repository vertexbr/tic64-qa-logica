# Aula 07 - quebrado 4 de 4: chave que não existe no dicionário
#
# Rode, leia a ÚLTIMA linha primeiro, e responda o tipo, a linha e a causa.
#
# Este é a Aula 05 cobrando o .get() que vocês aprenderam: com
# resultados.get("ignorado", 0) o programa devolveria zero em vez de quebrar.
# A escolha entre quebrar e devolver zero é sua, e depende de o campo ser
# obrigatório ou opcional.
#
# Estrutura de demonstração igual à dos outros três quebrados.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O relatório de execução mostra quantos casos passaram, quantos falharam e quantos
#   foram ignorados. Ignorado é campo opcional: pode não vir.
import traceback

resultados = {"passou": 12, "falhou": 3}

try:
    print(f"Ignorados: {resultados['ignorado']}")
except KeyError:
    traceback.print_exc()

print()
print(f"Com .get('ignorado', 0), sai: {resultados.get('ignorado', 0)}")
