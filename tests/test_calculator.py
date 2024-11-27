from calculator import suma, division,Calculadora 
import pytest

def test_suma_enteros():
    """Prueba con números enteros."""
    assert suma(2, 3) == 5

def test_suma_flotantes():
    """Prueba con números flotantes."""
    assert suma(2.5, 3.5) == 6.0

def test_suma_negativos():
    """Prueba con números negativos."""
    assert suma(-2, -3) == -5

def test_division_positivo():
    """Prueba con un divisor positivo."""
    assert division(10, 2) == 5

def test_division_negativo():
    """Prueba con un divisor negativo."""
    assert division(10, -2) == "Resultado: -5.0 (divisor negativo)"

def test_division_cero():
    """Prueba con un divisor cero."""
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        division(10, 0)

def test_division_caso_decimal():
    """Prueba con un divisor decimal."""
    assert division(7.5, 2.5) == 3.0
    
def test_suma():
    assert Calculadora.suma(3, 5) == 8

def test_resta():
    assert Calculadora.resta(10, 4) == 6

def test_multiplicacion():
    assert Calculadora.multiplicacion(2, 3) == 6

def test_division():
    assert Calculadora.division(10, 2) == 5
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        Calculadora.division(10, 0)

def test_potencia():
    assert Calculadora.potencia(2, 3) == 8
    assert Calculadora.potencia(5, 0) == 1
    assert Calculadora.potencia(2, -2) == 0.25