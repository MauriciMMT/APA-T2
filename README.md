# Segunda tarea de APA 2026: Manejo de números primos

# Maurici Mestres Teixidor

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
  - Se debe considerar que `numero` es un número natural y mayor que uno.
  - En caso contrario, la función debe elevar la excepción `TypeError` y finalizar la ejecución.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Modifique las funciones `mcm()` y `mcd()`, para que calculen el mínimo común múltiplo y el máximo común divisor
para un número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcm(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcd(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

El resultado de ejecutar `python primos.py` con la opción `-v` (verbosa) es el siguiente:

![Ejecución de los tests unitarios](img/Captura_de_pantalla_2026-03-30_155739.png)

#### Código desarrollado

```python
"""
Manejo de números primos - Segunda tarea de APA 2026

Alumno: Fulano Mengano Zutano

Tests unitarios de las funciones incluidas en este módulo:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
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
    """
    Determina si un número natural mayor que uno es primo.

    Argumentos:
        numero: número natural mayor que uno a evaluar.

    Salida:
        True si el número es primo, False en caso contrario.

    Excepciones:
        TypeError: si numero no es un número natural mayor que uno.

    >>> esPrimo(2)
    True
    >>> esPrimo(4)
    False
    >>> esPrimo(17)
    True
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError(f"El argumento debe ser un número natural mayor que uno, no {numero!r}")

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True


def primos(numero):
    """
    Devuelve todos los números primos menores que el argumento.

    Argumentos:
        numero: límite superior (excluido) de la búsqueda de primos.

    Salida:
        Tupla con todos los números primos menores que numero.

    >>> primos(10)
    (2, 3, 5, 7)
    >>> primos(2)
    ()
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve la descomposición en factores primos de un número.

    Argumentos:
        numero: número natural mayor que uno a descomponer.

    Salida:
        Tupla con los factores primos de numero en orden creciente (con repetición).

    >>> descompon(12)
    (2, 2, 3)
    >>> descompon(7)
    (7,)
    """
    factores = []
    divisor = 2
    while divisor * divisor <= numero:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    if numero > 1:
        factores.append(numero)
    return tuple(factores)


def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    Calcula el MCM a partir de la descomposición en factores primos de cada argumento,
    tomando para cada factor primo la mayor potencia presente en cualquiera de ellos.

    Argumentos:
        *numeros: dos o más números naturales mayores que uno.

    Salida:
        Mínimo común múltiplo de todos los argumentos.

    >>> mcm(4, 6)
    12
    >>> mcm(90, 14)
    630
    >>> mcm(42, 60, 70, 63)
    1260
    """
    # Reunir las descomposiciones en factores primos de todos los argumentos
    factores_por_numero = [descompon(n) for n in numeros]

    # Obtener todos los factores primos presentes
    todos_los_primos = set(f for factores in factores_por_numero for f in factores)

    resultado = 1
    for primo in todos_los_primos:
        # Tomar la mayor potencia de este primo entre todos los números
        max_potencia = max(factores.count(primo) for factores in factores_por_numero)
        resultado *= primo ** max_potencia

    return resultado


def mcd(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    Calcula el MCD a partir de la descomposición en factores primos de cada argumento,
    tomando para cada factor primo la menor potencia presente en todos ellos.

    Argumentos:
        *numeros: dos o más números naturales mayores que uno.

    Salida:
        Máximo común divisor de todos los argumentos.

    >>> mcd(12, 8)
    4
    >>> mcd(924, 780)
    12
    >>> mcd(840, 630, 1050, 1470)
    210
    """
    # Reunir las descomposiciones en factores primos de todos los argumentos
    factores_por_numero = [descompon(n) for n in numeros]

    # Solo interesan los factores presentes en TODOS los números
    factores_comunes = set(factores_por_numero[0])
    for factores in factores_por_numero[1:]:
        factores_comunes &= set(factores)

    resultado = 1
    for primo in factores_comunes:
        # Tomar la menor potencia de este primo entre todos los números
        min_potencia = min(factores.count(primo) for factores in factores_por_numero)
        resultado *= primo ** min_potencia

    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)