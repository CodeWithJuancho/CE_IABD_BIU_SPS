"""Ejercicio 1.c. Números combinatorios.
Fórmula: C(a,b) = a! / (b! * (a-b)!).
Completa ______ y sustituye cada ... por tu código. Puedes consultar recursos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca estándar de matemáticas.
import math
# Biblioteca de vectores.
import numpy as np
# Interfaz gráfica.
import matplotlib.pyplot as plt

m = 20
k = 4
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = [0] * len(n)  # Vector de resultados inicialmente a cero. Pista: zeros.

# %% 2. Programar las combinaciones.
def comb(a, b):
    # Implementa la fórmula del enunciado con factoriales y devuelve el resultado.
    return math.factorial(a) / (math.factorial(b) * math.factorial(a-b))

# %% 3. Calcular los valores.
# Escribe un bucle que calcule C(i+k,k), guarde cada resultado en y y lo imprima.
for i in n:
    y[i] = comb(i+k,k)
    print(y[i])

# %% 4. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: figure, plot, yscale y show.
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(n, n, marker='o', color='blue', label='n')
ax.plot(n, y, marker='s', color='red', label='combinación')

ax.set_title('Complejidad n vs números combinatorios')
ax.set_xlabel('n')
ax.set_ylabel('coste logaritmico de n')
ax.set_yscale('log')

ax.legend()

plt.show()

# Responde con comentarios:
# Simplifica C(i+4,4). ¿Qué crecimiento tiene cuando k permanece fijo?
# Tiene un crecimiento polinomial.