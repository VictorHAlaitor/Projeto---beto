import re
from datetime import datetime

def input_validado(mensagem: str, func_validacao, erro_msg="Valor inválido, tente novamente."):
    while True:
        valor = input(mensagem)
        if func_validacao(valor):
            return valor
        print(erro_msg)

def validar_email(email: str) -> bool:
    """
    Verifica se o e-mail possui formato válido básico (contém texto + '@' + texto + '.').
    """
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_data(data_str: str) -> bool:
    """
    Verifica se a data informada está no formato DD/MM/AAAA e, se possível,
    retorna True. Caso contrário, retorna False.
    """
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def validar_matricula_nao_vazia(matricula: str) -> bool:
    return bool(matricula and matricula.strip())