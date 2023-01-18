import numpy as np
import matplotlib.pyplot
import classfile as model
from classfile import MaterialBody, BodyTrajectory, func_y, func_x


def create_mb(x_0, y_0, r1, n_points):
    material_body = MaterialBody()
    material_body.setBody(x_0, y_0, r1, n_points)
    return material_body


def move_mb(time, h, mb, a, b, c):
    body_trajectory = BodyTrajectory()
    body_trajectory.setBodyTrajectory(time, h, mb, a, b, c)
    return body_trajectory


def plot_trajectory(mb, tr):
    for i in mb.material_points:
        matplotlib.pyplot.plot(i.coord_x, i.coord_y, 'r.')

    for i in tr.point_trajectories:
        matplotlib.pyplot.plot(i.x, i.y, 'b', linewidth=0.5)
        time = len(i.x) - 1
        matplotlib.pyplot.plot(i.x[time], i.y[time], 'g.')

    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.grid()
    matplotlib.pyplot.savefig('assets/plot_trajectory.svg', format='svg', dpi=1200)


def move_ts(time, h):
    t = h
    m = 0
    a = np.linspace(-5, 5, 11)
    x_s, y_s = np.meshgrid(a, a)
    velocity_fields = []
    for n in range(int(time / h)):
        space_points = []
        for i in range(11):
            for j in range(11):
                x = x_s[i, j]
                y = y_s[i, j]
                space_points.append(model.SpacePoint(m, x, y, func_x(t, x), func_y(t, y), t))
                m += 1
        velocity_fields.append(model.SpaceGrid(space_points))
        t += h
    return velocity_fields


def plot_velocity_fields(vf):
    h = vf[0].space_points[0].t
    t = h
    for n in range(len(vf)):
        matplotlib.pyplot.figure(n)
        matplotlib.pyplot.suptitle('t = ' + str(t))
        m = 0
        coord_x = []
        coord_y = []
        v_x = []
        v_y = []
        for i in range(11):
            for j in range(11):
                coord_x.append(vf[n].space_points[m].coord_x)
                coord_y.append(vf[n].space_points[m].coord_y)
                v_x.append(vf[n].space_points[m].velocity_x)
                v_y.append(vf[n].space_points[m].velocity_y)
                m += 1
        matplotlib.pyplot.subplot(1, 2, 1)
        matplotlib.pyplot.quiver(coord_x, coord_y, v_x, v_y)
        for p in range(1, 2):
            for q in range(0, 10):
                x = np.linspace(0.001, 1.0, 1000)
                d = func_y(t, 1) / func_x(t, 1)
                c = q * (p ** d)
                y = c * (x ** d)
                matplotlib.pyplot.subplot(1, 2, 2)
                matplotlib.pyplot.axis([-0.5, 1.5, -5, 50])
                matplotlib.pyplot.plot(x, y)
        t += h
        # plotlib.show()
        matplotlib.pyplot.savefig('assets/velocity_fields' + str(n) + '.svg', format='svg', dpi=1200)