from ex1 import *
from helpers import mat_to_ndarray
import scipy.io
import numpy as np
import pandas as pd
from itertools import combinations
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import figure

#data importation
MarketPath='/Users/sybil/PycharmProjects/causal-inference-project/market.mat'
Data=scipy.io.loadmat(MarketPath)
MarketData=Data["DI"].tolist()



#Function creation:
def VectorFct(D,k,t):
    MatrixOne=[]
    t+=1
    for i in range(t):
        Vector=[]
        for j in range(len(D[0])):
            Vector.append(MarketData[i][j][k])
        MatrixOne.append(Vector)
    return MatrixOne



def MatrixZFct(D,list,t):
    MatrixFinal=[]
    MatrixZ = []
    if t==0:
        for k in list:
            VectorTemp = []
            for j in range(len(D[0])):
                VectorTemp.append(MarketData[t][j][k])
            MatrixZ.append(VectorTemp)
    else:
        MatrixZ = []
        for i in range(t):
            for k in list:
                VectorTemp=[]
                for j in range(len(D[0])):
                    VectorTemp.append(MarketData[i][j][k])
                MatrixZ.append(VectorTemp)
    MatrixFinal.append(MatrixZ)
    return MatrixFinal


#directed information computation:
KList=[0,1,2,3,4,5,6,7,8,9,10,11]
PairList1=list(itertools.permutations(KList, 2))
PairList=list(itertools.permutations(KList, 2))

temp=0
DIList=[]
while len(PairList)>0:
     temp=0
     x = PairList[0][0]
     y = PairList[0][1]
     xy=[x,y]
     PairList.pop(0)
     UsedList=[n for n in KList if n not in xy]
     for t in range(1,6):
         Yt=VectorFct(MarketData,y,t)
         Z=MatrixZFct(MarketData,UsedList,t-1)[0]
         X=VectorFct(MarketData,x,t-1)
         Y=VectorFct(MarketData,y,t-1)
         Elmnt1 = np.linalg.det(np.cov(np.concatenate((Yt, Z), axis=0)))
         Elmnt2 = np.linalg.det(np.cov(np.concatenate((X,Y, Z), axis=0)))
         Elmnt3 = np.linalg.det(np.cov(np.concatenate((Y, Z), axis=0)))
         Elmnt4 = np.linalg.det(np.cov(np.concatenate((X,Yt, Z), axis=0)))
         temp+=np.log((Elmnt1*Elmnt2)/(Elmnt3*Elmnt4))
     DI=0.5*temp
     DIList.append(DI)

#discovering which nodes are linked:
Edgesxy=[]
for i in range(len(DIList)):
    if DIList[i]>0.5:
        Edgesxy.append(1)
    else:
        Edgesxy.append(0)
LinkedNode=[]

#Creation of the Graph
DG = nx.DiGraph()
for i in range(len(Edgesxy)):
    if Edgesxy[i]==1:
        LinkedNode.append(PairList1[i])
DG.add_edges_from(LinkedNode)
DG.add_node(3)
DG.add_node(10)
DG.add_node(11)
nx.draw_circular(DG, with_labels=True, font_weight='bold')
plt.savefig("GraphEx2.png")


#creation of the 12x12 Matrix containing the DIs
mat=np.zeros((12,12))

for i in range(len(PairList1)):
    mat[PairList1[i][0],PairList1[i][1]]=DIList[i]

Matrix_frame = pd.DataFrame(mat)
print(Matrix_frame.to_latex())
#Matrix_frame.to_excel("Matrix.xlsx")






