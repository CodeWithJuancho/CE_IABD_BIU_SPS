"""Ejercicio 1.c. Números combinatorios.
Fórmula: C(a,b) = a! / (b! * (a-b)!).
Completa ______ y sustituye cada ... por tu código. Puedes consultar recursos.
"""

# %% 1. Bibliotecas y datos de partida.
import math  # Biblioteca estándar de matemáticas.
import numpy as np  # Biblioteca de vectores.
import matplotlib.pyplot as plt  # Interfaz gráfica.

m = 20
k = 4
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(m)  # Vector de resultados inicialmente a cero. Pista: zeros.

# %% 2. Programar las combinaciones.
def comb(a, b):
    # Implementa la fórmula del enunciado con factoriales y devuelve el resultado.
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

# %% 3. Calcular los valores.
# Escribe un bucle que calcule C(i+k,k), guarde cada resultado en y y lo imprima.
for i in n:
    y[i] = comb(int(i) + k, k)
    print(i, y[i])

# %% 4. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: figure, plot, yscale y show.
plt.figure()
plt.plot(n, y)
plt.yscale("log")
plt.title(f"C(n+{k},{k}) (escala logarítmica)")
plt.show()

# Responde con comentarios:
# Simplifica C(i+4,4). ¿Qué crecimiento tiene cuando k permanece fijo?
# C(i+4,4) = (i+4)! / (4!·i!) = (i+1)(i+2)(i+3)(i+4) / 24.
# Es un polinomio de grado 4 en i, así que con k fijo el crecimiento es
# polinómico, Θ(i^k). En escala logarítmica la curva se aplana, como con n^2,
# a diferencia de 2^n (recta) o n! (curva que se empina).
