# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
from AlgorProgLineal import AlgorProgLineal
from AlgorCondInicMejor import AlgorCondInicMejor
from AlgorReduccLogar import AlgorReduccLogar
from CalcularR import calcularR
from DistribucionMax import EscribTx, DistribucionP, DistribucionMax, funcDistrComp
from disteuclidea import disteuclidea


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    landa = 0.5
    mu = 1
    mupri = 1

    q = 0.3
    p = 0.7
    T = np.array([[-mu, mu * q], [0, -mupri]])
    t = np.array([mu*p, mupri])
    pi = [1,0]
    A0 = np.array([[landa, 0],[0, landa]])
    A1 = T - np.dot(landa, np.identity(2))
    A2 = np.array([[mu * p, 0],[mupri, 0]])


    G_AlgorProgLineal, pasos = AlgorProgLineal(A0, A1, A2, 0.0001)
    print(f"G calculado por el algoritmo básico con {pasos} pasos \n {G_AlgorProgLineal} \n")


    G_AlgorCondInicMejor, pasos = AlgorCondInicMejor(A0, A1, A2, 0.0001)
    print(f"G calculado por el algoritmo de condicion inicia mejorada  con {pasos} pasos \n {G_AlgorCondInicMejor} \n")


    G_AlgorReduccLogar, pasos = AlgorReduccLogar(A0, A1, A2, 0.0001)
    print(f"G calculado por el algoritmo de reducción logarítmica con {pasos} pasos \n {G_AlgorReduccLogar} \n")

    R_AlgorProgLineal = calcularR(A0, A1, G_AlgorProgLineal)
    print(f"La matriz R obtenida con el algoritmo de Progresión Lineal es: \n {R_AlgorProgLineal}")

    R_AlgorCondInicMejor = calcularR(A0, A1, G_AlgorCondInicMejor)
    print(f"La matriz R obtenida con el algoritmo de condicion inicia mejorada es: \n {R_AlgorCondInicMejor}")

    R_AlgorReduccLogar = calcularR(A0, A1, G_AlgorReduccLogar)
    print(f"La matriz R obtenida con el algoritmo de Reducción Logarítmica es: \n {R_AlgorReduccLogar}")


    R2 = np.dot(A0, np.linalg.inv(np.identity(len(A0)) - A1 - A0))
    print(f"R2 es la matriz \n {R2} \n")

    r_error_cuad_AlgorProgLineal = disteuclidea(R_AlgorProgLineal, R2)
    print(f"la raíz del error cuadrático medio de la matriz R_AlgorProgLineal es: \n {r_error_cuad_AlgorProgLineal}")

    r_error_cuad_AlgorCondInicMejor = disteuclidea(R_AlgorCondInicMejor, R2)
    print(f"la raíz del error cuadrático medio de la matriz R_AlgorCondInicMejor es: \n {r_error_cuad_AlgorCondInicMejor}")

    r_error_cuad_AlgorReduccLogar = disteuclidea(R_AlgorReduccLogar, R2)
    print(f"la raíz del error cuadrático medio de la matriz R_AlgorReduccLogar es: \n {r_error_cuad_AlgorReduccLogar}")


    n=5

    Tx, t1 = EscribTx(A0, A1, A2, t, 7)
    print(f" la matriz T(x) es: \n {Tx} \n")
    print(f" el vector t es: \n {t} \n")

    p = DistribucionP(Tx, t1)
    print(f" el vector p(x) viene dada por \n{p}\n")

    pi = np.append(1,np.zeros(len(p)-1))
    Fmax = DistribucionMax(p, pi)
    print(f" La matriz de la función de distribución de nivel máximo viene dada por \n {Fmax} \n")

    U2 = A1 + np.dot(R2, A2)
    G2 = np.dot(np.linalg.inv(np.identity(len(A0))- U2),A2)
    print(G2)

    Fmax3 = funcDistrComp(A0, A1, A2, t, 12)
    print(Fmax3)

    x = np.arange(len(Fmax3))
    landa = 0.33
    mu = 0.5
    mupri = 0.9
    q = 0.3
    p = 0.7
    T = np.array([[-mu, mu * q], [0, -mupri]])
    t = np.array([mu * p, mupri])
    pi = [1, 0]
    A0 = np.array([[landa, 0], [0, landa]])
    A1 = T - np.dot(landa, np.identity(2))
    A2 = np.array([[mu * p, 0], [mupri, 0]])
    Fmax2 = funcDistrComp(A0, A1, A2, t, 12)
    print(Fmax2)
    landa = 0.25
    mu = 0.5
    mupri = 1.5
    q = 0.3
    p = 0.7
    T = np.array([[-mu, mu * q], [0, -mupri]])
    t = np.array([mu * p, mupri])
    pi = [1, 0]
    A0 = np.array([[landa, 0], [0, landa]])
    A1 = T - np.dot(landa, np.identity(2))
    A2 = np.array([[mu * p, 0], [mupri, 0]])
    Fmax1 = funcDistrComp(A0, A1, A2, t, 12)
    plt.plot(x, Fmax1, 'bo-', ms=8)
    plt.plot(x, Fmax2, 'ro-', ms=8)
    plt.plot(x, Fmax3, 'go-', ms=8)
    # Configurar la gráfica
    plt.xlabel('Valores de X')
    plt.ylabel('Probabilidad acumulada')
    plt.ylim(0, 1)
    plt.title('Función de máxima')
    plt.legend()
    # Mostrar la gráfica
    plt.show()















# See PyCharm help at https://www.jetbrains.com/help/pycharm/


