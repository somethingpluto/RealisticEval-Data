def frac_to_decimal(fraction: str) -> float:
    parts = [float(i) for i in fraction.split('/')]
    return parts[0] / parts[1]