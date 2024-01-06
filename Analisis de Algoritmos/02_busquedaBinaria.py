# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Thu Nov 17 11:46:29 2019

# @author: Lola
# """

# import numpy as np
# import matplotlib.pyplot as plt
# import time
# import random
# import matplotlib.animation as manimation

# import os

# print(os.getcwd(),"-------")
# #matplotlib.use('TkAgg')
# random.seed(10)
# np.random.seed(10)

# # def busquedaBinaria(lista,elemento):
# #     izq=0
# #     der=len(lista)-1
# #     iterations=0
# #     while izq<=der:
# #         mitad=(izq+der)//2
# # #        print(mitad,' ',izq,' ',der,' ',lista[mitad])
# #         if lista[mitad]==elemento:
# #             return mitad,iterations
# #         elif(elemento<lista[mitad]):
# #             der=mitad-1
# #         else:
# #             izq=mitad+1
# #         iterations+=1
# #     return -1,iterations

# # def busquedaLineal(lista,elemento):
# #     for idx,x in enumerate(lista):
# #         if x==elemento:
# #             return x,idx+1

# #elementNumArray=[100,200,400,800,1600,3200,6400,12800,25600,51200,102400,204800,204800*2,204800*4]

# def bubbleSort(lista):
#     n = len(lista)

#     for i in range(n-1):       # <-- bucle padre
#         for j in range(n-1-i): # <-- bucle hijo
#             if lista[j] > lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
    
# def quickSort(lista):
#     global steps_quick

#     if len(lista) < 2:
#         return lista 
#     else:
#         pivot = lista[0]
#         left = [i for i in lista[1:] if i <= pivot]
#         right = [i for i in lista[1:] if i > pivot]
#         steps_quick += 1
#         return quickSort(left) + [pivot] + quickSort(right)

# elementNumArray=[100,200,400,800,1600,3200,6400,12800]
# #elementNumArray=np.arange(100,204800,100)
# tiemposBi=[]
# iteracionesBi=[]
# tiemposLi=[]
# iteracionesLi=[]



# FFMpegWriter = manimation.writers['ffmpeg']

# metadata = dict(title='Busqueda BubbleSort vs QuickSot', artist='Lola Cervantes',comment='ya me quiero dormir :)')
# writer = FFMpegWriter(fps=24, metadata=metadata)

# fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,8))
# ax1.title.set_text('BubbleSort')
# ax2.title.set_text('QuickSort')
# ax1.set_ylabel("Pasos")
# ax1.set_xlabel("# Elementos")
# ax2.set_xlabel("# Elementos")
               
# with writer.saving(fig, "BubbleVsQuickSort.mp4", 100):

#     plt.ion()
#     for idx,elementNum in enumerate(elementNumArray):
#         lista=np.sort(np.linspace(0,100000,elementNum))
#         timeBuble = 0
#         timeQuick = 0
#         start=time.time()
#         elemento,it=bubbleSort(lista,lista[-1])    
#         finish=time.time() 
#         iteracionesBi.append(it)
#         tiemposBi.append(finish-start)
        
#         start=time.time()
#         elemento,it=quickSort(lista,lista[-1]) 
#         finish=time.time()
#         iteracionesLi.append(it)
#         tiemposLi.append(finish-start)
        
#         ax1.plot(elementNumArray[:idx+1], iteracionesLi, 'r-',label='BubbleSort')
#         ax2.plot(elementNumArray[:idx+1], iteracionesBi, 'b--',label='QuickSort')

#         fig.canvas.draw()
#         fig.canvas.flush_events()
#         plt.show(block=False)

#         time.sleep(1)
#         for i in range(24):
#          writer.grab_frame()

# #fig, ax = plt.subplots()
# #line1, =ax.plot(elementNumArray,tiempos)
# #line1, =ax.plot(elementNumArray,iteraciones)
# #plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:46:29 2019

@author: Lola
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as manimation
import os

#matplotlib.use('TkAgg')
random.seed(10)
np.random.seed(10)

def bubbleSort(lista):
    n = len(lista)
    iterations = 0

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            iterations += 1
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                # lista[j], lista[j+1] = lista[j+1], lista[j]

    return iterations

def quickSort(lista):
    global it_quick
    it_quick = 0

    def _quickSort(lista):
        global it_quick

        if len(lista) < 2:
            return lista
        else:
            pivot = lista[0]
            left = [i for i in lista[1:] if i <= pivot]
            right = [i for i in lista[1:] if i > pivot]
            it_quick += 1
            return _quickSort(left) + [pivot] + _quickSort(right)

    _quickSort(lista)
    return it_quick

elementNumArray = [100, 200, 400, 800, 1600, 3200, 6400, 12800]
tiemposBi = []
iteracionesBi = []
tiemposLi = []
iteracionesLi = []

FFMpegWriter = manimation.writers['ffmpeg']

metadata = dict(title='Busqueda BubbleSort vs QuickSort', artist='Lola Cervantes', comment='ya me quiero dormir :)')
writer = FFMpegWriter(fps=24, metadata=metadata)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
ax1.title.set_text('BubbleSort')
ax2.title.set_text('QuickSort')
ax1.set_ylabel("Pasos")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")

with writer.saving(fig, "BubbleVsQuickSort.mp4", 100):
    plt.ion()
    for idx, elementNum in enumerate(elementNumArray):
        lista = np.sort(np.linspace(0, 100000, elementNum))
        
        timeBubble = 0
        timeQuick = 0
        
        start = time.time()
        iteracionesBubble = bubbleSort(lista)
        finish = time.time()
        
        iteracionesBi.append(iteracionesBubble)
        tiemposBi.append(finish - start)

        start = time.time()
        iteracionesQuick = quickSort(lista)
        finish = time.time()
        
        iteracionesLi.append(iteracionesQuick)
        tiemposLi.append(finish - start)

        ax1.plot(elementNumArray[:idx + 1], iteracionesLi, 'r-', label='BubbleSort')
        ax2.plot(elementNumArray[:idx + 1], iteracionesBi, 'b--', label='QuickSort')

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show(block=False)

        time.sleep(1)
        for i in range(24):
            writer.grab_frame()

