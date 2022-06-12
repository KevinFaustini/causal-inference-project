from os import pathsep
from ex1 import *
from helpers import mat_to_ndarray
import networkx as nx
import matplotlib.pyplot as plt 


path_D1 = '/Users/hannamuller/Desktop/kevin/CI project/D1.mat'
# path_D2 = '/Users/hannamuller/Desktop/kevin/CI project/D2.mat'
# path_D3 = '/Users/hannamuller/Desktop/kevin/CI project/D3.mat'
# path_D4 = '/Users/hannamuller/Desktop/kevin/CI project/D4.mat'

D1 = mat_to_ndarray(path_D1)
# D2 = mat_to_ndarray(path_D2)
# D3 = mat_to_ndarray(path_D3)
# D4 = mat_to_ndarray(path_D4)

SGS_D1 = PC2(D1) 

d1_sgs = orient_edges(SGS_D1[0], SGS_D1[1])
# d1_pc1 = orient_edges(PC1(D1))
# d1_pc2 = orient_edges(PC2(D1))

print(d1_sgs)

# d1_graph = nx.from_numpy_array(d1_sgs, create_using = nx.DiGraph)
# subax1 = plt.subplot(121)
# nx.draw(d1_graph, with_labels=True, font_weight='bold')
# plt.show()



