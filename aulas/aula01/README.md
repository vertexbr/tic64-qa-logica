# Aula 01 - Do roteiro de teste ao algoritmo

Demonstrações de código da Aula 01, para rodar com `python` a partir da raiz do repositório (`(.venv)` ativo).

## Arquivos

- `aula01_classificar_defeito.py`
- `aula01_validar_login.py`

## `aula01_classificar_defeito.py`

A Aula 01 não escreve Python: a turma sai dela com o pseudocódigo no papel. Este arquivo é a tradução, em código, do algoritmo `classificar_defeito` ensinado em aula, com a regra de negócio e o pseudocódigo comentados no topo do arquivo antes da função.

Regra: defeito que impede o uso do sistema é severidade CRÍTICA; se não impede o uso mas afeta uma funcionalidade, é ALTA; qualquer outra coisa é BAIXA.

O arquivo também traz o "erro proposital" da aula: a mesma função com as duas condições invertidas, para mostrar que a ordem das condições muda o resultado sem gerar nenhum erro de execução.

```bash
python aulas/aula01/aula01_classificar_defeito.py
```

Saída:

```
Severidade: CRÍTICA
Severidade com a ordem trocada: ALTA
```

## `aula01_validar_login.py`

Tradução, em código, do algoritmo `validar_login` ditado pela turma na Aula 01, com a regra de negócio e o pseudocódigo comentados no topo do arquivo.

Regra: o login é aprovado se o usuário está ativo E a senha está correta; ao errar a senha três vezes o usuário é bloqueado, e depois de bloqueado não entra nem com a senha certa.

Executa os quatro casos do teste de mesa feito em aula.

```bash
python aulas/aula01/aula01_validar_login.py
```

Saída:

```
Caso 1 -> resultado: APROVADO | tentativas: 0
Caso 2 -> resultado: NEGADO | tentativas: 3
Caso 3 -> resultado: BLOQUEADO | tentativas: 3
Caso 4 -> resultado: NEGADO | tentativas: 1
```

---

Este README é gerado a partir da seção correspondente do [`README.md`](../../README.md) da raiz do repositório. Para alterar a explicação de um arquivo, edite lá e regenere aqui, para as duas fontes não divergirem.
