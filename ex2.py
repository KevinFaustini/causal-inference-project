from ex1 import *
from helpers import mat_to_ndarray
import scipy.io
import numpy as np

MarketPath='/Users/sybil/PycharmProjects/causal-inference-project/market.mat'
Data=scipy.io.loadmat(MarketPath)
MarketData=Data["DI"].tolist()

# CovMatrix=np.cov(VectorYArray,MatrixZArray, bias=True)
# print(np.linalg.det(CovMatrix))

#Function to create a vector given a dataset and a company number
def VectorFct(D,k):
    Vector=[]
    for j in range(len(D[0])):
        Vector.append(MarketData[0][j][k])
    VectorArray = np.array(Vector)
    return VectorArray

#function to
def MatrixZFct(D,list):
    MatrixZ=[]
    for k in list:
        MatrixZ.append(VectorFct(D,k))
    MatrixZArray = np.array(MatrixZ)
    return MatrixZArray





