from decimal import Decimal

def to_float(value):
    """Safely converts a value to float, accounting for Decimals and None."""
    if isinstance(value, Decimal):
        return float(value)
    return float(value) if value is not None else 0.0
