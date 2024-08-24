import cv2
import numpy as np
from matplotlib import pyplot as plt

def mediana(I):
    # Aplicar el filtro de la mediana utilizando una ventana de 3x3
    # El filtro de la mediana se aplica por separado en cada canal de la imagen a color
    Y = cv2.medianBlur(I, 3)
    return Y

# Cargar la imagen con ruido (en color)
# Se carga la imagen en color sin convertirla a escala de grises
imagen_ruido = cv2.imread('imagen1.jpg')

# Aplicar el filtro de la mediana a la imagen en color
# El filtro se aplicará en cada canal de color por separado
imagen_filtrada = mediana(imagen_ruido)

# Guardar la imagen filtrada
# El resultado se guarda en un archivo, permitiendo su análisis posterior y comparación con la imagen original
cv2.imwrite('parte1_p1.jpg', imagen_filtrada)

# Mostrar la imagen original y la imagen filtrada en color
# Comparación visual: La imagen original (con ruido) se muestra junto a la imagen filtrada para evidenciar
# la efectividad del filtro de la mediana.
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen con Ruido')
plt.imshow(cv2.cvtColor(imagen_ruido, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagen Filtrada')
plt.imshow(cv2.cvtColor(imagen_filtrada, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
