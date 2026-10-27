"""Ejercicio 1.b. Factorial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
import math  # Biblioteca estándar de matemáticas.
import numpy as np  # Biblioteca de vectores.
import matplotlib.pyplot as plt  # Interfaz gráfica.

m = 20
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(m)  # Vector de resultados inicialmente a cero. Pista: zeros.

# %% 2. Calcular factoriales.
# Escribe un bucle que calcule el factorial de cada tamaño, lo guarde y lo imprima.
# Pista: math dispone de una función para calcular factoriales.
for i in n:
    y[i] = math.factorial(i)
    print(i, y[i])

# %% 3. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: plot, yscale y show; crea una figura nueva para cada gráfico.
plt.figure()
plt.plot(n, y)
plt.yscale("log")
plt.title("Factorial n! (escala logarítmica)")
plt.show()

# Responde con comentarios:
# Compara con 2 elevado a n. ¿Cómo clasificarías el crecimiento del factorial?
# El factorial crece más deprisa que 2^n: con n=19, 2^19 ≈ 5,2e5 y 19! ≈ 1,2e17.
# En escala logarítmica 2^n es una recta, pero n! es una curva cuya pendiente
# aumenta (cada paso multiplica por n, no por una constante). Es un crecimiento
# superexponencial: n! ≈ sqrt(2πn)·(n/e)^n (Stirling), peor que cualquier c^n.
