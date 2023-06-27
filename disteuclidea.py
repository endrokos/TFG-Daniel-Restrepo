import numpy as np

def disteuclidea(R1, R2):
    suma = 0
    for i in range(0,len(R1)):
        for j in range(0,len(R1[0])):
            suma = suma + (R1[i][j] - R2[i][j])**2
    return (suma)**(1/2)