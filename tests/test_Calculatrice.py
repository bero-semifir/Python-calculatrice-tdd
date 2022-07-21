from src.Calculatrice import Calculatrice
from math import isinf

def test_addition_entier():
    res = Calculatrice().addition(5 , 6)
    assert res == 11

def test_addition_null():
    res = Calculatrice().addition(0, 8)
    assert res == 8

def test_addition_negatif():
    res = Calculatrice().addition(-2, 8)
    assert res == 6

def test_division_entier():
    res = Calculatrice().division(8, 2)
    assert res == 4

def test_division_negatif():
    res = Calculatrice().division(-8, 2)
    assert res == -4

def test_division_par_zero():
    res = Calculatrice().division(8, 0)
    assert isinf(res)

def test_division_nul():
    res = Calculatrice().division(0, 0)
    assert res == 0
