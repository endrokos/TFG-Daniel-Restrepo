import numpy as np

def EscribTx(A0, A1, A2, t, n):

    m = n * len(A0)

    DiagQ0 = np.tile(np.diag(A1, k=0), n)

    DiagQ1 = np.append(np.tile(np.array(np.append(np.diag(A1, k=1), 0)), n - 1), np.diag(A1, k=1))

    DiagQ2 = np.tile(np.diag(A0, k=0), n - 1)

    DiagQmenos2 = np.tile(np.array(np.diag(A2, k=0)), n - 1)

    DiagQmenos3 = np.append(np.tile(np.array(np.append(np.diag(A2, k=-1),0)), n - 2 ),np.diag(A2, k=-1))

    Q = np.zeros((m, m))
    Q = Q + np.diag(DiagQ0, k=0) + np.diag(DiagQ1, k=1) + np.diag(DiagQ2, k=2) + np.diag(DiagQmenos2, k=-2) + np.diag(DiagQmenos3, k=-3)
    t = np.append(t, np.zeros((n-1)*len(A1)))
    return Q, t

def DistribucionP(Tx, t):
    p = np.dot(-np.linalg.inv(Tx), t)
    return p

def DistribucionMax(p, pi):
    Fmax = np.dot(p,pi)
    return Fmax

def funcDistrComp(A0, A1, A2, t, n):
    Fmax = []
    for i in range(2,n):
        Tx, t1 = EscribTx(A0, A1, A2, t, i)
        p = DistribucionP(Tx, t1)
        pi = np.append(1, np.zeros(len(p) - 1))
        Fmax.append(DistribucionMax(p, pi))
    return Fmax