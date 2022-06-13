from ex1 import *
from helpers import mat_to_ndarray
import scipy.io
import numpy as np
from itertools import combinations
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import figure


MarketPath='/Users/sybil/PycharmProjects/causal-inference-project/market.mat'
Data=scipy.io.loadmat(MarketPath)
MarketData=Data["DI"].tolist()

# CovMatrix=np.cov(VectorYArray,MatrixZArray, bias=True)


#Function to create a vector given a dataset and a company number
def VectorFct(D,k,t):
    MatrixOne=[]
    t+=1
    for i in range(t):
        Vector=[]
        for j in range(len(D[0])):
            Vector.append(MarketData[i][j][k])
        #VectorArray = np.array(Vector)
        MatrixOne.append(Vector)
        #MatrixOneArray=np.array(MatrixOne)
    return MatrixOne

#print(len(VectorFct(MarketData,0,0)))

#function to create Matrix from a Dataset and a list of company.
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
    #MatrixFinalArray = np.array(MatrixFinal)
    return MatrixFinal


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
         Elmnt1=np.linalg.det(np.cov(np.concatenate((Yt, Z), axis=0)))
         Elmnt2 = np.linalg.det(np.cov(np.concatenate((X,Y, Z), axis=0)))
         Elmnt3 = np.linalg.det(np.cov(np.concatenate((Y, Z), axis=0)))
         Elmnt4 = np.linalg.det(np.cov(np.concatenate((X,Yt, Z), axis=0)))
         temp+=np.log((Elmnt1*Elmnt2)/(Elmnt3*Elmnt4))
     DI=0.5*temp
     DIList.append(DI)
print(PairList1)
print(DIList)



Edgesxy=[]
for i in range(len(DIList)):
    if DIList[i]>0.5:
        Edgesxy.append(1)
    else:
        Edgesxy.append(0)

LinkedNode=[]
DG = nx.DiGraph()
for i in range(len(Edgesxy)):
    if Edgesxy[i]==1:
        LinkedNode.append(PairList1[i])
print(LinkedNode)
DG.add_edges_from(LinkedNode)
nx.draw_circular(DG, with_labels=True)
plt.savefig("GraphEx2.png")





