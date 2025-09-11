"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from src.calculator import Calculator
def test_hello_message():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
     
    my_calculator = Calculator()
    assert my_calculator.addition(2,3) == 5

def test_substraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(6,2) == 4

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(3,5) == 15

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(8,2) == 4

def test_division_by_zero():
    my_calculator = Calculator()
    assert my_calculator.division(3,0) == "Erreur : division par zéro"

# TODO: ajoutez les tests