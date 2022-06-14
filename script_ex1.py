from ex1 import *
from helpers import mat_to_ndarray
import networkx as nx
import matplotlib.pyplot as plt 
import graphviz

path_D1 = '/Users/hannamuller/Desktop/kevin/CI project/D1.mat'
path_D2 = '/Users/hannamuller/Desktop/kevin/CI project/D2.mat'
path_D3 = '/Users/hannamuller/Desktop/kevin/CI project/D3.mat'
path_D4 = '/Users/hannamuller/Desktop/kevin/CI project/D4.mat'

output_path = '/Users/hannamuller/Desktop/kevin/CI project/graphs/'

D1 = mat_to_ndarray(path_D1)
D2 = mat_to_ndarray(path_D2)
D3 = mat_to_ndarray(path_D3)
D4 = mat_to_ndarray(path_D4)

datasets = [D1, D2, D3]
dnames = ['D1', 'D2', 'D3']

functions = [SGS, PC1, PC2]
fnames = ['SGS', 'PC1', 'PC2']

for ds, dname in zip(datasets, dnames):
    for f, fname in zip(functions, fnames):
        path = output_path + dname + '_' + fname + '_graph.png'

        f_output = f(ds)

        print('The algorithm ' + fname + ' performed ' + str(f_output[2]) + ' CI tests on the ' + dname + ' dataset.')

        G = nx.from_numpy_array(orient_edges(f_output[0], f_output[1]), create_using = nx.DiGraph)

        plt.figure()
        nx.draw_networkx(G, pos=nx.drawing.nx_agraph.graphviz_layout(G, prog="dot"), with_labels=True)        
        plt.savefig(path)


#for D4
f_output = PC2(D4)

print('The algorithm PC2 performed ' + str(f_output[2]) + ' CI tests on the D4 dataset.')

G = orient_edges(f_output[0], f_output[1])


