import numpy as np
import cv2
import matplotlib.pyplot as plt

# Función principal para cargar y procesar la imagen
def load_and_process_image(image_path, resize_dim=(128, 128)):
    """
    Carga una imagen desde una ruta especificada, la convierte a RGB, 
    la normaliza y la redimensiona para el análisis.

    Entrada:
        - image_path (str): Ruta del archivo de la imagen.
        - resize_dim (tuple): Dimensiones a las que se redimensiona la imagen (por defecto 128x128).
    
    Salida:
        - img_resized (np.ndarray): Imagen redimensionada y normalizada.
        - dims (tuple): Dimensiones de la imagen redimensionada.
    
    Restricciones:
        - La imagen debe estar en formato soportado por OpenCV.
        - La ruta debe ser válida y accesible.
    """
    img = cv2.imread("C:/Users/Felipe vargas/OneDrive - Estudiantes ITCR/Escritorio/CE5201-PAID/Tarea 2 - Grupo 4/Parte 2/lena.jpg")
    if img is None:
        raise ValueError("Error: No se pudo cargar la imagen.")
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0
    img_resized = cv2.resize(img, resize_dim)
    return img_resized, img_resized.shape


# Función que calcula la DFT-2D de una imagen a color
def DFT_2D(img):
    """
    Calcula la Transformada Discreta de Fourier (DFT) 2D de una imagen de entrada.

    Entrada:
        - img (np.ndarray): Imagen de entrada redimensionada (M x N x 3), 
                            los valores deben estar normalizados.
    
    Salida:
        - dft_result (np.ndarray): Matriz compleja con el resultado de la DFT 2D.
    
    Restricciones:
        - La imagen debe ser de dimensiones MxNx3 (imagen a color).
        - La imagen debe estar normalizada (valores entre 0 y 1).
    """
    M, N = img.shape[:2]
    dft_result = np.zeros((M, N), dtype=np.complex128)

    for u in range(M):
        for v in range(N):
            sum_term = 0
            for x in range(M):
                for y in range(N):
                    pixel = img[x, y].sum() / 3  # Promedio de los canales RGB
                    exponent = np.exp(-2j * np.pi * ((u * x / M) + (v * y / N)))
                    sum_term += pixel * exponent
            dft_result[u, v] = sum_term
    return dft_result


# Función para centrar el espectro de la DFT
def center_spectrum(F_result):
    """
    Aplica fftshift para centrar las frecuencias bajas en el espectro.

    Entrada:
        - F_result (np.ndarray): Matriz compleja de la DFT 2D sin centrar.
    
    Salida:
        - F_result_shifted (np.ndarray): Espectro centrado en las frecuencias bajas.
    
    Restricciones:
        - La entrada debe ser una matriz compleja de dimensiones MxN.
    """
    return np.fft.fftshift(F_result)


# Función para calcular la magnitud logarítmica del espectro
def calculate_log_magnitude(F_shifted):
    """
    Calcula la magnitud logarítmica de la DFT para visualizar mejor el espectro.

    Entrada:
        - F_shifted (np.ndarray): Matriz compleja con la DFT centrada.
    
    Salida:
        - spectral_magnitude (np.ndarray): Matriz en escala de grises del espectro de frecuencias.
    
    Restricciones:
        - Los valores complejos deben ser convertidos a magnitudes (valor absoluto).
    """
    return np.log(np.abs(F_shifted) + 1)  # Evitar log(0) con +1


# Función para graficar el espectro de frecuencias
def plot_spectrum(spectral_magnitude):
    """
    Grafica el espectro de frecuencias en una imagen en escala de grises.

    Entrada:
        - spectral_magnitude (np.ndarray): Espectro de frecuencias en escala logarítmica.
    
    Salida:
        - Visualización del espectro de frecuencias.
    
    Restricciones:
        - La entrada debe ser una matriz 2D en escala de grises.
    """
    plt.imshow(spectral_magnitude, cmap='gray')
    plt.title('Espectro DFT-2D')
    plt.axis('off')
    plt.show()


# Función principal que integra todos los pasos para procesar la imagen y visualizar el espectro
def process_image_and_plot_spectrum(image_path):
    """
    Carga una imagen, calcula la DFT 2D, centra el espectro, calcula la magnitud logarítmica
    y muestra el espectro de frecuencias.

    Entrada:
        - image_path (str): imagen xd.
    
    Salida:
        - Visualización del espectro de frecuencias.
    """
    # Cargar y redimensionar la imagen
    img_resized, dims = load_and_process_image(image_path)
    print(f"Imagen procesada con dimensiones: {dims}")

    # Calcular la DFT-2D
    F_result = DFT_2D(img_resized)
    print("Transformada Discreta de Fourier calculada.")

    # Centrar el espectro
    F_shifted = center_spectrum(F_result)
    print("Espectro centrado con fftshift.")

    # Calcular la magnitud logarítmica
    spectral_magnitude = calculate_log_magnitude(F_shifted)
    print(f"Valores del espectro: Mínimo = {spectral_magnitude.min()}, Máximo = {spectral_magnitude.max()}")

    # Graficar el espectro
    plot_spectrum(spectral_magnitude)


# Ejecutar el procesamiento completo para una imagen específica
process_image_and_plot_spectrum('lena.jpg')  # Cambia la ruta si es necesario