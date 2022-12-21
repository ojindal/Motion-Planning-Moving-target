import numpy as np
import matplotlib.pyplot as plt

def maps(map = 0):
  m = np.loadtxt('maps/map{}.txt'.format(map));
  return m

def plotting(path):
    map =np.loadtxt(path)*50
    coord = np.load('path.npy')
    target = np.load('target.npy')



    robotpos = [coord[0][0], coord[0][1]]
    targetpos = [target[-1][0], target[-1][1]]

    targetpos0 = [target[0][0], target[0][1]]

    f, ax = plt.subplots()
    ax.imshow( map.T, interpolation="none", cmap='gray_r', origin='lower', \
                extent=(-0.5, map.shape[0]-0.5, -0.5, map.shape[1]-0.5) )
    ax.axis([-0.5, map.shape[0]-0.5, -0.5, map.shape[1]-0.5])
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    f = 3
    r, c = targetpos0[0], targetpos0[1]
    for i in target:
        x_values = [r, i[0]]
        y_values = [c, i[1]]
        plt.plot(x_values, y_values, 'ro', linestyle="--", markersize=0.1)
        r, c = i[0], i[1]

    r, c = robotpos[0], robotpos[1]
    for i in coord:

        x_values = [r, i[0]]
        y_values = [c, i[1]]
        plt.plot(x_values, y_values, 'bo', linestyle="--", markersize=0.1)
        r, c = i[0], i[1]

    htp = ax.plot(targetpos0[0], targetpos0[1], 'gs', markersize=3*f)
    hr = ax.plot(robotpos[0], robotpos[1], 'bs', markersize=5*f)
    hr = ax.plot(coord[-1][0], coord[-1][1], 'bs', markersize=3.5*f)
    ht = ax.plot(targetpos[0], targetpos[1], 'rs', markersize=5*f)
    htp = ax.plot(targetpos0[0], targetpos0[1], 'gs', markersize=3*f)
    plt.savefig('3path.png', dpi=500)
    plt.show()


