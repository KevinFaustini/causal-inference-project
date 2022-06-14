import numpy as np
from ci_test import ci_test
from helpers import *



# D: Matrix of data (numpy array with size n*p -- sample*variable)
# returns G the adjacency matrix of our graph skeleton
# returns sepSets, a list of tuples containing a 1) the two independent 
# vertices in question packed in a tuple 2) the separating set as a list


def SGS(D):
    p = D.shape[1]

    #initialize empty graph over V ie. zeros square matrix of size p
    G = np.zeros((p,p), np.int8)
    V = [*range(p)] # [0, 1, 2, 3, ... , p-1]
    sepSets = []

    n_ci_test = 0
    
    for X in V:
        for Y in range(X,p): #avoids computations for say (4,2) since it has already been done for (2,4)
            if X != Y :
                indep_X_Y = False

                V_no_XY = V[:]
                V_no_XY.remove(X)
                V_no_XY.remove(Y)

                for Z in powerset(V_no_XY): 
                    indep_X_Y = ci_test(D, X, Y, Z)
                    n_ci_test += 1

                    if indep_X_Y:
                        sepSets.append(((X,Y), Z))
                        break

                if not indep_X_Y:
                    G[X,Y] = 1
                    G[Y,X] = 1


    return G, sepSets, n_ci_test

def PC1(D):
    p = D.shape[1] 
    G = np.ones((p,p), np.int8)
    V = [*range(p)]
    d = 0
    sepSets = []
    n_ci_test = 0

    # this convert our graph matrix to its adjacency list representation as a dictionary, 
    # (so that we easily get a list of a vertex's neighbours)
    # then it gets its values (so the list of neighbours of each vertex), then sorts
    # it so that the first item is the list of neighbours of the vertex who has the most 
    # neighbours. And then we compare its length to d (=step 4)
    while len(sorted(convert_adj_matrix_to_list(G).values(), key=len, reverse=True)[0]) >= d:
        for X in V:
            for Y in range(X, p):
                if X == Y:
                    G[X,X] = 0
                elif X != Y and G[X,Y] != 0:
                    V_no_XY = V[:]
                    V_no_XY.remove(X)
                    V_no_XY.remove(Y)

                    for Z in powerset(V_no_XY, d): 
                        
                        n_ci_test +=1
                        if ci_test(D, X, Y, Z):
                            sepSets.append(((X,Y), Z))
                            G[X,Y] = 0
                            G[Y,X] = 0
                            break 
        d += 1

    return G, sepSets, n_ci_test

def PC2(D):
    p = D.shape[1]

    G = np.zeros((p,p), np.int8)
    V = [*range(p)] 
    sepSets = []

    n_ci_test = 0

    for X in V:
        for Y in range(X, p):
            if X != Y:
                V_no_XY = V[:]
                V_no_XY.remove(X)
                V_no_XY.remove(Y)

                n_ci_test += 1

                if not ci_test(D, X, Y, V_no_XY):
                    G[X,Y] = 1
                    G[Y,X] = 1   

    d = 0

    while len(sorted(convert_adj_matrix_to_list(G).values(), key=len, reverse=True)[0]) >= d:
        for X in V:
            for Y in range(X, p):
                if X != Y and G[X,Y] != 0:
                    V_no_XY = V[:]
                    V_no_XY.remove(X)
                    V_no_XY.remove(Y)

                    for Z in powerset(V_no_XY, d):  

                        n_ci_test +=1                 
                        if ci_test(D, X, Y, Z):
                            sepSets.append(((X,Y), Z))
                            G[X,Y] = 0
                            G[Y,X] = 0
                            break 
        d += 1

    return G, sepSets, n_ci_test           


def orient_edges(adj_mat, sepSets):
    p = adj_mat.shape[0]
    G = adj_mat.copy()
    
    for X in range(p):
        for Y in range(p):
            for W in range(p):
                if isVstructure(G, sepSets, X, Y, W):
                    G[Y, X] = 0 # orient the edge X -> Y by removing the direction Y -> X
                    G[Y, W] = 0 

    for A in range(p): #meek rules
        for B in range(p):
            for C in range(p):
                if (G[A,B] == 1 and G[B,A] == 0 and
                    G[B,C] == 1 and G[C,B] == 1 and
                    G[A,C] == 0 and G[C,A] == 0):
                    
                    G[C,B] = 0

                if (G[A,B] == 1 and G[B,A] == 0 and
                    G[B,C] == 1 and G[C,B] == 0 and
                    G[A,C] == 1 and G[C,A] == 1):

                    G[C,A] == 0

    return G