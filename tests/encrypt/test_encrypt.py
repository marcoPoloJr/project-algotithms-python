""" a"""
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    """ a"""

    # Teste para key ímpar
    assert encrypt_message("message", 3) == "sem_egas"

    # Teste para key par
    assert encrypt_message("message", 4) == "ega_ssem"

    # Teste para key inválido
    assert encrypt_message("message", -2) == "egassem"

    # Teste para tipos incorretos de entrada
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 3)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("trybe", 3.9)
