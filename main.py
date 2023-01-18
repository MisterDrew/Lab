from constants import x_0, y_0, r1, n_points, time, h, a, b, c
from funcs import create_mb, move_mb, plot_trajectory, move_ts, plot_velocity_fields


def build():
    material_body = create_mb(x_0, y_0, r1, n_points)
    move_body = move_mb(time, h, material_body, a, b, c)
    plot_trajectory(material_body, move_body)
    velocity_fields = move_ts(1, 0.1)
    plot_velocity_fields(velocity_fields)


if __name__ == "__main__":
    build()