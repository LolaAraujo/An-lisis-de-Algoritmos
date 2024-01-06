# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 7:56:18 2023

@author: Lola
"""

import networkx as nx
import matplotlib.pyplot as plt
import random as rd

def peso(v1, v2, G):
    p = rd.randint(2,14)
    G.add_edge(v1, v2, weight = p)
    return v1, v2, p #devuelve la arista para guardarla
    

G = nx.Graph()
#vertices
nodo_inicial = 'L'
G.add_node(nodo_inicial)
G.add_nodes_from(['M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'A'])
aristas = [peso('L','U',G), peso('P','R',G), peso('U','A',G), peso('P','L',G), peso('M','R',G), peso('R','T',G), peso('R','S',G), peso('U','R',G),
           peso('S','U',G), peso('O','S',G), peso('N','S',G), peso('S','T',G), peso('A','S',G), peso('A','O',G), peso('O','N',G), peso('P','O',G),
           peso('N','M',G), peso('M','L',G), peso('T','N',G), peso('T','U',G), peso('M','T',G), peso('L','A',G), peso('U','N',G), peso('O','L',G), peso('R','N',G)]

#para que los vertices esten en un circulos y que las aristas no se vean sobrepuestas
pos = nx.circular_layout(G) 
plt.figure("Algoritmo Kruskal")
nx.draw(G,pos,with_labels=True)
labels=nx.get_edge_attributes(G,"weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()


def findSet(v, vertices):
    if vertices[v] != v:
        vertices[v] = findSet(vertices[v], vertices)
    return vertices[v]

def union(v1, v2, vertices):
    if v1 != v2:
        vertices[v1] = v2
        
    v1 = findSet(v1, vertices)
    v2 = findSet(v2, vertices)

# Ordena las aristas por peso
aristas.sort(key=lambda x: x[2])
print(aristas)

G_k = nx.Graph()
#diccionario para realizar un seguimiento de los vertices
node = {v: v for v in G.nodes}

for arista in aristas:
    v1, v2, p = arista
    if findSet(v1, node) != findSet(v2, node):
        G_k.add_edge(v1, v2, weight=p)
        union(v1, v2, node)


plt.figure("Algoritmo Kruskal: Camino minimo.")
nx.draw(G_k, pos, with_labels=True)
labels_k = nx.get_edge_attributes(G_k, "weight")
nx.draw_networkx_edge_labels(G_k, pos, edge_labels=labels_k)
plt.show()  
        

# grafo = nx.minimum_spanning_tree(G)
# visitados = []
# for aristas in grafo.edges(data=True):
#     visitados.append(aristas)
# print(visitados)
# Gm = nx.Graph() #Genera el grafo pero esta vacio
# Gm.add_nodes_from(['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'A'])
# Gm.add_edges_from(visitados)
# pos = nx.layout.circular_layout(Gm)
# plt.figure("Algoritmo Kruskal. Camino Minimo")
# nx.draw(Gm,pos,with_labels=True)
# labels=nx.get_edge_attributes(Gm,"weight")
# nx.draw_networkx_edge_labels(Gm, pos, edge_labels=labels)
# #plt.title("Kruskal aplicado")
# plt.show()


