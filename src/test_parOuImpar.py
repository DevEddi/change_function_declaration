import pytest
import app

def test_answer_impar():
    assert app.verificaFuncao(7) == 'Número ímpar'


def test_answer_par():
    assert app.verificaFuncao(16) == 'Número par'