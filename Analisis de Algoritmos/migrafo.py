# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:29:18 2021

@author: GabrielMtz
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node("A")
G.nodes["A"]["nombreLargo"]="vertice A"
print(G.nodes["A"])
G.nodes["A"]["nose"]=1234
print(G.nodes["A"])
G.add_edge("A","B",weight=3,heuristicaE=123.5,heristaicaM=135,nose=2132)
print(G.edges["A","B"])
G.add_edge("A","D",weight=4,nose=[12,12,1,3])
G.add_edge("B","C",weight=5,nose=[12,12,1,4])
G.add_edge("D","C",weight=1,nose=[12,12,1,5])
pos=nx.spring_layout(G)
plt.figure()
nx.draw(G,pos,with_labels=True)

labels=nx.get_edge_attributes(G,"nose")

nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
for vertice in G.nodes:
    print(vertice)
print(G.nodes["A"])
print(G.edges["A","D"])

plt.show()

