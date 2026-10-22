"""Ejercicio 1. Polinomial frente a exponencial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca para trabajar con vectores.
# import numpy as np
# Interfaz gráfica de Matplotlib.
import matplotlib.pyplot as plt

m = 20
n = range(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = [0] * len(n)  # Vector de ceros del mismo tamaño. Pista: zeros y len.

# %% 2. Calcular el polinomio.
# Escribe un bucle que guarde el cuadrado de cada tamaño en y y lo imprima.
for i in n:
    y[i] = i ** 2
    print(y[i])

# %% 3. Gráfico del polinomio con escala lineal.
# Crea una figura, dibuja n frente a y, añade título y muestra el gráfico.
# Pista: figure, plot, title, show.
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(n, n, marker='o', color='blue', label='n')
ax.plot(n, y, marker='s', color='red', label='n²')

ax.set_title('Complejidad n vs n²')
ax.set_xlabel('n')
ax.set_ylabel('coste de n')

ax.legend()

plt.show()

# %% 4. Gráfico del polinomio con escala vertical logarítmica.
# Dibuja los mismos datos en otra figura y cambia solo el eje vertical.
# Pista: yscale. El cero no se puede representar en esa escala.
fig_log, ax_log = plt.subplots(figsize=(8, 5))

ax_log.plot(n, n, marker='o', color='blue', label='n')
ax_log.plot(n, y, marker='s', color='red', label='n²')

ax_log.set_title('Complejidad n vs n²')
ax_log.set_xlabel('n')
ax_log.set_ylabel('coste logaritmico de n')
ax_log.set_yscale('log')

ax_log.legend()

plt.show()

# %% 5. Calcular la exponencial.
# Reinicia y y escribe el bucle para calcular e imprimir 2 elevado a cada tamaño.
for i in n:
    y[i] = 2 ** i
    print(y[i])

# %% 6. Gráfico de la exponencial.
# Crea otra figura y representa n frente a y con el eje vertical logarítmico.
fig_exp, ax_exp = plt.subplots(figsize=(8, 5))

ax_exp.plot(n, n, marker='o', color='blue', label='n')
ax_exp.plot(n, y, marker='s', color='red', label='2^n')

ax_exp.set_title('Complejidad n vs 2^n')
ax_exp.set_xlabel('n')
ax_exp.set_ylabel('coste logaritmico de n')
ax_exp.set_yscale('log')

ax_exp.legend()

plt.show()

# Responde con comentarios:
# ¿Qué función crece más deprisa? ¿Qué observas en las gráficas logarítmicas?
# La que más rápido crece es la exponencial. Las gráficas logarítmicas suben en el eje y según el nivel de complejidad y no solo por el coste. Hay que tener cuidado con las tareas cuya linea no se curban en sentido de acercase al eje x en estas gráfica.
