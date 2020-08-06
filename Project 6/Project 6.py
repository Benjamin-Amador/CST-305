#Benjamin Amador & Jeffrey Weidritch
#We used the math library to complete this code

import math

def taylorPDerivitave(y2, y1, y0, y10, y00, y2x, y1x, y0x):
    y1 = (y1 * y10) / y2
    y0 = (y0 * y00) / y2

    if y2 != 0:
        if (y0x == 0):
            if (y1x == 0):
                y20 = 0
            else:
                if y1x == 1:
                    y20 = y1 * y1x
                else:
                    y20 = 0
        else:
            if (y1x == 0):
                if y0x == 1:
                    y20 = y0 * y0x
                else:
                    y20 = 0
            else:
                if y1x == 1 and y0x == 1:
                    y20 = (y1 * y1x) + (y0 * y0x)
                elif y1x != 1 and y0x == 1:
                    y20 = y0 * y0x
                elif y1x == 1 and y0x != 1:
                    y20 = y1 * y1x
                else:
                    y20 = 0
    return(y20)

def taylorP(y2, y1, y0, y10, y00, g, n, x0):
    y0x = int(input("Enter what x is to the power of for y\n"))
    y1x = int(input("Enter what x is to the power of for y'\n"))
    y2x = int(input("Enter what x is to the power of for y''\n"))

    if (y2 != 0):
        if (y0x == 0):
            if (y1x == 0):
                if (y2x == 0):
                    y20 = (g - (y1 * y10) - (y0 - y00)) / y2
                else:
                    print("No Solution, Divide by 0 Error")
            else:
                if (y2x == 0):
                    y20 = (g - (y0 - y00)) / y2
                else:
                    print("No Solution, Divide by 0 Error")
        else:
            if (y1x == 0):
                if (y2x == 0):
                    y20 = (g - (y1 * y10)) / y2
                else:
                    print("No Solution, Divide by 0 Error")
            else:
                if (y2x == 0):
                    y20 = (g / y2)
                else:
                    print("No Solution, Divide by 0 Error")
    else:
        y20 = taylorPDerivitave(y2, y1, y0, y10, y00, y2x, y1x, y0x)
    print("y'' = ", y20)

    i = 2
    ygt2 = []
    while(i < n):
        if (i == 2):
            ygt2.append(taylorPDerivitave(y2, y1, y0, -y10, y00, y2x, y1x, y0x))
        elif (i == 3):
            y1 = ((y1 * y10) / y2) * y1x
            y0 = ((y0 * y00) / y2) * y0x
            if y1x > 0: y1x -= 1
            if y0x > 0: y0x -= 1
            ygt2.append(taylorPDerivitave(y2, y1, y0, y20, y10, y2x, y1x, y0x))
        elif (i == 4):
            y1 = ((y1 * y10) / y2) * y1x
            y0 = ((y0 * y00) / y2) * y0x
            if y1x > 0: y1x -= 1
            if y0x > 0: y0x -= 1
            ygt2.append(taylorPDerivitave(y2, y1, y0, ygt2[i - 4], y20, y2x, y1x, y0x))
        else:
            y1 = ((y1 * y10) / y2) * y1x
            y0 = ((y0 * y00) / y2) * y0x
            if y1x > 0: y1x -= 1
            if y0x > 0: y0x -= 1
            ygt2.append(taylorPDerivitave(y2, y1, y0, ygt2[i - 3], ygt2[i - 4], y2x, y1x, y0x))
        i += 1
        print("y ", i, "prime = ", ygt2[i - 3])

    y = y00 + (y10 * x0) + ((y20 / 2) * (x0 ** 2))
    for i in range(3, n + 1):
        y += ((ygt2[i - 3] / math.factorial(i)) * (x0 ** i))
    print("y = ", y)
    return

taylorP(1, -2, 1, -1, 1, 0, 4, 3.5)

