import matplotlib.pyplot as plt
import numpy as np


def graficar(point1, point2, point3, point4):

    m12 = (point2[1]-point1[1])/(point2[0]-point1[0])
    b12 = point1[1]

    m34 = (point4[1]-point3[1])/(point4[0]-point3[0])
    b34 = point3[1]

    x = np.linspace(-10, 10, 500)

    xi = (b12-b34) / (m34-m12)
    yi = m12 * xi + b12

    print('(xi,yi)', xi, yi)

    plt.plot(x, x*m12+b12)
    plt.plot(x, x*m34+b34)

    plt.xlim(-2, 8)
    plt.ylim(-2, 8)

    plt.grid(linestyle='dotted')

    plt.savefig("two_straight_lines_intersection_point_01.png",
                bbox_inches='tight')
    plt.scatter(xi, yi, color='black')

    plt.savefig("two_straight_lines_intersection_point_02.png",
                bbox_inches='tight')
    plt.show()
