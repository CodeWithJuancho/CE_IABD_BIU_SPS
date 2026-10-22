"""Ejercicio 1. Polinomial frente a exponencial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca para trabajar con vectores.
import numpy as np
# Interfaz gráfica de Matplotlib.
import matplotlib.pyplot as plt

m = 20
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(len(n))  # Vector de ceros del mismo tamaño. Pista: zeros y len.


# %% 2. Calcular el polinomio.
# Escribe un bucle que guarde el cuadrado de cada tamaño en y y lo imprima.
for i in range(len(n)):
    y[i] = n[i] ** 2  # Guarda el cuadrado del tamaño actual
    print(f"Tamaño: {n[i]}, Cuadrado: {y[i]}")  # Imprime el resultado

# %% 3. Gráfico del polinomio con escala lineal.
# Crea una figura, dibuja n frente a y, añade título y muestra el gráfico.
# Pista: figure, plot, title, show.
plt.figure()
plt.plot(n, y, label='Crecimiento')
plt.title('Polinomio y = n^2 (escala lineal)')
plt.xlabel('tamaño n')
plt.ylabel('Resultado y')
plt.show()

# %% 4. Gráfico del polinomio con escala vertical logarítmica.
# Dibuja los mismos datos en otra figura y cambia solo el eje vertical.
# Pista: yscale. El cero no se puede representar en esa escala.
plt.figure()
plt.plot(n, y, label='Crecimiento (Log)')
plt.yscale('log')  # Cambia el eje vertical a escala logarítmica
plt.title('Polinomio y = n^2 (escala logarítmica)')
plt.xlabel('tamaño n')
plt.ylabel('Resultado y (Escala Log)')
plt.show()

# %% 5. Calcular la exponencial.
# Reinicia y y escribe el bucle para calcular e imprimir 2 elevado a cada tamaño.
y = np.zeros(len(n))  # Reinicia 

for i in range(len(n)):
    y[i] = 2 ** n[i]  # Calcula 2 elevado al tamaño actual
    print(f"Tamaño: {n[i]}, Exponencial (2^n): {y[i]}")  # Imprime el resultado

# %% 6. Gráfico de la exponencial.
# Crea otra figura y representa n frente a y con el eje vertical logarítmico.
plt.figure()
plt.plot(n, y, label='Exponencial (Log)')
plt.yscale('log')  
plt.title('Exponencial y = 2^n (escala logarítmica)')
plt.xlabel('tamaño n')
plt.ylabel('Resultado y (Escala Log)')
plt.show()


# Responde con comentarios:
# ¿Qué función crece más deprisa?
# La función exponencial (2^n) crece muchísimo más deprisa que la polinomial (n^2).
# Al principio los valores son cercanos, pero a medida que 'n' aumenta, la exponencial
# se dispara de forma masiva superando por completo al polinomio.

# ¿Qué observas en las gráficas logarítmicas?
# Observo principalemente 2 cosas:
# 1. La función exponencial se transforma en una linea recta perfecta porque su ritmo de crecimiento multiplicativo es constante y coincide con la 
#    naturaleza del eje logarítmico.
# 2. La función polinomial (n^2) mantiene una ligera curvatura cóncava, demostrando que crece a un ritmo mucho más lento que cualquier crecimiento exponencial.