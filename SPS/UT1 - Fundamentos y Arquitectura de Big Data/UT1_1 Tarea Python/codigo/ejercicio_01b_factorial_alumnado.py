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

# %% 2. Calcular factoriales.
# Escribe un bucle que calcule el factorial de cada tamaño, lo guarde y lo imprima.
# Pista: math dispone de una función para calcular factoriales.
print("n (tamaño) | y = n! (operaciones)")
for i in range(len(n)):
    y[i] = math.factorial(int(n[i]))
    val_str = f"{y[i]:.4e}" if y[i] >= 1e10 else f"{int(y[i])}"
    print(f"{int(n[i]):>10} | {val_str:>21}")

# %% 3. Representar los resultados.
# Dibuja n frente a y con el eje vertical logarítmico y un título.
# Pista: plot, yscale y show; crea una figura nueva para cada gráfico.
plt.figure()
plt.plot(n, y, "o-", color="green", label="y = n!")
plt.yscale("log")
plt.title("Factorial y = n! (Escala vertical logarítmica)")
plt.xlabel("n (Tamaño del problema)")
plt.ylabel("log(y) (Operaciones)")
plt.grid(True)
plt.legend()
plt.show()

# Responde con comentarios:
# Compara con 2 elevado a n. ¿Cómo clasificarías el crecimiento del factorial?
#
#    La comparación con 2^n: El crecimiento del factorial (n!) es enormemente más rápido que el de la función exponencial (2^n).
#    A medida que n aumenta, el factorial supera a 2^n por muchos órdenes de magnitud:
#    Para n = 10: 2^10 = 1.024, mientras que 10! = 3.628.800 (más de 3.500 veces mayor).
#    Para n = 19: 2^19 = 524.288, mientras que 19! ≈ 1,216 * 10^17 (más de 230 mil millones de veces mayor).
#
#    En la clasificación del crecimiento del factorial se clasifica como SUPEREXPONENCIAL (O(n!)).
#    En una gráfica con eje vertical logarítmico (semilogarítmica):
#    Una función exponencial pura (como 2^n) se representa como una línea recta.
#    La curva del factorial es CONVEXA (se curva hacia arriba, acelerándose continuamente), ya que por la aproximación de Stirling log(n!) ≈ n * ln(n) - n, que crece más rápido que cualquier recta lineal n * ln(a).
