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

print(n)
print(y)

# %% 2. Programar las combinaciones.
def comb(a, b):
    # Implementa la fórmula del enunciado con factoriales y devuelve el resultado.
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

# %% 3. Calcular los valores.
# Escribe un bucle que calcule C(i+k,k), guarde cada resultado en y y lo imprima.
for i in range(len(n)):
    y[i] = comb(i + k, k)  # Calcula C(i+k, k) para el tamaño actual
    print(f"Tamaño: {n[i]}, Combinatorio C({n[i]}+{k},{k}): {y[i]}")  # Imprime el resultado

# %% 4. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: figure, plot, yscale y show.
plt.figure()
plt.plot(n, y, label='Crecimiento combinatorio')
plt.yscale('log')  # Cambia el eje vertical a escala logarítmica
plt.title('Combinatorio C(n+4, 4) (escala logarítmica)')
plt.xlabel('tamaño n')
plt.ylabel('Resultado y (Escala Log)')
plt.show()

# Responde con comentarios:
# Simplifica C(i+4,4). ¿Qué crecimiento tiene cuando k permanece fijo?
# C(i+4,4) = (i+4)! / (4! · i!) = (i+4)(i+3)(i+2)(i+1) / 24, que es un polinomio de grado 4.
# Por tanto, si k permanece fijo, el crecimiento es polinómico: aumenta como una potencia
# de n (en este caso n^4) y lo hace mucho más despacio que 2^n y que n!.
