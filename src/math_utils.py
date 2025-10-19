def is_prime(n: int) -> bool:
    """
    Determina si n es primo.
    Reglas:
      - n < 2  -> no primo
      - 2 o 3  -> primo
      - pares  -> no primo
      - probar divisores impares hasta sqrt(n)
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    d = 3
    # Nota: usamos d * d <= n para evitar sqrt
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def safe_div(a: int, b: int) -> int:
    """
    División entera segura.
    - Si b == 0: lanza ValueError
    - Si b != 0: retorna a // b
    """
    if b == 0:
        raise ValueError("division by zero")
    return a // b
