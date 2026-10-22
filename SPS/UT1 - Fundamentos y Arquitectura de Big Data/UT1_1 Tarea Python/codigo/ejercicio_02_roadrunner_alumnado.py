"""Ejercicio 2. Roadrunner.
Encuentra el mayor tamaño entero resoluble en un año de 365 días.
Coste: 10 elevado a la raíz cuadrada de [n * logaritmo decimal de n].
Completa ______ y sustituye cada ... por tu código. Puedes consultar recursos.
"""

# %% 1. Biblioteca y datos de partida.
# Biblioteca estándar de matemáticas.
import math

velocidad_cpu = 1.105 * 10**15  # Operaciones por segundo.
dias = 365
segundos = dias * 24 * 60 * 60     # Convierte los días a segundos.
presupuesto = velocidad_cpu * segundos  # Calcula las operaciones disponibles en ese tiempo.

# %% 2. Programar el coste.
def coste(n):
    # Traduce la fórmula del enunciado y devuelve su valor.
    # Pista: raíz, logaritmo decimal y potencias de Python.
    if n <= 1:
        return 1.0
    return 10 ** math.sqrt(n * math.log10(n))

# %% 3. Buscar el límite.
n = 1
# Escribe un bucle que avance de uno en uno mientras el coste sea admisible.
# Recalcula el coste en cada paso; considera admisible la igualdad.
while coste(n) <= presupuesto:
    n += 1

# %% 4. Mostrar y comprobar el resultado.
# Obtén el último tamaño admisible y muestra su valor.
# Comprueba también que el entero siguiente supera el presupuesto.
ultimo_admisible = n - 1

print(f"Presupuesto anual (365 días): {presupuesto:.6e} operaciones")
print(f"Mayor tamaño entero resoluble: n = {ultimo_admisible}")
print(f"Coste para n = {ultimo_admisible}: {coste(ultimo_admisible):.6e} operaciones (Admisible: {coste(ultimo_admisible) <= presupuesto})")
print(f"Coste para n = {n}: {coste(n):.6e} operaciones (Supera presupuesto: {coste(n) > presupuesto})")

# Responde con comentarios:
# ¿Qué valor representa n cuando termina tu búsqueda?
# 
#    Cuando termina el bucle while, la variable 'n' tiene el valor 218, que representa el PRIMER tamaño entero que EXCEDE el presupuesto de operaciones anuales disponibles.
#    Por lo tanto, el último tamaño admisible (el mayor problema resoluble en 365 días) es n - 1 = 217.
#    A pesar de contar con un superordenador de vanguardia como Roadrunner (capaz de realizar 1.105.000.000.000.000 operaciones por segundo) trabajando ininterrumpidamente durante todo un año (3,48 * 10^22 operaciones), un algoritmo con este coste no polinomial apenas permite resolver un problema de tamaño n = 217. Para un tamaño n = 218 ya se superaría el tiempo de un año completo.
