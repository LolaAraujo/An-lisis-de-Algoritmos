"""
Created on Thu Sep  11 2023
@author: Lola
"""

import cv2 as cv
import numpy as np

imagenOriginal=cv.imread('foto500x500.jpg')  #foto original
imagenEngris=cv.imread('foto500x500.jpg',0)  #foto a escala de grises

filas,columnas=np.shape(imagenEngris)

imagenFiltro = np.zeros((filas, columnas), dtype='uint8')

# kernel de Gauss (3x3)
kernel_gauss = [[1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]]

for fila in range(1,filas-1):
    for columna in range(1,columnas-1):
        suma=0
        for i in range(3):
            for j in range(3):
                suma=suma+imagenEngris[fila-1+i, columna-1+j] * kernel_gauss[i][j]
        imagenFiltro[fila, columna]=suma/16

# for i in range(1, filas-1):
#     for j in range(1, columnas-1):
#         imagenFiltro[i, j] = np.sum(imagenEngris[i-1:i+2, j-1:j+2] * kernel_gauss)
        
imagenFiltro = np.clip(imagenFiltro, 0, 255) #valores de rango [0,255]

cv.imshow('Imagen Original',imagenOriginal)
cv.imshow('Imagen en Grises',imagenEngris)
cv.imshow('Imagen con Filtro de Gauss',imagenFiltro)
cv.waitKey()

