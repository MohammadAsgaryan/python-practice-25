def safe_divide(a, b):
    """
    Safely divides two numbers.
    Returns result, or error message if division is not possible.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Inputs must be numbers."


def convert_to_int(value):
    """
    Converts input to integer.
    Returns integer, or None if conversion fails.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
