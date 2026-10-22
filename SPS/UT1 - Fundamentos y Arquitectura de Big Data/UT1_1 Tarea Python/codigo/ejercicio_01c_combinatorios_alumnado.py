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
y = np.zeros(len(n))  # Vector de resultados inicialmente a cero. Pista: zeros.

# %% 2. Programar las combinaciones.
def comb(a, b):
    # Implementa la fórmula del enunciado con factoriales y devuelve el resultado.
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

# %% 3. Calcular los valores.
# Escribe un bucle que calcule C(i+k,k), guarde cada resultado en y y lo imprima.
print(f"i (tamaño) | y = C(i+{k}, {k}) (operaciones)")
for i in range(len(n)):
    y[i] = comb(n[i] + k, k)
    print(f"{int(n[i]):>10} | {int(y[i]):>25}")

# %% 4. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: figure, plot, yscale y show.
plt.figure()
plt.plot(n, y, "o-", color="purple", label=f"y = C(n+{k}, {k})")
plt.yscale("log")
plt.title(f"Combinaciones C(n+{k}, {k}) con k={k} fijo (Escala vertical logarítmica)")
plt.xlabel("n (Tamaño del problema)")
plt.ylabel(f"log(y) (Operaciones)")
plt.grid(True)
plt.legend()
plt.show()

# Responde con comentarios:
# Simplifica C(i+4,4). ¿Qué crecimiento tiene cuando k permanece fijo?
# 
#    En la simplificación algebraica de C(i+4, 4):
#    Aplicando la fórmula C(a, b) = a! / (b! * (a - b)!):
#    C(i+4, 4) = (i+4)! / (4! * (i+4 - 4)!) = (i+4)! / (4! * i!) = ((i+4) * (i+3) * (i+2) * (i+1) * i!) / (24 * i!) = (i+4)(i+3)(i+2)(i+1) / 24 = (i^4 + 10*i^3 + 35*i^2 + 50*i + 24) / 24
#
#    Con respecto al crecimiento que tiene cuando k permanece fijo al permanecer fijo el valor de k (k = 4), los factoriales se cancelan y el término de mayor orden resultante es i^4 / 24.
#    Por lo tanto, el crecimiento es POLINOMIAL de orden O(i^4) [o O(n^k) en general].
