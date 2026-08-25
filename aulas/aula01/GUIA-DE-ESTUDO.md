# Guia de estudo · Aula 01

> Guia leve deste repositório, com um trecho de cada arquivo e uma sugestão de treino. Não confundir com o "guia de estudo" oficial do curso (documento selado, gerado no vault do curso) — este aqui é só para quem clonou o repositório treinar sozinho.

Veja o [README.md](README.md) desta pasta para a explicação completa de cada arquivo, com a saída esperada.

## `aula01_classificar_defeito.py`

A Aula 01 não escreve Python:

```python
def classificar_defeito(impede_uso: bool, afeta_funcionalidade: bool) -> str:
    if impede_uso:
        severidade = "CRÍTICA"
    elif afeta_funcionalidade:
        severidade = "ALTA"
    else:
        severidade = "BAIXA"

    return severidade

# Teste de mesa feito em aula: impede_uso = sim, afeta_funcionalidade = sim.
severidade_correta = classificar_defeito(impede_uso=True, afeta_funcionalidade=True)
print(f"Severidade: {severidade_correta}")
# VALIDE: severidade é uma entre CRÍTICA, ALTA, BAIXA -> CRÍTICA está na lista, teste de mesa OK

# ...
```

Arquivo completo: `aulas/aula01/aula01_classificar_defeito.py` (76 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.

## `aula01_validar_login.py`

Tradução, em código, do algoritmo `validar_login` ditado pela turma na Aula 01, com a regra de negócio e o pseudocódigo comentados no topo do arquivo.

```python
def validar_login(usuario_ativo: bool, senha_correta: bool, tentativas_falhas: int) -> tuple[str, int]:
    if tentativas_falhas >= 3:
        resultado = "BLOQUEADO"
    elif usuario_ativo and senha_correta:
        resultado = "APROVADO"
    else:
        tentativas_falhas = tentativas_falhas + 1
        resultado = "NEGADO"

    return resultado, tentativas_falhas

# Massa de dados do teste de mesa feito em aula, com o resultado esperado de cada linha:
#
# | Caso | usuario_ativo | senha_correta | tentativas_falhas | Resultado esperado          |
# |------|----------------|----------------|--------------------|------------------------------|
# ...
```

Arquivo completo: `aulas/aula01/aula01_validar_login.py` (65 linhas). Para treinar, rode o arquivo, troque um valor da massa de teste e rode de novo para ver o resultado mudar.
