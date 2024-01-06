import cv2 as cv
import numpy as np

imagenoriginal=cv.imread('pantallaVerde.jpg')
imagenOriginal=cv.resize(imagenoriginal,(1024,576),interpolation=cv.INTER_NEAREST)
imagencorea=cv.imread('corea.jpg')
imagenCorea=cv.resize(imagencorea,(1024,576),interpolation=cv.INTER_NEAREST)
cv.imshow('tokio',imagenOriginal)
cv.imshow('corea',imagenCorea)
cv.waitKey()
minBGR = np.array([0, 140, 0])
maxBGR = np.array([150, 255, 150])
 
maskBGR = cv.inRange(imagenOriginal,minBGR,maxBGR)
mask_inv = cv.bitwise_not(maskBGR)
cv.imshow('mascara',maskBGR)
cv.imshow('mascara_inv',mask_inv)

resultBGR = cv.bitwise_and(imagenOriginal, imagenOriginal, mask = mask_inv)
result_inv = cv.bitwise_and(imagenCorea, imagenCorea, mask = maskBGR)



cv.imshow('resultado',resultBGR)
cv.imshow('resultado_inv',result_inv)

total=cv.add(resultBGR,result_inv)
cv.imshow('resultado total',total)

cv.imwrite('resultado.jpg',total)
cv.waitKey()
cv.destroyAllWindows()