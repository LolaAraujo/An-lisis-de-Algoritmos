import cv2 as cv
import numpy as np

# Abre la cámara
cam = cv.VideoCapture(0)

# Lee la imagen de fondo (imagen a reemplazar)
imagenOriginal = cv.imread('pantallaVerde.jpg')

if cam.isOpened():
    while True:
        ret, frame = cam.read()
        if ret:
            # Convierte el frame capturado a RGB
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            # Define los valores de color verde que quieres reemplazar
            minBGR = np.array([35, 50, 35])
            maxBGR = np.array([90, 255, 90])

            # Crea una máscara para los píxeles verdes en el frame
            maskBGR = cv.inRange(frame, minBGR, maxBGR)
            mask_inv = cv.bitwise_not(maskBGR)

            # Reemplaza los píxeles verdes con la imagen de fondo
            result = cv.bitwise_and(frame, frame, mask=mask_inv) + cv.bitwise_and(imagenOriginal, imagenOriginal, mask=maskBGR)

            # Muestra el resultado en una ventana
            cv.imshow('Video con fondo reemplazado', result)

            # Presiona 'a' para salir del bucle
            if cv.waitKey(1) & 0xFF == ord('a'):
                break

# Libera la cámara y cierra todas las ventanas
cam.release()
cv.destroyAllWindows()
