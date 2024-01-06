# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 7:15:53 2023

@author: GabrielMtz
"""

import cv2
import numpy as np
import random 

nombreMapa="1"
#para cargar el mapa
mapa=cv2.imread('mapa'+nombreMapa+'.png')
# Para cargar la lista de indices
vertices=np.load("verticeMapa"+nombreMapa+".npy")
#pasamos la imagen a escala de grises
gray = cv2.cvtColor(mapa,cv2.COLOR_BGR2GRAY)
#muestro la imagen en escala de grises
cv2.imshow('mapa3',gray)
#obtengo un binarizacion en blanco de todos lo pixeles cuyo valor sea entre 254 y 2555
ret,th1 = cv2.threshold(gray,254,255,cv2.THRESH_BINARY)
kernel = np.ones((11,11), np.uint8) 
#aplico un filtro de dilatacion. Este filtro hace que los puntos blancos se expandan 
#probocando que algunos puntitos negros desaparecan #le pueden hacer un cv.imshow para que vean el resultado
th1 = cv2.dilate(th1,kernel,1)
#cv2.imshow('th1', th1) #-------------------------
kernel = np.ones((11,11), np.uint8) 
#cv2.imshow('kernel', kernel) #-------------------------
#Despues aplico uno de erosion que hace lo opuesto al de dilatacion
th1 = cv2.erode(th1,kernel,1)
#cv2.imshow('th1_2', th1) #-------------------------------
#aplico un flitro gausiando de 5x5  para suavisar los bordes 
th1 = cv2.GaussianBlur(th1,(5,5),cv2.BORDER_DEFAULT)
#binariso la imagen
ret,th2 = cv2.threshold(th1,235,255,cv2.THRESH_BINARY)
th2 = cv2.dilate(th2,kernel,1)
th2 = cv2.cvtColor(th2,cv2.COLOR_GRAY2BGR)

aristas = []
num_verif = 9

for verticeA in vertices:     
    cv2.circle(th2,(verticeA[1],verticeA[0]),3,(255,0,0),-1)
    #cv2.line(th2, verticeA[1], verticeB[0])
    for verticeB in vertices:
        if np.array_equal(verticeA, verticeB):
            x1, y1 = verticeA[1], verticeA[0]
            x2, y2 = verticeB[1], verticeB[0]

            ban = False
            medio = []
            
            for _ in range(num_verif):  # Generar 9 puntos medios (cambiar a 9 para 7 puntos)
                half_x = (x1 + x2) // 2
                half_y = (y1 + y2) // 2
                
                if (0 <= half_x < th2.shape[1]) and (0 <= half_y < th2.shape[0]) and (0 <= x1 < th2.shape[1]) and (0 <= y1 < th2.shape[0]) and (0 <= x2 < th2.shape[1]) and (0 <= y2 < th2.shape[0]):
                    if np.any(th2[half_y, half_x] == 255) and np.any(th2[y1, x1] == 255) and np.any(th2[y2, x2] == 255):
                        ban = True
                        medio.append((half_x, half_y))
                    else:
                        ban = False
                        break
                    x1, y1 = half_x, half_y  # Actualizar x1 y y1 para el próximo punto medio
                else:
                    ban = False
                    break

            if ban == True:
                aristas.append(((int(verticeB[1]), int(verticeB[0])), (int(verticeA[1]), int(verticeA[0]))))
                
print(medio)
print(aristas)
for ar in aristas:
    cv2.line(th2, ar, (169, 128, 233), 2)
        
cv2.imshow('asfe',th2)          


#cv2.imshow('thres2',th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

