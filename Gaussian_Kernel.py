import numpy as np
from scipy.sparse import linalg
from tqdm import tqdm

class GaussianKernel:
    def __init__(self,descrip_matrix):
        self.descrip_matrix = descrip_matrix

    def GaussianMatrix(self,sigma):
        X = self.descrip_matrix
        row,col=X.shape
        GassMatrix=np.zeros(shape=(row,row))
        for i in tqdm(range(row)):
            for j in range(row):
                GassMatrix[i,j]=self.Gaussian(X.getrow(i),X.getrow(j),sigma)
        return GassMatrix

    def Gaussian(self,x,y,sigma):
        return np.exp((-(linalg.norm(x-y)**2))/(2*sigma**2))
