"""
Created on Fri Aug 25 22:28:56 2023
@author: Maria Cervantes
"""
import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
video = cv.VideoCapture('video.mp4')

if cam.isOpened() and video.isOpened():
    while True:
        ret, frame = cam.read()
        frame = cv.resize(frame, (1024,576))  #Dimensiones de la cámara de video 
        retVideo, frameVideo = video.read()

        if ret and retVideo:
            # Ajusta las dimensiones del video por las de la salida de video en la cámara
            #Iguala tamaños.
            frame = cv.resize(frame, (frameVideo.shape[1], frameVideo.shape[0]))

            # Azul 0, 0, 255 (en formato BGR)
            minBGR = np.array([100, 0, 0])
            maxBGR = np.array([255, 100, 100])

            maskBGR = cv.inRange(frame, minBGR, maxBGR)
            mask_inv = cv.bitwise_not(maskBGR)

            resultBGR = cv.bitwise_and(frame, frame, mask=mask_inv)
            result_inv = cv.bitwise_and(frameVideo, frameVideo, mask=maskBGR)

            total = cv.add(resultBGR, result_inv)
            cv.imshow('Video con sustitucion de colores', total)

            if cv.waitKey(1) & 0xFF == ord('i'):
                break
            
        if not retVideo:
            video.set(cv.CAP_PROP_POS_FRAMES, 0)

cam.release()
video.release()
cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np

# cam = cv.VideoCapture(0)

# if cam.isOpened():
#     while True:
#         ret, frame = cam.read()

#         imagenCorea = cv.imread('coreano.jpg')
#         imagenCorea = cv.resize(imagenCorea, (1024, 576), interpolation=cv.INTER_NEAREST)
#         frame = cv.resize(frame, (1024,576))

#         # Azul 0, 0, 255 (en formato BGR)
#         minBGR = np.array([100, 0, 0])
#         maxBGR = np.array([255, 100, 100])

#         maskBGR = cv.inRange(frame, minBGR, maxBGR)
#         mask_inv = cv.bitwise_not(maskBGR)

#         resultBGR = cv.bitwise_and(frame, frame, mask=mask_inv)
#         result_inv = cv.bitwise_and(imagenCorea, imagenCorea, mask=maskBGR)

#         total = cv.add(resultBGR, result_inv)
#         cv.imshow('resultado total', total)
        
#         if cv.waitKey(1) & 0xFF == ord('i'):
#             break

# cam.release()
# cv.destroyAllWindows()
