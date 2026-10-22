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
# print (segundos)
presupuesto = velocidad_cpu * segundos  # Calcula las operaciones disponibles en ese tiempo.

print(f"Segundos en un año: {segundos}")
print(f"Presupuesto de operaciones: {presupuesto:.3e}")

# %% 2. Programar el coste.
def coste(n):
    # Traduce la fórmula del enunciado y devuelve su valor.
    # Pista: raíz, logaritmo decimal y potencias de Python.
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
ultimo = n - 1  # El bucle se detiene en el primer tamaño que ya no es admisible.
print(f"Último tamaño admisible: {ultimo} (coste: {coste(ultimo):.3e})")
print(f"Siguiente tamaño: {n} (coste: {coste(n):.3e})")
print(f"¿El siguiente supera el presupuesto? {coste(n) > presupuesto}")

# Responde con comentarios:
# ¿Qué valor representa n cuando termina tu búsqueda?
# n vale 218, que es el primer tamaño cuyo coste supera el presupuesto. Por eso el mayor tamaño resoluble es n - 1 = 217 
# (su coste, 3.29e22, cabe en el presupuesto de 3.48e22, mientras que el de 218, 3.79e22, ya no cabe).
