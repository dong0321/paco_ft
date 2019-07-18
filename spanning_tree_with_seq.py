#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:07:10 2018

@author: dzhong
"""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

#G = nx.DiGraph()
G = nx.MultiDiGraph()
G.add_node("0",fontsize=25,penwidth=3)

for i in range(1):
    G.add_nodes_from([1,2,4,8],fontsize=25,penwidth=3)
    G.add_nodes_from([3,5,9,6,10],fontsize=25,penwidth=3)
    G.add_nodes_from([7,11],fontsize=25,penwidth=3)

#   G.add_node("Process_%i" % i)
#   G.add_node("Grandchild_%i" % i)
#   G.add_node("Greatgrandchild_%i" % i)
    G.add_edge(0,1,label="seq:1", fontsize=20,penwidth=3)
    G.add_edge(0,2,label="seq:3", fontsize=20,penwidth=3)
    G.add_edge(0,4,label="seq:5", fontsize=20,penwidth=3)
    G.add_edge(0,8,label="seq:7", fontsize=20,penwidth=3)
    G.add_edge(0,10, color='blue', label="seq:4", fontsize=20,penwidth=3)
    #G.add_node(2,color='blue',style='filled',weight=0.5)
    G.add_edge(0,11,color='blue', label="seq:2", fontsize=20,penwidth=3)
    G.add_edge(0,4, color='blue', label="seq:8", fontsize=20,penwidth=3)
    #G.add_node(2,color='blue',style='filled',weight=0.5)
    G.add_edge(0,8, label="seq:6",color='blue', fontsize=20,penwidth=3)
    G.add_edges_from([(1, 3), (1, 5),(1, 9),(2, 6), (2, 10)],penwidth=3)
    G.add_edges_from([(3, 7), (3, 11)],penwidth=3)

 #   G.add_edge("0", "Process_%i" % i)
 #   G.add_edge("Process_%i" % i, "Grandchild_%i" % i)
#    G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)
for u,v,d in G.edges(data=True):
    d['weight']=30
    #d['color']='green'
    print(d)
# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"
write_dot(G,'test.dot')

#run in shell: dot -Tpdf test.dot -o review_reorder_span.pdf

