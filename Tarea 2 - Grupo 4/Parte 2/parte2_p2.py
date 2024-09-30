import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.fft import fftshift

# Cargar la imagen 'lena.jpg' en color
image = cv2.imread('C:/Users/Felipe vargas/OneDrive - Estudiantes ITCR/Escritorio/CE5201-PAID/Tarea 2 - Grupo 4/Parte 2/lena.jpg')

# Convertir la imagen a escala de grises para la DFT-2D
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtener las dimensiones de la imagen
m, n = image_gray.shape

# ====== Matriz J obtenida de la Pregunta 1 ======
# Matriz J real obtenida en la Pregunta 1
J = np.array([[0, 1, 0, 0],
              [-1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, -1, 0]])

# Función que aplica la DFT-2D hipercompleja a un píxel
def F_transform_pixel(A):
    return np.array([[0, -A, 0, 0],
                     [A, 0, 0, 0],
                     [0, 0, 0, -A],
                     [0, 0, A, 0]])

# Función E generalizada con la matriz J
def E_matrix(p, q, T):
    I4 = np.eye(4)  # Matriz identidad 4x4
    cos_term = np.cos(2 * np.pi * p * q / T)
    sin_term = np.sin(2 * np.pi * p * q / T)
    return I4 * cos_term - J * sin_term

# Implementar la DFT-2D Hipercompleja
def hypercomplex_dft(image):
    m, n = image.shape
    F_uv = np.zeros((m, n, 4, 4), dtype=complex)

    for u in range(m):
        for v in range(n):
            sum_F = np.zeros((4, 4), dtype=complex)
            for r in range(m):
                for s in range(n):
                    A_pixel = image[r, s]
                    F_A = F_transform_pixel(A_pixel)
                    E_r_u = E_matrix(r, u, m)
                    E_s_v = E_matrix(s, v, n)
                    # Multiplicación matricial hipercompleja
                    sum_F += np.dot(np.dot(E_r_u, F_A), E_s_v.T.conjugate())
            F_uv[u, v] = (1 / np.sqrt(m * n)) * sum_F
    
    return F_uv

# Aplicar la DFT-2D Hipercompleja a la imagen en escala de grises
F_transformed = hypercomplex_dft(image_gray)

# Calcular el espectro usando la norma de Frobenius (norma matricial)
spectrum_hypercomplex = np.zeros((m, n))

for u in range(m):
    for v in range(n):
        norm_value = np.linalg.norm(F_transformed[u, v], 'fro')  # Usar la norma de Frobenius
        spectrum_hypercomplex[u, v] = np.log(1 + norm_value)  # Representación logarítmica

# Normalizar el espectro
spectrum_hypercomplex /= np.max(spectrum_hypercomplex)

# Aplicar fftshift para centrar las frecuencias bajas
spectrum_hypercomplex_shifted = fftshift(spectrum_hypercomplex)

# ====== Mostrar las dos imágenes juntas en una sola ventana ======
fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # Crear una figura con 2 subplots

# Imagen 1: Imagen original en color
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Mostrar la imagen en color
axs[0].set_title('Imagen Original (lena.jpg)')
axs[0].axis('off')  # Quitar los ejes

# Imagen 2: Espectro de Frecuencia (DFT-2D Hipercompleja)
axs[1].imshow(spectrum_hypercomplex_shifted, cmap='gray', vmin=0, vmax=1)
axs[1].set_title('Espectro de Frecuencia (DFT-2D Hipercompleja)')
axs[1].axis('off')  # Quitar los ejes

# Ajustar el layout para que no haya superposiciones
plt.tight_layout()
plt.show()
