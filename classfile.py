import numpy as np


def func_x(t, x):

    return -np.cosh(t) * x


def func_y(t, y):

    return t * y


def runge_method(x_0, h, n, func, a, b, c):
    x_t = []
    x_t.append(x_0)
    t = 1*10**-5

    for i in range(n):
        x_n = x_t[i]
        k1 = func(t, x_n)
        k2 = func(t + c[2] * h, x_n + a[2, 1] * h * k1)
        k3 = func(t + c[3] * h, x_n + a[3, 1] * h * k1 + a[3, 2] * h * k2)
        x_t.append(x_n + h * (k1 * b[1] + k2 * b[2] + k3 * b[3]))
        t += h

    return x_t


class MaterialPoint:

    def __init__(self, coord_x, coord_y, x_0, y_0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.x_0 = x_0
        self.y_0 = y_0


class MaterialBody:

    def __init__(self):
        self.material_points = None

    def setBody(self, x_0, y_0, r1, n_points):

        mpoint = []
        alpha = np.linspace(0, np.pi / 2, n_points)
        x_r1 = x_0 + r1 * np.cos(alpha)
        # print(x_r1)
        y_r1 = y_0 + r1 * np.sin(alpha)
        # print(y_r1)
        for xcord, ycord in zip(x_r1, y_r1):
            mpoint.append(MaterialPoint(xcord, ycord, xcord, ycord))
        self.material_points = mpoint


class PointTrajectory:

    def __init__(self, material_point, x, y):
        self.material_point = material_point
        self.x = x
        self.y = y


class BodyTrajectory:

    def __init__(self):
        self.material_body = None
        self.point_trajectories = None

    def setBodyTrajectory(self, time, h, mb, a, b, c):
        pointtr = []
        for i in mb.material_points:
            x_0 = i.x_0
            y_0 = i.y_0

            n = int(time / h) + 1
            x_t = runge_method(x_0, h, n, func_x, a, b, c)
            y_t = runge_method(y_0, h, n, func_y, a, b, c)
            pointtr.append(PointTrajectory(i, x_t, y_t))

        self.point_trajectories = pointtr
        self.material_body = mb


class SpacePoint:

    def __init__(self, i, coord_x, coord_y, velocity_x, velocity_y, t):
        self.i = i
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.t = t


class SpaceGrid:

    def __init__(self, space_points):
        self.space_points = space_points

    def setSpaceGrid(self, t):
        spoints = []
        m = 0
        a = np.linspace(-5, 5, 11)
        x_s, y_s = np.meshgrid(a, a)
        for i in range(11):
            for j in range(11):
                x = x_s[i, j]
                y = y_s[i, j]
                spoints.append(SpacePoint(x, y, func_x(t, x), func_y(t, y), t, i))
                m += 1
        self.space_points = spoints