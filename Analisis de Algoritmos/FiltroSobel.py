import cv2 as cv
import numpy as np

# Leer la imagen en escala de grises
imagenEngris = cv.imread('corea.jpg', 0)

# Crear una matriz de ceros para el resultado
resultado = np.zeros_like(imagenEngris)

# Definir los kernels de Sobel para detección vertical y horizontal
sobel_vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_horizontal = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Aplicar el filtro de Sobel en la dirección vertical
for i in range(1, imagenEngris.shape[0] - 1):
    for j in range(1, imagenEngris.shape[1] - 1):
        gx = np.sum(imagenEngris[i-1:i+2, j-1:j+2] * sobel_vertical)
        gy = np.sum(imagenEngris[i-1:i+2, j-1:j+2] * sobel_horizontal)
        resultado[i, j] = np.sqrt(gx*2 + gy*2)

# Visualizar la imagen resultante
cv.imshow('Resultado', resultado)
cv.waitKey(0)