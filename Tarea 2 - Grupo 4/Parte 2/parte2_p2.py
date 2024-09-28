import numpy as np
import cv2
import matplotlib.pyplot as plt

# Definir la matriz J2 de entradas reales obtenida en la Pregunta 1
J2 = np.array([[0, 1, 0, 0],
               [-1, 0, 0, 0],
               [0, 0, 0, 1],
               [0, 0, -1, 0]])

# Cargar la imagen 'lena.jpg' en escala de grises
image = cv2.imread("C:/Users/Felipe vargas/OneDrive - Estudiantes ITCR/Escritorio/CE5201-PAID/Tarea 2 - Grupo 4/Parte 2/lena.jpg", cv2.IMREAD_GRAYSCALE)

# Obtener las dimensiones de la imagen
m, n = image.shape

# Definir la transformada F para un píxel usando la matriz J2
def F_transform(A_pixel):
    Ar = A_pixel  # La imagen es en escala de grises, por lo que A_pixel es un valor único
    
    # Crear la matriz 4x4 utilizando Ar para representar el píxel
    F_A = np.array([[0, -Ar, 0, 0],
                    [Ar, 0, 0, 0],
                    [0, 0, 0, -Ar],
                    [0, 0, Ar, 0]])
    return F_A

# Definir la matriz E usando la matriz J2
def E_matrix(p, q, r, T):
    I_4 = np.eye(4)  # Matriz identidad 4x4
    
    # Calcular el término coseno y seno para la matriz E
    cos_term = np.cos(2 * np.pi * p * q / T)
    sin_term = np.sin(2 * np.pi * p * q / T)
    
    # Construir la matriz E
    E = I_4 * cos_term - J2 * sin_term
    return E

# Implementar la DFT-2D Hiperpcompleja
def hypercomplex_dft(image):
    m, n = image.shape  # Dimensiones de la imagen
    F_uv = np.zeros((m, n, 4, 4), dtype=complex)  # Inicializar la matriz F(u, v)

    # Recorrer las frecuencias (u, v)
    for u in range(m):
        for v in range(n):
            sum_F = np.zeros((4, 4), dtype=complex)  # Inicializar la suma
            
            # Calcular la suma doble de la fórmula DFT-2D
            for r in range(m):
                for s in range(n):
                    A_pixel = image[r, s]  # Valor de intensidad del píxel
                    
                    # Aplicar la transformación F[A(x, y)]
                    F_A = F_transform(A_pixel)
                    
                    # Obtener las matrices E correspondientes
                    E_r_u = E_matrix(r, u, s, m)
                    E_s_v = E_matrix(s, v, r, n)
                    
                    # Sumar a la matriz de frecuencia F(u, v)
                    sum_F += np.dot(np.dot(E_r_u, F_A), E_s_v.T)
            
            # Normalizar el resultado
            F_uv[u, v] = (1 / np.sqrt(m * n)) * sum_F
    
    return F_uv

# Aplicar la DFT-2D Hiperpcompleja
F_transformed = hypercomplex_dft(image)

# Calcular el espectro usando la norma matricial en lugar del valor absoluto
# Representación logarítmica
spectrum = np.zeros((m, n))

for u in range(m):
    for v in range(n):
        # Usar una norma matricial, por ejemplo, la norma de Frobenius
        norm_value = np.linalg.norm(F_transformed[u, v], 'fro')
        # Aplicar la representación logarítmica
        spectrum[u, v] = np.log(1 + norm_value)

# Mostrar el espectro en una imagen
plt.figure(figsize=(6, 6))
plt.imshow(spectrum, cmap='gray')
plt.title('Espectro de Frecuencia (DFT-2D Hiperpcompleja)')
plt.colorbar()
plt.show()
