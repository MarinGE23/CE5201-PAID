import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.fft import fftshift, fft2

# Cargar la imagen 'lena.jpg' en escala de grises
image = cv2.imread('C:/Users/Felipe vargas/OneDrive - Estudiantes ITCR/Escritorio/CE5201-PAID/Tarea 2 - Grupo 4/Parte 2/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen fue cargada correctamente
if image is None:
    print("Error al cargar la imagen.")
else:
    print("Imagen cargada correctamente.")

# Obtener las dimensiones de la imagen
m, n = image.shape

# ====== DFT-2D Hiperpcompleja ======

# Definir la matriz J2 obtenida en la Pregunta 1
J2 = np.array([[0, 1, 0, 0],
               [-1, 0, 0, 0],
               [0, 0, 0, 1],
               [0, 0, -1, 0]])

# Definir la transformada F para un píxel usando la matriz J2
def F_transform(A_pixel):
    Ar = A_pixel  # La imagen es en escala de grises, por lo que A_pixel es un valor único
    F_A = np.array([[0, -Ar, 0, 0],
                    [Ar, 0, 0, 0],
                    [0, 0, 0, -Ar],
                    [0, 0, Ar, 0]])
    return F_A

# Definir la matriz E usando la matriz J2
def E_matrix(p, q, r, T):
    I_4 = np.eye(4)  # Matriz identidad 4x4
    cos_term = np.cos(2 * np.pi * p * q / T)
    sin_term = np.sin(2 * np.pi * p * q / T)
    E = I_4 * cos_term - J2 * sin_term
    return E

# Implementar la DFT-2D Hiperpcompleja
def hypercomplex_dft(image):
    m, n = image.shape
    F_uv = np.zeros((m, n, 4, 4), dtype=complex)

    for u in range(m):
        for v in range(n):
            sum_F = np.zeros((4, 4), dtype=complex)
            for r in range(m):
                for s in range(n):
                    A_pixel = image[r, s]
                    F_A = F_transform(A_pixel)
                    E_r_u = E_matrix(r, u, s, m)
                    E_s_v = E_matrix(s, v, r, n)
                    # Aquí corregimos la multiplicación matricial:
                    sum_F += np.dot(np.dot(E_r_u, F_A), E_s_v.T.conjugate())  # Añadimos el conjugado traspuesto
            F_uv[u, v] = (1 / np.sqrt(m * n)) * sum_F
    
    return F_uv

# Aplicar la DFT-2D Hiperpcompleja
F_transformed = hypercomplex_dft(image)

# Calcular el espectro usando la norma de Frobenius
spectrum_hypercomplex = np.zeros((m, n))

for u in range(m):
    for v in range(n):
        norm_value = np.linalg.norm(F_transformed[u, v], 'fro')
        spectrum_hypercomplex[u, v] = np.log(1 + norm_value)

# Normalizar el espectro
spectrum_hypercomplex /= np.max(spectrum_hypercomplex)

# Aplicar fftshift para centrar las frecuencias bajas
spectrum_hypercomplex_shifted = fftshift(spectrum_hypercomplex)

# Mostrar el espectro de la DFT-2D hiperpcompleja
plt.figure(figsize=(6, 6))
plt.imshow(spectrum_hypercomplex_shifted, cmap='gray', vmin=0, vmax=1)
plt.title('Espectro de Frecuencia (DFT-2D Hiperpcompleja)')
plt.colorbar()
plt.show()

# ====== DFT-2D Normal ======
# Aplicar la DFT-2D normal a la imagen para comparación
F_dft_normal = fft2(image)
spectrum_normal = np.log(1 + np.abs(F_dft_normal))
spectrum_normal_shifted = fftshift(spectrum_normal)

# Normalizar el espectro de la DFT-2D normal
spectrum_normal_shifted /= np.max(spectrum_normal_shifted)

# Mostrar el espectro de la DFT-2D normal
plt.figure(figsize=(6, 6))
plt.imshow(spectrum_normal_shifted, cmap='gray', vmin=0, vmax=1)
plt.title('Espectro de Frecuencia (DFT-2D Normal)')
plt.colorbar()
plt.show()
