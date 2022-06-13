from ex1 import *
from helpers import mat_to_ndarray
import scipy.io
import numpy as np
from itertools import combinations

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
Klist2=[2,3,4,5,6,7,8,9,10,11]
PairList1=list(combinations(KList, 2))
PairList=list(combinations(KList, 2))
#
# Yt = VectorFct(MarketData,1,2)
# Z = MatrixZFct(MarketData, Klist2,2)[0]
# X=VectorFct(MarketData,0,2)
#
# print(len(np.concatenate((Yt,Z,X),axis=0)))

temp=0
DIList=[]
while len(PairList)>0:
     temp=0
     x = PairList[0][0]
     y = PairList[0][1]
     xy=[x,y]
     PairList.pop(0)
     UsedList=[n for n in KList if n not in xy]
     for t in range(6):
         Yt=VectorFct(MarketData,y,t+1)
         Z=MatrixZFct(MarketData,UsedList,t)[0]
         X=VectorFct(MarketData,x,t)
         Y=VectorFct(MarketData,y,t)
         Elmnt1=np.linalg.det(np.cov(np.concatenate((Yt, Z), axis=0)))
         Elmnt2 = np.linalg.det(np.cov(np.concatenate((X,Y, Z), axis=0)))
         Elmnt3 = np.linalg.det(np.cov(np.concatenate((Y, Z), axis=0)))
         Elmnt4 = np.linalg.det(np.cov(np.concatenate((X,Yt, Z), axis=0)))
         temp+=np.log((Elmnt1*Elmnt2)/(Elmnt3*Elmnt4))
     DI=0.5*temp
     DIList.append(DI)
print(len(DIList))
print(len(PairList1))



        # Elmnt1= np.linalg.det(np.cov(Yt, Z, bias=True))
        # Elmnt2=np.linalg.det(np.cov(Y,Z,X, bias=True))
        # Elmnt3=np.linalg.det(np.cov(Y,Z, bias=True))
        # Elmnt4= np.linalg.det(np.cov(Yt,Z,X, bias=True))

    #print(DI)
    #DIList.append(DI)





# Z=MatrixZFct(MarketData, [2,3,4,5,6,7,8,9,10,11],0)[0]
# Y=VectorFct(MarketData,0,0)[0]
#
# CovMatrix=np.cov(Y,Z, bias=True)
#
# print(np.linalg.det(CovMatrix))
#
#
# Now we contruct the matrix of y and z:
# print(MatrixZFct(MarketData,liste,1))
# CovMatrix=np.cov(VectorYArray,MatrixZArray, bias=True)
#
#
# #
# # def Merge2Matrix(y,z):
# #     Merged=[]
# #     Merged.append(y)
# #     Merged.append(z)
# #     MergedArray = np.array(Merged)
# #     return MergedArray
#
# # Y=VectorFct(MarketData,0,1)
# # Z=MatrixZFct(MarketData,[2,3,4,5,6,7,8,9,10,11],1)
# # print(Merge2Matrix(Y,Z))
#
#




