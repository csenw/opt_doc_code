from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X, Y = np.meshgrid(x,y,sparse=True)
f = X**2 + 3*Y**2
surf = ax.plot_surface(X,Y,f, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

xx =np.array([])
yy =np.array([])
ff =np.array([])
# initial guess (2,2)
xx = np.append(xx, 2)
yy = np.append(yy, 2)
ff = np.append(ff, xx[0]**2 + 3*yy[0]**2)
#plt.plot([xx[0]], [yy[0]], [ff[0]], marker='o',markersize=5, markerfacecolor='green', alpha=0.6)
fig.colorbar(surf, shrink=0.5, aspect=5)
j=0
while True:
    # calculate the optimal tau (learning rate)
    plt.plot([xx[j]], [yy[j]], [ff[j]], marker='o',markersize=5, markerfacecolor='green', alpha=0.6)
    tau = (xx[j]**2+9*yy[j]**2) / (2*xx[j]**2+54*yy[j]**2)
    # update the next location: new (x,y)
    xx = np.append(xx, (1-2*tau)*xx[j])
    yy = np.append(yy, (1-6*tau)*yy[j])
    # update the new function value
    ff = np.append(ff,xx[j+1]**2 + 3* yy[j+1]**2)
    # print (j, tau, xx[j+1], yy[j+1], ff[j+1])
    # the convergence criteria
    if np.abs(ff[j+1]-ff[j]) < 1e-6: break
    j=j+1
plt.show()


