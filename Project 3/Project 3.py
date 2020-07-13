#The programmers for this code are Benjamin Amador and Jeffrey Weidritch
#We used the time,numpy,matplotlib,and math libraries
#Python program to implement Green's Function, Undetermined Coefficients, and Variation of Parameters

import time
import numpy as np
from scipy.integrate import quad
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
startTime = time.time()

def greenFunction():
    #cn = quad(ynx * fx, a, b, args=(a, b))/((lambdavariable - lambdan) * quad(rfunction() * ynx**2, a, b, args=(a, b)))
    return 0

def undeterminedCoefficients(a, b, c, xa, xb, xc):
    r1 = rfunctionUpper(a, b, c)
    print(r1)
    r2 = rfunctionLower(a, b, c)
    print(r2)
    ycx = "c1 * e^(", r1, "* x) + c2 * e^(", r2, "* x)"
    print("c1 * e^(", r1, "* x) + c2 * e^(", r2, "* x)")
    ypx = "Ax^2 + Bx + C"
    yppx = "2Ax + B"
    ypppx = "2A"
    print(a, "(", ypppx, ") + ", b, "(", yppx, ") + ", c, "(", ypx, ")")
    if (a == 0):
        if(b == 0):
            if(c == 0):
                print("0")
            else:
                print(c, "Ax^2 + ", c, "B + ", c, "C")
        else:
            if (c == 0):
                print(b * 2, "Ax + ", b, "B")
            else:
                print(c, "Ax^2 + (", c, "B + ", b * 2, "A)x + (", b, "B + ", c, "C)")
    else:
        if (b == 0):
            if (c == 0):
                print(a * 2, "A")
            else:
                print(c, "Ax^2 + ", c, "B + (", a * 2, "A + ", c, "C)")
        else:
            if (c == 0):
                print(b * 2, "Ax + (", a * 2, "A + ", b, "B)")
            else:
                print(c, "Ax^2 + (", c, "B + ", b * 2, "A)x + (", a * 2, "A + ", b, "B + ", c, "C)")
    A = xa / c
    print(A)
    B = (xb - (b * 2 * A)) / c
    print(B)
    C = (xc - ((a * 2 * A) + (b * B))) / c
    print(C)
    ypx = A, "x^2 + ", B, "x + ", C
    print(ypx)
    print(ypx, " + ", ycx)
    yx = ypx, " + ", ycx


    def function(x1):
        y1 = ((A * x1 ** 2) + (B * x1) + C) + math.exp(r1 * x1) + math.exp(r2 * x1)
        return np.int(y1)

    x = np.array(range(10))
    y = np.vectorize(function)

    plt.plot(x, y(x), label = yx)
    plt.xlabel('x')
    plt.ylabel('y')
    print("Program ran for %s seconds" % (time.time() - startTime))  # Prints the runtime
    plt.show()
    return yx


def variationOfParameters():
    return 0

def rfunctionUpper(a, b, c):
    r = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    return r

def rfunctionLower(a, b, c):
    r = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    return r



#print(rfunctionUpper(1, 2, 1))
#print(rfunctionLower(1, 2, 1))
undeterminedCoefficients(1, 2, 1, 0, 2, 0)