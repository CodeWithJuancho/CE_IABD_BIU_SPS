"""Ejercicio 1.b. Factorial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca estándar de matemáticas.
import math
# Biblioteca de vectores.
import numpy as np
# Interfaz gráfica.
import matplotlib.pyplot as plt

m = 20
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(len(n))  # Vector de resultados inicialmente a cero. Pista: zeros.

print(n)
print(y)

# %% 2. Calcular factoriales.
# Escribe un bucle que calcule el factorial de cada tamaño, lo guarde y lo imprima.
# Pista: math dispone de una función para calcular factoriales.
for i in range(len(n)):
    y[i] = math.factorial(n[i])  # Calcula el factorial del tamaño actual
    print(f"Tamaño: {n[i]}, Factorial (n!): {y[i]}")  # Imprime el resultado

# %% 3. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: plot, yscale y show; crea una figura nueva para cada gráfico.
plt.figure()
plt.plot(n, y, label='Crecimiento factorial')
plt.yscale('log')  # Cambia el eje vertical a escala logarítmica
plt.title('Factorial y = n! (escala logarítmica)')
plt.xlabel('tamaño n')
plt.ylabel('Resultado y (Escala Log)')
plt.show()

# Responde con comentarios:
# Compara con 2 elevado a n. ¿Cómo clasificarías el crecimiento del factorial?
# El crecimiento del factorial (n!) es extremadamente más rápido que el de la exponencial (2^n). Supera a cualquier exponencial, 
# por eso se clasifica como crecimiento superexponencial.
# Al observar la gráfica logarítmica del factorial, vemos que NO se genera una línea recta, sino una curva que se inclina hacia arriba de forma convexa.
