"""Small math functions used for GitHub and testing exercises."""


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Subtract right from left."""
    return left - right


def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right


def divide(left: float, right: float) -> float:
    """Divide left by right."""
    if right == 0:
        raise ValueError("Cannot divide by zero")
    return left / right
