"""Ejercicio 1. Polinomial frente a exponencial.
Completa ______ y sustituye cada ... por tu código.
Puedes consultar apuntes o Internet. Ejecuta los bloques cuando estén completos.
"""

# %% 1. Bibliotecas y datos de partida.
# Biblioteca para trabajar con vectores.
import numpy as np
# Interfaz gráfica de Matplotlib.
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

m = 20
n = np.arange(m)  # Tamaños desde 0 hasta m-1. Pista: arange.
y = np.zeros(len(n))  # Vector de ceros del mismo tamaño. Pista: zeros y len.

# %% 2. Calcular el polinomio.
# Escribe un bucle que guarde el cuadrado de cada tamaño en y y lo imprima.
print("n (tamaño) | y = n^2 (operaciones)")
for i in range(len(n)):
    y[i] = n[i] ** 2
    print(f"{int(n[i]):>10} | {int(y[i]):>21}")

y_pol = y.copy()

# %% 3. Gráfico del polinomio con escala lineal.
# Crea una figura, dibuja n frente a y, añade título y muestra el gráfico.
# Pista: figure, plot, title, show.
g1 = {
    "titulo": "Polinomio y = n^2 (Escala lineal)",
    "x": n,
    "y": y_pol,
    "yscale": "linear",
    "ylabel": "y (Operaciones)",
    "color": "tab:blue",
    "label": "y = n^2",
}

# %% 4. Gráfico del polinomio con escala vertical logarítmica.
# Dibuja los mismos datos en otra figura y cambia solo el eje vertical.
# Pista: yscale. El cero no se puede representar en esa escala.
g2 = {
    "titulo": "Polinomio y = n^2 (Escala vertical logarítmica)",
    "x": n[1:],  # Se omite n=0 porque log(0) no está definido
    "y": y_pol[1:],
    "yscale": "log",
    "ylabel": "log(y) (Operaciones)",
    "color": "tab:blue",
    "label": "y = n^2",
}

# %% 5. Calcular la exponencial.
# Reinicia y y escribe el bucle para calcular e imprimir 2 elevado a cada tamaño.
y = np.zeros(len(n))
print("\nn (tamaño) | y = 2^n (operaciones)")
for i in range(len(n)):
    y[i] = 2 ** n[i]
    print(f"{int(n[i]):>10} | {int(y[i]):>21}")

y_exp = y.copy()

# %% 6. Gráfico de la exponencial.
# Crea otra figura y representa n frente a y con el eje vertical logarítmico.
g3 = {
    "titulo": "Exponencial y = 2^n (Escala vertical logarítmica)",
    "x": n,
    "y": y_exp,
    "yscale": "log",
    "ylabel": "log(y) (Operaciones)",
    "color": "red",
    "label": "y = 2^n",
}

# Visor interactivo para cambiar entre las 3 gráficas con botones ← y → o teclado
graficas = [g1, g2, g3]
indice = [0]

fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.2)

def mostrar_grafica(idx):
    ax.clear()
    g = graficas[idx]
    ax.plot(g["x"], g["y"], "o-", color=g["color"], label=g["label"])
    ax.set_yscale(g["yscale"])
    ax.set_title(f"[{idx + 1}/3] {g['titulo']}", fontsize=12, pad=10)
    ax.set_xlabel("n (Tamaño del problema)")
    ax.set_ylabel(g["ylabel"])
    ax.grid(True)
    ax.legend(loc="upper left")
    fig.canvas.draw_idle()

mostrar_grafica(indice[0])

# Botones de navegación ← y →
ax_prev = plt.axes([0.38, 0.05, 0.1, 0.07])
ax_next = plt.axes([0.52, 0.05, 0.1, 0.07])
btn_prev = Button(ax_prev, "←", hovercolor="0.85")
btn_next = Button(ax_next, "→", hovercolor="0.85")

def siguiente(event=None):
    indice[0] = (indice[0] + 1) % len(graficas)
    mostrar_grafica(indice[0])

def anterior(event=None):
    indice[0] = (indice[0] - 1) % len(graficas)
    mostrar_grafica(indice[0])

btn_next.on_clicked(siguiente)
btn_prev.on_clicked(anterior)

def on_key(event):
    if event.key in ["right", "d", " "]:
        siguiente()
    elif event.key in ["left", "a"]:
        anterior()

fig.canvas.mpl_connect("key_press_event", on_key)

plt.show()

# Responde con comentarios:
# ¿Qué función crece más deprisa? ¿Qué observas en las gráficas logarítmicas?
# 
#   La función exponencial (2^n) crece muchísimo más deprisa que la función polinomial (n^2).
#   A medida que n aumenta, la diferencia es abrumadora:
#   Para n = 10: n^2 = 100 mientras que 2^10 = 1.024 (10 veces más).
#   Para n = 19: n^2 = 361 mientras que 2^19 = 524.288 (más de 1.450 veces más).
#
#   En la gráfica logarítmica del polinomio (y = n^2), la curva es CÓNCAVA (se curva hacia abajo y se aplana a medida que n crece), ya que log(n^2) = 2 * log(n), mostrando un crecimiento sublineal en esta escala.
#   En la gráfica logarítmica de la exponencial (y = 2^n), la curva se convierte en una LÍNEA RECTA PERFECTA, ya que log(2^n) = n * log(2), lo que demuestra que su tasa de crecimiento relativo es constante y exponencialmente explosiva.
