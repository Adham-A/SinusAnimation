import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    """Generate the main animation
    """

    fig = plt.figure()
    plt.axis('off')

    x_values = np.linspace(0, np.pi*4, 2000)
    y_values = np.sin(x_values)

    rainbow = plt.cm.get_cmap('gist_rainbow')
    # rainbow_r = rainbow.reversed()
    list_r = rainbow(np.linspace(0, 1, len(x_values)))
    # list_r_r = rainbow_r(np.linspace(0, 1, len(x_values)))

    sin1 = plt.scatter(x_values, y_values, color=list_r, marker=".")
    sin2 = plt.scatter(x_values, -y_values, color=list_r, marker=".")

    def animate(i, sin1, sin2):
        data_sin1 = np.column_stack((x_values, np.sin(x_values+i/10)))
        data_sin2 = np.column_stack((x_values, -np.sin(x_values+i/10)))
        sin1.set_offsets(data_sin1)
        sin2.set_offsets(data_sin2)
        # sin1.set_color(np.roll(list_r,10*i,axis=0))
        # sin2.set_color(np.roll(list_r,10*i,axis=0))
        return sin1, sin2,

    ani = animation.FuncAnimation(fig, animate, blit=False, frames=range(600),
                                  fargs=(sin1, sin2))
    writer = animation.FFMpegWriter(
        fps=60, metadata=dict(artist='Me'), bitrate=4000)
    ani.save(f"animation_sin_{time.time_ns()}.mp4", writer=writer)


if __name__ == "__main__":
    main()
