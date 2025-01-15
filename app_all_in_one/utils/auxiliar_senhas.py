import re
from hashlib import sha256
from os import getenv, urandom

from dotenv import load_dotenv


def pegar_senha_tratada(salt: bytes, senha: str) -> bool | bytes:

    if not is_senha_forte(senha):
        print(
            "A senha deve conter pelo menos 8 caracteres, incluindo:\nletras maiúsculas, minúsculas, números e caracteres especiais\n"
        )
        return False

    return hash_senha(salt, senha)


def is_senha_forte(senha) -> bool:
    """
    ^
    (?=.*[0-9])           // deve conter ao menos um dígito
    (?=.*[a-z])           // deve conter ao menos uma letra minúscula
    (?=.*[A-Z])           // deve conter ao menos uma letra maiúscula
    (?=.*[$&@#])          // deve conter ao menos um caractere especial
    [a-zA-Z0-9$&@#]{8,}   // deve conter ao menos 8 caracteres
    $
    """
    senha_forte = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$&@#])[a-zA-Z0-9$&@#]{8,}$"
    return bool(re.match(senha_forte, senha))


def gerar_salt() -> bytes:
    # valor de salt 128 bits
    salt = urandom(16)
    return salt


def gerar_pepper() -> bytes:
    load_dotenv()
    pepper = getenv("PEPPER")
    return pepper.encode()


def hash_senha(salt: bytes, senha: str) -> bytes:
    senha_hash = sha256(salt + senha.encode() + gerar_pepper())
    return salt + senha_hash.digest()
