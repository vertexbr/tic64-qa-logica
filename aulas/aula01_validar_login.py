# Aula 01 - algoritmo de validação de login
#
# Regra de negócio, dita em aula antes de qualquer linha de pseudocódigo:
#   O login é aprovado se o usuário está ativo E a senha está correta.
#   Ao errar a senha três vezes, o usuário é bloqueado, e depois de bloqueado
#   ele não entra nem com a senha certa.
#
# Algoritmo em pseudocódigo, ditado pela turma e escrito em aula:
#
#   ALGORITMO validar_login
#   ENTRADA: usuario_ativo (sim/não), senha_correta (sim/não), tentativas_falhas (número)
#
#   INÍCIO
#       SE tentativas_falhas >= 3 ENTÃO
#           resultado recebe "BLOQUEADO"
#       SENÃO SE usuario_ativo é verdadeiro E senha_correta é verdadeiro ENTÃO
#           resultado recebe "APROVADO"
#       SENÃO
#           tentativas_falhas recebe tentativas_falhas + 1
#           resultado recebe "NEGADO"
#       FIM SE
#
#       ESCREVER resultado
#       VALIDE: resultado é uma entre APROVADO, NEGADO, BLOQUEADO
#   FIM
#
# A condição de bloqueio vem primeiro na escada de propósito: se ela viesse
# depois da checagem de senha, um usuário já bloqueado entraria acertando a
# senha, e isso seria uma falha de segurança escrita em três linhas de
# pseudocódigo.

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
# | 1    | sim            | sim            | 0                  | APROVADO                     |
# | 2    | sim            | não            | 2                  | NEGADO, e tentativas vira 3  |
# | 3    | sim            | sim            | 3                  | BLOQUEADO                    |
# | 4    | não            | sim            | 0                  | NEGADO                       |

resultado_1, tentativas_1 = validar_login(usuario_ativo=True, senha_correta=True, tentativas_falhas=0)
print(f"Caso 1 -> resultado: {resultado_1} | tentativas: {tentativas_1}")

resultado_2, tentativas_2 = validar_login(usuario_ativo=True, senha_correta=False, tentativas_falhas=2)
print(f"Caso 2 -> resultado: {resultado_2} | tentativas: {tentativas_2}")

resultado_3, tentativas_3 = validar_login(usuario_ativo=True, senha_correta=True, tentativas_falhas=3)
print(f"Caso 3 -> resultado: {resultado_3} | tentativas: {tentativas_3}")
# Usuário ativo e senha correta, mas o bloqueio já venceu: a primeira condição
# da escada pega antes de a senha ser olhada.

resultado_4, tentativas_4 = validar_login(usuario_ativo=False, senha_correta=True, tentativas_falhas=0)
print(f"Caso 4 -> resultado: {resultado_4} | tentativas: {tentativas_4}")
