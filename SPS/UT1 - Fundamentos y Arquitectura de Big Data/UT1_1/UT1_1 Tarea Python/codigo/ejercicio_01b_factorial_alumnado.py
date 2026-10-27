"""Ejercicio 1.b. Factorial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca estándar de matemáticas.
import math
# Biblioteca de vectores.
# import numpy as np
# Interfaz gráfica.
import matplotlib.pyplot as plt

m = 20
n = range(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = [0] * len(n)  # Vector de resultados inicialmente a cero. Pista: zeros.

# %% 2. Calcular factoriales.
# Escribe un bucle que calcule el factorial de cada tamaño, lo guarde y lo imprima.
# Pista: math dispone de una función para calcular factoriales.
for i in n:
    y[i] = math.factorial(i)
    print(y[i])

# %% 3. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: plot, yscale y show; crea una figura nueva para cada gráfico.
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(n, n, marker='o', color='blue', label='n')
ax.plot(n, y, marker='s', color='red', label='n!')

ax.set_title('Complejidad n vs n!')
ax.set_xlabel('n')
ax.set_ylabel('coste logaritmico de n')
ax.set_yscale('log')

ax.legend()

plt.show()

# Responde con comentarios:
# Compara con 2 elevado a n. ¿Cómo clasificarías el crecimiento del factorial?
# El crecimiento es mucho mayor, ya que se multiplican las misma veces, pero los operandos son mucho mayores en el factorial.
