import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
imagenBN = cv.imread('foto.jpg', 0)

# Obtener dimensiones de la imagen
filas, columnas = imagenBN.shape

# Definir el kernel de Gauss (3x3)
kernel_gauss = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]]) / 16

# Crear una imagen en blanco para el resultado del filtro Gaussiano
imagenFiltrada = np.zeros((filas, columnas), dtype='uint8')

# Aplicar el filtro de Gauss
for i in range(1, filas-1):
    for j in range(1, columnas-1):
        imagenFiltrada[i, j] = np.sum(imagenBN[i-1:i+2, j-1:j+2] * kernel_gauss)

# Asegurarse de que los valores estén en el rango [0, 255]
imagenFiltrada = np.clip(imagenFiltrada, 0, 255)

# Mostrar la imagen original en escala de grises
cv.imshow('Imagen Original', imagenBN)

# Mostrar la imagen filtrada con el filtro de Gauss
cv.imshow('Filtro de Gauss', imagenFiltrada)

cv.waitKey()

