
import numpy as np

def AlgorCondInicMejor(A0, A1, A2, epsilon):
    G = np.dot(np.linalg.inv(np.identity(len(A0)) - A1 - A0), A2)
    Gold = np.identity(len(A0))
    cont = 0
    while np.linalg.norm(G - Gold, np.inf) > epsilon and cont!=3:
        Gold = G
        U = A1 + np.dot(A0, G)
        G = np.dot(np.linalg.inv(np.identity(len(A0)) - U), A2)
        cont = cont + 1
    return G, cont