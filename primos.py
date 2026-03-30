"""
Manejo de números primos - Segunda tarea de APA 2026
Alumno: Fulano Mengano Zutano

>>> [ n for n in range(2, 50) if esPrimo(n) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcm(42, 60, 70, 63)
1260
>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """Devuelve True si numero es primo, False si no. Eleva TypeError si numero < 2.
    >>> esPrimo(2), esPrimo(4), esPrimo(17)
    (True, False, True)
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError(f"Se esperaba un entero >= 2, no {numero!r}")
    return all(numero % d != 0 for d in range(2, int(numero**0.5) + 1))

def primos(numero):
    """Devuelve una tupla con los primos menores que numero.
    >>> primos(10)
    (2, 3, 5, 7)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos de numero.
    >>> descompon(12)
    (2, 2, 3)
    """
    factores, d = [], 2
    while d * d <= numero:
        while numero % d == 0:
            factores.append(d)
            numero //= d
        d += 1
    if numero > 1:
        factores.append(numero)
    return tuple(factores)

def mcm(*nums):
    """Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    >>> mcm(42, 60, 70, 63)
    1260
    """
    facs = [descompon(n) for n in nums]
    primos_presentes = set(p for f in facs for p in f)
    return __import__('math').prod(
        p ** max(f.count(p) for f in facs) for p in primos_presentes
    )

def mcd(*nums):
    """Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    >>> mcd(840, 630, 1050, 1470)
    210
    """
    facs = [descompon(n) for n in nums]
    primos_comunes = set(facs[0]).intersection(*facs[1:])
    return __import__('math').prod(
        p ** min(f.count(p) for f in facs) for p in primos_comunes
    )

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)