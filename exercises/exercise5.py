"""For, Sum, Reduce."""


from unittest import result


def sumatoria_basico(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """
    suma=0
    for i in range(n+1):
        suma=suma+i
    
    return suma

# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """
    return sum(range(n+1))


# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """
    producto=1

    if numeros == []:
        producto=0
        return producto
    
    for i in range(len(numeros)):
        producto=producto*numeros[i]
    
    return producto
    
# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN
