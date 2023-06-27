import numpy as np

def AlgorProgLineal(A0,A1,A2, epsilon):

    G = np.dot(np.linalg.inv(np.identity(len(A0)) - A1), A2)
    em = np.ones(len(A0))
    cont=0
    while ((em[0] - np.dot(G, em)[0])**1000 + (em[1] - np.dot(G, em)[1])**1000)**(1/1000) > epsilon and cont!=3:
        U = A1 + np.dot(A0, G)
        G = np.dot(np.linalg.inv(np.identity(len(A0)) - U), A2)
        cont = cont + 1
    return G, cont