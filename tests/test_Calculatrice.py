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
    assert Calculatrice().division(0, 25) == 0

def test_puissance_entier():
    assert Calculatrice().puissance(5, 2) == 25
    assert Calculatrice().puissance(4, 3) == 64

def test_puissance_negatif():
    assert Calculatrice().puissance(5, -2) == 0.04
    assert Calculatrice().puissance(28, -34) == 6.260758248562819e-50

def test_puissance_zero():
    assert Calculatrice().puissance(8, 0) == 1
