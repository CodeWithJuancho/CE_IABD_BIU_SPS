"""Ejercicio 1.c. Números combinatorios.
Fórmula: C(a,b) = a! / (b! * (a-b)!).
Completa ______ y sustituye cada ... por tu código. Puedes consultar recursos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca estándar de matemáticas.
# Biblioteca de vectores.
# Interfaz gráfica.

import math
import matplotlib.pyplot as plt
import numpy as np

m = 20
k = 4
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(len(n))  # Vector de resultados inicialmente a cero. Pista: zeros.

# %% 2. Programar las combinaciones.
def comb(a, b):
    # Implementa la fórmula del enunciado con factoriales y devuelve el resultado.
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))

# %% 3. Calcular los valores.
# Escribe un bucle que calcule C(i+k,k), guarde cada resultado en y y lo imprima.
for i in range(len(n)):
    y[i] = comb(n[i] + k, k)
    print(f"Tamaño: {n[i]}, Combinación: {y[i]}")

# %% 4. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: figure, plot, yscale y show.
plt.figure()
plt.plot(n, y)
plt.yscale("log")
plt.title("Combinaciones (escala logarítmica)")
plt.xlabel("Tamaño")
plt.ylabel("Valor")
plt.show()

# Responde con comentarios:
# Simplifica C(i+4,4). ¿Qué crecimiento tiene cuando k permanece fijo?
# C(i+4,4) = (i+4)! / (4! * i!) = (i+4)(i+3)(i+2)(i+1) / (4!)
# El crecimiento es polinomial. 