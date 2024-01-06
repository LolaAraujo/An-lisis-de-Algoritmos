# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 22:28:56 2023

@author: Maria Cervantes
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

arr=[4,8,6,7,8,9,9,8,7,6,5]

plt.plot(arr)
plt.ylabel('numeros')
plt.show()

plt.figure()
x1=[3,2,4,1]
x2=[1,3,16,9]
plt.plot(x1,x2)
plt.show()

plt.figure()
plt.plot(x1,x2,'ro')
plt.axis([0,20,0,10])
plt.grid()
plt.show()

plt.figure()
t=np.arange(-5,5,.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'go')
# plt.plot(t,t,'r--')

plt.show()

grupos=["grupo 1","grupo2","grupo3"]
valores=[1,10,100]
plt.figure()
plt.subplot(1,3,1)
plt.bar(grupos,valores)
plt.subplot(1,3,2)
plt.scatter(grupos,valores)
plt.subplot(1,3,3)
plt.plot(grupos,valores)
plt.suptitle("tipos de graficas")
plt.show()


def f(x):
    y = 5*x**4-12*x**3+9*x**2-6*x+3
    return y
def fPrima(x):
    return 20*x**3-36*x**2+18*x-6
def fpPrima(x):
    return 60*x**2-72*x+18

def fCod(x):
    return 8*x+4

t=np.arange(0,40,2)
plt.figure()
plt.plot(t, fCod(t), 'mo')
#plt.plot(t,f(t),'k',t,fPrima(t),'bo',t,fpPrima(t),'m')
plt.show()

img=mpimg.imread('lenna.jpg')
height,width,channels=img.shape
imgGray=np.zeros((height,width))
for i in range(height):
    for j in range(width):
        imgGray[i,j]=(int(img[i,j,0])\
            +int(img[i,j,1])+int(img[i,j,2]))//3
plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(imgGray,cmap=plt.cm.gray)
