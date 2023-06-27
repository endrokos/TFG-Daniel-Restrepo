import numpy as np

def calcularR(A0, A1, G):
    U = A1 + np.dot(A0, G)
    R = np.dot(A0, np.linalg.inv(np.identity(len(U)) - U))
    return R