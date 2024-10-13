def bezier(t: float, p0: float, p1: float, p2: float, p3: float) -> float:
    d = 1 - t
    return (p0 * d * d * d +
            3 * p1 * d * d * t +
            3 * p2 * d * t * t +
            p3 * t * t * t)