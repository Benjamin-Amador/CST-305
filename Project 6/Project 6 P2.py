#Benjamin Amador & Jeffrey Weidritch
#We used numpy to work on this code

import numpy as np

#x = 0, (x^2 + 4)y'' + y = x, n<= 8
def ordinaryPoint(x):
    try: Px = 0 / ((x **2) + 4)
    except:
        print("The point is singular!")
        return
    try: Qx = 1 / ((x **2) + 4)
    except:
        print("The point is singular!")
        return
    Phix = x / ((x **2) + 4)
    return Px, Qx, Phix

def taylorS(x, n):
    if ordinaryPoint(x):
        Px, Qx, Phix = ordinaryPoint(x)
        normalCoefficients = np.zeros((n, 2))
        primeCoefficients = np.zeros((n, 2))
        prime2Coefficients = np.zeros((n, 2))
        matches = np.zeros((n, 3))
        for i in range(0, n):
            normalCoefficients[i, 0] = (i + 1) * Qx
            normalCoefficients[i, 1] = i
            if i != 0: primeCoefficients[i, 1] = i - 1
            primeCoefficients[i, 0] = (i * (i + 1)) * Px
            if i != 0: prime2Coefficients[i, 1] = i - 2
            prime2Coefficients[i, 0] = (i * (i +1)) * (i - 1)

        for i in range(0, n):
            for j in range(0, n):
                if normalCoefficients[i, 1] > primeCoefficients[n - 1, 1]:
                    matches[i, 0] = normalCoefficients[i, 0]
                    delattr(matches[i, 1])
                    delattr(matches[i, 2])
                    break
                for k in range(0, n):
                    if normalCoefficients[i, 1] == primeCoefficients[j, 1] == prime2Coefficients[k, 1]:
                        print("Normal: ", normalCoefficients[i, 0], "\nPrime: ", primeCoefficients[j, 0])
                        print("Double prime: ", prime2Coefficients[k, 0])
                        matches[i, 0] = normalCoefficients[i, 0]
                        matches[i, 1] = primeCoefficients[j, 0]
                        matches[i, 2] = prime2Coefficients[k, 0]
                    elif normalCoefficients[i, 1] == primeCoefficients[j, 1] > prime2Coefficients[n-1, 1]:
                        matches[i, 0] = normalCoefficients[i, 0]
                        matches[i, 1] = primeCoefficients[j, 0]
                        delattr(matches[i, 2])
                        break

        print(matches)
    else: return

taylorS(0, 8)