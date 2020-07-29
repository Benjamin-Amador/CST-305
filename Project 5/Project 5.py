#Benjamin Amador & Jeffrey Weidritch
#We used numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=21, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (10, 20, 10)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    if xs[i] >= 17:  #This is the Critical Threshold. you can change this at anytime by adjusting the number.
        print("The system is too slow")
        break
    else:
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("Fragmentation")
ax.set_ylabel("Fragment Load Time")
ax.set_zlabel("File Load Time")
ax.set_title("Lorenz Attractor")

figure = plt.figure()
bx = figure.gca()

bx.plot(xs, ys, lw=0.5)
bx.set_xlabel("Fragmentation")
bx.set_ylabel("Fragment Load Time")
bx.set_title("Lorenz Attractor")

figr = plt.figure()
cx = figr.gca()

cx.plot(xs, zs, lw=0.5)
cx.set_xlabel("Fragmentation")
cx.set_ylabel("File Load Time")
cx.set_title("Lorenz Attractor")

figur = plt.figure()
dx = figur.gca()

dx.plot(ys, zs, lw=0.5)
dx.set_xlabel("Fragment Load Time")
dx.set_ylabel("File Load Time")
dx.set_title("Lorenz Attractor")
plt.show()