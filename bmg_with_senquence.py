#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:43:44 2019

@author: dzhong
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:07:10 2018

@author: dzhong
"""
from networkx import *
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
import math

plt.figure(figsize=(8, 8))


num_nodes=12
log2 = int(math.log(num_nodes, 2))


G = nx.cycle_graph(num_nodes)

#labels={(0,1):'seq:1',(0,11):'seq:6',(0,2):'seq:2',(0,10):'seq:5',(0,4):'seq:3',(0,8):'seq:4'}
labels={(3,5):'seq:3',(3,4):'seq:1',(3,7):'seq:5'}

for x in range (0, num_nodes):
    for j in range (0, log2+1):
        G.add_edge(x, (x - (pow(2,j)) +num_nodes)%num_nodes)
        G.add_edge(x, (x+pow(2,j))%num_nodes)
"""
for x in range (3, 4):
    for j in range (0, log2+1):
        nx.draw_networkx_edges( G, pos=nx.circular_layout(G), 
                                edgelist=[(x, (x - (pow(2,j)) +num_nodes)%num_nodes)],
                                width=3,edge_color='k',alpha =0.7)
       
        nx.draw_networkx_edges( G, pos=nx.circular_layout(G), 
                                edgelist=[(x, (x+pow(2,j))%num_nodes)],
                                width=3,edge_color='k',alpha =0.7, arrows=True,arrowsize=20, arrowstyle='fancy')
"""      
labels1={(3,7):'seq:8'}
labels2={(3,2):'seq:2',(3,1):'seq:4'}
labels3={(3,11):'seq:6'}
labels4={(3,11):'seq:7'}

nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels =labels , label_pos = 0.5, font_size = 15)

nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels =labels1 , label_pos = 0.3,
                             label_color='blue', font_size = 15,font_color='blue')
nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels =labels2 , label_pos = 0.5,
                             label_color='blue', font_size = 15,font_color='blue')

nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels =labels3 , label_pos = 0.5,
                             label_color='blue', font_size = 15,font_color='blue')
nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels =labels4 , label_pos = 0.3,
                             label_color='blue', font_size = 15,font_color='black')


posi=nx.circular_layout(G)
new_posi=nx.circular_layout(G)

posi['0']=posi.pop(3)
posi['1']=posi.pop(4)
posi['2']=posi.pop(5)
posi['3']=posi.pop(6)
posi['4']=posi.pop(7)
posi['5']=posi.pop(8)
posi['6']=posi.pop(9)
posi['7']=posi.pop(10)
posi['8']=posi.pop(11)
posi['9']=posi.pop(0)
posi['10']=posi.pop(1)
posi['11']=posi.pop(2)

new_posi[0]=posi.pop('0')
new_posi[1]=posi.pop('1')
new_posi[2]=posi.pop('2')
new_posi[3]=posi.pop('3')
new_posi[4]=posi.pop('4')
new_posi[5]=posi.pop('5')
new_posi[6]=posi.pop('6')
new_posi[7]=posi.pop('7')
new_posi[8]=posi.pop('8')
new_posi[9]=posi.pop('9')
new_posi[10]=posi.pop('10')
new_posi[11]=posi.pop('11')


nx.draw_networkx_edges( G, pos=nx.circular_layout(G), 
                                edgelist=[(3,4),(3,5),(3,1),(3,2)],
                                width=3,edge_color='black',alpha =0.7)

nx.draw_networkx_edges( G, pos=nx.circular_layout(G), 
                                edgelist=[(3,7),(3,11)],
                                width=3,edge_color='black',alpha =0.7)
#for x in range (4, 5):
    #for j in range (0, log2+1):
       # nx.draw_networkx_edges( G, pos=nx.circular_layout(G), 
                     #           edgelist=[(x, (x - (pow(2,j)) +num_nodes)%num_nodes)],
                      #          width=3,edge_color='r',alpha =0.7)
       
        #nx.draw_networkx_edges( G, pos=nx.circular_layout(G), 
                       #         edgelist=[(x, (x+pow(2,j))%num_nodes)],
                            #    width=3,edge_color='r',alpha =0.7, arrows=True,arrowsize=20, arrowstyle='fancy')
        
#labels1={(4,0):'seq:2',(4,8):'seq:1',(4,2):'seq:4',(4,6):'seq:3',(4,3):'seq:6',(4,5):'seq:5'}
        
#nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels =labels1 , label_pos = 0.6, font_size = 14, font_color='r')
nodes = nx.draw_networkx_nodes(G, new_posi,node_color='white',node_size=1500,linewidths=3)
nodes.set_edgecolor('black')

nx.draw(G, with_labels=True, node_color='none', pos=new_posi,#pos=nx.circular_layout(G), 
       edge_color ='black', width=2, font_size=30, font_weight ="regular",style = "dotted")
plt.savefig('review_BMG_seq.png',dpi=300,bbox_inches='tight')
plt.savefig('review_BMG_seq.pdf',dpi=300,bbox_inches='tight')

