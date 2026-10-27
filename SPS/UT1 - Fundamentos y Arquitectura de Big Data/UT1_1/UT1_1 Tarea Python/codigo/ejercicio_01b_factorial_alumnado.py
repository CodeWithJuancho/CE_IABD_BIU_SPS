"""Ejercicio 1.b. Factorial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca estándar de matemáticas.
# Biblioteca de vectores.
# Interfaz gráfica.
import numpy as np
import math
import matplotlib.pyplot as plt

m = 20
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(m)  # Vector de resultados inicialmente a cero. Pista: zeros.
print(n, y)
# %% 2. Calcular factoriales.
# Escribe un bucle que calcule el factorial de cada tamaño, lo guarde y lo imprima.
# Pista: math dispone de una función para calcular factoriales.
for i in n:
    y[i] = math.factorial(i)
    print(y[i])

# %% 3. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: plot, yscale y show; crea una figura nueva para cada gráfico.
plt.figure()
plt.yscale("log")
plt.plot(n[1:],y[1:])
plt.title("Grafica de eje vertical logarítmico")
plt.show()
# Responde con comentarios:
# Compara con 2 elevado a n. ¿Cómo clasificarías el crecimiento del factorial?
plt.figure()
plt.yscale("log")
plt.plot(2**n)
plt.title("Grafica de eje vertical logarítmico")
plt.show()

# 2^n crece mucho mas lento que el factorial