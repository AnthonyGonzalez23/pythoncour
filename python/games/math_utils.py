def addition(a, b):
    """Add two numbers and return the result."""
    return a + b

def soustraction(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiplication(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def division(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Division par zéro n'est pas autorisée.")
    return a / b

def puissance(a, b):
    """Raise a to the power of b and return the result."""
    return a ** b