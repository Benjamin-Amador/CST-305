# Python program to implement Runge Kutta method
import time
import math
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(1100)
startTime = time.time()

def dydx(x, y):
    return (y/(math.exp(x) - 1))


# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, h, I, count):
    y = y0
    "Apply Runge Kutta Formulas to find next value of y"
    k1 = dydx(x0, y)
    count += 1
    #print("K1 =",k1)
    k2 = dydx(x0 + (0.5 * h), y + ((0.5 * h) * k1))
    count += 1
    #print("K2 =",k2)
    k3 = dydx(x0 + (0.5 * h), y + ((0.5 * h) * k2))
    count += 1
    #print("K3 =",k3)
    k4 = dydx(x0 + h, y + h * k3)
    count += 1
    #print("K4 =",k4)

    # Update next value of y
    y = y + (h / 6.0) * (k1 + (2 * k2) + (2 * k3) + k4)
    count += 1
    yAxisPoints.append(y)

    # Update next value of x
    x = x0 + h
    count += 1
    xAxisPoints.append(x)
    print("x =",x,"\t|\t","y =",y,"\t\t","count =",count,"\t\t","solution",1000 - I,"\t\t","Execute time:",time.time()-startTime,"seconds")
    if (I > 0):
        rungeKutta(x,y,h,I-1,count)
    else:
        plt.plot(xAxisPoints, yAxisPoints, color='green', linestyle='dashed', marker='o', markerfacecolor='blue',
                 markersize=12)  # Adding graph values in and customizing the graph
        plt.ylim(5, 8)  # Setting the graph limits for the y axis
        plt.xlim(1, 21)  # Setting the graph limits for the x axis

        plt.xlabel("x axis")  # Labeling the x axis
        plt.ylabel("y axis")  # Labeling the y axis
        print("Program ran for %s seconds" % (time.time() - startTime))  # Prints the runtime
        plt.show()  # Printing the graph


# Driver method
x0 = 1
y0 = 5
h = 0.02
count = 0
xAxisPoints = [1]
yAxisPoints = [5]
rungeKutta(x0, y0, h, 999, count)