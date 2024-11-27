def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def division(a, b):
    """
    Realiza la división de dos números.
    - Si el divisor es 0, lanza un ValueError.
    - Si el divisor es negativo, devuelve el resultado con un mensaje indicando divisor negativo.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    if b < 0:
        return f"Resultado: {a / b} (divisor negativo)"
    return a / b


class Calculadora:
    """Clase que realiza varias operaciones matemáticas."""

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    @staticmethod
    def potencia(base, exponente):
        return base ** exponente
