import numpy as np
import cv2
from scipy.ndimage import median_filter
import matplotlib.pyplot as plt

def rotacion(I, ang):
    # Obtener las dimensiones de la imagen
    m, n, r = I.shape

    # Calcular el centro de la imagen
    xc, yc = m // 2, n // 2

    # Crear la matriz de rotación utilizando la transformación afín
    a0 = np.cos(np.radians(ang))
    a1 = np.sin(np.radians(ang))
    b0 = -np.sin(np.radians(ang))
    b1 = np.cos(np.radians(ang))

    # Inicializar la imagen rotada como una matriz de ceros
    Y = np.zeros_like(I)

    for x in range(m):
        for y in range(n):
            # Aplicar las fórmulas de rotación
            x_aux = int(a0 * (x - xc) + a1 * (y - yc) + xc)
            y_aux = int(b0 * (x - xc) + b1 * (y - yc) + yc)

            # Asegurar que las coordenadas estén dentro de los límites
            if 0 <= x_aux < m and 0 <= y_aux < n:
                Y[x_aux, y_aux, :] = I[x, y, :]

    return Y

def aplicar_filtro_mediana(Y):
    # Aplicar el filtro de mediana solo a los píxeles negros
    mask = np.all(Y == [0, 0, 0], axis=-1)
    Y_filtrado = np.copy(Y)

    for i in range(3):  # Procesamos cada canal por separado
        canal = Y[:,:,i]
        canal_filtrado = median_filter(canal, size=3)
        Y_filtrado[:,:,i][mask] = canal_filtrado[mask]

    return Y_filtrado

# Cargar la imagen barbara.jpg en su resolución original
I = cv2.imread('barbara.jpg')

# Aplicar la función de rotación con un ángulo de 45 grados
Y_sin_filtro = rotacion(I, 45)

# Aplicar el filtro de la mediana a los píxeles negros de la imagen rotada
Y_con_filtro = aplicar_filtro_mediana(Y_sin_filtro)

# Mostrar las tres imágenes juntas para comparar
plt.figure(figsize=(15, 5))

# Mostrar la imagen original
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

# Mostrar la imagen rotada sin filtro
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(Y_sin_filtro, cv2.COLOR_BGR2RGB))
plt.title('Rotación 45° Sin Filtro')
plt.axis('off')

# Mostrar la imagen rotada con filtro de la mediana aplicado
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(Y_con_filtro, cv2.COLOR_BGR2RGB))
plt.title('Rotación 45° Con Filtro de Mediana')
plt.axis('off')

# Guardar la figura combinada en un archivo
plt.savefig('barbara_comparacion_triple.png')

# Mostrar la figura combinada en pantalla
plt.show()
