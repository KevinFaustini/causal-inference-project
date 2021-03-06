from collections import defaultdict
from itertools import chain, combinations
import scipy.io as sio
import numpy as np


#return the subsets of the input list S of size d, or all of them if d is not specified
#eg: S = [1,2,3] then powerset(S) = [[], [1], [2], [1,2], [3], [1,3], ...]

def powerset(fullset, d=None):
    if d != None:
        return [list(i) for i in combinations(fullset, d)]
    else:
        listsub = list(fullset)
        subsets = []
        for i in range(2**len(listsub)):
            subset = []
            for k in range(len(listsub)):            
                if i & 1<<k:
                    subset.append(listsub[k])
            subsets.append(subset)        
        return subsets

def convert_adj_matrix_to_list(matrix):
    adjList = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]== 1:
                adjList[i].append(j)
            if adjList[i] is None:
                adjList[i].append(None)
                
    return adjList


def isVstructure(G, sepSets, X, Y, W):
    if G[X,Y] != 1 or G[Y, W] != 1 or G[X,W] != 0 : #is the trio a potential V structure ?
        return False
    else :
        for tuple in sepSets:
            if tuple[0] == (X,W):
                return Y not in tuple[1]


# load mat file into a n*p numpy array
def mat_to_ndarray(path):
    mat_as_dict = sio.loadmat(path) #loadmat returns a dict

    return mat_as_dict.get('D')