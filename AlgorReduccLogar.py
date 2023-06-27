import numpy as np

def AlgorReduccLogar( A0, A1, A2, epsilon):
    H = np.dot(np.linalg.inv(np.identity(len(A1)) - A1), A0)
    L = np.dot(np.linalg.inv(np.identity(len(A1)) - A1), A2)
    G = L
    T = H
    em = np.ones(len(A0))
    cont = 0
    while ((em[0] - np.dot(G, em)[0])**1000 + (em[1] - np.dot(G, em)[1])**1000)**(1/1000) > epsilon and cont!=3:
        U = np.dot(H,L) + np.dot(L, H)
        M = np.dot(H, H)
        H = np.dot(np.linalg.inv(np.identity(len(A0)) - U), M)
        M = np.dot(L, L)
        L = np.dot(np.linalg.inv(np.identity(len(A0)) - U), M)
        G = G + np.dot(T, L)
        T = np.dot(T, H)
        cont= cont + 1
    return G, cont


