import sys
import os
# Adiciona o diretório app ao path para o pytest encontrar o módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.converter import f_to_c, c_to_f

def test_f_to_c_success():
    assert f_to_c(32) == 0
    assert f_to_c(212) == 100

def test_c_to_f_success():
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212
